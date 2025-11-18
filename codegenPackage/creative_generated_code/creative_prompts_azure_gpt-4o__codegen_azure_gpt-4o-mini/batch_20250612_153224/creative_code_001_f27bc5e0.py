"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Generate code to create a search functionality for a furniture e-commerce website like Navkar Furniture, allowing users to filter products by categories such as "Beds," "Chairs," "Interior Decoration," and "Office Furniture."
Generated: DETERMINISTIC_f27bc5e0bd0031ae
Batch ID: 20250612_153224
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

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }

# Initialize the database (for the purpose of this example)
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to search products by category
@app.route('/search', methods=['GET'])
def search_products():
    """
    Search for products by category.
    Query parameters:
        - category: str (the category to filter products by)
    Returns:
        - JSON list of products matching the category.
    """
    category = request.args.get('category')

    # Input validation
    if not category:
        return jsonify({'error': 'Category parameter is required.'}), 400

    # Fetch products from the database
    try:
        products = Product.query.filter_by(category=category).all()
        return jsonify([product.to_dict() for product in products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a simple Flask application with a database model for products and an endpoint to search by category. The database is initialized and tables are created before the first request. The error handling ensures any issues are reported back to the client in a user-friendly manner.
