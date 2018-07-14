
from odoo import models,fields,api
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta


class HrEgyptContract(models.Model):
     _name = 'hr.contract'
     _inherit = 'hr.contract'


     new_employee = fields.Boolean(string='New Employee')

     total_gross = fields.Float(string='Total Gross without Allowances', required=True)

     variable = fields.Float(string='Variable Insured Salary')

     basic = fields.Float(string='Basic')

     socialpremium_nt = fields.Float(string='Social Premium - Nontaxable')

     living_allowance = fields.Float(string='Living Allowances')

     transportation_allowance = fields.Float(string='Transportation Allowance')

     mobile_allownance = fields.Float(string='Mobile Allowance')

     representation_allowance = fields.Float(string='Representation Allowance')

     hazard_allowance = fields.Float(string='Hazard Allowance')

     other_allowance = fields.Float(string='Other Allowance')

     permit_expiry = fields.Date(string='Permit Expiry Date')



     @api.onchange('total_gross')
     def _wgaes(self):
         if self.total_gross <= 1370:
             self.wage = self.total_gross
             self.variable = 0
             self.basic = 0
         elif self.total_gross > 1370 and self.total_gross <= 2480 :
                 self.wage = 1370
                 self.variable = self.total_gross - 1370
         else:
             self.wage = 1370
             self.variable = 2480
             self.basic = (self.total_gross - 1370) - 2480


     @api.onchange('new_employee','trial_date_start')
     def _newemployee(self):
        if self.new_employee == True:
         if self.trial_date_start:
             trial_date_start = fields.Date.from_string(self.trial_date_start)
             print(trial_date_start)
             print(type(trial_date_start))
             next_date =trial_date_start + relativedelta(months=+3)
             print(next_date)
             self.write({'trial_date_end':next_date})
             self.trial_date_end=next_date
             self.date_start = self.trial_date_end
             end_duration = trial_date_start + relativedelta(months=12)
             self.date_end = end_duration








