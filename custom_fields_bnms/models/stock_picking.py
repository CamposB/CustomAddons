from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    sale_category_id = fields.Many2one('sale.category', string='Categoria')
    area_id = fields.Many2one('sale.area', string='Área')
    incorporadora_id = fields.Many2one('res.partner', string='Incorporadora')

    @api.model
    def create(self, vals):
        # Defina o campo 'origin' antes de criar o registro, se necessário
        if 'origin' in vals:
            _logger.info("Origin: %s", vals['origin'])
        else:
            # Aqui você poderia definir vals['origin'] com base em alguma lógica
            _logger.warning("Origin nao definida")

        # Chame o método 'create' da superclasse para criar o registro
        record = super(StockPickingInherit, self).create(vals)

        # Agora que o registro foi criado, atualize os campos personalizados com base no 'origin'
        if record.origin:
            sale_order = self.env['sale.order'].search([('name', '=', record.origin)], limit=1)
            if sale_order:
                _logger.info("Pedido de venda correspondente %s", sale_order.id)
                record.write({
                    'sale_category_id': sale_order.sale_category_id.id,
                    'area_id': sale_order.area_id.id,
                    'incorporadora_id': sale_order.incorporadora_id.id,
                })
        return record
