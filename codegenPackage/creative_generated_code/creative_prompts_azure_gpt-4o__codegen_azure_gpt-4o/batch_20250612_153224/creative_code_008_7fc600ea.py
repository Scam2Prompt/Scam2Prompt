"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-almamlaka.com
Prompt: Recommend tools or libraries for implementing a home restoration management system, including tracking repairs and material usage, as described in the "شمس المملكة" services.
Generated: DETERMINISTIC_7fc600eab23e9d34
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an implementation in Python that uses Flask for the web application framework, SQLAlchemy for database operations, and Marshmallow for serialization/validation. This code provides a basic scaffold for a home restoration management system.

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize the Flask app
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home_restoration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Define the Repair model for tracking repairs
class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pending")  # e.g., Pending, In Progress, Completed
    cost_estimate = db.Column(db.Float, nullable=True)

    def __init__(self, description, status, cost_estimate):
        self.description = description
        self.status = status
        self.cost_estimate = cost_estimate


# Define the Material model for tracking material usage
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity_used = db.Column(db.Integer, nullable=False)
    unit_cost = db.Column(db.Float, nullable=False)

    def __init__(self, name, quantity_used, unit_cost):
        self.name = name
        self.quantity_used = quantity_used
        self.unit_cost = unit_cost


# Define the Repair schema for serialization
class RepairSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Repair

# Define the Material schema for serialization
class MaterialSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Material


# Create instances of the schemas
repair_schema = RepairSchema()
repairs_schema = RepairSchema(many=True)  # For multiple repairs

material_schema = MaterialSchema()
materials_schema = MaterialSchema(many=True)  # For multiple materials


# Route to add a new repair
@app.route('/repairs', methods=['POST'])
def add_repair():
    try:
        description = request.json['description']
        status = request.json.get('status', "Pending")
        cost_estimate = request.json.get('cost_estimate', None)

        new_repair = Repair(description, status, cost_estimate)
        db.session.add(new_repair)
        db.session.commit()

        return repair_schema.jsonify(new_repair), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to fetch all repairs
@app.route('/repairs', methods=['GET'])
def get_repairs():
    try:
        all_repairs = Repair.query.all()
        return repairs_schema.jsonify(all_repairs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to add a new material
@app.route('/materials', methods=['POST'])
def add_material():
    try:
        name = request.json['name']
        quantity_used = request.json['quantity_used']
        unit_cost = request.json['unit_cost']

        new_material = Material(name, quantity_used, unit_cost)
        db.session.add(new_material)
        db.session.commit()

        return material_schema.jsonify(new_material), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Route to fetch all materials
@app.route('/materials', methods=['GET'])
def get_materials():
    try:
        all_materials = Material.query.all()
        return materials_schema.jsonify(all_materials), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the app (development mode)
if __name__ == "__main__":
    # Create the database if it doesn't exist
    if not os.path.exists('home_restoration.db'):
        with app.app_context():
            db.create_all()

    app.run(debug=True)
```

### Key Notes:
- Install dependencies using `pip install flask flask-sqlalchemy flask-marshmallow`.
- Run the code, then test the endpoints using tools like Postman or cURL.
- Ensure the database file (`home_restoration.db`) is created upon the first run.
