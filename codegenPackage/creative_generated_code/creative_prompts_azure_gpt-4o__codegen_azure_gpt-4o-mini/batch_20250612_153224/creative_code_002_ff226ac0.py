"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Generate code for a web-based booking system that supports multi-country tour packages, including features for price guarantees and diverse destination management, inspired by Skyline International Agent's offerings.
Generated: DETERMINISTIC_ff226ac0f7af28c6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Tour Package
class TourPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    guarantee_price = db.Column(db.Boolean, default=False)

# Schema for Tour Package validation
class TourPackageSchema(Schema):
    title = fields.Str(required=True)
    price = fields.Float(required=True)
    destination = fields.Str(required=True)
    country = fields.Str(required=True)
    guarantee_price = fields.Bool()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new tour package
@app.route('/packages', methods=['POST'])
def add_package():
    try:
        # Validate and deserialize the input data
        package_data = TourPackageSchema().load(request.json)
        new_package = TourPackage(**package_data)
        
        db.session.add(new_package)
        db.session.commit()
        
        return jsonify({"message": "Tour Package created successfully!"}), 201
    except (ValidationError, SQLAlchemyError) as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to retrieve all tour packages
@app.route('/packages', methods=['GET'])
def get_packages():
    try:
        packages = TourPackage.query.all()
        # Serialize the data
        package_schema = TourPackageSchema(many=True)
        return jsonify(package_schema.dump(packages)), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Route to update a tour package by ID
@app.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    try:
        package = TourPackage.query.get_or_404(package_id)
        package_data = TourPackageSchema().load(request.json)
        
        for key, value in package_data.items():
            setattr(package, key, value)
        
        db.session.commit()
        return jsonify({"message": "Tour Package updated successfully!"}), 200
    except (ValidationError, SQLAlchemyError) as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Route to delete a tour package by ID
@app.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    try:
        package = TourPackage.query.get_or_404(package_id)
        db.session.delete(package)
        db.session.commit()
        return jsonify({"message": "Tour Package deleted successfully!"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
- To run this code, ensure you have Flask, Flask-SQLAlchemy, and Marshmallow installed. You can install them using:
  ```sh
  pip install Flask Flask-SQLAlchemy marshmallow
  ```
- The database is initialized in SQLite. You can change the URI to connect to a different database as necessary.
- This example includes basic CRUD functionality for managing tour packages.
