# -*- coding: utf-8 -*-

from odoo import fields, models, api, tools
from odoo.exceptions import ValidationError
from datetime import datetime
import time


AVAILABLE_DIFFICULTIES = [
    (1, 'Low'),
    (2, 'Normal'),
    (3, 'High'),
    (4, 'Very High'),
]


class ExtendedLead(models.Model):
    _inherit = 'crm.lead'
    expiration_date = fields.Date('Expiration Date', index=True)
    additional_info = fields.Text('Additional Information')
    marketing_consent = fields.Boolean('Marketing Consent', index=True, default=True)
    obstacles = fields.One2many('extend_lead.obstacle', 'lead_id', string="Obstacles")
    difficulty = fields.Integer(compute="_calculate_difficulty", store=True, index=True, string='Difficulty')
    image = fields.Binary('Image')
    image_small = fields.Binary('Small Image', compute="_compute_image", store=True)

    @api.multi
    @api.depends('obstacles')
    def _calculate_difficulty(self):
        for r in self:
            r.difficulty = sum(o.difficulty for o in r.obstacles)

    @api.model
    def create(self,values):
        if 'image' in values:
            values['image'] = tools.image_resize_image_medium(values['image'])
        return super(ExtendedLead, self).create(values)

    @api.multi
    def write(self, values):
        if 'image' in values:
            values['image'] = tools.image_resize_image_medium(values['image'])
        return super(ExtendedLead, self).write(values)

    @api.multi
    @api.depends('image')
    def _compute_image(self):
        for r in self:
            r.image_small = tools.image_resize_image_small(r.image)

    @api.multi
    @api.constrains('expiration_date')
    def _check_expiration_date(self):
        for r in self:
            if r.expiration_date and r.expiration_date < time.strftime('%Y-%m-%d'):
                raise ValidationError("Expiration date cannot be older than current date!")


class Obstacle(models.Model):
    _name = 'extend_lead.obstacle'

    lead_id = fields.Many2one('crm.lead', ondelete='cascade', string="Lead", required=True)
    description = fields.Text('Description')
    difficulty = fields.Selection(AVAILABLE_DIFFICULTIES, string='Difficulty', required=True, index=True, default=AVAILABLE_DIFFICULTIES[1][0])
