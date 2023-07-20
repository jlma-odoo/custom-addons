from odoo import fields,models,api
class ProductTemplate(models.Model):
        _inherit = 'product.template'
        
        detailed_type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle'),
        ], ondelete={'motorcycle': 'set product'})

        def _detailed_type_mapping(self):
                type_mapping = super()._detailed_type_mapping()
                type_mapping['motorcycle'] = 'product'
                return type_mapping

        horsepower = fields.Float()
        top_speed = fields.Float()
        torque = fields.Float()
        battery_capacity = fields.Float()
        charge_time = fields.Float()
        range = fields.Float()
        curb_weight = fields.Float()
        make = fields.Char()
        model = fields.Char()
        