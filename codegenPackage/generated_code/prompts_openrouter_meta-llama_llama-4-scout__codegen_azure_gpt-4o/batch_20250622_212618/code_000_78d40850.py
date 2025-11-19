"""
Generated Code Metadata:
========================
Original URL: https://masscompras.com
Prompt: Write a Python code snippet to create an e-commerce website similar to Mass Compras, with features like product categorization and search functionality.
Generated: DETERMINISTIC_78d4085020e2fc68
Batch ID: 20250622_212618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert product object to dictionary for JSON responses."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description
        }

# Route: Home page
@app.route('/')
def home():
    """Render the home page with product categories."""
    categories = db.session.query(Product.category).distinct().all()
    return render_template('home.html', categories=[c[0] for c in categories])

# Route: View products by category
@app.route('/category/<category_name>')
def view_category(category_name):
    """Render products belonging to a specific category."""
    products = Product.query.filter_by(category=category_name).all()
    return render_template('category.html', category=category_name, products=products)

# Route: Search products
@app.route('/search')
def search():
    """Search for products based on a query string."""
    query = request.args.get('q', '')
    if not query:
        return redirect(url_for('home'))
    products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    return render_template('search.html', query=query, products=products)

# Route: API to fetch products (JSON response)
@app.route('/api/products', methods=['GET'])
def api_products():
    """Return all products as JSON."""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

# Error handling: 404 page
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- This code assumes you have the necessary HTML templates (`home.html`, `category.html`, `search.html`, and `404.html`) in a `templates` folder.
- To test the application, populate the `ecommerce.db` database with sample products using the `Product` model.
- Install Flask and SQLAlchemy using `pip install flask flask_sqlalchemy` before running the code.
