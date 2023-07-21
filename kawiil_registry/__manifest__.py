{
    'name' : 'Motorcycle Registry',
    'summary' : 'Manage Registration of Motorcycles',
    'description': '''
                    Motorcycle Registry
                    ====================
                    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.
                    ''',
    'autor' : 'jlma-odoo',
    'website' : 'https://github.com/jlma-odoo/custom-addons',
    'category' : 'Kawiil/custom',
    'application' : 'True',
    'depends' : ['base','stock'],
    'data' : [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'security/motorcycle_registry_security.xml',
        'data/motorcycle_data.xml',
        'views/motorcycle_registry_menuitems.xml',
        'views/motorcycle_views.xml',
        'views/motorcycle_views_inherit.xml',

    ],
    'demo' : [
        'demo/demo_data.xml',
    ],
}