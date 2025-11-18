"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultech.ci
Prompt: Write a script to manage user roles and permissions in Odoo, ensuring the solution aligns with ConsulTech's focus on boosting productivity.
Generated: DETERMINISTIC_99a901c1eb130559
Batch ID: 20250612_150718
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

class UserRole(models.Model):
    _name = 'consultech.user.role'
    _description = 'User Roles for ConsulTech'

    name = fields.Char(string='Role Name', required=True)
    description = fields.Text(string='Role Description')
    permission_ids = fields.Many2many('consultech.permission', string='Permissions')

    @api.constrains('name')
    def _check_unique_role_name(self):
        """Ensure role names are unique."""
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise exceptions.ValidationError(f"Role name '{record.name}' must be unique.")

class Permission(models.Model):
    _name = 'consultech.permission'
    _description = 'Permissions for ConsulTech'

    name = fields.Char(string='Permission Name', required=True)
    description = fields.Text(string='Permission Description')

    @api.constrains('name')
    def _check_unique_permission_name(self):
        """Ensure permission names are unique."""
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise exceptions.ValidationError(f"Permission name '{record.name}' must be unique.")

class ResUsers(models.Model):
    _inherit = 'res.users'

    role_ids = fields.Many2many('consultech.user.role', string='User Roles')

    @api.constrains('role_ids')
    def _check_user_roles(self):
        """Ensure users have at least one role."""
        for user in self:
            if not user.role_ids:
                raise exceptions.ValidationError("Users must have at least one role assigned.")

    @api.model
    def create(self, vals):
        """Override create method to include role validation."""
        # Call the base method to create the user
        user = super(ResUsers, self).create(vals)
        # Validate roles after creation
        user._check_user_roles()
        return user

    def write(self, vals):
        """Override write method to include role validation."""
        # Call the base method to update the user
        result = super(ResUsers, self).write(vals)
        # Validate roles after update
        for user in self:
            user._check_user_roles()
        return result

# Example data setup for testing purposes (to be used in Odoo shell or migration scripts)
def setup_initial_data(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Create sample permissions
    permission_read = env['consultech.permission'].create({'name': 'Read Data', 'description': 'Allows reading data'})
    permission_write = env['consultech.permission'].create({'name': 'Write Data', 'description': 'Allows writing data'})
    
    # Create sample roles with permissions
    role_admin = env['consultech.user.role'].create({'name': 'Administrator', 'description': 'Admin role with all permissions'})
    role_admin.permission_ids = [(4, permission_read.id), (4, permission_write.id)]

    role_user = env['consultech.user.role'].create({'name': 'User', 'description': 'Standard user role'})
    role_user.permission_ids = [(4, permission_read.id)]

    # Log the creation of initial data for auditing
    _logger.info("Initial user roles and permissions have been set up.")
```
