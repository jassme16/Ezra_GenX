# -*- coding: utf-8 -*-
from openerp import models, fields,api


class genxMenuAudit(models.Model):
    _name = 'sys.genx.audit'

    _description = 'A Basic audit trail for Genx'

    name = fields.Char('Name')
    description = fields.Text('Description')
    user_id_trigger = fields.Many2one('res.users', 'User ID')
    menu_triggered = fields.Char('Menu Used')
    event_happened = fields.Char('User Interactions')
    old_value = fields.Char('Old Value')
    new_value = fields.Char('New Value')

    #Follow Up
    #dev_object_triggered = fields.Char()