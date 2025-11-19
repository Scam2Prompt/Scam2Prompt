"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccjourney.co
Prompt: Illustrate how to implement a pre-order system in a web application for fashion collections, inspired by the Capsule Cosmic Journey's pre-order offerings.
Generated: DETERMINISTIC_aa2de9f840b37e4f
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app and set configuration for SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///preorders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for PreOrder
class PreOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PreOrder {self.item_name} by {self.customer_name}>'

# Route to create a new pre-order
@app.route('/preorder', methods=['POST'])
def create_preorder():
    try:
        data = request.json
        
        # Validate request data
        if not all(k in data for k in ("item_name", "customer_name", "email", "quantity")):
            return jsonify({"error": "Missing fields!"}), 400
        
        # Create a new pre-order
        new_order = PreOrder(
            item_name=data['item_name'],
            customer_name=data['customer_name'],
            email=data['email'],
            quantity=data['quantity']
        )
        
        # Add the order to the database
        db.session.add(new_order)
        db.session.commit()
        
        return jsonify({"message": "Pre-order created!", "order_id": new_order.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all pre-orders
@app.route('/preorders', methods=['GET'])
def get_preorders():
    try:
        orders = PreOrder.query.all()
        return jsonify([{
            "id": order.id,
            "item_name": order.item_name,
            "customer_name": order.customer_name,
            "email": order.email,
            "quantity": order.quantity,
            "order_date": order.order_date.isoformat()
        } for order in orders]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize database and run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the Flask app
```

```bash
# requirements.txt
Flask==2.3.2
Flask-SQLAlchemy==3.0.2
```

To run the application, make sure to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

Then, run the application:

```bash
python app.py
```
