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
Inventory Management System for a Tech Store using Python and Flask

This implementation uses the Flask framework for the API backend and SQLAlchemy for database operations.
It provides features to track computer accessories and customer preferences.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the ComputerAccessory model
class ComputerAccessory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the CustomerPreference model
class CustomerPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    preferred_brand = db.Column(db.String(50), nullable=False)
    preferred_accessory = db.Column(db.String(100), nullable=False)

# Create database tables
db.create_all()

# Define endpoints

@app.route('/accessories', methods=['POST'])
def add_accessory():
    """
    Add a new computer accessory to the inventory.
    Expects JSON input with fields: name, brand, quantity, price.
    """
    data = request.get_json()
    try:
        accessory = ComputerAccessory(
            name=data['name'],
            brand=data['brand'],
            quantity=data['quantity'],
            price=data['price']
        )
        db.session.add(accessory)
        db.session.commit()
        return jsonify({'message': 'Accessory added successfully!'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Accessory already exists.'}), 400

@app.route('/accessories', methods=['GET'])
def list_accessories():
    """
    Retrieve the list of all computer accessories in the inventory.
    """
    accessories = ComputerAccessory.query.all()
    result = [
        {'id': accessory.id, 'name': accessory.name, 'brand': accessory.brand,
         'quantity': accessory.quantity, 'price': accessory.price}
        for accessory in accessories
    ]
    return jsonify(result), 200

@app.route('/preferences', methods=['POST'])
def add_customer_preference():
    """
    Add a customer's preferences for tech accessories.
    Expects JSON input with fields: customer_name, preferred_brand, preferred_accessory.
    """
    data = request.get_json()
    try:
        preference = CustomerPreference(
            customer_name=data['customer_name'],
            preferred_brand=data['preferred_brand'],
            preferred_accessory=data['preferred_accessory']
        )
        db.session.add(preference)
        db.session.commit()
        return jsonify({'message': 'Customer preference added successfully!'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400

@app.route('/preferences', methods=['GET'])
def list_customer_preferences():
    """
    Retrieve the list of all customer preferences.
    """
    preferences = CustomerPreference.query.all()
    result = [
        {'id': preference.id, 'customer_name': preference.customer_name,
         'preferred_brand': preference.preferred_brand, 'preferred_accessory': preference.preferred_accessory}
        for preference in preferences
    ]
    return jsonify(result), 200

@app.route('/accessories/<int:id>', methods=['PUT'])
def update_accessory(id):
    """
    Update the details of a specific accessory by ID.
    Expects JSON input with fields: name, brand, quantity, price.
    """
    data = request.get_json()
    accessory = ComputerAccessory.query.get(id)
    if not accessory:
        return jsonify({'error': 'Accessory not found.'}), 404
    
    try:
        accessory.name = data.get('name', accessory.name)
        accessory.brand = data.get('brand', accessory.brand)
        accessory.quantity = data.get('quantity', accessory.quantity)
        accessory.price = data.get('price', accessory.price)
        db.session.commit()
        return jsonify({'message': 'Accessory updated successfully!'}), 200
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400

@app.route('/accessories/<int:id>', methods=['DELETE'])
def delete_accessory(id):
    """
    Delete a specific accessory by ID.
    """
    accessory = ComputerAccessory.query.get(id)
    if not accessory:
        return jsonify({'error': 'Accessory not found.'}), 404
    
    db.session.delete(accessory)
    db.session.commit()
    return jsonify({'message': 'Accessory deleted successfully!'}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def route_not_found(e):
    return jsonify({'error': 'Route not found.'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
