# -*- coding: utf-8 -*-
{
    'name': "tareas_app",

    'summary': """
        Aplicación para la gestión de tareas""",

    'description': """
        Aplicación para la gestión de tareas simple
    """,

    'author': "Alberto Aparicio",
    'website': "http://www.aaparicio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/tareas_view.xml',
        'views/categorias_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
