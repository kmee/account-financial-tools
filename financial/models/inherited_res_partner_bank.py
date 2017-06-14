# -*- coding: utf-8 -*-
# Copyright 2017 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from __future__ import division, print_function, unicode_literals

from odoo import fields, models


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'
    # _inherits = ['mail.thread']

    initial_balance = fields.Monetary(
        track_visibility='onchange',
        default=0.00
    )
    date_balance = fields.Date(
        track_visibility='onchange',
        default=fields.Date.context_today,
    )
    # account_id = fields.Many2one(
    #     comodel_name='account.account',
    #     string='Account',
    #     ondelete='restrict',
    # )
