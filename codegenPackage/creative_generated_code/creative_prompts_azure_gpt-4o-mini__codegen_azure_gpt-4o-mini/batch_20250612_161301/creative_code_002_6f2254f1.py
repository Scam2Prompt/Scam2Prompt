"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digisou-ltd.com
Prompt: Generate a sample app development project that focuses on customer engagement, inspired by the innovative app solutions offered by DigiSou.
Generated: DETERMINISTIC_6f2254f1cbc1e6d7
Batch ID: 20250612_161301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/customers`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# customer_engagement_app.py

import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Customer {self.name}>'

# Route to add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    try:
        new_customer = Customer(name=data['name'], email=data['email'])
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer added successfully!', 'customer': data}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        return jsonify([{'id': c.id, 'name': c.name, 'email': c.email} for c in customers]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update customer information
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.json
    try:
        customer = Customer.query.get_or_404(customer_id)
        customer.name = data.get('name', customer.name)
        customer.email = data.get('email', customer.email)
        db.session.commit()
        return jsonify({'message': 'Customer updated successfully!', 'customer': {'id': customer.id, 'name': customer.name, 'email': customer.email}}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete a customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted successfully!'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

### Requirements
Make sure to install Flask and Flask-SQLAlchemy before running the code:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### How to Run
1. Save the above code to a file named `customer_engagement_app.py`.
2. Run the application using: 
   ```bash
   python customer_engagement_app.py
   ```
3. Use a tool like Postman or curl to interact with the API at `http://127.0.0.1:5000/customers`.
