"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekrollindustrial.com.br
Prompt: Create an API that integrates with Tekroll Industrial's equipment for swine farming, allowing users to track productivity and equipment usage.
Generated: DETERMINISTIC_106f90021c068249
Batch ID: 20250612_160526
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
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy (replace with actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///swine_farming.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for tracking equipment usage
class EquipmentUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.String(80), nullable=False)
    usage_hours = db.Column(db.Float, nullable=False)
    productivity = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "equipment_id": self.equipment_id,
            "usage_hours": self.usage_hours,
            "productivity": self.productivity
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/equipment', methods=['POST'])
def add_equipment_usage():
    """Endpoint to add equipment usage data."""
    data = request.json
    if not data or 'equipment_id' not in data or 'usage_hours' not in data or 'productivity' not in data:
        raise BadRequest("Missing required data: equipment_id, usage_hours, productivity")

    new_usage = EquipmentUsage(
        equipment_id=data['equipment_id'],
        usage_hours=data['usage_hours'],
        productivity=data['productivity']
    )

    db.session.add(new_usage)
    db.session.commit()

    return jsonify(new_usage.serialize()), 201

@app.route('/api/equipment/<int:id>', methods=['GET'])
def get_equipment_usage(id):
    """Endpoint to retrieve equipment usage data by ID."""
    usage = EquipmentUsage.query.get(id)
    if not usage:
        raise NotFound("Equipment usage not found")

    return jsonify(usage.serialize()), 200

@app.route('/api/equipment', methods=['GET'])
def list_equipment_usage():
    """Endpoint to list all equipment usage data."""
    usages = EquipmentUsage.query.all()
    return jsonify([usage.serialize() for usage in usages]), 200

@app.route('/api/equipment/<int:id>', methods=['DELETE'])
def delete_equipment_usage(id):
    """Endpoint to delete equipment usage data by ID."""
    usage = EquipmentUsage.query.get(id)
    if not usage:
        raise NotFound("Equipment usage not found")

    db.session.delete(usage)
    db.session.commit()

    return jsonify({"message": "Equipment usage deleted successfully"}), 204

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle 400 errors."""
    return jsonify({"error": str(error)}), 400

@app.errorhandler(InternalServerError)
def handle_internal_server_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the app on localhost port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
```
