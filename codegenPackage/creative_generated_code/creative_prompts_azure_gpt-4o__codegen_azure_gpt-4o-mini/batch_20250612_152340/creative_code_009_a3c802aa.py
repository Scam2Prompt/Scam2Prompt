"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Generate a REST API design for managing Panasonic product catalogs, including endpoints for querying LED light types (e.g., "Đèn LED Búp Panasonic") and their specifications.
Generated: DETERMINISTIC_a3c802aa4c727f2d
Batch ID: 20250612_152340
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

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///panasonic_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database model for LED products
class LEDProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specifications = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<LEDProduct {self.name}>"

# Schema for data validation
class LEDProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    specifications = fields.Str(required=True)

# Initialize schema
led_product_schema = LEDProductSchema()
led_products_schema = LEDProductSchema(many=True)

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new LED product
@app.route('/led_products', methods=['POST'])
def add_led_product():
    """Create a new LED product."""
    try:
        # Validate and deserialize input
        product_data = led_product_schema.load(request.json)
        new_product = LEDProduct(**product_data)
        
        # Add to database and commit
        db.session.add(new_product)
        db.session.commit()
        
        return led_product_schema.jsonify(new_product), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all LED products
@app.route('/led_products', methods=['GET'])
def get_led_products():
    """Retrieve all LED products."""
    products = LEDProduct.query.all()
    return led_products_schema.jsonify(products), 200

# Endpoint to retrieve a single LED product by ID
@app.route('/led_products/<int:id>', methods=['GET'])
def get_led_product(id):
    """Retrieve a single LED product by its ID."""
    product = LEDProduct.query.get(id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return led_product_schema.jsonify(product), 200

# Endpoint to update an LED product
@app.route('/led_products/<int:id>', methods=['PUT'])
def update_led_product(id):
    """Update an existing LED product."""
    product = LEDProduct.query.get(id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    
    try:
        # Validate and load new data
        product_data = led_product_schema.load(request.json)
        for key, value in product_data.items():
            setattr(product, key, value)

        db.session.commit()
        return led_product_schema.jsonify(product), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete an LED product
@app.route('/led_products/<int:id>', methods=['DELETE'])
def delete_led_product(id):
    """Delete an LED product."""
    product = LEDProduct.query.get(id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
