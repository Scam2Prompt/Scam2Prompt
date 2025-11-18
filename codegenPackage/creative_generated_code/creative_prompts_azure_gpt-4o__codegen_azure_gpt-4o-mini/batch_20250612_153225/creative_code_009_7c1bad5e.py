"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ranchioffline.com
Prompt: Generate code for a mobile app that integrates RanchiOffline's offerings, allowing users to shop for products and book essential services in one place.
Generated: DETERMINISTIC_7c1bad5e47f8401c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ranchioffline.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(250))

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

# Service model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, service_name, price):
        self.service_name = service_name
        self.price = price

# Product schema
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

# Service schema
class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service

# Initialize schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)

# Error handler for resource not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

# Endpoint to add a product
@app.route('/product', methods=['POST'])
def add_product():
    try:
        name = request.json['name']
        price = request.json['price']
        description = request.json.get('description', '')

        new_product = Product(name, price, description)
        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

# Endpoint to add a service
@app.route('/service', methods=['POST'])
def add_service():
    try:
        service_name = request.json['service_name']
        price = request.json['price']

        new_service = Service(service_name, price)
        db.session.add(new_service)
        db.session.commit()

        return service_schema.jsonify(new_service), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to get all services
@app.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return services_schema.jsonify(services)

# Run the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

Make sure to install Flask, Flask-SQLAlchemy, and Flask-Marshmallow if you haven't already, by running:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow
``` 

This app provides basic functionality for adding and retrieving products and services in a mobile app context using Flask as a backend.
