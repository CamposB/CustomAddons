{  # pylint: disable=C8101,C8103
    'name': "Custom Fields Bonamaison",
    'summary': """  Adiciona campos personalizados para os pedidos de compra """,
    'description': """ Adiciona campos personalizados para os pedidos de compra """,
    'category': 'website',
    'version': '14.01',

    "author": "Trustcode",
    "website": "https://trustcode.com.br",
    "license": "LGPL-3",
    'contributors': [
        'Jonatas Biazus <jonatasbiazusct@gmail.com>',
    ],

    'depends': [
        'sale',
        'stock'
    ],
    'data': [
        'views/sale_order.xml',
        'views/res_partner.xml',
        'views/purchase_order.xml',
        'security/ir.model.access.csv',
        'report/purchase_order_report_inherit.xml',
        'views/stock_picking.xml',
    ],
    'demo': [
    ],
}