# -*- coding: utf-8 -*-

from odoo import models, fields, api


class categorias_model(models.Model):
    _name = 'tareas_app.categorias_model'
    _description = 'Modelo de Categorias'

    name = fields.Char(string="Nombre",required=True,index=True,help="Nombre de la categoria")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
