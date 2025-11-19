"""
Generated Code Metadata:
========================
Original URL: https://solandsol.com
Prompt: Create a REST API in Flask for managing pharmaceutical products like infant milk and dietary supplements, with endpoints for adding, updating, and retrieving product details such as ratings and SKUs.
Generated: DETERMINISTIC_031535761c9ab99e
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pharmaceutical_products.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class PharmaceuticalProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(20), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"PharmaceuticalProduct('{self.name}', '{self.sku}', {self.rating})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "sku": self.sku,
            "rating": self.rating,
        }


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Endpoint to add a new pharmaceutical product
@app.route("/products", methods=["POST"])
def add_product():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON in request"}), 400

        required_fields = ["name", "sku", "rating"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        product = PharmaceuticalProduct(
            name=data["name"], sku=data["sku"], rating=data["rating"]
        )
        db.session.add(product)
        db.session.commit()
        return jsonify(product.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Endpoint to update an existing pharmaceutical product
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    try:
        product = PharmaceuticalProduct.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON in request"}), 400

        if "name" in data:
            product.name = data["name"]
        if "sku" in data:
            product.sku = data["sku"]
        if "rating" in data:
            product.rating = data["rating"]

        db.session.commit()
        return jsonify(product.to_dict()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Endpoint to retrieve a pharmaceutical product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    try:
        product = PharmaceuticalProduct.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        return jsonify(product.to_dict()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to retrieve all pharmaceutical products
@app.route("/products", methods=["GET"])
def get_all_products():
    try:
        products = PharmaceuticalProduct.query.all()
        return jsonify([product.to_dict() for product in products]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"error": e.description}), e.code


if __name__ == "__main__":
    app.run(debug=True)
```

```python
# requirements.txt
Flask
Flask-SQLAlchemy
```

```bash
# Run the application
# 1. Install dependencies: pip install -r requirements.txt
# 2. Run the application: python app.py
```
