from odoo import fields, models, api, _
from odoo.exceptions import Warning, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    role = fields.Selection(string="Role", selection=[
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('designer', 'Designer')
    ], required=False)
    # nip = fields.Char(string="NIP")