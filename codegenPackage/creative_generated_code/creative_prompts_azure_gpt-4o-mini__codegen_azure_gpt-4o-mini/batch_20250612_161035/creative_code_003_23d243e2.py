"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkarabia.net
Prompt: Create a REST API endpoint that retrieves information about Spark Arabia's heavy equipment rental options and customized rental packages.
Generated: DETERMINISTIC_23d243e2b185c7f4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equipment_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database model for Equipment
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rental_price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))

# Marshmallow schema for serialization
class EquipmentSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    rental_price = fields.Float(required=True)
    description = fields.Str()

# Initialize the schema
equipment_schema = EquipmentSchema(many=True)

# API endpoint to retrieve equipment rental options
@app.route('/api/equipment', methods=['GET'])
def get_equipment():
    """Retrieve all available equipment for rental."""
    try:
        # Query all equipment from the database
        equipment_list = Equipment.query.all()
        result = equipment_schema.dump(equipment_list)
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Error retrieving equipment: {e}")
        return jsonify({"error": "An error occurred while retrieving equipment."}), 500

# API endpoint to retrieve customized rental packages
@app.route('/api/packages', methods=['GET'])
def get_packages():
    """Retrieve customized rental packages (mock data for demonstration)."""
    try:
        # Example of some customized packages
        packages = [
            {"package_id": 1, "equipment_names": ["Excavator", "Bulldozer"], "discount": 10},
            {"package_id": 2, "equipment_names": ["Forklift"], "discount": 5}
        ]
        return jsonify(packages), 200
    except Exception as e:
        logger.error(f"Error retrieving packages: {e}")
        return jsonify({"error": "An error occurred while retrieving packages."}), 500

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Return a custom 404 error message."""
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_error(error):
    """Return a custom 500 error message."""
    return jsonify({"error": "Internal server error"}), 500

# Main function to run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
