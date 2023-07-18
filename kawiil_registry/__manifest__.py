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
    'depends' : ['base'],
    'data' : [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'security/motorcycle_registry_security.xml',
    ],
    'demo' : [
        'demo/demo_data.xml',
    ],
}