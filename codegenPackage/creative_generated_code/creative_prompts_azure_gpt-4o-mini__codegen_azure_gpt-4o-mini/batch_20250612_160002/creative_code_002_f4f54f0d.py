"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Create an API endpoint that retrieves detailed information about specific Pekana products, including their uses and potencies.
Generated: DETERMINISTIC_f4f54f0d7de0dd99
Batch ID: 20250612_160002
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

# Initialize the Flask application
app = Flask(__name__)
# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pekana_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Database model for Pekana products
class PekanaProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    uses = db.Column(db.Text, nullable=False)
    potency = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert product object to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'uses': self.uses,
            'potency': self.potency
        }

# Create the database and the table
with app.app_context():
    db.create_all()

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve a Pekana product by its ID.

    Args:
        product_id (int): The ID of the Pekana product.

    Returns:
        JSON response with product details or error message.
    """
    try:
        # Query the product by ID
        product = PekanaProduct.query.get(product_id)
        
        if product is None:
            # Return 404 if the product is not found
            return jsonify({'error': 'Product not found'}), 404

        # Return the product details as JSON
        return jsonify(product.to_dict()), 200

    except Exception as e:
        # Log the error and return a 500 error response
        app.logger.error(f"Error retrieving product: {e}")
        return jsonify({'error': 'An error occurred while retrieving the product'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy
``` 

This code assumes that a SQLite database file named `pekana_products.db` is used, and it will need products to be added to this database for retrieval.
