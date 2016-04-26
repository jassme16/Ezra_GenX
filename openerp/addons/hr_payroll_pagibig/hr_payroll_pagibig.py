# -*- coding: utf-8 -*-
from openerp import models, fields, api
import xlwt
from cStringIO import StringIO
import base64


#STATE= [
#    ('draft', 'Draft'),
#    ('approved', 'Approved'),
#    ('post', 'Paid')
#]

#class pagibigContriMain(models.Model):
#    _name = 'payroll.pagibig.main'
#    _description = 'Pag-ibig Employees Contributions'


#class pagibigContriDetail(models.Model):
#    _name = 'payroll.pagibig.detail'
#    _description = 'Pag-ibig Employees detail Contributions'