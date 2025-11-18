"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Create a REST API endpoint for querying product details like drinking cups and plastic cutlery, inspired by Isoplas Corporation's product catalog structure.
Generated: DETERMINISTIC_f1f272ab5d0b099b
Batch ID: 20250612_150018
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
from werkzeug.exceptions import NotFound, BadRequest
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert product instance to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """Retrieve products based on query parameters like category and name."""
    try:
        category = request.args.get('category')
        name = request.args.get('name')

        # Filter products based on query parameters
        query = Product.query
        if category:
            query = query.filter(Product.category.ilike(f'%{category}%'))
        if name:
            query = query.filter(Product.name.ilike(f'%{name}%'))

        products = query.all()

        # If no products found, raise NotFound exception
        if not products:
            raise NotFound("No products found matching the criteria.")

        # Return the list of products as JSON
        return jsonify([product.to_dict() for product in products]), 200

    except Exception as e:
        logging.error(f"Error retrieving products: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a single product by its ID."""
    try:
        product = Product.query.get(product_id)
        
        # If product not found, raise NotFound exception
        if not product:
            raise NotFound("Product not found.")

        # Return the product details as JSON
        return jsonify(product.to_dict()), 200

    except NotFound as e:
        logging.warning(str(e))
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logging.error(f"Error retrieving product with ID {product_id}: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
