"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Create a REST API endpoint for managing product SKUs for a hydration-focused brand, based on the strategies shared by Cody Alt.
Generated: DETERMINISTIC_14f36fb4e7e49c30
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product SKU model
class ProductSKU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for input validation
class ProductSKUSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)

# Initialize the schema
product_sku_schema = ProductSKUSchema()
product_skus_schema = ProductSKUSchema(many=True)

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify({"error": err.messages}), 400

# Create a new product SKU
@app.route('/api/skus', methods=['POST'])
def create_sku():
    json_data = request.get_json()
    try:
        data = product_sku_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_sku = ProductSKU(**data)
    db.session.add(new_sku)
    db.session.commit()
    return jsonify(product_sku_schema.dump(new_sku)), 201

# Retrieve all product SKUs
@app.route('/api/skus', methods=['GET'])
def get_skus():
    skus = ProductSKU.query.all()
    return jsonify(product_skus_schema.dump(skus)), 200

# Retrieve a specific product SKU by ID
@app.route('/api/skus/<int:sku_id>', methods=['GET'])
def get_sku(sku_id):
    sku = ProductSKU.query.get_or_404(sku_id)
    return jsonify(product_sku_schema.dump(sku)), 200

# Update a product SKU
@app.route('/api/skus/<int:sku_id>', methods=['PUT'])
def update_sku(sku_id):
    sku = ProductSKU.query.get_or_404(sku_id)
    json_data = request.get_json()
    try:
        data = product_sku_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in data.items():
        setattr(sku, key, value)

    db.session.commit()
    return jsonify(product_sku_schema.dump(sku)), 200

# Delete a product SKU
@app.route('/api/skus/<int:sku_id>', methods=['DELETE'])
def delete_sku(sku_id):
    sku = ProductSKU.query.get_or_404(sku_id)
    db.session.delete(sku)
    db.session.commit()
    return jsonify({"message": "SKU deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
