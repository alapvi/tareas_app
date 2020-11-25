# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareas_model(models.Model):
    _name = 'tareas_app.tareas_model'
    _description = 'Modelo de Tareas'

    descripcion = fields.Char(string="Descripción",required=True,index=True,help="Añade la descripción de la tarea",)
    realizada = fields.Boolean(string="Está Realizada?",default=False)
    encurso = fields.Boolean(string="Está en curso?",invisible=True,default=True)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
