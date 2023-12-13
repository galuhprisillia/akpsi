from odoo import fields, models, api, _
from odoo.exceptions import Warning, ValidationError
import logging


class ResPartner(models.Model):
    _inherit = 'res.partner'

    role = fields.Selection(string="Role", selection=[
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('designer', 'Designer')
    ], required=False)
    nip = fields.Char(string="NIP")

    @api.model
    def create(self, vals):
        vals['nip'] = self.env['ir.sequence'].next_by_code('nik.seq')
        res = super(ResPartner, self).create(vals)
        # write the code for creating the account and assign to partner
        return res

    def action_validated(self):
        data = {
            'name': self.name,
            'login': self.email,
            'password': "1",
            'email': self.email,
            'mobile': self.mobile,
        }
        self.env['res.users']._signup_create_user(data)
        return