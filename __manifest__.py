# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "KeDaTech Test",
    'summary': "Test Modules",
    'description': """
        This module only for examination in KeDaTech
        """,    
    'version': '1.0',
    'depends': ['base','account','purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/kedatech_views.xml',
    ],
    'license': 'LGPL-3',
}
