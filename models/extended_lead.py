# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import datetime
import time


class CreditPartner(models.Model):
    _inherit = 'crm.lead'
    expiration_date = fields.Date('Expiration Date')
    additional_info = fields.Text('Additional Information')

    @api.constrains('expiration_date')
    def _check_expiration_date(self):
        for r in self:
            if r.expiration_date and r.expiration_date < time.strftime('%Y-%m-%d'):
                raise ValidationError("Expiration date cannot be older than current date!")
