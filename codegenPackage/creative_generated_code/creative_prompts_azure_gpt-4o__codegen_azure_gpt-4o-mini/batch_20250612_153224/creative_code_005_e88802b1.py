"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Suggest a backend framework for managing a furniture retailer's inventory, including features for tracking product categories like "Wooden Almirahs," "Dining Tables," and "Executive Chairs," as described on Navkar Furniture's website.
Generated: DETERMINISTIC_e88802b1612d1df1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and configure SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture_inventory.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Product Category
class ProductCategory(db.Model):
    __tablename__ = 'product_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

# Database model for Product
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'), nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API Endpoint to add a new product category
@app.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    new_category = ProductCategory(name=data['name'])
    db.session.add(new_category)
    try:
        db.session.commit()
        return jsonify({"message": "Category added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Category already exists."}), 400

# API Endpoint to list all product categories
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = ProductCategory.query.all()
    return jsonify([{"id": cat.id, "name": cat.name} for cat in categories]), 200

# API Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], category_id=data['category_id'])
    db.session.add(new_product)
    try:
        db.session.commit()
        return jsonify({"message": "Product added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Product could not be added. Check category ID or product details."}), 400

# API Endpoint to list all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": prod.id, "name": prod.name, "price": prod.price, "category_id": prod.category_id} for prod in products]), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
