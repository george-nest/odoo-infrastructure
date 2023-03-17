# -*- coding: utf-8 -*-
{
    'name': "infra",

    'summary': """
         infra module""",

    'description': """
     """,

    'author': "Inform Help",
    'website': "https://www.i-help.pro",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customization',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'external_dependencies': {'python': [], },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/infra_inf_user.xml',
        # 'views/templates.xml',
    ],

    'installable': True,
    'auto_install': False,

    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}