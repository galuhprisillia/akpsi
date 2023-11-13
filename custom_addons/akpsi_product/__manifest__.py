# -*- coding: utf-8 -*-
{
    'name': 'AKPSI',
    'version': '16.0.0',
    'category': 'product',
    'summary': 'Base Master',
    'description': 'Product',
    'live_test_url': '',
    'sequence': '1',
    'website': '',
    'author': 'kelompok 7',
    'maintainer': 'kelompok 7',
    'license': 'LGPL-3',
    'support': '',
    'depends': [
        'base',
        'web',
        'mail',
        'project'
    ],
    'demo': [],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/akpsi_product.xml',
        'views/akpsi_project.xml',
        'views/akpsi_employee.xml',
        'views/list_menu.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'qweb': [],
}
