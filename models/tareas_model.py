# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareas_model(models.Model):
    _name = 'tareas_app.tareas_model'
    _description = 'Modelo de Tareas'

    name = fields.Char(string="Descripción",required=True,index=True,help="Añade la descripción de la tarea",)
    realizada = fields.Boolean(string="Está Realizada?",default=False)
    active = fields.Boolean(string="Está en curso?",invisible=True,default=True)

    def cambiaEstado(self):
        self.ensure_one()
        self.realizada = not self.realizada    
        return True

    def limpiaRealizadas(self):
        return True


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
