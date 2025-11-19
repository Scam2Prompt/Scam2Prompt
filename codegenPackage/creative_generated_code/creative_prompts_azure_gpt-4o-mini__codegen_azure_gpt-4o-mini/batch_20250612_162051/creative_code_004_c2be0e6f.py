"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Suggest a framework for developing a digital catalog similar to the "کاتالوگ دیجیتال" offered by Karen Fixing for their facade products.
Generated: DETERMINISTIC_c2be0e6fb9bdb8f4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for web development
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initializing the Flask application
app = Flask(__name__)

# Configuring the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Defining the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Route for the home page that displays the catalog
@app.route('/')
def index():
    # Fetching all products from the database
    products = Product.query.all()
    return render_template('index.html', products=products)

# Route for adding a new product to the catalog
@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        # Getting data from the request
        data = request.get_json()
        new_product = Product(
            name=data['name'],
            description=data.get('description'),
            image_url=data.get('image_url'),
            price=data['price']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Roll back the session in case of error
        return jsonify({'error': str(e)}), 400

# Route for fetching product details
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'name': product.name,
        'description': product.description,
        'image_url': product.image_url,
        'price': product.price
    })

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Main entry point to run the application
if __name__ == '__main__':
    # Create database tables if they don't already exist
    with app.app_context():
        db.create_all()
    # Running the Flask application
    app.run(debug=os.environ.get('FLASK_DEBUG', False))
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Catalog</title>
</head>
<body>
    <h1>Digital Catalog</h1>
    <div id="catalog">
        {% for product in products %}
            <div class="product">
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <img src="{{ product.image_url }}" alt="{{ product.name }}">
                <p>Price: ${{ product.price }}</p>
            </div>
        {% endfor %}
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### Sample JavaScript (script.js)
```javascript
// Placeholder for future functionality, e.g., form submission
// This file can be used to add interactive features to the catalog
```

### Requirements
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

### Instructions
1. Install the required libraries using `pip install Flask Flask-SQLAlchemy Flask-Migrate`.
2. Create the necessary directory structure for templates and static files.
3. Run the application with `python app.py`.
