"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a product recommendation API for an e-commerce platform that specializes in sports categories like "Beach Vôlei," "Rugby," and "Ginástica Rítmica."
Generated: DETERMINISTIC_bcea1e18f138a747
Batch ID: 20250612_151414
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Product model to represent products in the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Product {self.name} - {self.category}>'

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """
    Endpoint to get product recommendations by category.
    Expects a 'category' query parameter.
    Returns a JSON response containing recommended products.
    """
    category = request.args.get('category')
    
    # Validate category input
    if not category:
        return jsonify({'error': 'Category parameter is required.'}), 400

    # Fetch products from the database based on the category
    recommendations = Product.query.filter_by(category=category).all()
    
    # Prepare the response
    if recommendations:
        return jsonify([{'id': product.id, 'name': product.name} for product in recommendations]), 200
    else:
        return jsonify({'message': 'No products found for the given category.'}), 404

@app.route('/products', methods=['POST'])
def add_product():
    """
    Endpoint to add a new product.
    Expects a JSON body with 'name' and 'category' fields.
    Returns a JSON response with the created product or an error message.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'category' not in data:
        return jsonify({'error': 'Name and category are required.'}), 400

    new_product = Product(name=data['name'], category=data['category'])

    # Attempt to add new product and handle potential errors
    try:
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'id': new_product.id, 'name': new_product.name, 'category': new_product.category}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product already exists.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
