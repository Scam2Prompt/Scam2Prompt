"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Illustrate how to implement a RESTful API to manage inventory for various additives and pigments, referencing the product categories from M J Pigment & Additives.
Generated: DETERMINISTIC_497cb5eaab3548c1
Batch ID: 20250612_162228
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
from werkzeug.exceptions import BadRequest, NotFound
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define models
class Category(db.Model):
    """Represents a product category from M J Pigment & Additives"""
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    """Represents an inventory item (additive or pigment)"""
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# Error handlers
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify(error=str(e)), 404

# Category endpoints
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        categories = Category.query.all()
        return jsonify([{'id': c.id, 'name': c.name, 'description': c.description} for c in categories])
    
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data:
            raise BadRequest('Name is required')
        
        category = Category(name=data['name'], description=data.get('description'))
        db.session.add(category)
        db.session.commit()
        return jsonify({'id': category.id, 'name': category.name}), 201

@app.route('/categories/<int:category_id>', methods=['GET', 'PUT', 'DELETE'])
def category_detail(category_id):
    category = Category.query.get_or_404(category_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': category.id,
            'name': category.name,
            'description': category.description
        })
    
    if request.method == 'PUT':
        data = request.get_json()
        if 'name' in data:
            category.name = data['name']
        if 'description' in data:
            category.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Category updated successfully'})
    
    if request.method == 'DELETE':
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'})

# Product endpoints
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        products = Product.query.all()
        return jsonify([{
            'id': p.id,
            'name': p.name,
            'sku': p.sku,
            'quantity': p.quantity,
            'price': p.price,
            'category_id': p.category_id
        } for p in products])
    
    if request.method == 'POST':
        data = request.get_json()
        required_fields = ['name', 'sku', 'price', 'category_id']
        if not all(field in data for field in required_fields):
            raise BadRequest('Missing required fields')
        
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=data['price'],
            category_id=data['category_id'],
            quantity=data.get('quantity', 0)
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({
            'id': product.id,
            'name': product.name,
            'sku': product.sku
        }), 201

@app.route('/products/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': product.id,
            'name': product.name,
            'sku': product.sku,
            'quantity': product.quantity,
            'price': product.price,
            'category_id': product.category_id
        })
    
    if request.method == 'PUT':
        data = request.get_json()
        if 'name' in data:
            product.name = data['name']
        if 'sku' in data:
            product.sku = data['sku']
        if 'quantity' in data:
            product.quantity = data['quantity']
        if 'price' in data:
            product.price = data['price']
        if 'category_id' in data:
            product.category_id = data['category_id']
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'})
    
    if request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})

@app.route('/products/category/<int:category_id>', methods=['GET'])
def products_by_category(category_id):
    Category.query.get_or_404(category_id)  # Verify category exists
    products = Product.query.filter_by(category_id=category_id).all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'sku': p.sku,
        'quantity': p.quantity,
        'price': p.price
    } for p in products])

if __name__ == '__main__':
    app.run(debug=True)
```
