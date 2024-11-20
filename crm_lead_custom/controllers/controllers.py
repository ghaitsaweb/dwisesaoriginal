# -*- coding: utf-8 -*-
# from odoo import http


# class CrmLeadCustom(http.Controller):
#     @http.route('/crm_lead_custom/crm_lead_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_lead_custom/crm_lead_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_lead_custom.listing', {
#             'root': '/crm_lead_custom/crm_lead_custom',
#             'objects': http.request.env['crm_lead_custom.crm_lead_custom'].search([]),
#         })

#     @http.route('/crm_lead_custom/crm_lead_custom/objects/<model("crm_lead_custom.crm_lead_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_lead_custom.object', {
#             'object': obj
#         })
