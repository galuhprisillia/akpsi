from odoo import fields, models, api, _
from odoo.exceptions import Warning, ValidationError


class AKPSIProduct(models.Model):
    _name = 'akpsi.product'
    _description = 'AKPSI Product'
    _inherit = 'mail.thread'
    _rec_name = 'product_name'

    product_name = fields.Char(string="Product Name", tracking=True)
    product_designer = fields.Many2one(comodel_name='res.partner', string="Designer", tracking=True)
    product_type = fields.Selection(string="Type", selection=[
        ('ppt','Power Point'),
        ('icon', 'Icon Bundle')
    ], tracking=True)
    product_doc = fields.Binary(string="Product", tracking=True)
    state = fields.Selection(string="Product State", selection=[
        ('draft','Draft'),
        ('submitted', 'Submitted'),
        ('validated', 'Validated'),
        ('accepted', 'Accepted'),
        ('back_to_draft', 'Back to Draft')
    ], default='draft', tracking=True)
    mp_ids = fields.One2many(comodel_name='marketplace', inverse_name='product_id', string='Markeplace')

    def action_submitted(self):
        for me in self:
            if me.state != 'draft':
                continue
            me.update({
                'state': 'submitted'
            })
        return

    def action_validated(self):
        for me in self:
            if me.state != 'submitted':
                continue
            me.update({
                'state': 'validated'
            })
        return

    def action_accepted(self):
        for me in self:
            if me.state != 'validated':
                continue
            me.update({
                'state': 'accepted'
            })
        return

    def action_back_to_draft(self):
        for me in self:
            if me.state != 'validated':
                continue
            me.update({
                'state': 'draft'
            })
        return


class Marketplace(models.Model):
    _name = 'marketplace'
    _description = 'Marketplace'
    _inherit = 'mail.thread'
    _rec_name = 'mp_name'

    mp_name = fields.Selection(string="Marketplace Name", selection=[
        ('graphicriver', 'Graphicriver'),
        ('envato_elements', 'Envato Elements'),
        ('canva', 'Canva'),
        ('iconfinder','Iconfinder'),
        ('iconscout', 'Iconscout'),
        ('adobe_stock', 'Adobe Stock'),
        ('thenounproject', 'Thenounproject')
    ])
    mp_sku = fields.Char(string="SKU")
    product_id = fields.Many2one(comodel_name='akpsi.product', string="Product")
