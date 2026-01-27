{
    'name': 'Vehicle Trip Management',
    'version': '18.0.1.2.0',
    'category': 'Fleet',
    'summary': 'Vehicle Trips, Costing, Accounting & Reports',
    'author': 'Kandil',
    'application': True,
    'price': 100,
    'license': 'LGPL-3',
    'depends': ['fleet', 'hr', 'project', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/vehicle_trip_menu.xml',
        'views/vehicle_trip_config_views.xml',
        'views/vehicle_trip_views.xml',
        'views/res_config_settings_views.xml',
        'reports/vehicle_trip_pivot_views.xml',
        'reports/vehicle_trip_report_templates.xml',
        'reports/vehicle_trip_report_actions.xml'
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
}
