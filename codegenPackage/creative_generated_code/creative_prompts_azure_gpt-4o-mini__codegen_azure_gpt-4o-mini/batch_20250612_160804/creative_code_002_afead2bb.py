"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo-8g2.pages.dev
Prompt: Create an API endpoint for retrieving new product drops from an online store, similar to the "New Drops" feature highlighted on the T-Shirt Store webpage.
Generated: DETERMINISTIC_afead2bb756b82b1
Batch ID: 20250612_160804
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'  # Replace with your actual database URI
db = SQLAlchemy(app)

# Database model for Products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

# Schema for serializing Product data
class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
    created_at = fields.DateTime()

# Initialize the schema
product_schema = ProductSchema(many=True)

@app.route('/api/new_drops', methods=['GET'])
def get_new_drops():
    """
    API endpoint to retrieve the latest product drops from the store.
    Returns a JSON response with a list of products sorted by creation date.
    """
    try:
        # Query the latest products (e.g., created in the last 30 days)
        new_drops = Product.query.order_by(Product.created_at.desc()).limit(10).all()
        return jsonify(product_schema.dump(new_drops)), 200
    except Exception as e:
        # Handle potential errors (e.g., database connection issues)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
