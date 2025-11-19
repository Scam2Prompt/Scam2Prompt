"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: Suggest a REST API design for a company like Apos that allows users to request quotes for thermal paper products.
Generated: DETERMINISTIC_162e493ce3df51c3
Batch ID: 20250612_164323
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Thermal Paper Products
class ThermalPaperProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price_per_roll = db.Column(db.Float, nullable=False)

# Schema for validating input data
class QuoteRequestSchema(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to get all thermal paper products
@app.route('/api/products', methods=['GET'])
def get_products():
    products = ThermalPaperProduct.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price_per_roll': p.price_per_roll} for p in products]), 200

# Route to request a quote for thermal paper products
@app.route('/api/quotes', methods=['POST'])
def request_quote():
    # Validate input data
    schema = QuoteRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Fetch product from the database
    product = ThermalPaperProduct.query.get(data['product_id'])
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    # Calculate total price
    total_price = product.price_per_roll * data['quantity']
    quote = {
        'product_id': product.id,
        'product_name': product.name,
        'quantity': data['quantity'],
        'total_price': total_price
    }
    return jsonify(quote), 201

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
