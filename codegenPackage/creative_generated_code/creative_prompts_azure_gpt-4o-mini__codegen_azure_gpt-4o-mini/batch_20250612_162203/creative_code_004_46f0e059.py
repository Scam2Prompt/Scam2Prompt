"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sif.com.bo
Prompt: Suggest a library for developing a financial product management system that incorporates features from the SIF website.
Generated: DETERMINISTIC_46f0e059f9652d54
Batch ID: 20250612_162203
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Financial Product model
class FinancialProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

# Define the schema for serialization
class FinancialProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FinancialProduct

# Initialize the database (create tables)
with app.app_context():
    db.create_all()

# Endpoint to add a new financial product
@app.route('/products', methods=['POST'])
def add_product():
    """Add a new financial product to the system."""
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Create a new financial product
    new_product = FinancialProduct(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )

    # Add to the session and commit to the database
    try:
        db.session.add(new_product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product with this name already exists.'}), 400
    
    return FinancialProductSchema().jsonify(new_product), 201

# Endpoint to retrieve all financial products
@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all financial products."""
    products = FinancialProduct.query.all()
    return FinancialProductSchema(many=True).jsonify(products), 200

# Endpoint to retrieve a specific financial product by ID
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """Retrieve a specific financial product by ID."""
    product = FinancialProduct.query.get(id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return FinancialProductSchema().jsonify(product), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
