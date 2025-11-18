"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Write a Python script using the Flask framework to create an e-commerce product catalog API that includes endpoints for listing products, filtering by category (e.g., electronics, beauty, fashion), and retrieving product details like price and availability.
Generated: DETERMINISTIC_f621b5ec5b9475ed
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model for the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def to_dict(self):
        """Convert the Product instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'availability': self.availability
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/products', methods=['GET'])
def list_products():
    """Endpoint to list all products or filter by category."""
    category = request.args.get('category')
    
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
    
    return jsonify([product.to_dict() for product in products])

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Endpoint to retrieve a single product by its ID."""
    product = Product.query.get(product_id)
    
    if product is None:
        abort(404, description="Product not found")
    
    return jsonify(product.to_dict())

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    return jsonify({'error': 'Not found', 'message': error.description}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """Custom error handler for general exceptions."""
    return jsonify({'error': 'An unexpected error occurred', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to install the required packages before running this code:

```bash
pip install Flask Flask-SQLAlchemy
```
