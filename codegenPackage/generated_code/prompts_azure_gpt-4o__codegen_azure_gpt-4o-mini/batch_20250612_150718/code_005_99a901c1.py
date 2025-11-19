"""
Generated Code Metadata:
========================
Original URL: https://consultech.ci
Prompt: Write a script to manage user roles and permissions in Odoo, ensuring the solution aligns with ConsulTech's focus on boosting productivity.
Generated: DETERMINISTIC_99a901c1eb130559
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class UserRole(models.Model):
    _name = 'consultech.user.role'
    _description = 'User Role Management'

    name = fields.Char(string='Role Name', required=True)
    description = fields.Text(string='Role Description')
    permission_ids = fields.Many2many('consultech.permission', string='Permissions')

    @api.constrains('name')
    def _check_unique_role_name(self):
        """Ensure that role names are unique."""
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise exceptions.ValidationError("Role name must be unique.")

class Permission(models.Model):
    _name = 'consultech.permission'
    _description = 'Permission Management'

    name = fields.Char(string='Permission Name', required=True)
    description = fields.Text(string='Permission Description')

    @api.constrains('name')
    def _check_unique_permission_name(self):
        """Ensure that permission names are unique."""
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise exceptions.ValidationError("Permission name must be unique.")

class ResUsers(models.Model):
    _inherit = 'res.users'

    role_ids = fields.Many2many('consultech.user.role', string='User Roles')

    @api.model
    def assign_role_to_user(self, user_id, role_id):
        """Assign a role to a user."""
        user = self.browse(user_id)
        role = self.env['consultech.user.role'].browse(role_id)
        if not user or not role:
            raise exceptions.ValidationError("User or Role not found.")
        user.role_ids |= role

    @api.model
    def remove_role_from_user(self, user_id, role_id):
        """Remove a role from a user."""
        user = self.browse(user_id)
        role = self.env['consultech.user.role'].browse(role_id)
        if not user or not role:
            raise exceptions.ValidationError("User or Role not found.")
        user.role_ids -= role

    @api.model
    def get_user_permissions(self, user_id):
        """Get all permissions for a user based on their roles."""
        user = self.browse(user_id)
        if not user:
            raise exceptions.ValidationError("User not found.")
        permissions = self.env['consultech.permission']
        for role in user.role_ids:
            permissions |= role.permission_ids
        return permissions

# Example usage:
# user = self.env['res.users'].browse(user_id)
# user.assign_role_to_user(user.id, role_id)
# user.remove_role_from_user(user.id, role_id)
# permissions = user.get_user_permissions(user.id)
```
