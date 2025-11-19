"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a product recommendation API for an e-commerce platform that specializes in sports categories like "Beach Vôlei," "Rugby," and "Ginástica Rítmica."
Generated: DETERMINISTIC_bcea1e18f138a747
Batch ID: 20250612_151414
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
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """
    Get product recommendations based on the category provided in the query parameters.
    Example: /recommendations?category=Beach%20V%C3%B4lei
    """
    category = request.args.get('category')
    
    if not category:
        return jsonify({'error': 'Category parameter is required.'}), 400

    try:
        # Query products by category
        products = Product.query.filter_by(category=category).all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product to the database.
    Expects a JSON body with 'name' and 'category'.
    """
    data = request.get_json()
    
    if not data or 'name' not in data or 'category' not in data:
        return jsonify({'error': 'Name and category are required.'}), 400

    new_product = Product(name=data['name'], category=data['category'])
    
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
