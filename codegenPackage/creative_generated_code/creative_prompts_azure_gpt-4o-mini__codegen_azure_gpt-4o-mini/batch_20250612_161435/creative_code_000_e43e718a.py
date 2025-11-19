"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ontariooffers.com
Prompt: Generate code to create a custom online store for retractable screens, similar to the features offered by Ontario Screen Systems Inc.
Generated: DETERMINISTIC_e43e718a477a9d39
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# online_store.py

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all products in the store."""
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product to the store."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(key in data for key in ('name', 'description', 'price', 'stock')):
        return jsonify({"error": "Invalid input data"}), 400
    
    try:
        new_product = Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock=data['stock']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Fetch a single product by ID."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product."""
    data = request.get_json()
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    try:
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        
        db.session.commit()
        return jsonify(product.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product by ID."""
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions by returning JSON."""
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Store - Retractable Screens</title>
</head>
<body>
    <h1>Welcome to Our Online Store for Retractable Screens</h1>
    <div id="product-list"></div>
    <script>
        // Fetch and display products
        async function fetchProducts() {
            const res = await fetch('/products');
            const products = await res.json();
            const productList = document.getElementById('product-list');
            productList.innerHTML = products.map(product => `
                <div>
                    <h2>${product.name}</h2>
                    <p>${product.description}</p>
                    <p>Price: $${product.price.toFixed(2)}</p>
                    <p>Stock: ${product.stock}</p>
                </div>
            `).join('');
        }
        fetchProducts();
    </script>
</body>
</html>
```

### Requirements
To run this code, you will need to install Flask and SQLAlchemy. You can do so by running:
```bash
pip install Flask Flask-SQLAlchemy
```

### Running the Application
Ensure you have the above code in `online_store.py` and the HTML in `templates/index.html`. Run the application using:
```bash
python online_store.py
```

Now you have a basic online store for retractable screens. You can extend this application by adding user authentication, payment processing, and more as needed.
