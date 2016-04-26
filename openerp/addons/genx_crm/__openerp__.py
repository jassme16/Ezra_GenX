# -*- coding: utf-8 -*-
{
    'name': 'GenX - CRM Extension',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
     *  Extend CRM: Remove "Odoo" in Deduplicate Contacts, Sales Configuration in Settings, etc.
    """,
    'author': 'Data Genesis',
    'website': 'http://www.datagenesis.com.ph/',
    'depends': ['genx','crm'],
    'init_xml': [],
    'data': [
        'settings_sale_configuration.xml',
        'crm_deduplicate_contacts.xml'
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [],
    'installable': True,
    'auto_install': False,
}