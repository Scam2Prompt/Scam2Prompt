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

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError

class CustomUserRole(models.Model):
    """Model to define custom user roles for ConsulTech's productivity focus"""
    _name = 'custom.user.role'
    _description = 'Custom User Role'
    _order = 'sequence, name'

    name = fields.Char(string='Role Name', required=True, translate=True)
    description = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence', default=10)
    active = fields.Boolean(string='Active', default=True)
    permission_ids = fields.Many2many(
        'ir.model.access',
        'custom_role_permission_rel',
        'role_id', 'permission_id',
        string='Permissions'
    )
    user_ids = fields.Many2many(
        'res.users',
        'custom_role_user_rel',
        'role_id', 'user_id',
        string='Users'
    )

    @api.constrains('name')
    def _check_name_unique(self):
        for role in self:
            if self.search_count([('name', '=ilike', role.name), ('id', '!=', role.id)]):
                raise ValidationError(_('Role name must be unique!'))

class ResUsers(models.Model):
    """Extend res.users to add role management functionality"""
    _inherit = 'res.users'

    custom_role_ids = fields.Many2many(
        'custom.user.role',
        'custom_role_user_rel',
        'user_id', 'role_id',
        string='Custom Roles'
    )

    def _get_custom_permissions(self):
        """Get all permissions from user's custom roles"""
        self.ensure_one()
        permissions = self.env['ir.model.access']
        for role in self.custom_role_ids:
            permissions |= role.permission_ids
        return permissions

    def has_custom_permission(self, model_name, permission_type='read'):
        """
        Check if user has permission on model from custom roles
        :param model_name: str - technical name of the model
        :param permission_type: str - one of: read, write, create, unlink
        :return: bool
        """
        self.ensure_one()
        if self.has_group('base.group_system'):
            return True
            
        model = self.env['ir.model'].search([('model', '=', model_name)], limit=1)
        if not model:
            return False
            
        permissions = self._get_custom_permissions()
        domain = [
            ('model_id', '=', model.id),
            ('perm_' + permission_type, '=', True)
        ]
        return bool(permissions.search_count(domain))

class CustomRolePermissionRule(models.Model):
    """Rules to apply permissions based on conditions"""
    _name = 'custom.role.permission.rule'
    _description = 'Custom Role Permission Rule'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    model_id = fields.Many2one(
        'ir.model',
        string='Model',
        required=True,
        ondelete='cascade'
    )
    domain = fields.Char(string='Domain', required=True, default='[]')
    role_id = fields.Many2one(
        'custom.user.role',
        string='Role',
        required=True,
        ondelete='cascade'
    )
    permission_type = fields.Selection(
        [
            ('read', 'Read'),
            ('write', 'Write'),
            ('create', 'Create'),
            ('unlink', 'Delete')
        ],
        string='Permission Type',
        required=True
    )
    apply_to_all = fields.Boolean(string='Apply to All Records', default=False)

    @api.constrains('domain')
    def _check_domain_validity(self):
        for rule in self:
            try:
                domain = eval(rule.domain)
                if not isinstance(domain, list):
                    raise ValidationError(_('Domain must be a list of tuples'))
            except Exception as e:
                raise ValidationError(_('Invalid domain: %s') % str(e))

    def check_access(self, user, record):
        """
        Check if user has access to specific record based on rules
        :param user: res.users record
        :param record: target record
        :return: bool
        """
        self.ensure_one()
        if not user or not record:
            return False
            
        if self.model_id.model != record._name:
            return False
            
        if not user.has_custom_permission(self.model_id.model, self.permission_type):
            return False
            
        if self.apply_to_all:
            return True
            
        try:
            domain = eval(self.domain)
            return record in self.env[record._name].search(domain)
        except Exception:
            return False

def post_load():
    """Patch Odoo's access control to include custom role permissions"""
    from odoo import api
    from odoo.models import BaseModel

    original_check_access_rights = BaseModel.check_access_rights

    @api.model
    def check_access_rights(self, operation, raise_exception=True):
        try:
            # First try standard Odoo permissions
            return original_check_access_rights(self, operation, raise_exception)
        except AccessError:
            # Fall back to custom role permissions
            if self.env.user.has_custom_permission(self._name, operation):
                return True
            if raise_exception:
                raise AccessError(_("You don't have the access rights for this operation."))
            return False

    BaseModel.check_access_rights = check_access_rights

# Register the post-load hook
import odoo
odoo.api.post_load = post_load
```
