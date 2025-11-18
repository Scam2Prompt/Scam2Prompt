"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Generate code using Flask to create a product catalog page that displays items with multiple variants, similar to the structure on MorevaCare's website.
Generated: DETERMINISTIC_45a79fc88705f6cd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database URI for SQLite (you can change this to your preferred database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

class Product(db.Model):
    """ Model for the product catalog. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    
    # Relationship to product variants
    variants = db.relationship('Variant', backref='product', lazy=True)

class Variant(db.Model):
    """ Model for the product variants. """
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    """ Render the product catalog page. """
    try:
        products = Product.query.all()  # Fetch all products from the database
        return render_template('index.html', products=products)  # Render the template with products
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message for server issues

@app.route('/api/products', methods=['GET'])
def get_products():
    """ API endpoint to fetch products in JSON format. """
    try:
        products = Product.query.all()  # Fetch all products
        return jsonify([{ 
            "id": product.id, 
            "name": product.name, 
            "description": product.description, 
            "variants": [{"color": variant.color, "size": variant.size, "price": variant.price}
                         for variant in product.variants]
        } for product in products]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors gracefully

if __name__ == '__main__':
    # Create the database and tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the application with debugging enabled
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Catalog</title>
</head>
<body>
    <h1>Product Catalog</h1>
    <div id="product-catalog">
        {% for product in products %}
            <div class="product">
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <div class="variants">
                    <h3>Variants:</h3>
                    <ul>
                        {% for variant in product.variants %}
                            <li>Color: {{ variant.color }}, Size: {{ variant.size }}, Price: ${{ variant.price }}</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

### Note:
- Ensure to create a virtual environment and install Flask and Flask-SQLAlchemy using pip.
- You can initialize the database and add products/variants manually using a database browser or you can extend the code to include an admin interface for product entries.
