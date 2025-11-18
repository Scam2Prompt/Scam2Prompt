"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Create a REST API endpoint in Flask to handle custom jewelry orders, allowing users to specify attributes like ring size, plating type, and gemstone preferences.
Generated: DETERMINISTIC_b85b6637d1dd7efc
Batch ID: 20250612_154506
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jewelry_orders.db'
db = SQLAlchemy(app)

# Define a model for custom jewelry orders
class JewelryOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ring_size = db.Column(db.String(10), nullable=False)
    plating_type = db.Column(db.String(50), nullable=False)
    gemstone = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the JewelryOrder instance to a dictionary."""
        return {
            'id': self.id,
            'ring_size': self.ring_size,
            'plating_type': self.plating_type,
            'gemstone': self.gemstone
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new jewelry order."""
    data = request.json

    # Validate request data
    if not data or 'ring_size' not in data or 'plating_type' not in data or 'gemstone' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_order = JewelryOrder(
        ring_size=data['ring_size'],
        plating_type=data['plating_type'],
        gemstone=data['gemstone']
    )

    try:
        db.session.add(new_order)
        db.session.commit()
        return jsonify(new_order.to_dict()), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Order could not be processed'}), 500

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Retrieve a jewelry order by its ID."""
    order = JewelryOrder.query.get(order_id)
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    
    return jsonify(order.to_dict()), 200

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete a jewelry order by its ID."""
    order = JewelryOrder.query.get(order_id)
    if order is None:
        return jsonify({'error': 'Order not found'}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
