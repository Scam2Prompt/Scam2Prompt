"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamelevenx1.xyz
Prompt: Create an API endpoint that allows users to track their orders in real-time, reflecting the order tracking feature highlighted on ayuwin.
Generated: DETERMINISTIC_49f7517e0d71e6b5
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI (replace with your database configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)

# Order model definition
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'status': self.status,
            'updated_at': self.updated_at.isoformat()
        }

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to track orders
@app.route('/api/orders/<int:order_id>', methods=['GET'])
def track_order(order_id):
    """
    Retrieve the tracking details of an order by order_id.
    
    :param order_id: The ID of the order to track.
    :return: JSON containing order tracking details or an error message.
    """
    order = Order.query.get(order_id)
    
    if order is None:
        abort(404, description="Order not found.")

    return jsonify(order.to_dict()), 200

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handling for general exceptions
@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to replace the database URI with your production database configuration, and install Flask and SQLAlchemy if you haven't already.
