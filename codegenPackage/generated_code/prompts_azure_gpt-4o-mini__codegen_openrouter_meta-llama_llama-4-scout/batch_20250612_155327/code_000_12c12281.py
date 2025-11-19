"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Generate a code snippet for a custom web application that integrates with an ERP system, focusing on lead tracking and inventory management as described on MDA Tech Sys.
Generated: DETERMINISTIC_12c122812a06327e
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lead_tracker.py

"""
Lead Tracker and Inventory Management System
=============================================

This module provides a basic implementation of a lead tracking and inventory management system.
It integrates with an ERP system and provides endpoints for lead management and inventory updates.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure database connection
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///lead_tracker.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Lead(db.Model):
    """
    Lead Model

    Attributes:
        id (int): Unique identifier for the lead
        name (str): Lead name
        email (str): Lead email
        phone (str): Lead phone number
        status (str): Lead status (e.g., new, converted, lost)
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="new")

    def __repr__(self):
        return f"Lead('{self.name}', '{self.email}', '{self.phone}', '{self.status}')"


class Inventory(db.Model):
    """
    Inventory Model

    Attributes:
        id (int): Unique identifier for the inventory item
        product_name (str): Product name
        quantity (int): Quantity in stock
        unit_price (float): Unit price of the product
    """

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    unit_price = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"Inventory('{self.product_name}', '{self.quantity}', '{self.unit_price}')"


@app.route("/leads", methods=["GET", "POST"])
def leads():
    """
    Lead Management Endpoint

    GET: Retrieve all leads
    POST: Create a new lead
    """

    if request.method == "GET":
        leads = Lead.query.all()
        return jsonify([{"id": lead.id, "name": lead.name, "email": lead.email, "phone": lead.phone, "status": lead.status} for lead in leads])

    elif request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        lead = Lead(name=data["name"], email=data["email"], phone=data["phone"])
        db.session.add(lead)
        db.session.commit()
        return jsonify({"id": lead.id, "name": lead.name, "email": lead.email, "phone": lead.phone, "status": lead.status}), 201


@app.route("/leads/<int:lead_id>", methods=["GET", "PUT", "DELETE"])
def lead(lead_id):
    """
    Lead Detail Endpoint

    GET: Retrieve a lead by ID
    PUT: Update a lead
    DELETE: Delete a lead
    """

    lead = Lead.query.get(lead_id)
    if not lead:
        return jsonify({"error": "Lead not found"}), 404

    if request.method == "GET":
        return jsonify({"id": lead.id, "name": lead.name, "email": lead.email, "phone": lead.phone, "status": lead.status})

    elif request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        lead.name = data.get("name", lead.name)
        lead.email = data.get("email", lead.email)
        lead.phone = data.get("phone", lead.phone)
        lead.status = data.get("status", lead.status)
        db.session.commit()
        return jsonify({"id": lead.id, "name": lead.name, "email": lead.email, "phone": lead.phone, "status": lead.status})

    elif request.method == "DELETE":
        db.session.delete(lead)
        db.session.commit()
        return jsonify({"message": "Lead deleted successfully"})


@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    """
    Inventory Management Endpoint

    GET: Retrieve all inventory items
    POST: Create a new inventory item
    """

    if request.method == "GET":
        inventory_items = Inventory.query.all()
        return jsonify([{"id": item.id, "product_name": item.product_name, "quantity": item.quantity, "unit_price": item.unit_price} for item in inventory_items])

    elif request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        item = Inventory(product_name=data["product_name"], quantity=data["quantity"], unit_price=data["unit_price"])
        db.session.add(item)
        db.session.commit()
        return jsonify({"id": item.id, "product_name": item.product_name, "quantity": item.quantity, "unit_price": item.unit_price}), 201


@app.route("/inventory/<int:item_id>", methods=["GET", "PUT", "DELETE"])
def inventory_item(item_id):
    """
    Inventory Item Detail Endpoint

    GET: Retrieve an inventory item by ID
    PUT: Update an inventory item
    DELETE: Delete an inventory item
    """

    item = Inventory.query.get(item_id)
    if not item:
        return jsonify({"error": "Inventory item not found"}), 404

    if request.method == "GET":
        return jsonify({"id": item.id, "product_name": item.product_name, "quantity": item.quantity, "unit_price": item.unit_price})

    elif request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request data"}), 400

        item.product_name = data.get("product_name", item.product_name)
        item.quantity = data.get("quantity", item.quantity)
        item.unit_price = data.get("unit_price", item.unit_price)
        db.session.commit()
        return jsonify({"id": item.id, "product_name": item.product_name, "quantity": item.quantity, "unit_price": item.unit_price})

    elif request.method == "DELETE":
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Inventory item deleted successfully"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
