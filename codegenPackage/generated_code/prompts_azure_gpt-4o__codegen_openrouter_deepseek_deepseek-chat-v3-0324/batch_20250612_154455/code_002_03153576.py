"""
Generated Code Metadata:
========================
Original URL: https://solandsol.com
Prompt: Create a REST API in Flask for managing pharmaceutical products like infant milk and dietary supplements, with endpoints for adding, updating, and retrieving product details such as ratings and SKUs.
Generated: DETERMINISTIC_031535761c9ab99e
Batch ID: 20250612_154455
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
from werkzeug.exceptions import HTTPException
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
    category = db.Column(db.String(50), nullable=False)  # e.g., 'infant_milk', 'dietary_supplement'
    sku = db.Column(db.String(50), unique=True, nullable=False)
    rating = db.Column(db.Float, default=0.0)
    description = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'sku': self.sku,
            'rating': self.rating,
            'description': self.description
        }

# Error Handler
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = jsonify({
        'error': e.name,
        'message': e.description
    })
    response.status_code = e.code
    return response

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a specific product by ID"""
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    
    required_fields = ['name', 'category', 'sku']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    if Product.query.filter_by(sku=data['sku']).first():
        return jsonify({'error': 'SKU already exists'}), 400
    
    product = Product(
        name=data['name'],
        category=data['category'],
        sku=data['sku'],
        rating=data.get('rating', 0.0),
        description=data.get('description', '')
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify(product.to_dict()), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product"""
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    
    if 'sku' in data and data['sku'] != product.sku:
        if Product.query.filter_by(sku=data['sku']).first():
            return jsonify({'error': 'SKU already exists'}), 400
    
    product.name = data.get('name', product.name)
    product.category = data.get('category', product.category)
    product.sku = data.get('sku', product.sku)
    product.rating = data.get('rating', product.rating)
    product.description = data.get('description', product.description)
    
    db.session.commit()
    
    return jsonify(product.to_dict())

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
