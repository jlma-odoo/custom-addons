from odoo import fields,models,api
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _rec_name = "registry_number"
    _description = "modulo de prueba"
    registry_number = fields.Char(required=True,default='CRM0000',readonly=True)
    vin = fields.Char(string = "Código de identificación (vin)",required=True)
    first_name = fields.Char(string = "Nombres", required=True)
    last_name = fields.Char(string = "Apellidos", required=True)
    picture = fields.Image(string = "Foto")
    current_mileage = fields.Float("Mileage")
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number',('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.crm')
        return super().create(vals_list)

    @api.constrains('vin')
    def _check_vin_number(self):
        for motorcycle in self:
            regex = r'^[A-Z]{4}[0-9]{2}[0-9A-Z]{2}[0-9]{6}$'
            if(re.match(regex,motorcycle.vin)==None):
                raise ValidationError('Vin format incorrect')


    @api.constrains('license_plate')
    def _check_license_plate(self):
        for motorcycle in self:
            regex = r'[A-Z][A-Z]?[A-Z]?[A-Z]?[0-9][0-9]?[0-9]?[A-Z]?[A-Z]?'
            if(re.match(regex,motorcycle.vin)==None):
                raise ValidationError('License plate format incorrect')



