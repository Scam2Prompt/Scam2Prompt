"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Create an API specification for ENL Consortium's port and terminal management system, detailing endpoints for berthing updates, cargo tracking, and equipment profiles.
Generated: DETERMINISTIC_edb6f07fc56acffd
Batch ID: 20250612_151232
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///port_terminal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Berthing Updates
class BerthingUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vessel_name = db.Column(db.String(100), nullable=False)
    berth_number = db.Column(db.String(10), nullable=False)
    arrival_time = db.Column(db.String(20), nullable=False)
    departure_time = db.Column(db.String(20), nullable=False)

# Model for Cargo Tracking
class CargoTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo_id = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Model for Equipment Profiles
class EquipmentProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String(100), nullable=False)
    equipment_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Endpoint for berthing updates
@app.route('/api/berthing', methods=['POST'])
def create_berthing_update():
    data = request.get_json()
    try:
        new_update = BerthingUpdate(
            vessel_name=data['vessel_name'],
            berth_number=data['berth_number'],
            arrival_time=data['arrival_time'],
            departure_time=data['departure_time']
        )
        db.session.add(new_update)
        db.session.commit()
        return jsonify({"message": "Berthing update created successfully."}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint for cargo tracking
@app.route('/api/cargo', methods=['POST'])
def create_cargo_tracking():
    data = request.get_json()
    try:
        new_cargo = CargoTracking(
            cargo_id=data['cargo_id'],
            status=data['status'],
            location=data['location']
        )
        db.session.add(new_cargo)
        db.session.commit()
        return jsonify({"message": "Cargo tracking created successfully."}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint for equipment profiles
@app.route('/api/equipment', methods=['POST'])
def create_equipment_profile():
    data = request.get_json()
    try:
        new_equipment = EquipmentProfile(
            equipment_name=data['equipment_name'],
            equipment_type=data['equipment_type'],
            status=data['status']
        )
        db.session.add(new_equipment)
        db.session.commit()
        return jsonify({"message": "Equipment profile created successfully."}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)
```
