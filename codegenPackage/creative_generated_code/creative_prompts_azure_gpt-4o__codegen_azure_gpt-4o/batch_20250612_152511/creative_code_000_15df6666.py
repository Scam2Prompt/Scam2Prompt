"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Write code to create an e-commerce platform for selling gift cards and in-game currency, similar to the categories listed on "ای ار گیفت," including Apple, Xbox, Blizzard Battle.net, PUBG Mobile, and Fortnite.
Generated: DETERMINISTIC_15df6666bfac79f0
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the Flask application
app = Flask(__name__)

# Database setup (SQLite for simplicity here, replace with production DB as needed)
DATABASE_URL = "sqlite:///ecommerce.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Define the Product model
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)

# Create the database tables
Base.metadata.create_all(engine)

# Error handling utility function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = session.query(Product).all()
        return jsonify([{
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "description": p.description
        } for p in products])
    except Exception as e:
        return error_response(f"Error fetching products: {str(e)}", 500)

# Route to get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = session.query(Product).filter_by(id=product_id).first()
        if not product:
            return error_response("Product not found", 404)
        return jsonify({
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": product.price,
            "description": product.description
        })
    except Exception as e:
        return error_response(f"Error fetching product: {str(e)}", 500)

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.json
        if not all(key in data for key in ("name", "category", "price")):
            return error_response("Missing required fields: name, category, price")
        
        new_product = Product(
            name=data["name"],
            category=data["category"],
            price=data["price"],
            description=data.get("description", "")
        )
        session.add(new_product)
        session.commit()
        return jsonify({"message": "Product added successfully", "product_id": new_product.id}), 201
    except Exception as e:
        session.rollback()
        return error_response(f"Error adding product: {str(e)}", 500)

# Route to update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.json
        product = session.query(Product).filter_by(id=product_id).first()
        if not product:
            return error_response("Product not found", 404)
        
        product.name = data.get("name", product.name)
        product.category = data.get("category", product.category)
        product.price = data.get("price", product.price)
        product.description = data.get("description", product.description)
        session.commit()
        
        return jsonify({"message": "Product updated successfully"})
    except Exception as e:
        session.rollback()
        return error_response(f"Error updating product: {str(e)}", 500)

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        product = session.query(Product).filter_by(id=product_id).first()
        if not product:
            return error_response("Product not found", 404)
        
        session.delete(product)
        session.commit()
        return jsonify({"message": "Product deleted successfully"})
    except Exception as e:
        session.rollback()
        return error_response(f"Error deleting product: {str(e)}", 500)

# Route to search products by category
@app.route('/products/search', methods=['GET'])
def search_products():
    try:
        category = request.args.get("category")
        if not category:
            return error_response("Missing required query parameter: category")
        
        products = session.query(Product).filter_by(category=category).all()
        return jsonify([{
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "description": p.description
        } for p in products])
    except Exception as e:
        return error_response(f"Error searching products: {str(e)}", 500)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
