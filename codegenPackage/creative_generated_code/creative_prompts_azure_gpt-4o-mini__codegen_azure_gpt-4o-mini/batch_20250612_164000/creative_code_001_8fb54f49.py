"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: How can I create a custom e-commerce platform that integrates with a direct selling system, based on the features outlined by Jieya Software?
Generated: DETERMINISTIC_8fb54f49b85b8884
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_platform.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and schema
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Define the Product schema
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

# Initialize the database
with app.app_context():
    db.create_all()

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description})
    response.content_type = "application/json"
    return response

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.json
        new_product = Product(name=data['name'], price=data['price'], stock=data['stock'])
        db.session.add(new_product)
        db.session.commit()
        return ProductSchema().jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return ProductSchema(many=True).jsonify(products), 200

# Route to update a product
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        product = Product.query.get_or_404(id)
        data = request.json
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        db.session.commit()
        return ProductSchema().jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to delete a product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow

### Installation
To set up the environment and install the required packages, use the following commands:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
```

### Running the Application
1. Save the code to a file named `e_commerce_platform.py`.
2. Run the application using the command:
```bash
python e_commerce_platform.py
```
3. Use an API client (like Postman) to interact with the endpoints.
