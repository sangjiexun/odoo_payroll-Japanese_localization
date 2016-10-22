# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons import decimal_precision as dp


class HrContract(models.Model):
    _inherit = 'hr.contract'

    overtime_allowance = fields.Float(string='Overtime allowance', digits=dp.get_precision('Payroll'))
    commuting_allowance = fields.Float(string='Commuting allowance', digits=dp.get_precision('Payroll'))
    health_insurance = fields.Float(string='Health insurance', digits=dp.get_precision('Payroll'))
    nursing_insurance = fields.Float(string='Nursing insurance', digits=dp.get_precision('Payroll'))
    employees_pension = fields.Float(string='Employee\'s pension', digits=dp.get_precision('Payroll'))
    unemployment_insurance_employee = fields.Float(string='Unemployment insurance(Employee\'s share)', digits=dp.get_precision('Payroll'))
    unemployment_insurance_employer = fields.Float(string='Unemployment insurance(Employer\'s share', digits=dp.get_precision('Payroll'))
    workmens_compensation_insurance = fields.Float(string='Workmen\'s compensation insurance', digits=dp.get_precision('Payroll'))
    income_tax = fields.Float(string='Income tax', digits=dp.get_precision('Payroll'))
    resident_tax = fields.Float(string='Resident tax', digits=dp.get_precision('Payroll'))


