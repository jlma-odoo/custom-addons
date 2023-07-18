from odoo import fields,models

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _rec_name = "registry_number"
    _description = "modulo de prueba"
    registry_number = fields.Char(required=True)
    vin = fields.Char(string = "Código de identificación (vin)",required=True)
    first_name = fields.Char(string = "Nombres", required=True)
    last_name = fields.Char(string = "Apellidos", required=True)
    picture = fields.Image(string = "Foto")
    current_mileage = fields.Float("Mileage")
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()



    """
    vin - char, required
first_name - char, required
last_name - char, required
picture - image
current_mileage - float
license_plate - char
certificate_title - binary
register_date - date
    """