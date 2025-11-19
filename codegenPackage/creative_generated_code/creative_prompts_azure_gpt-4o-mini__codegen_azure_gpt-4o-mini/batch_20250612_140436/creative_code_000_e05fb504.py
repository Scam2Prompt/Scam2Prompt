"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraphicdesigner.link
Prompt: Generate a code snippet for an online store that allows customers to order graphic design services and pay after service completion.
Generated: DETERMINISTIC_e05fb504a96bd8f7
Batch ID: 20250612_140436
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
from werkzeug.exceptions import NotFound, BadRequest
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing graphic design service orders
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    service_description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'service_description': self.service_description,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Create all database tables
with app.app_context():
    db.create_all()

@app.route('/order', methods=['POST'])
def create_order():
    """Create a new order for graphic design services."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'customer_name' not in data or 'service_description' not in data:
        raise BadRequest("Missing required fields: 'customer_name' and 'service_description'.")

    new_order = Order(
        customer_name=data['customer_name'],
        service_description=data['service_description']
    )
    
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify(new_order.to_dict()), 201

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve an order by its ID."""
    order = Order.query.get(order_id)
    if order is None:
        raise NotFound("Order not found.")
    return jsonify(order.to_dict()), 200

@app.route('/order/<int:order_id>/pay', methods=['PUT'])
def pay_for_order(order_id):
    """Mark an order as completed and update its status to 'Paid'."""
    order = Order.query.get(order_id)
    if order is None:
        raise NotFound("Order not found.")
    
    order.status = 'Paid'
    db.session.commit()
    
    return jsonify(order.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True)
```
