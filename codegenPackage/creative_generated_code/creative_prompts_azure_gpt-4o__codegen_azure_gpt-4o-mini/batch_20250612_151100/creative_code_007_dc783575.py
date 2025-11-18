"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teameleven-x1.xyz
Prompt: Write a script to integrate payment methods and shipping options into an e-commerce app, similar to the system described on the website.
Generated: DETERMINISTIC_dc7835753fe6317e
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_integration.py

import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Payment Methods
class PaymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    method_name = db.Column(db.String(50), nullable=False)

# Database model for Shipping Options
class ShippingOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option_name = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Float, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a payment method
@app.route('/payment-methods', methods=['POST'])
def add_payment_method():
    try:
        data = request.get_json()
        method_name = data.get('method_name')

        if not method_name:
            return jsonify({"error": "Method name is required"}), 400

        new_method = PaymentMethod(method_name=method_name)
        db.session.add(new_method)
        db.session.commit()
        
        return jsonify({"message": "Payment method added", "id": new_method.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to list all payment methods
@app.route('/payment-methods', methods=['GET'])
def get_payment_methods():
    methods = PaymentMethod.query.all()
    return jsonify([{"id": method.id, "method_name": method.method_name} for method in methods]), 200

# Endpoint to add a shipping option
@app.route('/shipping-options', methods=['POST'])
def add_shipping_option():
    try:
        data = request.get_json()
        option_name = data.get('option_name')
        cost = data.get('cost')

        if not option_name or cost is None:
            return jsonify({"error": "Option name and cost are required"}), 400

        new_option = ShippingOption(option_name=option_name, cost=cost)
        db.session.add(new_option)
        db.session.commit()
        
        return jsonify({"message": "Shipping option added", "id": new_option.id}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to list all shipping options
@app.route('/shipping-options', methods=['GET'])
def get_shipping_options():
    options = ShippingOption.query.all()
    return jsonify([{"id": option.id, "option_name": option.option_name, "cost": option.cost} for option in options]), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- This script requires `Flask` and `Flask-SQLAlchemy`. Ensure you have them installed:
```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
- Save the code to a file named `e_commerce_integration.py`.
- Run the application with:
```bash
python e_commerce_integration.py
```

### API Endpoints
- **POST /payment-methods**: Add a new payment method.
- **GET /payment-methods**: Retrieve all payment methods.
- **POST /shipping-options**: Add a new shipping option.
- **GET /shipping-options**: Retrieve all shipping options.
