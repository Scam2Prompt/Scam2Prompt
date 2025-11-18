"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokisystem.com
Prompt: Develop a custom Odoo-based management system tailored for a specific industry, as described by Floki Systems' expertise in ERP implementations.
Generated: DETERMINISTIC_4db4a3067670949c
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class CustomManagementSystem(models.Model):
    """Custom Management System for Industry-Specific ERP Implementation."""
    _name = 'custom.management.system'
    _description = 'Custom Management System tailored for specific industry needs'

    # Define fields for the custom management system
    name = fields.Char(string='Name', required=True, help='Name of the entity')
    description = fields.Text(string='Description', help='Detailed description of the entity')
    date_created = fields.Datetime(string='Date Created', default=fields.Datetime.now, help='Creation date of the record')
    active = fields.Boolean(string='Active', default=True, help='Indicates if the record is active')
    user_id = fields.Many2one('res.users', string='User', help='User associated with the record')

    @api.constrains('name')
    def _check_name(self):
        """Ensure the name field is unique."""
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise exceptions.ValidationError("The name must be unique.")

    @api.model
    def create(self, vals):
        """Override the create method to add custom logic."""
        try:
            record = super(CustomManagementSystem, self).create(vals)
            return record
        except Exception as e:
            raise exceptions.UserError(f"Error creating record: {str(e)}")

    def write(self, vals):
        """Override the write method to add custom logic."""
        try:
            result = super(CustomManagementSystem, self).write(vals)
            return result
        except Exception as e:
            raise exceptions.UserError(f"Error updating record: {str(e)}")

    def unlink(self):
        """Override the unlink method to add custom logic before deletion."""
        for record in self:
            if not record.active:
                raise exceptions.UserError("Cannot delete an inactive record.")
        return super(CustomManagementSystem, self).unlink()

    @api.model
    def get_active_records(self):
        """Get all active records."""
        active_records = self.search([('active', '=', True)])
        return active_records

    @api.model
    def archive_record(self):
        """Archive the current record by marking it as inactive."""
        for record in self:
            record.active = False
```
