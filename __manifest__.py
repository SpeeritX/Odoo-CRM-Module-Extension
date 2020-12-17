# -*- coding: utf-8 -*-
{
    'name': "Extend Lead",

    'summary': "Extends crm_lead model",

    'description': """
        Extends crm_lead model with new functionalities.
    """,

    'author': "SpeeritX",
    'website': "https://github.com/SpeeritX",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        'views/extend_lead_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
