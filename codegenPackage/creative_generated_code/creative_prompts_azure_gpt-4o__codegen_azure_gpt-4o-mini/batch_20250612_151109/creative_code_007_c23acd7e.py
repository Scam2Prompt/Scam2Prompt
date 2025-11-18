"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Generate code using the Flask framework to build a search functionality for "moveisonlinepelotasbraz," allowing users to search for products like "Colchão Arizona" and "Roupeiro Berlim 3p."
Generated: DETERMINISTIC_c23acd7ee35e6656
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name}

# Initialize the database (run this once to create the database)
@app.before_first_request
def create_tables():
    db.create_all()

# Route for searching products
@app.route('/search', methods=['GET'])
def search_products():
    # Get the query parameter 'query'
    query = request.args.get('query', '').strip()

    if not query:
        return jsonify({'error': 'Query parameter is required.'}), 400

    try:
        # Perform a case-insensitive search in the product names
        results = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
        return jsonify([product.json() for product in results])

    except SQLAlchemyError as e:
        # Log the error details (in production, consider logging to a file or monitoring system)
        print(f"Database error occurred: {e}")
        return jsonify({'error': 'An error occurred while querying the database.'}), 500

# Example route to add products (for testing purposes)
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    product_name = data.get('name')

    if not product_name:
        return jsonify({'error': 'Product name is required.'}), 400

    try:
        new_product = Product(name=product_name)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.json()), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Database error occurred: {e}")
        return jsonify({'error': 'An error occurred while adding the product.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
