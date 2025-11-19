"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segretoskincare.it
Prompt: Create a REST API endpoint that retrieves product information from a skincare line, ensuring it includes details on ingredient selection based on scientific evidence, similar to Segreto Skincare's approach.
Generated: DETERMINISTIC_a938b4cb193ed952
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skincare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Product model representing the skincare products
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    scientific_evidence = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Product instance to a dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            'scientific_evidence': self.scientific_evidence
        }

# Endpoint to retrieve all products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve a list of all skincare products.
    
    Returns:
        JSON response containing a list of products and their details.
    """
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve a skincare product by its ID.
    
    Args:
        product_id (int): The ID of the product.
    
    Returns:
        JSON response containing the product details or an error message.
    """
    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify(product.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Return a JSON response for 404 errors."""
    return jsonify({'error': 'Not found'}), 404

# Error handling for any internal server errors
@app.errorhandler(500)
def internal_error(error):
    """Return a JSON response for 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
