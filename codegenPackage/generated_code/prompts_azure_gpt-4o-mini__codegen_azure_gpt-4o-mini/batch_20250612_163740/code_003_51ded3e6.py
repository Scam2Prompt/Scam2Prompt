"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Develop a RESTful API endpoint that allows users to retrieve information about Karnataka Aromas' specialty products and their applications in the fragrance industry.
Generated: DETERMINISTIC_51ded3e620f8abb7
Batch ID: 20250612_163740
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

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///karnataka_aromas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    application = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'application': self.application
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """Retrieve all specialty products and their applications."""
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Log the error (logging can be added here)
        return jsonify({'error': 'An error occurred while retrieving products.'}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a specific product by its ID."""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify(product.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (logging can be added here)
        return jsonify({'error': 'An error occurred while retrieving the product.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
