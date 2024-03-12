{
    'name': "Cotação Personalizada Bonamaison",
    'summary': """  Addons que aplica as personalizações Bonamaison no Cotação/Pedido """,
    'category': 'sale',
    'version': '14.01',
    "author": "Trustcode",
    "website": "https://trustcode.com.br",
    'depends': [
        'sale_management',
        'contacts',
        'l10n_br_sale',
        'stock',
        'purchase',
        'base'
    ],
    'data': [
        'reports/report_content_layout_custom_bnms.xml',
        'reports/report_layout_background_bnms.xml',
        'reports/romaneio_entrega.xml',
        'views/sale_order_form.xml',
    ],
}