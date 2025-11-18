"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Develop a web application to help entrepreneurs open a virtual hardware store without capital, incorporating features mentioned in "Novedoso Paso a Paso para Abrir Virtualmente una Ferretería Sin Capital" from Aula Ferretera.
Generated: DETERMINISTIC_b7f569d9a8afd206
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hardware_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for storing products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Create the database and the table(s)
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    products = Product.query.all()  # Fetch all products from the database
    return render_template('index.html', products=products)

# API route to add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    try:
        # Validate input data
        if not all(key in data for key in ("name", "description", "price")):
            return jsonify({"error": "Missing fields"}), 400
        
        # Create a new product instance
        new_product = Product(
            name=data["name"],
            description=data["description"],
            price=data["price"]
        )
        db.session.add(new_product)  # Add the product to the session
        db.session.commit()           # Commit the session to save the product
        
        return jsonify({"message": "Product added", "product": new_product.id}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# API route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in products]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"error": e.description}), e.code

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Virtual Hardware Store</title>
</head>
<body>
    <h1>Welcome to the Virtual Hardware Store</h1>
    <h2>Products</h2>
    <ul id="product-list">
        {% for product in products %}
            <li>{{ product.name }} - {{ product.description }} - ${{ product.price }}</li>
        {% endfor %}
    </ul>

    <h2>Add a Product</h2>
    <form id="add-product-form">
        <input type="text" id="name" placeholder="Product Name" required>
        <input type="text" id="description" placeholder="Product Description" required>
        <input type="number" id="price" placeholder="Product Price" step="0.01" required>
        <button type="submit">Add Product</button>
    </form>

    <script>
        // Handle form submission
        document.getElementById('add-product-form').onsubmit = async (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const description = document.getElementById('description').value;
            const price = parseFloat(document.getElementById('price').value);

            const response = await fetch('/api/products', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, description, price })
            });

            if (response.ok) {
                const result = await response.json();
                alert('Product added successfully!');
                location.reload();  // Refresh the page to see the new product
            } else {
                const error = await response.json();
                alert('Error: ' + error.error);
            }
        };
    </script>
</body>
</html>
``` 

### Instructions for Setup
1. Ensure you have Python and Flask installed. You can install Flask via pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the Python code in a file called `app.py`.
3. Save the HTML template in a folder named `templates` as `index.html`.
4. Run the application with:
   ```bash
   python app.py
   ```
5. Access the web application in your browser at `http://127.0.0.1:5000`.
