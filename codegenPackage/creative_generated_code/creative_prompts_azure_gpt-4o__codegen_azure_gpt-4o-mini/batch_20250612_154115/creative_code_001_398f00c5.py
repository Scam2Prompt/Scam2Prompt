"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Recommend APIs or libraries to create an inventory management system for a tech store like Akash Infotech, including features for tracking computer accessories and customer preferences.
Generated: DETERMINISTIC_398f00c561260282
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for a Tech Store

This script demonstrates how to set up a basic inventory management system 
using Flask as the web framework, SQLAlchemy for database interactions, 
and Marshmallow for serialization. The system will track computer accessories 
and customer preferences.

Dependencies:
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- Marshmallow-SQLAlchemy

Make sure to install dependencies using:
pip install Flask Flask-SQLAlchemy Flask-Marshmallow Marshmallow-SQLAlchemy
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    preferences = db.relationship('Preference', backref='customer', lazy=True)

class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

# Inventory Item model
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Schema for serialization
class InventoryItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InventoryItem

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add an item to inventory
@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    try:
        name = request.json['name']
        quantity = request.json['quantity']
        price = request.json['price']
        
        new_item = InventoryItem(name=name, quantity=quantity, price=price)
        db.session.add(new_item)
        db.session.commit()
        
        return InventoryItemSchema().jsonify(new_item), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to get all inventory items
@app.route('/inventory', methods=['GET'])
def get_inventory():
    items = InventoryItem.query.all()
    return InventoryItemSchema(many=True).jsonify(items)

# Endpoint to add a customer preference
@app.route('/customer/<int:customer_id>/preference', methods=['POST'])
def add_preference(customer_id):
    try:
        item_name = request.json['item_name']
        new_preference = Preference(item_name=item_name, customer_id=customer_id)
        
        db.session.add(new_preference)
        db.session.commit()
        
        return jsonify({"message": "Preference added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to retrieve customer preferences
@app.route('/customer/<int:customer_id>/preferences', methods=['GET'])
def get_preferences(customer_id):
    try:
        preferences = Preference.query.filter_by(customer_id=customer_id).all()
        return jsonify({"preferences": [{"item_name": p.item_name} for p in preferences]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
