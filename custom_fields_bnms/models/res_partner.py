from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    incorporadora_id = fields.Many2one('res.partner', string='Incorporadora')
