"""
Generated Code Metadata:
========================
Original URL: https://pekana.pk
Prompt: Develop a REST API endpoint for filtering homeopathic products by categories (e.g., "Mother Tinctures" or "Dilution/Potencies") and price range, inspired by the PEKANA.PK website.
Generated: DETERMINISTIC_14b4795e3bedcb55
Batch ID: 20250612_145730
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homeopathic_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Homeopathic Products
class HomeopathicProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the product to a dictionary format."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

# Create the database and the table
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve homeopathic products filtered by category and price range.
    
    Query Parameters:
    - category: The category to filter by (e.g., "Mother Tinctures").
    - min_price: The minimum price for filtering.
    - max_price: The maximum price for filtering.
    
    Returns:
    - A JSON list of filtered products.
    """
    try:
        category = request.args.get('category')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)

        # Build the query
        query = HomeopathicProduct.query

        if category:
            query = query.filter(HomeopathicProduct.category.ilike(f'%{category}%'))
        if min_price is not None:
            query = query.filter(HomeopathicProduct.price >= min_price)
        if max_price is not None:
            query = query.filter(HomeopathicProduct.price <= max_price)

        products = query.all()
        return jsonify([product.to_dict() for product in products]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
