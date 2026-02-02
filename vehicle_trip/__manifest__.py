{
'name': 'Vehicle Trip Management',
'version': '1.2',
'summary': 'Vehicle Trips, Costing, Accounting & Reports',
'author': 'Kandil',
'website': 'https://kandiltech.com',
'category': 'Fleet',
'depends': ['fleet', 'hr', 'project', 'account'],
'data': [
 # 1. الأمان
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
'application': True,
'price': 100,
'license': 'LGPL-3',
}
