"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for iron and aluminum carpentry services, similar to those offered by Aluivars.
Generated: DETERMINISTIC_3289c3ea9602be5e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Carpentry Services Quote Request System**
=============================================

### Dependencies

This code uses Python 3.9+, Flask 2.2.2, and SQLAlchemy 1.4.42.

### Database Schema

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL
);

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE quotes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

CREATE TABLE materials (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE quote_materials (
    quote_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (quote_id, material_id),
    FOREIGN KEY (quote_id) REFERENCES quotes(id),
    FOREIGN KEY (material_id) REFERENCES materials(id)
);
```

### Python Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@host:port/dbname"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    quotes = db.relationship("Quote", backref="user", lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    quotes = db.relationship("Quote", backref="service", lazy=True)

    def __repr__(self):
        return f"Service('{self.name}')"


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    materials = db.relationship("Material", secondary="quote_materials", backref="quotes", lazy=True)

    def __repr__(self):
        return f"Quote('{self.id}', '{self.user_id}', '{self.service_id}')"


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Material('{self.name}')"


class QuoteMaterial(db.Model):
    __tablename__ = "quote_materials"
    quote_id = db.Column(db.Integer, db.ForeignKey("quote.id"), primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey("material.id"), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"QuoteMaterial('{self.quote_id}', '{self.material_id}')"


@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data["name"], email=data["email"], phone=data["phone"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@app.route("/services", methods=["POST"])
def create_service():
    try:
        data = request.get_json()
        new_service = Service(name=data["name"], description=data["description"])
        db.session.add(new_service)
        db.session.commit()
        return jsonify({"message": "Service created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@app.route("/quotes", methods=["POST"])
def create_quote():
    try:
        data = request.get_json()
        new_quote = Quote(
            user_id=data["user_id"],
            service_id=data["service_id"],
            description=data["description"],
        )
        db.session.add(new_quote)
        db.session.commit()
        return jsonify({"message": "Quote created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@app.route("/quotes/<int:quote_id>/materials", methods=["POST"])
def add_material_to_quote(quote_id):
    try:
        data = request.get_json()
        quote = Quote.query.get(quote_id)
        if not quote:
            return jsonify({"message": "Quote not found"}), 404
        material = Material.query.get(data["material_id"])
        if not material:
            return jsonify({"message": "Material not found"}), 404
        existing_material = QuoteMaterial.query.filter_by(
            quote_id=quote_id, material_id=data["material_id"]
        ).first()
        if existing_material:
            return jsonify({"message": "Material already added to quote"}), 400
        new_material = QuoteMaterial(quote_id=quote_id, material_id=data["material_id"], quantity=data["quantity"])
        db.session.add(new_material)
        db.session.commit()
        return jsonify({"message": "Material added to quote successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
```
