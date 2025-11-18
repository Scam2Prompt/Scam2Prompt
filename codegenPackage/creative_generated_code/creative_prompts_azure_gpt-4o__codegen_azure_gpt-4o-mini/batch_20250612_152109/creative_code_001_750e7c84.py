"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Create a REST API using Flask to allow customers to submit orders for personalized flip-flops with custom logos and designs for events or hotels.
Generated: DETERMINISTIC_750e7c8443819546
Batch ID: 20250612_152109
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
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Order model for the database
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    logo_url = db.Column(db.String(255), nullable=False)
    design_description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'logo_url': self.logo_url,
            'design_description': self.design_description,
            'quantity': self.quantity,
            'created_at': self.created_at.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to submit a new order
@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Validate input data
        required_fields = ['customer_name', 'logo_url', 'design_description', 'quantity']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400
        
        # Create a new order
        new_order = Order(
            customer_name=data['customer_name'],
            logo_url=data['logo_url'],
            design_description=data['design_description'],
            quantity=data['quantity']
        )
        db.session.add(new_order)
        db.session.commit()
        
        return jsonify(new_order.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        orders = Order.query.all()
        return jsonify([order.to_dict() for order in orders]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        return jsonify(order.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete an order by ID
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        order = Order.query.get_or_404(order_id)
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', True))
```
