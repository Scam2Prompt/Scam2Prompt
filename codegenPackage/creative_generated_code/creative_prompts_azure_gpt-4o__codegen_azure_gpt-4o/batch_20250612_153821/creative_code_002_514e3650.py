"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenzo.online
Prompt: Generate code for creating a scalable backend system for an e-commerce platform that supports seamless transactions and personalized user experiences, inspired by Fenzo's backend development services.
Generated: DETERMINISTIC_514e365077a71afc
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Scalable Backend System for an E-Commerce Platform
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
import os

# Flask application setup
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database initialization
db = SQLAlchemy(app)

# Models
class User(db.Model):
    """User model which stores user data."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Product(db.Model):
    """Product model which stores product details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

class Order(db.Model):
    """Order model which stores order information."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

# Error handler
@app.errorhandler(404)
def not_found_error(e):
    """Handle 404 errors gracefully."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    """Handle server errors gracefully."""
    return jsonify({"error": "Internal Server Error"}), 500

# Routes
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    try:
        user = User(name=data['name'], email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all products."""
    products = Product.query.all()
    product_list = [{"id": p.id, "name": p.name, "description": p.description, "price": p.price, "stock": p.stock} for p in products]
    return jsonify(product_list), 200

@app.route('/order', methods=['POST'])
def create_order():
    """Create a new order."""
    data = request.json
    try:
        product = Product.query.get(data['product_id'])
        if not product or product.stock < data['quantity']:
            return jsonify({"error": "Product not available or insufficient stock"}), 400
        total_price = product.price * data['quantity']
        order = Order(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'], total_price=total_price)
        product.stock -= data['quantity']
        db.session.add(order)
        db.session.commit()
        return jsonify({"message": "Order created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/personalization/<int:user_id>', methods=['GET'])
def get_personalized_recommendations(user_id):
    """Generate personalized product recommendations for a user."""
    # In a production system, this logic can involve a recommendation engine.
    recommendations = Product.query.order_by(Product.price.desc()).limit(5).all()
    recommendation_list = [{"id": p.id, "name": p.name, "price": p.price} for p in recommendations]
    return jsonify({"user_id": user_id, "recommendations": recommendation_list}), 200

# Database initialization script
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Application entry point
if __name__ == '__main__':
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
