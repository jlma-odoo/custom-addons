from odoo import fields,models,api
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _rec_name = "registry_number"
    _description = "modulo de prueba"
    registry_number = fields.Char(required=True,default='CRM0000',readonly=True)
    vin = fields.Char(string = "Código de identificación (vin)",required=True)
    picture = fields.Image(string = "Foto")
    current_mileage = fields.Float("Mileage")
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()
    owner_id = fields.Many2one(comodel_name="res.partner", string='Owner',ondelete='cascade')
    email = fields.Char(related='owner_id.email')
    phone = fields.Char(related='owner_id.phone')
    make = fields.Char(compute='_compute_registry_data')
    model = fields.Char(compute='_compute_registry_data')
    year = fields.Char(compute='_compute_registry_data')

    @api.depends('vin')
    def _compute_registry_data(self):
        self.make =''
        self.model =''
        self.year =''

        for motorcycle in self:
            if not motorcycle.vin == False:
                    motorcycle.make = motorcycle.vin[0:2]
                    motorcycle.model = motorcycle.vin[2:4]
                    motorcycle.year = motorcycle.vin[4:6]


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
            if(motorcycle.vin== False or motorcycle.vin == '' or re.match(regex,motorcycle.vin)==None):
                raise ValidationError('Vin format incorrect')


    @api.constrains('license_plate')
    def _check_license_plate(self):
        for motorcycle in self:
            regex = r'[A-Z][A-Z]?[A-Z]?[A-Z]?[0-9][0-9]?[0-9]?[A-Z]?[A-Z]?'
            if(motorcycle.license_plate == False or motorcycle.license_plate == '' or re.match(regex,motorcycle.license_plate)==None):
                raise ValidationError('License plate format incorrect')



