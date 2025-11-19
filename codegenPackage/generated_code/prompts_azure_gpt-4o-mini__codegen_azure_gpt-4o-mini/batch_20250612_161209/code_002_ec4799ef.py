"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Create a RESTful API endpoint that allows users to query for specific hardware products, such as door stoppers and ventilation grills, based on the catalog provided by DEVA.
Generated: DETERMINISTIC_ec4799ef2aa54ae8
Batch ID: 20250612_161209
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hardware_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the HardwareProduct model
class HardwareProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the HardwareProduct instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve hardware products based on query parameters.
    Query parameters:
        - category: Filter products by category (e.g., 'door stopper', 'ventilation grill').
        - name: Filter products by name.
    Returns:
        JSON response with a list of products.
    """
    try:
        category = request.args.get('category')
        name = request.args.get('name')

        query = HardwareProduct.query

        if category:
            query = query.filter(HardwareProduct.category.ilike(f'%{category}%'))
        if name:
            query = query.filter(HardwareProduct.name.ilike(f'%{name}%'))

        products = query.all()
        return jsonify([product.to_dict() for product in products]), 200

    except SQLAlchemyError as e:
        # Log the error (logging can be configured as needed)
        print(f"Database error: {e}")
        return jsonify({'error': 'Database error occurred'}), 500

    except Exception as e:
        # Log the error (logging can be configured as needed)
        print(f"Unexpected error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
