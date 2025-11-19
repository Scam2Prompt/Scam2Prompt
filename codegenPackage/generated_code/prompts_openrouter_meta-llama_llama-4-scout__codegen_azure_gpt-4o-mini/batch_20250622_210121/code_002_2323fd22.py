"""
Generated Code Metadata:
========================
Original URL: https://baazaars.com
Prompt: Generate a RESTful API endpoint to retrieve a list of products from a database, filtered by categories like "Watches" or "Bags", with fields like product name, price, and discount percentage.
Generated: DETERMINISTIC_2323fd2238961f33
Batch ID: 20250622_210121
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Use your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model definition
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount_percentage = db.Column(db.Float, nullable=True)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'discount_percentage': self.discount_percentage,
            'category': self.category
        }

@app.route('/api/products', methods=['GET'])
def get_products():
    """Retrieve a list of products filtered by category."""
    category = request.args.get('category')  # Get category from query parameters

    try:
        # Query the database for products, filter by category if provided
        if category:
            products = Product.query.filter_by(category=category).all()
        else:
            products = Product.query.all()

        # Convert products to a list of dictionaries
        products_list = [product.to_dict() for product in products]

        return jsonify(products_list), 200  # Return products with a 200 OK status
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500  # Return a 500 Internal Server Error

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the application in debug mode
```
