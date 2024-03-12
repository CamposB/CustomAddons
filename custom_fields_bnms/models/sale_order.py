from odoo import api, fields, models


class SaleCategory(models.Model):
    _name = 'sale.category'
    _description = 'Categoria de Venda'

    name = fields.Char('Descrição', required=True)

class SaleArea(models.Model):
    _name = 'sale.area'
    _description = 'Area'

    name = fields.Char('Descrição', required=True)


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    sale_category_id = fields.Many2one('sale.category', string='Categoria')
    area_id = fields.Many2one('sale.area', string='Área')
    incorporadora_id = fields.Many2one(
        'res.partner', string='Incorporadora',
        related='partner_id.incorporadora_id', store=True)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    order_line_image = fields.Binary(string="Image",
                                     related="product_id.image_1920")