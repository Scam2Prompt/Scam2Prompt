"""
Generated Code Metadata:
========================
Original URL: https://consultech.ci
Prompt: "Generate a Python code snippet for integrating Odoo with Oracle JD Edwards for enterprise resource planning."
Generated: DETERMINISTIC_8d9cddaaef4fca07
Batch ID: 20250622_212709
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
Odoo-JD Edwards Integration Module

This module provides integration between Odoo ERP and Oracle JD Edwards ERP systems.
It handles data synchronization for common ERP operations like orders, inventory, and accounting.

Requirements:
- Python 3.6+
- Odoo API access
- JD Edwards EnterpriseOne Web Services
- requests library
- xmltodict library (optional for XML handling)
"""

import logging
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import json
from odoo import models, fields, api, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class JDEdwardsIntegration(models.Model):
    _name = 'jde.integration'
    _description = 'JD Edwards Integration Configuration'

    name = fields.Char(string='Name', required=True)
    jde_url = fields.Char(string='JDE Base URL', required=True)
    jde_username = fields.Char(string='JDE Username', required=True)
    jde_password = fields.Char(string='JDE Password', required=True)
    active = fields.Boolean(string='Active', default=True)
    last_sync_date = fields.Datetime(string='Last Synchronization Date')
    sync_interval = fields.Integer(string='Sync Interval (minutes)', default=60)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    @api.model
    def _get_default_integration(self):
        return self.search([('active', '=', True)], limit=1)

    def test_connection(self):
        """Test connection to JD Edwards system"""
        self.ensure_one()
        try:
            response = self._jde_api_call('GET', 'jderest/v1/test')
            if response.status_code == 200:
                raise UserError(_("Connection successful!"))
            else:
                raise UserError(_("Connection failed: %s") % response.text)
        except Exception as e:
            raise UserError(_("Connection error: %s") % str(e))

    def _jde_api_call(self, method, endpoint, data=None, params=None):
        """Make API call to JD Edwards system"""
        url = f"{self.jde_url.rstrip('/')}/{endpoint}"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        auth = HTTPBasicAuth(self.jde_username, self.jde_password)

        try:
            response = requests.request(
                method,
                url,
                auth=auth,
                headers=headers,
                json=data,
                params=params,
                timeout=30
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            _logger.error("JD Edwards API Error: %s", str(e))
            raise UserError(_("JD Edwards API Error: %s") % str(e))

    def sync_products(self):
        """Sync products from JD Edwards to Odoo"""
        self.ensure_one()
        try:
            response = self._jde_api_call('GET', 'jderest/v1/products')
            products = response.json().get('products', [])

            Product = self.env['product.product']
            for product_data in products:
                product = Product.search([('default_code', '=', product_data.get('itemNumber'))], limit=1)
                vals = {
                    'name': product_data.get('description'),
                    'default_code': product_data.get('itemNumber'),
                    'list_price': product_data.get('price'),
                    'standard_price': product_data.get('cost'),
                    'type': 'product',
                }
                if product:
                    product.write(vals)
                else:
                    Product.create(vals)

            self.last_sync_date = datetime.now()
            return True
        except Exception as e:
            _logger.error("Product sync failed: %s", str(e))
            raise UserError(_("Product sync failed: %s") % str(e))

    def sync_customers(self):
        """Sync customers from JD Edwards to Odoo"""
        self.ensure_one()
        try:
            response = self._jde_api_call('GET', 'jderest/v1/customers')
            customers = response.json().get('customers', [])

            Partner = self.env['res.partner']
            for customer_data in customers:
                partner = Partner.search([('ref', '=', customer_data.get('customerNumber'))], limit=1)
                vals = {
                    'name': customer_data.get('name'),
                    'ref': customer_data.get('customerNumber'),
                    'street': customer_data.get('address1'),
                    'street2': customer_data.get('address2'),
                    'city': customer_data.get('city'),
                    'zip': customer_data.get('postalCode'),
                    'phone': customer_data.get('phone'),
                    'email': customer_data.get('email'),
                    'customer_rank': 1,
                }
                if partner:
                    partner.write(vals)
                else:
                    Partner.create(vals)

            self.last_sync_date = datetime.now()
            return True
        except Exception as e:
            _logger.error("Customer sync failed: %s", str(e))
            raise UserError(_("Customer sync failed: %s") % str(e))

    def create_jde_sales_order(self, order):
        """Create sales order in JD Edwards from Odoo"""
        self.ensure_one()
        try:
            order_lines = []
            for line in order.order_line:
                order_lines.append({
                    'itemNumber': line.product_id.default_code,
                    'quantity': line.product_uom_qty,
                    'unitPrice': line.price_unit,
                    'lineDescription': line.name,
                })

            data = {
                'orderNumber': order.name,
                'customerNumber': order.partner_id.ref,
                'orderDate': fields.Datetime.to_string(order.date_order),
                'orderLines': order_lines,
            }

            response = self._jde_api_call('POST', 'jderest/v1/salesorders', data=data)
            if response.status_code == 201:
                order.message_post(body=_("Order successfully created in JD Edwards"))
                return True
            else:
                raise UserError(_("Order creation failed in JD Edwards: %s") % response.text)
        except Exception as e:
            _logger.error("Order creation failed: %s", str(e))
            raise UserError(_("Order creation failed: %s") % str(e))

    def cron_sync_jde_data(self):
        """Scheduled job to sync data with JD Edwards"""
        integrations = self.search([('active', '=', True)])
        for integration in integrations:
            try:
                integration.sync_products()
                integration.sync_customers()
            except Exception as e:
                _logger.error("Scheduled sync failed for %s: %s", integration.name, str(e))
```
