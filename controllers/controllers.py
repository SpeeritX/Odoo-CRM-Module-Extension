# -*- coding: utf-8 -*-
from odoo import http

# class ExtendLead(http.Controller):
#     @http.route('/extend_lead/extend_lead/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extend_lead/extend_lead/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extend_lead.listing', {
#             'root': '/extend_lead/extend_lead',
#             'objects': http.request.env['extend_lead.extend_lead'].search([]),
#         })

#     @http.route('/extend_lead/extend_lead/objects/<model("extend_lead.extend_lead"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extend_lead.object', {
#             'object': obj
#         })