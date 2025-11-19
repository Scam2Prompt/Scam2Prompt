"""
Generated Code Metadata:
========================
Original URL: https://flokisystem.com
Prompt: "Write a Python code snippet using Odoo framework for developing a custom management system for a specific industry."
Generated: DETERMINISTIC_1d7194f362168ccf
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class CustomManagementSystem(models.Model):
    """Custom Management System for Industry-Specific Operations"""
    _name = 'custom.management.system'
    _description = 'Custom Management System'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    industry_type = fields.Selection([
        ('manufacturing', 'Manufacturing'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('retail', 'Retail'),
        ('other', 'Other')
    ], string='Industry Type', required=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    end_date = fields.Date(string='End Date')
    active = fields.Boolean(string='Active', default=True)
    manager_id = fields.Many2one('res.users', string='Manager', required=True)
    team_member_ids = fields.Many2many('res.users', string='Team Members')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        """Override create method to generate unique reference"""
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('custom.management.system') or _('New')
        return super(CustomManagementSystem, self).create(vals)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Validate that end_date is after start_date"""
        for record in self:
            if record.end_date and record.end_date < record.start_date:
                raise ValidationError(_('End date must be after start date.'))

    def action_start(self):
        """Change status to 'In Progress'"""
        for record in self:
            if record.status != 'draft':
                raise UserError(_('Only draft records can be started.'))
            record.status = 'in_progress'

    def action_complete(self):
        """Change status to 'Completed'"""
        for record in self:
            if record.status != 'in_progress':
                raise UserError(_('Only records in progress can be completed.'))
            record.status = 'completed'

    def action_cancel(self):
        """Change status to 'Cancelled'"""
        for record in self:
            if record.status == 'completed':
                raise UserError(_('Completed records cannot be cancelled.'))
            record.status = 'cancelled'

    def action_reset_to_draft(self):
        """Reset status to 'Draft'"""
        for record in self:
            if record.status not in ('cancelled', 'in_progress'):
                raise UserError(_('Only cancelled or in-progress records can be reset.'))
            record.status = 'draft'

    def unlink(self):
        """Prevent deletion of active records"""
        for record in self:
            if record.status == 'in_progress':
                raise UserError(_('You cannot delete a record in progress.'))
        return super(CustomManagementSystem, self).unlink()

    @api.model
    def get_dashboard_data(self):
        """Return aggregated data for dashboard view"""
        return {
            'total': self.search_count([]),
            'draft': self.search_count([('status', '=', 'draft')]),
            'in_progress': self.search_count([('status', '=', 'in_progress')]),
            'completed': self.search_count([('status', '=', 'completed')]),
            'cancelled': self.search_count([('status', '=', 'cancelled')]),
        }
```
