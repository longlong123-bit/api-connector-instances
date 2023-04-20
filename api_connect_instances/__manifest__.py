{
    'name': 'API Connect Instances',
    'version': '13.0.1.0',
    'summary': 'Connect Odoo Application with Viettel Post',
    'description': """
        The Odoo Viettel Post Connector module is an integrated product between the odoo application and the carrier Viettel Post. 
        The application provides features, which through the api to manipulate directly into the dashboard of Viettel Post.
    """,
    'category': 'Inventory/Delivery Connector',
    'support': 'odoo.tangerine@gmail.com',
    'author': 'Tangerine',
    'license': 'OPL-1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/select_deli_carrier_wizard_views.xml',
        'views/api_connect_instances_views.xml',
        'views/api_connect_history_views.xml',
        'views/api_endpoint_config_views.xml',
        'views/menus.xml'
    ],
    'auto_install': False,
    'application': False
}