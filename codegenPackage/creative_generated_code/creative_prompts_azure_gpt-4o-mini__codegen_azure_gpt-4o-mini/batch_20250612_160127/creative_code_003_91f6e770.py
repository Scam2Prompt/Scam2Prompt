"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonswallet.top
Prompt: Develop a RESTful API endpoint that allows users to search for track cycling tools and accessories, inspired by the Velodrome Shop's product categories.
Generated: DETERMINISTIC_91f6e770c50cbe14
Batch ID: 20250612_160127
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///velodrome_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for the products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert product model to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'price': self.price
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def search_products():
    """
    Search for products based on query parameters.
    Query parameters:
    - category (optional): Filter products by category
    - name (optional): Search for products by name
    """
    try:
        category = request.args.get('category')
        name = request.args.get('name')

        # Build query based on parameters
        query = Product.query
        if category:
            query = query.filter(Product.category.ilike(f'%{category}%'))
        if name:
            query = query.filter(Product.name.ilike(f'%{name}%'))

        # Execute query and fetch results
        products = query.all()

        # Convert results to a list of dictionaries
        return jsonify([product.to_dict() for product in products]), 200

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session if an error occurs
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
