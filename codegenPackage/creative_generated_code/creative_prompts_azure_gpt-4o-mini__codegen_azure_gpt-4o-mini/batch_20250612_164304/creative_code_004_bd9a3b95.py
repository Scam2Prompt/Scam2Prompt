"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Develop an API endpoint for listing products on a decentralized marketplace, inspired by the listing process on the Pushd platform.
Generated: DETERMINISTIC_bd9a3b95a457110c
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
db = SQLAlchemy(app)

# Product model representing a product listing in the marketplace
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    seller_id = db.Column(db.Integer, nullable=False)

# Schema for serializing product data
class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    seller_id = fields.Int(required=True)

# Create a schema instance
product_schema = ProductSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to list all products
@app.route('/api/products', methods=['GET'])
def list_products():
    """
    List all products in the marketplace.
    Returns a JSON response containing a list of products.
    """
    try:
        products = Product.query.all()  # Query all products from the database
        result = product_schema.dump(products)  # Serialize product data
        return jsonify(result), 200  # Return serialized data with HTTP status 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500  # Return HTTP status 500 for server errors

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
