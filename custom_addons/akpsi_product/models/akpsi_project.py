from odoo import fields, models, api, _
from odoo.exceptions import Warning, ValidationError
import logging


class AKPSIProject(models.Model):
    _inherit = "project.task"

    product_id = fields.Many2one(comodel_name='akpsi.product', string="Product")
    

class Project(models.Model):
    _inherit = "project.project"


    def action_view_tasks(self):
        stage = self.env['project.task.type'].search([('user_id', '=', False)])
        for stg in stage:
            stg.update({
                'project_ids': [(4, self.id)]
            })
        return super(Project, self).action_view_tasks()