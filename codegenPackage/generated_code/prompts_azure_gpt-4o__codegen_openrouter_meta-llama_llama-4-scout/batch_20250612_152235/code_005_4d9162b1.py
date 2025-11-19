"""
Generated Code Metadata:
========================
Original URL: https://alphaonlineservices.com
Prompt: Write code for a custom e-commerce website with clean, secure, and scalable backend development, following the principles of Alpha Online Services' web development approach.
Generated: DETERMINISTIC_4d9162b1baefc2ea
Batch ID: 20250612_152235
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/products`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/login`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/orders`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/register`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**E-Commerce Website Backend**
================================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Flask-Bcrypt 1.0+
* Flask-JWT-Extended 4.0+

### Code
```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False, default="customer")

    def __init__(self, email, password, role):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")
        self.role = role

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity


# Routes
@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({"error": "Email already exists"}), 400
        new_user = User(email, password, "customer")
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid credentials"}), 401
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/products", methods=["GET"])
def get_products():
    try:
        products = Product.query.all()
        output = []
        for product in products:
            product_data = {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
            }
            output.append(product_data)
        return jsonify({"products": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/products", methods=["POST"])
@jwt_required
def create_product():
    try:
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        description = data["description"]
        new_product = Product(name, price, description)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/orders", methods=["POST"])
@jwt_required
def create_order():
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        product_id = data["product_id"]
        quantity = data["quantity"]
        new_order = Order(user_id, product_id, quantity)
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"message": "Order created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt

Flask==2.0.2
Flask-SQLAlchemy==2.5.1
Flask-Bcrypt==1.0.1
Flask-JWT-Extended==4.0.0
```

```python
# .gitignore

__pycache__/
*.py[cod]
instance/
ecommerce.db
```

### Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python app.py`
3. Use a tool like `curl` or a REST client to interact with the API.

**Example Requests**

* Register a new user: `curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "password"}' http://localhost:5000/register`
* Login: `curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "password": "password"}' http://localhost:5000/login`
* Get products: `curl -X GET http://localhost:5000/products`
* Create a product: `curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <access_token>" -d '{"name": "New Product", "price": 19.99, "description": "This is a new product"}' http://localhost:5000/products`
* Create an order: `curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <access_token>" -d '{"product_id": 1, "quantity": 2}' http://localhost:5000/orders`
