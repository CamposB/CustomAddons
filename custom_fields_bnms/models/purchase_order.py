from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    purchase_line_image = fields.Binary(string="Image",
                                        related="product_id.image_1920")

    data_prog = fields.Datetime(string='Data Prog.', store=True)
