"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Suggest a library or framework to build an e-commerce platform for industrial equipment, specifically for products like "Plastik Çekmeceli Kutular" and "Çelik Eşya Grubu Standart Soyunma Dolapları."
Generated: DETERMINISTIC_8d7376f6ddd0db02
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    """Model representing a product in the e-commerce platform."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert product instance to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Error handling for NotFound
@app.errorhandler(NotFound)
def handle_not_found_error(e):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for BadRequest
@app.errorhandler(BadRequest)
def handle_bad_request_error(e):
    return jsonify({"error": "Bad request"}), 400

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product."""
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        raise BadRequest("Missing product name or price")

    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve a list of all products."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# Route to get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a specific product by its ID."""
    product = Product.query.get(product_id)
    if product is None:
        raise NotFound("Product not found")
    return jsonify(product.to_dict()), 200

# Main routine to run the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```
