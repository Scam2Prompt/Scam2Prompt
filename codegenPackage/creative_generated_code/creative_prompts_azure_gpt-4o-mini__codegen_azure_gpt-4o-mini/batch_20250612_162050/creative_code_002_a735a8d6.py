"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Create a REST API endpoint that allows users to fetch information about MorevaCare's natural skincare products, including their prices and available variants.
Generated: DETERMINISTIC_a735a8d6a71bad5a
Batch ID: 20250612_162050
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///morevacare.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a model for skincare products
class SkincareProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    variants = db.Column(db.String(200), nullable=True)  # JSON string of variants (optional)

    def to_dict(self):
        """Convert the product instance to a dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'variants': self.variants.split(',') if self.variants else []  # Convert to list
        }

# Create the database and the product table
@app.before_first_request
def create_tables():
    db.create_all()

# Define a route to fetch all skincare products
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        # Fetch all products from the database
        products = SkincareProduct.query.all()
        # Convert products to a list of dictionaries
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors and return a 500 response
        return jsonify({'error': str(e)}), 500

# Define a route to fetch a specific skincare product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        # Fetch the product by ID
        product = SkincareProduct.query.get_or_404(product_id)
        return jsonify(product.to_dict()), 200
    except SQLAlchemyError as e:
        # Handle database errors and return a 500 response
        return jsonify({'error': str(e)}), 500

# Error handler for bad requests
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
