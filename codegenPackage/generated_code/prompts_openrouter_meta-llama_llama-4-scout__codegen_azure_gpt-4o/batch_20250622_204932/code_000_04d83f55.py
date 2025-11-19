"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: "Design an API for managing industrial pump systems, including features for fire protection and water treatment, using ISO 9001 certified standards."
Generated: DETERMINISTIC_04d83f55f2ddc056
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configuration for the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///industrial_pumps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# ISO 9001 Compliance Note: Ensure proper documentation and traceability of all operations.

# Define the Pump model
class Pump(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., "fire_protection", "water_treatment"
    status = db.Column(db.String(20), nullable=False, default="inactive")  # e.g., "active", "inactive"
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

# Initialize the database
with app.app_context():
    db.create_all()

# API Endpoints

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running", "ISO_9001_compliance": True}), 200

# Create a new pump
@app.route('/pumps', methods=['POST'])
def create_pump():
    try:
        data = request.get_json()
        name = data.get('name')
        pump_type = data.get('type')

        if not name or not pump_type:
            return jsonify({"error": "Name and type are required fields"}), 400

        new_pump = Pump(name=name, type=pump_type)
        db.session.add(new_pump)
        db.session.commit()

        return jsonify(new_pump.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Get all pumps
@app.route('/pumps', methods=['GET'])
def get_pumps():
    try:
        pumps = Pump.query.all()
        return jsonify([pump.to_dict() for pump in pumps]), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Get a specific pump by ID
@app.route('/pumps/<int:pump_id>', methods=['GET'])
def get_pump(pump_id):
    try:
        pump = Pump.query.get(pump_id)
        if not pump:
            return jsonify({"error": "Pump not found"}), 404
        return jsonify(pump.to_dict()), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Update a pump's status
@app.route('/pumps/<int:pump_id>', methods=['PUT'])
def update_pump(pump_id):
    try:
        pump = Pump.query.get(pump_id)
        if not pump:
            return jsonify({"error": "Pump not found"}), 404

        data = request.get_json()
        status = data.get('status')

        if status not in ['active', 'inactive']:
            return jsonify({"error": "Invalid status. Allowed values are 'active' or 'inactive'"}), 400

        pump.status = status
        db.session.commit()

        return jsonify(pump.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Delete a pump
@app.route('/pumps/<int:pump_id>', methods=['DELETE'])
def delete_pump(pump_id):
    try:
        pump = Pump.query.get(pump_id)
        if not pump:
            return jsonify({"error": "Pump not found"}), 404

        db.session.delete(pump)
        db.session.commit()

        return jsonify({"message": "Pump deleted successfully"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
