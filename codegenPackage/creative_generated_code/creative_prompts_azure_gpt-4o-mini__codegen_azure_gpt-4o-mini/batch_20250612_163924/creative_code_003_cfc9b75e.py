"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biogreenasia.com
Prompt: Create a REST API endpoint for managing orders on an e-commerce site similar to Bio Green Asia, focusing on natural products like floor cleaners and hand washes.
Generated: DETERMINISTIC_cfc9b75e5d44e1bb
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Order model definition
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        """Convert the Order object to a dictionary."""
        return {
            'id': self.id,
            'product_name': self.product_name,
            'quantity': self.quantity,
            'customer_name': self.customer_name,
            'address': self.address
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    try:
        new_order = Order(
            product_name=data['product_name'],
            quantity=data['quantity'],
            customer_name=data['customer_name'],
            address=data['address']
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify(new_order.to_dict()), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database integrity error."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

# Endpoint to retrieve a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found."}), 404
    return jsonify(order.to_dict()), 200

# Endpoint to update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found."}), 404

    data = request.get_json()
    try:
        order.product_name = data.get('product_name', order.product_name)
        order.quantity = data.get('quantity', order.quantity)
        order.customer_name = data.get('customer_name', order.customer_name)
        order.address = data.get('address', order.address)
        
        db.session.commit()
        return jsonify(order.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found."}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted successfully."}), 204

if __name__ == '__main__':
    app.run(debug=os.getenv("FLASK_DEBUG", "True") == "True")
```

Make sure to install the necessary dependencies for this code to run:
```bash
pip install Flask Flask-SQLAlchemy
```

To run the application, set the environment variable for Flask:
```bash
export FLASK_APP=your_script_name.py
export FLASK_ENV=development
flask run
```
