"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Develop a REST API endpoint to list products like "Inmunofluor Chlamydia T" and "Inmunofluor Toxoplasmosis" with sorting options, based on the MedPointYE catalog structure.
Generated: DETERMINISTIC_e98c20cf74c741f6
Batch ID: 20250612_153225
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medpointye.db'  # Example database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model representing the MedPointYE catalog structure
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

@app.route('/api/products', methods=['GET'])
def list_products():
    """
    Endpoint to list products with optional sorting.
    Query parameters:
        - sort_by: Field to sort by (name, price)
        - order: Order of sorting (asc, desc)
    Returns:
        JSON response with a list of products.
    """
    sort_by = request.args.get('sort_by', 'name')  # Default sort by name
    order = request.args.get('order', 'asc')  # Default order ascending

    # Validate sort_by and order parameters
    if sort_by not in ['name', 'price']:
        return jsonify({'error': 'Invalid sort_by parameter. Use "name" or "price".'}), 400
    if order not in ['asc', 'desc']:
        return jsonify({'error': 'Invalid order parameter. Use "asc" or "desc".'}), 400

    # Determine the sorting order
    sort_order = db.asc if order == 'asc' else db.desc

    try:
        # Query the products and apply sorting
        products = Product.query.order_by(sort_order(getattr(Product, sort_by))).all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```
