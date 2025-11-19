"""
Generated Code Metadata:
========================
Original URL: https://dextranslogistics.com
Prompt: "Design a RESTful API for a logistics management system that integrates with Dextrans Logistics' services for transportation, warehousing, and cargo insurance."
Generated: DETERMINISTIC_b7bf1e2267df9407
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Cargo model
class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    destination = db.Column(db.String(255), nullable=False)

    def __init__(self, description, weight, destination):
        self.description = description
        self.weight = weight
        self.destination = destination

# Define the Cargo schema
class CargoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cargo

# Initialize the database
with app.app_context():
    db.create_all()

# Create a new cargo entry
@app.route('/cargo', methods=['POST'])
def add_cargo():
    try:
        data = request.get_json()
        if not data or 'description' not in data or 'weight' not in data or 'destination' not in data:
            raise BadRequest("Missing required fields: description, weight, destination")

        new_cargo = Cargo(description=data['description'], weight=data['weight'], destination=data['destination'])
        db.session.add(new_cargo)
        db.session.commit()

        return CargoSchema().jsonify(new_cargo), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all cargo entries
@app.route('/cargo', methods=['GET'])
def get_cargo():
    try:
        all_cargo = Cargo.query.all()
        return CargoSchema(many=True).jsonify(all_cargo), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a specific cargo entry by ID
@app.route('/cargo/<int:cargo_id>', methods=['GET'])
def get_cargo_by_id(cargo_id):
    try:
        cargo = Cargo.query.get(cargo_id)
        if cargo is None:
            raise NotFound("Cargo not found")
        return CargoSchema().jsonify(cargo), 200
    except NotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update a cargo entry
@app.route('/cargo/<int:cargo_id>', methods=['PUT'])
def update_cargo(cargo_id):
    try:
        cargo = Cargo.query.get(cargo_id)
        if cargo is None:
            raise NotFound("Cargo not found")

        data = request.get_json()
        if 'description' in data:
            cargo.description = data['description']
        if 'weight' in data:
            cargo.weight = data['weight']
        if 'destination' in data:
            cargo.destination = data['destination']

        db.session.commit()
        return CargoSchema().jsonify(cargo), 200
    except NotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a cargo entry
@app.route('/cargo/<int:cargo_id>', methods=['DELETE'])
def delete_cargo(cargo_id):
    try:
        cargo = Cargo.query.get(cargo_id)
        if cargo is None:
            raise NotFound("Cargo not found")

        db.session.delete(cargo)
        db.session.commit()
        return jsonify({"message": "Cargo deleted successfully"}), 204
    except NotFound as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
