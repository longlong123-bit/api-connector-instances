{
    'name': 'API Connect Instances',
    'version': '16.0.1.0',
    'summary': 'The API Connect Instance module is a pre-built integration tool that enables easy integration of various shipping modules. It serves as an extensible solution for integrating shipping modules seamlessly.',
    'description': """""",
    'category': 'Inventory/Delivery Connector',
    'support': 'odoo.tangerine@gmail.com',
    'author': 'Tangerine',
    'license': 'OPL-1',
    'depends': ['base', 'mail', 'stock', 'delivery'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/select_deli_carrier_wizard_views.xml',
        'views/stock_picking_views.xml',
        'views/res_partner_views.xml',
        'views/api_connect_instances_views.xml',
        'views/api_connect_history_views.xml',
        'views/api_endpoint_config_views.xml',
        'views/menus.xml'
    ],
    'images': ['static/description/thumbnail.gif'],
    'auto_install': False,
    'application': False
}
