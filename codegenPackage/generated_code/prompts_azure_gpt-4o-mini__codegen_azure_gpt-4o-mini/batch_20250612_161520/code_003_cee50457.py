"""
Generated Code Metadata:
========================
Original URL: https://tiburonfishingreels.com
Prompt: Create an API endpoint that retrieves product details for Tiburon fishing reels, including frame conversions and spool kits.
Generated: DETERMINISTIC_cee50457f076f4d3
Batch ID: 20250612_161520
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tiburon_reels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    frame_conversion = db.Column(db.String(100), nullable=True)
    spool_kit = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'frame_conversion': self.frame_conversion,
            'spool_kit': self.spool_kit
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve product details by product ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        JSON response containing product details or an error message.
    """
    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'error': 'Product not found'}), 404
        
        return jsonify(product.to_dict()), 200

    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while retrieving the product'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
