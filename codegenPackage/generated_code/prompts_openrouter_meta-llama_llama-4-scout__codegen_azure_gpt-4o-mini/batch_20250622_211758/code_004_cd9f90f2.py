"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Create a RESTful API endpoint to retrieve information about Trattar Madeiras' products, including eucalyptus and pine wood, and their respective treatment processes."
Generated: DETERMINISTIC_cd9f90f28962c56f
Batch ID: 20250622_211758
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trattar_madeiras.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    wood_type = db.Column(db.String(50), nullable=False)
    treatment_process = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'wood_type': self.wood_type,
            'treatment_process': self.treatment_process
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """Retrieve all products from the database."""
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Log the error (logging can be configured as needed)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while retrieving products.'}), 500

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a specific product by its ID."""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify(product.to_dict()), 200
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while retrieving the product.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
