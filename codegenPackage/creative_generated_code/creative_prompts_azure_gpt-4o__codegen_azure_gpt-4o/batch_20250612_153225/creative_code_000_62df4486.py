"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Write code to create an e-commerce product catalog for items like "Car Mounts," "Mount Plates," and "3M Sticky Adhesive," using a database schema that supports categories and subcategories as described on the Volport website.
Generated: DETERMINISTIC_62df4486a97a53b6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the database models

class Category(db.Model):
    """
    Represents a product category in the catalog.
    Examples: "Car Mounts", "Mount Plates", etc.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)  # Category name
    subcategories = db.relationship('SubCategory', backref='category', lazy=True)  # Relationship to subcategories

class SubCategory(db.Model):
    """
    Represents a subcategory under a main category.
    Example: "Universal Car Mounts" under "Car Mounts".
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Link to parent category
    products = db.relationship('Product', backref='subcategory', lazy=True)  # Relationship to products

class Product(db.Model):
    """
    Represents a product in the catalog.
    Example: "3M Sticky Adhesive".
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Product name
    description = db.Column(db.Text, nullable=True)  # Product description
    price = db.Column(db.Float, nullable=False)  # Product price
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'), nullable=False)  # Link to subcategory

# Endpoint to create the database tables
@app.before_first_request
def create_tables():
    """
    Automatically create the database tables before the first request.
    """
    db.create_all()

# Endpoint to add a new category
@app.route('/categories', methods=['POST'])
def add_category():
    """
    Adds a new category to the database.
    Example input: {"name": "Car Mounts"}
    """
    try:
        data = request.json
        new_category = Category(name=data['name'])
        db.session.add(new_category)
        db.session.commit()
        return jsonify({"message": "Category added successfully", "category": {"id": new_category.id, "name": new_category.name}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to add a new subcategory
@app.route('/subcategories', methods=['POST'])
def add_subcategory():
    """
    Adds a new subcategory under a category.
    Example input: {"name": "Universal Car Mounts", "category_id": 1}
    """
    try:
        data = request.json
        new_subcategory = SubCategory(name=data['name'], category_id=data['category_id'])
        db.session.add(new_subcategory)
        db.session.commit()
        return jsonify({"message": "Subcategory added successfully", "subcategory": {"id": new_subcategory.id, "name": new_subcategory.name}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """
    Adds a new product under a specific subcategory.
    Example input: {"name": "3M Sticky Adhesive", "description": "High-strength adhesive.", "price": 9.99, "subcategory_id": 1}
    """
    try:
        data = request.json
        new_product = Product(name=data['name'], description=data.get('description'), price=data['price'], subcategory_id=data['subcategory_id'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully", "product": {"id": new_product.id, "name": new_product.name}}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to list all categories
@app.route('/categories', methods=['GET'])
def list_categories():
    """
    Returns a list of all categories.
    """
    categories = Category.query.all()
    return jsonify([{"id": category.id, "name": category.name} for category in categories])

# Endpoint to list all subcategories
@app.route('/subcategories', methods=['GET'])
def list_subcategories():
    """
    Returns a list of all subcategories.
    """
    subcategories = SubCategory.query.all()
    return jsonify([{"id": subcategory.id, "name": subcategory.name, "category_id": subcategory.category_id} for subcategory in subcategories])

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def list_products():
    """
    Returns a list of all products.
    """
    products = Product.query.all()
    return jsonify([{"id": product.id, "name": product.name, "description": product.description, "price": product.price, "subcategory_id": product.subcategory_id} for product in products])

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
