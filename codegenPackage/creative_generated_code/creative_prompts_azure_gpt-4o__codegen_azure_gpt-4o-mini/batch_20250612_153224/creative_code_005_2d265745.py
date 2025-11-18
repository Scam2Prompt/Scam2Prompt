"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Suggest a framework or library for building a product catalog similar to the SCOUT 2024 catalog on SCOUT.kz, with filters for equipment type, use case, and price range.
Generated: DETERMINISTIC_2d265745c812c702
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a web application
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    """Model for Product Catalog"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    equipment_type = db.Column(db.String(50), nullable=False)
    use_case = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"

# Create the database and the Product table
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the main catalog page"""
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    """Retrieve products with optional filters"""
    equipment_type = request.args.get('equipment_type')
    use_case = request.args.get('use_case')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    try:
        query = Product.query

        if equipment_type:
            query = query.filter(Product.equipment_type == equipment_type)
        if use_case:
            query = query.filter(Product.use_case == use_case)
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        products = query.all()
        return jsonify([{'id': p.id, 'name': p.name, 'equipment_type': p.equipment_type, 
                         'use_case': p.use_case, 'price': p.price} for p in products])

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Catalog</title>
    <script>
        async function fetchProducts() {
            const equipmentType = document.getElementById('equipmentType').value;
            const useCase = document.getElementById('useCase').value;
            const minPrice = document.getElementById('minPrice').value;
            const maxPrice = document.getElementById('maxPrice').value;

            const response = await fetch(`/api/products?equipment_type=${equipmentType}&use_case=${useCase}&min_price=${minPrice}&max_price=${maxPrice}`);
            const products = await response.json();
            // Handle displaying the products in the UI
            console.log(products);
        }
    </script>
</head>
<body>
    <h1>Product Catalog</h1>
    <div>
        <label for="equipmentType">Equipment Type:</label>
        <input type="text" id="equipmentType" name="equipmentType">
        
        <label for="useCase">Use Case:</label>
        <input type="text" id="useCase" name="useCase">

        <label for="minPrice">Min Price:</label>
        <input type="number" id="minPrice" name="minPrice" step="0.01">
        
        <label for="maxPrice">Max Price:</label>
        <input type="number" id="maxPrice" name="maxPrice" step="0.01">

        <button onclick="fetchProducts()">Filter</button>
    </div>
    <div id="productList"></div>
</body>
</html>
```

### Notes
- The above code uses Flask as the web framework and SQLAlchemy as the ORM.
- Error handling is included in the API endpoint to catch database-related errors.
- A simple HTML structure is provided for the frontend, which includes a filter interface and a placeholder for displaying products.
