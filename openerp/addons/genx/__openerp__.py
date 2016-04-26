# -*- coding: utf-8 -*-
{
    'name': 'GenX Company Setup',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
     *  Install all required modules with company customizations.
     *  Change page favicon and title.
     *  Insert company info and logo.
     *  Checks the technical features box for administrator user.
     *  Change "Powered By Odoo" to "Powered By Data Genesis" in login and other pages.
     *  Remove Manage Database in login.
     *  Remove My Odoo.com account, About Odoo, Help, Odoo Support in right side dropdown menu.
     *  Replace "Odoo" with "GenX" in help labels when record is empty in all modules.
     *  Replace "Odoo" with "GenX" in welcome message to group when Messaging (mail) is installed.
     *  Delete Sent By and Access Link in Email Template footer.
     *  Remove all Odoo's in FAQ for import (Frequently Asked Questions.
     *  Replace "Odoo" with GenX in Public and Portal Tooltips in User's Settings.
    """,
    'author': 'Data Genesis',
    'website': 'http://www.datagenesis.com.ph/',
    'depends': ['web','mail', 'base', 'base_import'],
    'css': ['static/src/css/style.css'],
    'init_xml': [],
    'data': [
        "views/res_company_view.xml",
        "views/res_groups_view.xml",
        "views/webclient_template.xml",
        "view_help.xml",
        "mail_group_message.xml",
        "base_data_users_settings.xml"
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
        "static/src/xml/base.xml",
        "static/src/xml/base_import_faq.xml"
    ],
    'installable': True,
    'auto_install': False,
}