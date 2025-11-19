"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Suggest a set of features and functionalities for a web-based platform that allows builders to select and purchase door hardware and locksmith services from a company like Southern Brass.
Generated: DETERMINISTIC_b707334bf16d7200
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///door_hardware.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define database models
class Product(db.Model):
    """Model for door hardware products."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Service(db.Model):
    """Model for locksmith services."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    """Model for customer orders."""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all available door hardware products."""
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock
    } for product in products])

@app.route('/services', methods=['GET'])
def get_services():
    """Fetch all available locksmith services."""
    services = Service.query.all()
    return jsonify([{
        'id': service.id,
        'name': service.name,
        'description': service.description,
        'price': service.price
    } for service in services])

@app.route('/order', methods=['POST'])
def create_order():
    """Create a new order for products or services."""
    try:
        data = request.json
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        product_id = data.get('product_id')
        service_id = data.get('service_id')
        quantity = data.get('quantity', 1)

        # Validate input
        if not customer_name or not customer_email:
            return jsonify({'error': 'Customer name and email are required'}), 400

        if product_id:
            product = Product.query.get(product_id)
            if not product:
                return jsonify({'error': 'Product not found'}), 404
            if product.stock < quantity:
                return jsonify({'error': 'Insufficient stock'}), 400
            total_price = product.price * quantity
            product.stock -= quantity
        elif service_id:
            service = Service.query.get(service_id)
            if not service:
                return jsonify({'error': 'Service not found'}), 404
            total_price = service.price * quantity
        else:
            return jsonify({'error': 'Either product_id or service_id must be provided'}), 400

        # Create order
        order = Order(
            customer_name=customer_name,
            customer_email=customer_email,
            product_id=product_id,
            service_id=service_id,
            quantity=quantity,
            total_price=total_price
        )
        db.session.add(order)
        db.session.commit()

        return jsonify({'message': 'Order created successfully', 'order_id': order.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Fetch details of a specific order."""
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    return jsonify({
        'id': order.id,
        'customer_name': order.customer_name,
        'customer_email': order.customer_email,
        'product_id': order.product_id,
        'service_id': order.service_id,
        'quantity': order.quantity,
        'total_price': order.total_price
    })

# Error handling for 404 routes
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
