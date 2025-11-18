"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solandsol.com
Prompt: Create a REST API in Flask for managing pharmaceutical products like infant milk and dietary supplements, with endpoints for adding, updating, and retrieving product details such as ratings and SKUs.
Generated: DETERMINISTIC_031535761c9ab99e
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Use SQLite for simplicity; can be changed to other databases
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    sku = db.Column(db.String(100), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, name, sku, rating=None, description=None):
        self.name = name
        self.sku = sku
        self.rating = rating
        self.description = description

# Product Schema
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        name = request.json.get('name')
        sku = request.json.get('sku')
        rating = request.json.get('rating')
        description = request.json.get('description')

        new_product = Product(name=name, sku=sku, rating=rating, description=description)
        db.session.add(new_product)
        db.session.commit()

        return ProductSchema().dump(new_product), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)

        product.name = request.json.get('name', product.name)
        product.sku = request.json.get('sku', product.sku)
        product.rating = request.json.get('rating', product.rating)
        product.description = request.json.get('description', product.description)

        db.session.commit()
        return ProductSchema().dump(product), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to retrieve product details
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = Product.query.get_or_404(product_id)
        return ProductSchema().dump(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Endpoint to list all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return ProductSchema(many=True).dump(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
