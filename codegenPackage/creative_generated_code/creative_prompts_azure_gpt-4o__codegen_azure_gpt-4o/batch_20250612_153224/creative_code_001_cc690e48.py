"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Recommend libraries or APIs to manage inventory for agricultural equipment sales and rentals, referencing SARL VERDIER's services in motoculture and irrigation equipment.
Generated: DETERMINISTIC_cc690e48a4c68c54
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for Agricultural Equipment Sales and Rentals

This script provides a simple inventory management system for agricultural equipment,
with reference to SARL VERDIER's services in motoculture and irrigation equipment.
It uses Python and SQLite for database management. Additional libraries can be added 
to enhance functionality.

Dependencies:
- SQLite (Python's built-in library)
- Flask (For API and web services)
- Marshmallow (For serialization and validation)
- SQLAlchemy (For ORM and database operations)

Install dependencies:
pip install flask sqlalchemy marshmallow
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and configure SQLite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Equipment(db.Model):
    """
    Equipment model to represent agricultural equipment.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., "Motoculture", "Irrigation"
    quantity = db.Column(db.Integer, nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)  # Rental price per day
    price_sale = db.Column(db.Float, nullable=True)      # Sale price

    def __repr__(self):
        return f"<Equipment {self.name} ({self.category})>"

# Schema for serialization and validation
class EquipmentSchema(Schema):
    """
    Marshmallow schema for Equipment model serialization and validation.
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    quantity = fields.Int(required=True)
    price_per_day = fields.Float(required=True)
    price_sale = fields.Float()

equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)

# Routes
@app.route('/equipment', methods=['POST'])
def add_equipment():
    """
    Add a new equipment to the inventory.
    """
    try:
        # Parse and validate incoming JSON data
        data = request.get_json()
        equipment_data = equipment_schema.load(data)

        # Create and save equipment
        new_equipment = Equipment(**equipment_data)
        db.session.add(new_equipment)
        db.session.commit()

        return jsonify(equipment_schema.dump(new_equipment)), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/equipment', methods=['GET'])
def list_equipment():
    """
    List all equipment in the inventory.
    """
    try:
        all_equipment = Equipment.query.all()
        return jsonify(equipments_schema.dump(all_equipment)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/equipment/<int:equip_id>', methods=['PUT'])
def update_equipment(equip_id):
    """
    Update an existing equipment.
    """
    try:
        # Fetch equipment by ID
        equipment = Equipment.query.get_or_404(equip_id)

        # Parse and validate incoming JSON data
        data = request.get_json()
        equipment_data = equipment_schema.load(data, partial=True)

        # Update fields
        for key, value in equipment_data.items():
            setattr(equipment, key, value)

        db.session.commit()
        return jsonify(equipment_schema.dump(equipment)), 200
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/equipment/<int:equip_id>', methods=['DELETE'])
def delete_equipment(equip_id):
    """
    Delete an equipment from the inventory.
    """
    try:
        # Fetch equipment by ID
        equipment = Equipment.query.get_or_404(equip_id)

        # Delete equipment
        db.session.delete(equipment)
        db.session.commit()

        return jsonify({"message": "Equipment deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500


# Command to initialize database
@app.cli.command('init-db')
def init_db():
    """
    Initialize the SQLite database (create tables).
    """
    db.create_all()
    print("Database initialized successfully.")


# Entry point for running the application
if __name__ == "__main__":
    app.run(debug=True)
```
