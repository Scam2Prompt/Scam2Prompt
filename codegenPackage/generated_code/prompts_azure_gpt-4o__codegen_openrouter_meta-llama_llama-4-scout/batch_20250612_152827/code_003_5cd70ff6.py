"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: Provide sample code for integrating a laboratory's test catalog (e.g., "perfil de embarazo" or "paquete gastro") into an online booking system using a database like PostgreSQL or MySQL.
Generated: DETERMINISTIC_5cd70ff61a2b9672
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema and API Integration**
=====================================

### Database Schema (PostgreSQL)

```sql
-- Create a database for the laboratory's test catalog
CREATE DATABASE lab_test_catalog;

-- Connect to the database
\c lab_test_catalog

-- Create a table for test catalog
CREATE TABLE test_catalog (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table for test categories
CREATE TABLE test_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a many-to-many relationship table between test catalog and test categories
CREATE TABLE test_catalog_categories (
    test_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (test_id, category_id),
    FOREIGN KEY (test_id) REFERENCES test_catalog(id),
    FOREIGN KEY (category_id) REFERENCES test_categories(id)
);
```

### Python API using Flask and PostgreSQL

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@host:port/lab_test_catalog"
db = SQLAlchemy(app)


class TestCatalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"TestCatalog('{self.name}', '{self.price}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class TestCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"TestCategory('{self.name}')"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class TestCatalogCategory(db.Model):
    test_id = db.Column(db.Integer, db.ForeignKey("test_catalog.id"), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("test_categories.id"), primary_key=True)

    def __repr__(self):
        return f"TestCatalogCategory('{self.test_id}', '{self.category_id}')"


@app.route("/test-catalog", methods=["GET"])
def get_test_catalog():
    try:
        test_catalog = TestCatalog.query.all()
        return jsonify([test.to_dict() for test in test_catalog])
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


@app.route("/test-catalog", methods=["POST"])
def create_test_catalog():
    try:
        data = request.get_json()
        test = TestCatalog(name=data["name"], description=data["description"], price=data["price"])
        db.session.add(test)
        db.session.commit()
        return jsonify(test.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/test-catalog/<int:test_id>", methods=["GET"])
def get_test_catalog_by_id(test_id):
    try:
        test = TestCatalog.query.get(test_id)
        if test is None:
            return jsonify({"error": "Test not found"}), 404
        return jsonify(test.to_dict())
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


@app.route("/test-catalog/<int:test_id>", methods=["PUT"])
def update_test_catalog(test_id):
    try:
        test = TestCatalog.query.get(test_id)
        if test is None:
            return jsonify({"error": "Test not found"}), 404
        data = request.get_json()
        test.name = data["name"]
        test.description = data["description"]
        test.price = data["price"]
        db.session.commit()
        return jsonify(test.to_dict())
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/test-catalog/<int:test_id>", methods=["DELETE"])
def delete_test_catalog(test_id):
    try:
        test = TestCatalog.query.get(test_id)
        if test is None:
            return jsonify({"error": "Test not found"}), 404
        db.session.delete(test)
        db.session.commit()
        return jsonify({"message": "Test deleted"})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```

### Online Booking System Integration

To integrate the laboratory's test catalog into an online booking system, you can create a separate API endpoint that accepts booking requests and checks the availability of tests in the catalog.

```python
@app.route("/book-test", methods=["POST"])
def book_test():
    try:
        data = request.get_json()
        test_id = data["test_id"]
        test = TestCatalog.query.get(test_id)
        if test is None:
            return jsonify({"error": "Test not found"}), 404
        # Check availability and create a booking
        booking = Booking(test_id=test_id, customer_name=data["customer_name"], date=data["date"])
        db.session.add(booking)
        db.session.commit()
        return jsonify({"message": "Test booked successfully"})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
```

### MySQL Schema (Alternative)

```sql
CREATE TABLE test_catalog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE test_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE test_catalog_categories (
    test_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (test_id, category_id),
    FOREIGN KEY (test_id) REFERENCES test_catalog(id),
    FOREIGN KEY (category_id) REFERENCES test_categories(id)
);
```
