# -*- coding: utf-8 -*-
from odoo import http

class Motorcycle(http.Controller):
    @http.route('/motorcycles/', auth='public', website=True)
    def index(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type','=','motorcycle')])
        return http.request.render('kawiil_registry.template_website',{
            'motorcycles' : motorcycles,
        })