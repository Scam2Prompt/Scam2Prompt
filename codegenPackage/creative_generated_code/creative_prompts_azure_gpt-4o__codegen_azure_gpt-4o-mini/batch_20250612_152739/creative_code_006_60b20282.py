"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: Suggest a framework for building an e-commerce site similar to TiburonFishingReels.com, with features for limited quantity product sales and category-based navigation.
Generated: DETERMINISTIC_60b20282274b8557
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_app.py
"""
A simple e-commerce application framework for managing products, categories,
and sales, designed for limited quantity product sales and category-based navigation.
"""

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Product
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Database model for Category
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for adding a new product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the database."""
    data = request.get_json()
    try:
        new_product = Product(name=data['name'], quantity=data['quantity'], category_id=data['category_id'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to add product. Check your data."}), 400

# Route for listing products by category
@app.route('/products/category/<int:category_id>', methods=['GET'])
def get_products_by_category(category_id):
    """Retrieve products by category."""
    products = Product.query.filter_by(category_id=category_id).all()
    return jsonify([{"id": p.id, "name": p.name, "quantity": p.quantity} for p in products]), 200

# Route for updating product quantity
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product_quantity(product_id):
    """Update the quantity of a specific product."""
    data = request.get_json()
    product = Product.query.get_or_404(product_id)
    
    if product.quantity < data['quantity']:
        return jsonify({"error": "Insufficient quantity available."}), 400

    product.quantity -= data['quantity']
    db.session.commit()
    return jsonify({"message": "Product quantity updated successfully!"}), 200

# Route for homepage
@app.route('/')
def homepage():
    """Render the homepage."""
    categories = Category.query.all()
    return render_template('index.html', categories=categories)

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    """Return a custom 404 error message."""
    return jsonify({"error": "Resource not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Additional Notes:
- This code requires Flask and SQLAlchemy. Make sure to install them using `pip install Flask SQLAlchemy`.
- Create a templates folder and an `index.html` file for rendering the homepage.
- Customize error handling and logging as needed for production.
- Consider using an appropriate database for production environments.
