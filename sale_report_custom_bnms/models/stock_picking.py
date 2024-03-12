from odoo import api, fields, models,_


class StockMove(models.Model):
	_inherit = "stock.move"

	image_128 = fields.Binary(string="Image")

	@api.onchange('product_id')
	def onchange_product_image(self):
		for product in self:
			product.image_128 = product.product_id.image_128