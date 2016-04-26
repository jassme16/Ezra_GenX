# -*- coding: utf-8 -*-
{
    'name': 'GenX - POS Extension',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
     *  Remove Odoo Logo in POS interface.
     *  Replace title and favicon.
    """,
    'author': 'Data Genesis',
    'website': 'http://www.datagenesis.com.ph/',
    'depends': ['point_of_sale'],
    'init_xml': [],
    'data': [
        "views/pos_template_02.xml"
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
        "static/src/xml/pos.xml",
    ],
    'installable': True,
    'auto_install': False,
}