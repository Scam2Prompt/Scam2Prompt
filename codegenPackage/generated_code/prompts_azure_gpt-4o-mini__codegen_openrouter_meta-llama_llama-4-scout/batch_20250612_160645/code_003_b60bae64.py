"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Provide a code example for a web application that allows users to book laptop rentals, based on the digital solutions mentioned in the Azuharu article about Sewa Laptop Surabaya.
Generated: DETERMINISTIC_b60bae6437bce7bf
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# laptop_rental_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///laptop_rental.db"
db = SQLAlchemy(app)


class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    rentals = db.relationship("Rental", backref="user", lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Laptop(db.Model):
    """Laptop model"""
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    rentals = db.relationship("Rental", backref="laptop", lazy=True)

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Rental(db.Model):
    """Rental model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    laptop_id = db.Column(db.Integer, db.ForeignKey("laptop.id"), nullable=False)
    rental_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_id, laptop_id):
        self.user_id = user_id
        self.laptop_id = laptop_id


@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        user = User(data["name"], data["email"], data["password"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        user = User.query.filter_by(email=data["email"]).first()
        if user and user.check_password(data["password"]):
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/laptops", methods=["GET"])
def get_laptops():
    try:
        laptops = Laptop.query.all()
        output = []
        for laptop in laptops:
            laptop_data = {"id": laptop.id, "brand": laptop.brand, "model": laptop.model}
            output.append(laptop_data)
        return jsonify({"laptops": output}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/rentals", methods=["POST"])
def create_rental():
    try:
        data = request.json
        rental = Rental(data["user_id"], data["laptop_id"])
        db.session.add(rental)
        db.session.commit()
        return jsonify({"message": "Rental created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@app.route("/rentals/<int:rental_id>/return", methods=["PATCH"])
def return_rental(rental_id):
    try:
        rental = Rental.query.get(rental_id)
        if rental:
            rental.return_date = datetime.utcnow() + timedelta(days=1)
            db.session.commit()
            return jsonify({"message": "Rental returned successfully"}), 200
        return jsonify({"message": "Rental not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
