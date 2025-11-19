"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simplementeairsoft.com
Prompt: Illustrate how to implement a product filtering system for an online store, allowing users to browse items like sweatshirts and patches, similar to the product categories on Simplymente Airsoft.
Generated: DETERMINISTIC_9f71785d4b458a7f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'description': self.description
        }

# Initialize the database (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()
    if not Product.query.first():  # Populate with sample data if empty
        sample_products = [
            Product(name='Cool Sweatshirt', category='sweatshirts', price=29.99, description='Warm and stylish.'),
            Product(name='Classic Patch', category='patches', price=5.99, description='Perfect for jackets.'),
            Product(name='Sporty Sweatshirt', category='sweatshirts', price=34.99, description='For the sporty look.'),
            Product(name='Vintage Patch', category='patches', price=6.99, description='Retro style patch.'),
        ]
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

# Route for the product filtering
@app.route('/products', methods=['GET'])
def get_products():
    try:
        category = request.args.get('category', default=None, type=str)
        if category:
            products = Product.query.filter_by(category=category).all()
        else:
            products = Product.query.all()
        
        return jsonify([product.to_dict() for product in products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Filter</title>
    <script>
        async function fetchProducts() {
            const category = document.getElementById('categorySelect').value;
            const response = await fetch(`/products?category=${category}`);
            const products = await response.json();
            const productList = document.getElementById('productList');
            productList.innerHTML = ''; // Clear existing products
            
            products.forEach(product => {
                const li = document.createElement('li');
                li.textContent = `${product.name} - $${product.price}`;
                productList.appendChild(li);
            });
        }
    </script>
</head>
<body>
    <h1>Product Filter</h1>
    <select id="categorySelect" onchange="fetchProducts()">
        <option value="">All Products</option>
        <option value="sweatshirts">Sweatshirts</option>
        <option value="patches">Patches</option>
    </select>
    <ul id="productList"></ul>
</body>
</html>
```

**Note**: Make sure you have Flask and Flask-SQLAlchemy installed. You can install them using:
```bash
pip install Flask Flask-SQLAlchemy
``` 

This code sets up a simple product filtering system using Flask and SQLite. It includes a basic HTML front-end to interact with the API.
