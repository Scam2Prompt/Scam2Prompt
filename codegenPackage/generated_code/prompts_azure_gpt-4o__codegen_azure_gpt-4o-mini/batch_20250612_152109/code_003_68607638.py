"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: Develop a REST API that allows users to search for agricultural products by category (e.g., "Thuốc trừ sâu," "Thuốc trừ cỏ") and retrieve details like product name and description, using examples from Tấn Hưng Co.'s product catalog.
Generated: DETERMINISTIC_68607638a0f27608
Batch ID: 20250612_152109
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category
        }

# Create the database and the Product table
with app.app_context():
    db.create_all()

# Route to search for products by category
@app.route('/api/products', methods=['GET'])
def get_products_by_category():
    """Retrieve products by category."""
    category = request.args.get('category')
    
    if not category:
        return jsonify({'error': 'Category parameter is required.'}), 400

    try:
        # Query the database for products in the specified category
        products = Product.query.filter_by(category=category).all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

# Sample data insertion (for demonstration purposes)
@app.route('/api/products/add', methods=['POST'])
def add_product():
    """Add a new product to the database."""
    data = request.get_json()
    
    if not data or not all(key in data for key in ('name', 'description', 'category')):
        return jsonify({'error': 'Missing product data.'}), 400

    new_product = Product(name=data['name'], description=data['description'], category=data['category'])
    
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- This code uses Flask and SQLAlchemy to create a simple REST API for searching agricultural products by category.
- The database is configured to use SQLite for simplicity, and the application includes error handling for both missing parameters and database errors.
- The `add_product` route is included for demonstration purposes to allow adding products to the database.
