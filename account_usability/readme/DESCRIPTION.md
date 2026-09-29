This module extends the Odoo CE account module to add all the missing or
hidden things that are hidden and available only on EE version.

1)  This module adds missing menu entries and views for the
    **Account** module.
    - Bank Statements and Cash Registers, under *Accounting > Accounting >
      Bank and Cash*
    - Account Tags, under *Accounting > Configuration > Accounting > Account
      Tags*, with the list of accounts using each tag
2)  This module also enables the option to enable or disable Anglo-Saxon
    accounting in the Accounting Settings.
3)  In Odoo CE, the group 'Show Full Accounting Features' is hidden.
    With that module, the group is selectable in the user form view.
    Also the group "Billing / xxx" are renamed into "Accounting / yyy"
    to fit with the EE terms.
4)  Rename the main menu 'Billing' into 'Accounting' to fit with EE
    naming.
5) Allow to configure **Fiscalyear Last Day** on accounting configuration page.

Since Odoo 20.0 the model `account.group` no longer exists: the chart of
accounts hierarchy is handled natively by the parent account
(`account.account.parent_id`), so this module no longer adds the Account
Groups menu nor the accounts list on account groups.
