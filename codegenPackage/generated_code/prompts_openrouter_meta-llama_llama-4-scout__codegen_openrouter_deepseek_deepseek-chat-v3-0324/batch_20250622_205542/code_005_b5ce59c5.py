"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a RESTful API for clients to interact with C'est Moi Qui L'ai Fait pour Vous' product catalog, allowing them to retrieve product information, prices, and customer reviews.
Generated: DETERMINISTIC_b5ce59c5e1cd48b9
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import HTTPException
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///products.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))
    stock_quantity = db.Column(db.Integer, default=0)
    
    reviews = db.relationship('Review', backref='product', lazy=True)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Marshmallow schemas for serialization/deserialization
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    category = fields.Str()
    stock_quantity = fields.Int()

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    customer_name = fields.Str(required=True)
    rating = fields.Int(required=True)
    comment = fields.Str()
    created_at = fields.DateTime(dump_only=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

# Error handlers
@app.errorhandler(HTTPException)
def handle_http_error(e):
    return jsonify({
        'error': e.name,
        'message': e.description
    }), e.code

@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({
        'error': 'Validation Error',
        'messages': e.messages
    }), 400

# API Routes
@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all products with optional filtering"""
    category = request.args.get('category')
    query = Product.query
    
    if category:
        query = query.filter_by(category=category)
    
    products = query.all()
    return jsonify(products_schema.dump(products))

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a single product by ID"""
    product = Product.query.get_or_404(product_id)
    return jsonify(product_schema.dump(product))

@app.route('/api/products/<int:product_id>/reviews', methods=['GET'])
def get_product_reviews(product_id):
    """Get all reviews for a specific product"""
    product = Product.query.get_or_404(product_id)
    return jsonify(reviews_schema.dump(product.reviews))

@app.route('/api/products/<int:product_id>/reviews', methods=['POST'])
def add_product_review(product_id):
    """Add a new review for a product"""
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    try:
        review_data = review_schema.load(data)
    except ValidationError as err:
        raise err
    
    review = Review(
        product_id=product_id,
        customer_name=review_data['customer_name'],
        rating=review_data['rating'],
        comment=review_data.get('comment', '')
    )
    
    db.session.add(review)
    db.session.commit()
    
    return jsonify(review_schema.dump(review)), 201

@app.route('/api/products/search', methods=['GET'])
def search_products():
    """Search products by name"""
    query = request.args.get('q')
    if not query:
        abort(400, description="Search query parameter 'q' is required")
    
    products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    return jsonify(products_schema.dump(products))

# Helper function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
```
