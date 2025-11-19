"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: "Write a Python script to implement an ERP system for a small business using Odoo."
Generated: DETERMINISTIC_7e9dfcdbb493518c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Odoo ERP System Implementation for Small Business

This script demonstrates how to create custom Odoo modules for a small business ERP system.
It includes models for Products, Customers, Sales Orders, and Inventory.

Requirements:
- Odoo 14.0 or later
- Python 3.6+
"""

from odoo import models, fields, api, exceptions, _

class Product(models.Model):
    """Product model extending Odoo's product.template"""
    _inherit = 'product.template'

    barcode = fields.Char('Barcode', required=True)
    reorder_level = fields.Integer('Reorder Level', default=10)
    supplier_id = fields.Many2one('res.partner', string='Primary Supplier')

class Customer(models.Model):
    """Customer model extending Odoo's res.partner"""
    _inherit = 'res.partner'

    customer_code = fields.Char('Customer Code', required=True)
    credit_limit = fields.Float('Credit Limit', default=1000.0)
    loyalty_points = fields.Integer('Loyalty Points', default=0)

class SalesOrder(models.Model):
    """Custom Sales Order model"""
    _inherit = 'sale.order'

    delivery_date = fields.Date('Delivery Date', required=True)
    sales_rep_id = fields.Many2one('res.users', string='Sales Representative')
    discount_percent = fields.Float('Discount %', default=0.0)

    @api.constrains('discount_percent')
    def _check_discount_percent(self):
        """Validate discount percentage"""
        for order in self:
            if order.discount_percent < 0 or order.discount_percent > 100:
                raise exceptions.ValidationError(
                    _("Discount percentage must be between 0 and 100"))

    def action_confirm(self):
        """Override confirm action to apply discount"""
        for order in self:
            if order.discount_percent > 0:
                for line in order.order_line:
                    line.discount = order.discount_percent
        return super(SalesOrder, self).action_confirm()

class Inventory(models.Model):
    """Inventory management model"""
    _name = 'business.inventory'
    _description = 'Inventory Management'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Integer('Quantity', default=0)
    location = fields.Char('Location', required=True)
    last_restock = fields.Date('Last Restock Date')

    @api.model
    def check_low_stock(self):
        """Check for products below reorder level"""
        products = self.env['product.product'].search([])
        low_stock = []
        
        for product in products:
            inventory = self.search([('product_id', '=', product.id)], limit=1)
            if inventory and inventory.quantity < product.reorder_level:
                low_stock.append(product.name)
        
        if low_stock:
            return {
                'warning': {
                    'title': _('Low Stock Alert'),
                    'message': _('The following products are low on stock:\n%s') % 
                              '\n'.join(low_stock)
                }
            }
        return {}

class BusinessERP(models.Model):
    """Main ERP model for business operations"""
    _name = 'business.erp'
    _description = 'Business ERP System'

    @api.model
    def generate_monthly_report(self):
        """Generate monthly sales and inventory report"""
        sales = self.env['sale.order'].search([
            ('date_order', '>=', fields.Date.start_of('month')),
            ('state', '=', 'sale')
        ])
        
        total_sales = sum(order.amount_total for order in sales)
        inventory_value = sum(
            inv.product_id.list_price * inv.quantity 
            for inv in self.env['business.inventory'].search([])
        )
        
        return {
            'total_sales': total_sales,
            'inventory_value': inventory_value,
            'order_count': len(sales)
        }

# XML files would be needed for views and menus (not shown here)
```
