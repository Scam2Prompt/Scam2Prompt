"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Create a REST API in Flask for Meta+ to handle customer orders, including endpoints for querying product availability (e.g., stainless steel, aluminum) and placing orders with delivery details.
Generated: DETERMINISTIC_55ba2ba41865844c
Batch ID: 20250612_151659
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    material = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.Boolean, default=True)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    delivery_address = db.Column(db.String(200), nullable=False)
    
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

# Create the database and tables
with app.app_context():
    db.create_all()

# Endpoint to check product availability
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products with their availability status."""
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'material': p.material, 'availability': p.availability} for p in products])

# Endpoint to place an order
@app.route('/orders', methods=['POST'])
def place_order():
    """Place an order for a product with delivery details."""
    data = request.json
    
    # Validate input data
    if not data or 'product_id' not in data or 'delivery_address' not in data:
        abort(400, description="Bad Request: 'product_id' and 'delivery_address' are required fields.")
    
    product = Product.query.get(data['product_id'])
    
    # Check if the product exists and is available
    if not product or not product.availability:
        abort(404, description="Not Found: Product is not available.")
    
    # Create a new order
    new_order = Order(product_id=data['product_id'], delivery_address=data['delivery_address'])
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify({'message': 'Order placed successfully!', 'order_id': new_order.id}), 201

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not Found', 'message': error.description}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors."""
    return jsonify({'error': 'Bad Request', 'message': error.description}), 400

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
