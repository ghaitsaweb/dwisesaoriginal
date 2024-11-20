# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class crm_lead_custom(models.Model):
    _inherit = 'crm.lead'
    _description = 'crm_lead_custom.crm_lead_custom'


    customer_type = fields.Selection([
    ('government', 'Government'),
    ('company', 'Company'),
    ('retail', 'Retail')], string='Customer Type')
    project = fields.Boolean(string='Project?')
    project_name = fields.Many2one('project.project', string='Project Name')
    project_id = fields.Char(string='Project ID', )
    project_manager = fields.Many2one('hr.employee', string='Project Manager')
    planned_date_start = fields.Date(string='Planned Start Date')
    planned_date_end = fields.Date(string='Planned End Date')
    cogs = fields.Float(string='COGS')
    margin = fields.Float(string='Margin', compute='_compute_margin', store=True)
    margin_percent = fields.Float(string='Margin %', compute='_compute_margin_percent', store=True)
    po_date = fields.Date(string='PO Date')



    @api.onchange('project', 'project_name', 'stage_id')
    def create_project_if_needed(self):
        if self.project and not self.project_name:
            # if not self.project_manager:
            #     raise UserError("Please input Project Manager!")
            # Create new project
            project_vals = {
                'name': self.stage_id.name,  # Nama proyek sesuai dengan nama stage pipeline
                'user_id': self.project_manager.user_id.id,
            }
            project = self.env['project.project'].create(project_vals)
            self.project_name = project.id


    @api.depends('expected_revenue', 'cogs')
    def _compute_margin(self):
        for record in self:
            record.margin = record.expected_revenue - record.cogs

    @api.depends('margin', 'expected_revenue')
    def _compute_margin_percent(self):
        for record in self:
            if record.expected_revenue:
                record.margin_percent = (record.margin / record.expected_revenue) * 100
            else:
                record.margin_percent = 0.0

    @api.model
    def create(self, vals):
        if vals.get('stage_id') and self.env['crm.stage'].browse(vals['stage_id']).is_won:
            if vals.get('project'):
                raise UserError("Please input Project Manager!")
        return super(crm_lead_custom, self).create(vals)



class project_project_custom(models.Model):
    _inherit = 'project.project'
    _description = 'crm_lead_custom.project_project'


    project_id = fields.Char(string='Project ID', )


# class respartnercustom(models.Model):
#     _inherit = 'res.partner'
#     _description = 'crm_lead_custom.res_partner'


#     customers_id = fields.Char(string='Customer ID', )
