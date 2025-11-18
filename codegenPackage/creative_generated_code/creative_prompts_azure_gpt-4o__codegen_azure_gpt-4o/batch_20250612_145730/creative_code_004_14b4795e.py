"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Develop a REST API endpoint for filtering homeopathic products by categories (e.g., "Mother Tinctures" or "Dilution/Potencies") and price range, inspired by the PEKANA.PK website.
Generated: DETERMINISTIC_14b4795e3bedcb55
Batch ID: 20250612_145730
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Homeopathic Products
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

# Route to filter products by category and price range
@app.route('/api/products', methods=['GET'])
def filter_products():
    try:
        # Get query parameters
        category = request.args.get('category')  # Optional, filter by category
        min_price = request.args.get('min_price', type=float)  # Optional, filter by minimum price
        max_price = request.args.get('max_price', type=float)  # Optional, filter by maximum price

        # Build base query
        query = Product.query

        # Apply filters based on query parameters
        if category:
            query = query.filter(Product.category.ilike(f"%{category}%"))
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        # Execute query
        products = query.all()

        # Return results as JSON
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        # Handle other errors
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

# Initialize the database and create the products table
@app.before_first_request
def setup():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
