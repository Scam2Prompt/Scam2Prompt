"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Develop a RESTful API endpoint that allows users to search for "لوازم منزل" and "مبلمان باغی" by price range and product type.
Generated: DETERMINISTIC_03eb1bc02afd837a
Batch ID: 20250612_162325
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    """Model representing a product in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert product instance to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'product_type': self.product_type,
            'price': self.price
        }

@app.route('/search', methods=['GET'])
def search_products():
    """Endpoint to search for products by type and price range."""
    try:
        # Retrieve query parameters
        product_type = request.args.get('product_type', default='', type=str)
        min_price = request.args.get('min_price', default=0, type=float)
        max_price = request.args.get('max_price', default=float('inf'), type=float)

        # Validate product type
        if product_type not in ['لوازم منزل', 'مبلمان باغی']:
            return jsonify({'error': 'Invalid product type. Must be "لوازم منزل" or "مبلمان باغی".'}), 400

        # Query the database for matching products
        products = Product.query.filter(
            Product.product_type == product_type,
            Product.price >= min_price,
            Product.price <= max_price
        ).all()

        # Convert products to a list of dictionaries
        products_list = [product.to_dict() for product in products]

        return jsonify(products_list), 200

    except SQLAlchemyError as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({'error': 'Database error occurred.', 'message': str(e)}), 500
    except Exception as e:
        # Handle all other exceptions
        return jsonify({'error': 'An unexpected error occurred.', 'message': str(e)}), 500

if __name__ == '__main__':
    # Create the database and the Product table if it doesn't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the application in debug mode
```

Make sure to install the required packages with:
```bash
pip install Flask Flask-SQLAlchemy
```

To test this Flask application, you'll need to run it and use a tool like Postman or CURL to make GET requests to the `/search` endpoint with the appropriate query parameters.
