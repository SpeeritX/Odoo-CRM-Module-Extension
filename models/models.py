# -*- coding: utf-8 -*-
import time

from odoo import models, fields, api
# class extend_lead(models.Model):
#     _name = 'extend_lead.extend_lead'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100