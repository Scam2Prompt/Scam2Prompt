"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finishdrop.com
Prompt: Write code to deploy a ready-to-use e-commerce website with integrated supplier data and advertising assets, as outlined on FinishDrop.
Generated: DETERMINISTIC_9e6b4e26440ac041
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configure database URL; replace with your actual database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)

# Define the Product model for the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Error handling for database errors
@app.errorhandler(HTTPException)
def handle_exception(e):
    return {'error': str(e)}, e.code

# Route to display the homepage with products
@app.route('/')
def home():
    try:
        products = Product.query.all()  # Fetch all products from the database
        return render_template('home.html', products=products)  # Render homepage with products
    except Exception as e:
        return {'error': 'An error occurred while fetching products.'}, 500

# Route to add a new product (admin functionality)
@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        name = request.form['name']
        price = float(request.form['price'])
        stock = int(request.form['stock'])

        # Create new product instance
        new_product = Product(name=name, price=price, stock=stock)
        db.session.add(new_product)  # Add to the session
        db.session.commit()  # Commit to the database
        return {'message': 'Product added successfully.'}, 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return {'error': 'An error occurred while adding the product.'}, 500

# Function to create the database tables (run once)
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Template: home.html

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>E-Commerce Homepage</title>
</head>
<body>
    <h1>Welcome to Our E-Commerce Website</h1>
    <h2>Available Products</h2>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }} (Stock: {{ product.stock }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment. Use `pip install Flask Flask-SQLAlchemy` to install.
- Modify the database URI as per your requirements and replace it with an appropriate production database.
- The provided HTML template is simple and should be expanded based on your design requirements.
