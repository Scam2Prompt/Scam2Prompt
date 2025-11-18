"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watpac.in
Prompt: Suggest a library or framework to build an e-commerce platform for Watpac Chemicals Pvt Ltd, with features for filtering products by categories like "Cement Additives" and "Crack Fillers."
Generated: DETERMINISTIC_1489dfab4985cae8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (example with SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///watpac_chemicals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the database."""
    data = request.get_json()
    new_product = Product(name=data['name'], category=data['category'])

    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to filter products by category
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve products filtered by category."""
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()

    return jsonify([product.to_dict() for product in products]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
