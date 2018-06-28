# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.multi
    def do_toggle_button(self):
        for todo in self:
            todo.is_done = not todo.is_done
    
    @api.multi
    def do_clear_done(self):
        dones = self.search([
            ('is_done', '=', True)
        ])

        dones.write({
            'active': False
        })