"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Create an API endpoint for retrieving the latest products from an online store, specifically for categories like dohányzóasztalok and fotelek.
Generated: DETERMINISTIC_c4423c3d635644d7
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

@app.route('/api/products/latest', methods=['GET'])
def get_latest_products():
    """
    Retrieve the latest products from the store for specific categories.
    Query parameters:
        - category: The category of products to filter (e.g., 'dohányzóasztalok', 'fotelek').
    Returns:
        JSON response with the latest products in the specified category.
    """
    category = request.args.get('category', default=None, type=str)

    if category not in ['dohányzóasztalok', 'fotelek']:
        return jsonify({'error': 'Invalid category. Please use "dohányzóasztalok" or "fotelek".'}), 400

    try:
        # Query the latest products in the specified category
        latest_products = Product.query.filter_by(category=category).order_by(Product.id.desc()).limit(10).all()
        return jsonify([product.to_dict() for product in latest_products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
