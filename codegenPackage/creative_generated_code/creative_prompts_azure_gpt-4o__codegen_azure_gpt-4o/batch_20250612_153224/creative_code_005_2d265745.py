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
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure SQLAlchemy for database storage
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model for storing product details in the database
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each product
    name = db.Column(db.String(100), nullable=False)  # Name of the product
    equipment_type = db.Column(db.String(50), nullable=False)  # Type of equipment
    use_case = db.Column(db.String(50), nullable=False)  # Use case of the product
    price = db.Column(db.Float, nullable=False)  # Price of the product

# Create the database tables
with app.app_context():
    db.create_all()

# Route: Home Page (to display the product catalog)
@app.route('/')
def home():
    return render_template('index.html')  # Render catalog frontend (HTML template)

# Route: Fetch products with filters applied
@app.route('/products', methods=['GET'])
def get_products():
    try:
        # Retrieve filter query parameters
        equipment_type = request.args.get('equipment_type')  # Filter by equipment type
        use_case = request.args.get('use_case')  # Filter by use case
        min_price = request.args.get('min_price', type=float)  # Minimum price filter
        max_price = request.args.get('max_price', type=float)  # Maximum price filter

        # Build query dynamically based on filters
        query = Product.query
        if equipment_type:
            query = query.filter(Product.equipment_type == equipment_type)
        if use_case:
            query = query.filter(Product.use_case == use_case)
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        # Execute query and fetch results
        products = query.all()

        # Serialize product data for JSON response
        product_list = [{
            'id': product.id,
            'name': product.name,
            'equipment_type': product.equipment_type,
            'use_case': product.use_case,
            'price': product.price
        } for product in products]

        # Return JSON response with the filtered product list
        return jsonify({'products': product_list}), 200

    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

# Route: Add a new product to the catalog
@app.route('/products', methods=['POST'])
def add_product():
    try:
        # Parse JSON request body
        data = request.get_json()
        name = data.get('name')
        equipment_type = data.get('equipment_type')
        use_case = data.get('use_case')
        price = data.get('price')

        # Validate required fields
        if not name or not equipment_type or not use_case or price is None:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create new Product instance
        new_product = Product(name=name, equipment_type=equipment_type, use_case=use_case, price=price)

        # Save product to database
        db.session.add(new_product)
        db.session.commit()

        # Return success response
        return jsonify({'message': 'Product added successfully', 'product_id': new_product.id}), 201

    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

# Entry point of the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
```

### Notes:
1. This code uses Flask and SQLAlchemy for backend development.
2. The database used is SQLite, which is simple and suitable for prototyping.
3. Filters for equipment type, use case, and price range are implemented in the `GET /products` route.
4. The front-end (`index.html`) is not provided but should use AJAX or a similar method to interact with the `/products` API.
5. Proper error handling is included for unexpected scenarios.
