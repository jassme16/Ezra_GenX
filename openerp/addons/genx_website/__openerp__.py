# -*- coding: utf-8 -*-
{
    'name': 'GenX - Website Extension',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
     *  Extend Website: Remove "Create a free website with Odoo" in the footer of website.
     *  Extend Website: Change placeholder of social media accounts in Website Settings (replace "openerp" with "datagen").
    """,
    'author': 'Data Genesis',
    'website': 'http://www.datagenesis.com.ph/',
    'depends': ['genx', 'website'],
    'init_xml': [],
    'data': [
        'views/website_templates.xml',
        'views/website_views_social_media.xml',
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [],
    'installable': True,
    'auto_install': False,
}