from odoo import fields, models, api, _
from odoo.exceptions import Warning, ValidationError


class AKPSIProject(models.Model):
    _inherit = "project.task"

    product_id = fields.Many2one(comodel_name='akpsi.product', string="Product")