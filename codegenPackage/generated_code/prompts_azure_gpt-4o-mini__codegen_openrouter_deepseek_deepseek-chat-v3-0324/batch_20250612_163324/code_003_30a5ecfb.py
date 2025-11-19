"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Create a RESTful API endpoint to manage product listings for construction and garden equipment, inspired by the offerings on the Gala Games app blog.
Generated: DETERMINISTIC_30a5ecfb5297e05e
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///products.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product Model
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'construction' or 'garden'
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    stock_quantity = db.Column(db.Integer, nullable=False, default=0)
    is_available = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Product {self.name}>'

# Product Schema for validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str()
    stock_quantity = fields.Int(required=True)
    is_available = fields.Bool()

# Initialize schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create database tables
with app.app_context():
    db.create_all()

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error', 'message': str(error)}), 500

# Routes
@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    try:
        products = Product.query.all()
        return jsonify(products_schema.dump(products))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a single product by ID"""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify(product_schema.dump(product))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product"""
    try:
        data = request.get_json()
        # Validate input data
        errors = product_schema.validate(data)
        if errors:
            return jsonify({'error': errors}), 400
            
        product = Product(
            name=data['name'],
            category=data['category'],
            price=data['price'],
            description=data.get('description', ''),
            stock_quantity=data['stock_quantity'],
            is_available=data.get('is_available', True)
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify(product_schema.dump(product)), 201
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product"""
    try:
        product = Product.query.get_or_404(product_id)
        data = request.get_json()
        
        # Validate input data
        errors = product_schema.validate(data, partial=True)
        if errors:
            return jsonify({'error': errors}), 400
            
        product.name = data.get('name', product.name)
        product.category = data.get('category', product.category)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)
        product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
        product.is_available = data.get('is_available', product.is_available)
        
        db.session.commit()
        
        return jsonify(product_schema.dump(product))
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
