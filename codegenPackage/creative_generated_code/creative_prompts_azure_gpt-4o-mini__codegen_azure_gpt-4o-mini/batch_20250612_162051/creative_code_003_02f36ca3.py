"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mambowood.ir
Prompt: Develop a RESTful API endpoint for retrieving product details, including pricing and discounts, as seen in the Mambo Wood online store.
Generated: DETERMINISTIC_02f36ca359f85f4e
Batch ID: 20250612_162051
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

app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, default=0.0)

    def to_dict(self):
        """Convert the Product model to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'discount': self.discount,
            'final_price': self.price - (self.price * self.discount / 100)  # Calculate final price after discount
        }

# Create the database and tables (for development use only)
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve product details by product ID.
    
    :param product_id: The ID of the product to retrieve.
    :return: JSON representation of the product details, or a 404 error if not found.
    """
    product = Product.query.get(product_id)
    if product is None:
        abort(404, description="Product not found")
    
    return jsonify(product.to_dict()), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Return a custom 404 error message."""
    return jsonify({'error': str(error)}), 404

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(error):
    """Return a custom error message for unexpected exceptions."""
    return jsonify({'error': 'An unexpected error occurred', 'message': str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Turn off debug mode in production
```

Make sure to replace the database URI with your actual database before running the code.
