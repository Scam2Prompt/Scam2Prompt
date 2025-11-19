"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://startupsadvisory.com
Prompt: Generate a code snippet for a commission-free ordering system that can be integrated into a restaurant's website.
Generated: DETERMINISTIC_004acae7daa22641
Batch ID: 20250612_161035
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
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing order information
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    items = db.Column(db.Text, nullable=False)  # Assuming items are stored as a string
    total_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Order {self.id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/order', methods=['POST'])
def create_order():
    """
    Create a new order.
    Expects JSON data with customer_name, items and total_price.
    """
    try:
        data = request.get_json()
        
        # Validate input data
        if not all(key in data for key in ('customer_name', 'items', 'total_price')):
            return jsonify({"error": "Missing required fields"}), 400
        
        new_order = Order(
            customer_name=data['customer_name'],
            items=data['items'],
            total_price=data['total_price']
        )
        
        db.session.add(new_order)
        db.session.commit()
        
        return jsonify({"message": "Order created successfully", "order_id": new_order.id}), 201

    except Exception as e:
        db.session.rollback()  # Rollback the session on error
        return jsonify({"error": str(e)}), 500

@app.route('/orders', methods=['GET'])
def get_orders():
    """
    Retrieve all orders.
    Returns a list of orders in JSON format.
    """
    try:
        orders = Order.query.all()
        return jsonify([{
            "id": order.id,
            "customer_name": order.customer_name,
            "items": order.items,
            "total_price": order.total_price,
            "created_at": order.created_at.isoformat()
        } for order in orders]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

**Note**: Ensure you have the Flask and SQLAlchemy libraries installed. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
