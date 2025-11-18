"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Create an API recommendation for integrating Roshako's product catalog into an industrial procurement system, focusing on their welding electrodes and high-performance alloys.
Generated: DETERMINISTIC_edc7c496ac72f72d
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure database (replace 'sqlite:///products.db' with your database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"<Product {self.name}>"

# Create a schema for serializing Product
class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)

# Initialize the schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# API endpoint to retrieve products by category
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    Retrieve products based on category query parameter.
    Query parameter example: ?category=welding
    """
    category = request.args.get('category', default=None, type=str)

    if category:
        try:
            products = Product.query.filter_by(category=category).all()
            return products_schema.dump(products), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Category parameter is required."}), 400

# API endpoint to add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    """
    Add a new product to the catalog.
    Expects a JSON body with the product information.
    """
    try:
        product_data = request.get_json()
        # Validate and deserialize input data
        product = product_schema.load(product_data)
        new_product = Product(**product)

        db.session.add(new_product)
        db.session.commit()
        
        return product_schema.dump(new_product), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a product by ID
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product by ID.
    Expects a JSON body with the updated product information.
    """
    try:
        product_data = request.get_json()
        product = Product.query.get_or_404(product_id)

        # Validate and update product fields
        validated_data = product_schema.load(product_data)
        for key, value in validated_data.items():
            setattr(product, key, value)

        db.session.commit()
        return product_schema.dump(product), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a product by ID
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product by ID.
    """
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found."}), 404

# Initialize database and run the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```
