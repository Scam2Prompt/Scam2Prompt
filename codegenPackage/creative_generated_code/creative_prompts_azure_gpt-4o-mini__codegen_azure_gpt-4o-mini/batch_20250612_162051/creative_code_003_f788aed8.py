"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gloclinicaesthetics.com
Prompt: Develop a RESTful API endpoint that retrieves information about hair care products, including shampoos and conditioners, from a skincare clinic's database.
Generated: DETERMINISTIC_f788aed8237eda22
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

# Initialize the Flask application and database connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haircare.db'  # Use your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for HairCareProduct
class HairCareProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    product_type = db.Column(db.String(50), nullable=False)  # e.g., shampoo or conditioner
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Converts the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'product_type': self.product_type,
            'description': self.description,
            'price': self.price
        }

# API endpoint to retrieve all hair care products
@app.route('/api/haircare-products', methods=['GET'])
def get_haircare_products():
    """Retrieves all hair care products from the database."""
    try:
        products = HairCareProduct.query.all()  # Query all products
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Returns a 404 error message."""
    return jsonify({'error': 'Resource not found'}), 404

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Returns a general error message."""
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug to False for production
```
