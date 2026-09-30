# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged("post_install", "-at_install")
class TestAccountUsability(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))

    def test_tag_accounts(self):
        tag = self.env["account.account.tag"].create(
            {"name": "Usability Tag", "applicability": "accounts"}
        )
        account = self.env["account.account"].create(
            {"code": "100901", "name": "Usability Account", "tag_ids": [(4, tag.id)]}
        )
        self.assertIn(account, tag.account_ids)
        other = self.env["account.account"].create(
            {"code": "100902", "name": "Usability Account 2"}
        )
        tag.account_ids = [(4, other.id)]
        self.assertIn(tag, other.tag_ids)

    def test_tax_group_taxes(self):
        group = self.env["account.tax.group"].create({"name": "Usability Group"})
        tax = self.env["account.tax"].create(
            {"name": "Usability Tax", "amount": 5.0, "tax_group_id": group.id}
        )
        self.assertEqual(group.tax_ids, tax)

    def test_settings_fiscal_year_and_anglo_saxon(self):
        company = self.env.company
        settings = self.env["res.config.settings"].create(
            {
                "anglo_saxon_accounting": True,
                "fiscalyear_last_day": 30,
                "fiscalyear_last_month": "6",
            }
        )
        settings.execute()
        self.assertTrue(company.anglo_saxon_accounting)
        self.assertEqual(company.fiscalyear_last_day, 30)
        self.assertEqual(company.fiscalyear_last_month, "6")

    def test_groups_renamed(self):
        user_group = self.env.ref("account.group_account_user")
        manager_group = self.env.ref("account.group_account_manager")
        self.assertEqual(user_group.name, "Bookkeeper")
        self.assertEqual(
            self.env.ref("account.group_account_readonly").name, "Read-only"
        )
        self.assertEqual(manager_group.name, "Accountant")
        self.assertIn(user_group, manager_group.implied_ids)
        self.assertEqual(self.env.ref("account.menu_finance").name, "Accounting")

    def test_bank_and_cash_menus(self):
        menu = self.env.ref("account_usability.menu_accounting_bank_and_cash")
        self.assertEqual(
            menu.child_id.mapped("action"),
            [
                self.env.ref("account.action_bank_statement_tree"),
                self.env.ref("account.action_view_bank_statement_tree"),
            ],
        )

    def test_no_empty_templates_menu(self):
        # The chart templates are not records since 17.0, so the "Templates"
        # menu would be an entry with no child.
        self.assertFalse(
            self.env.ref(
                "account_usability.menu_account_coa_settings",
                raise_if_not_found=False,
            )
        )
