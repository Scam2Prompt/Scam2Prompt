"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaonlineservices.com
Prompt: Write code for a custom e-commerce website with clean, secure, and scalable backend development, following the principles of Alpha Online Services' web development approach.
Generated: DETERMINISTIC_4d9162b1baefc2ea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///ecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f'<Order {self.id}>'

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'description': p.description, 'price': p.price, 'stock': p.stock} for p in products])

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data or 'stock' not in data:
        abort(400, description="Invalid input: name, price, and stock are required.")
    
    new_product = Product(name=data['name'], description=data.get('description'), price=data['price'], stock=data['stock'])
    
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'id': new_product.id}), 201

# Route to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or 'product_id' not in data or 'quantity' not in data:
        abort(400, description="Invalid input: product_id and quantity are required.")
    
    product = Product.query.get(data['product_id'])
    if not product:
        abort(404, description="Product not found.")

    if data['quantity'] > product.stock:
        abort(400, description="Insufficient stock available.")
    
    new_order = Order(product_id=data['product_id'], quantity=data['quantity'])
    
    product.stock -= data['quantity']  # Deduct stock
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'id': new_order.id}), 201

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': error.description}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

# Main entry point to run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')  # Run the app
```

### Setup Instructions
1. Install the necessary packages using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```
2. Set up the environment variable for your database connection:
   ```bash
   export DATABASE_URL="your_database_connection_string"
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Make sure to run migrations if you're using a production database.

### Notes
- Ensure that proper security measures are implemented, such as validating user input, using HTTPS, etc.
- The database used in the example is SQLite for simplicity; switch to a more robust solution for production.
- Consider adding user authentication and authorization for a complete e-commerce solution.
