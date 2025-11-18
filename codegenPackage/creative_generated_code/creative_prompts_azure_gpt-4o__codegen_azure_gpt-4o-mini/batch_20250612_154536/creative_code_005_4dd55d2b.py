"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: Suggest an API for real-time analytics and monitoring of Vertiv's cooling systems in large-scale industrial facilities.
Generated: DETERMINISTIC_4dd55d2b388af27b
Batch ID: 20250612_154536
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
from flask_marshmallow import Marshmallow
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///cooling_systems.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow for serialization
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the CoolingSystem model
class CoolingSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, name, temperature, status):
        self.name = name
        self.temperature = temperature
        self.status = status

# Define the CoolingSystem schema
class CoolingSystemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CoolingSystem

# Initialize the schema
cooling_system_schema = CoolingSystemSchema()
cooling_systems_schema = CoolingSystemSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new cooling system
@app.route('/api/cooling_systems', methods=['POST'])
def add_cooling_system():
    """Endpoint to add a new cooling system."""
    try:
        name = request.json['name']
        temperature = request.json['temperature']
        status = request.json['status']

        new_system = CoolingSystem(name=name, temperature=temperature, status=status)
        db.session.add(new_system)
        db.session.commit()

        logging.info(f'New cooling system added: {new_system.name}')
        return cooling_system_schema.jsonify(new_system), 201
    except Exception as e:
        logging.error(f'Error adding cooling system: {e}')
        return jsonify({'message': 'Failed to add cooling system'}), 500

# API endpoint to get all cooling systems
@app.route('/api/cooling_systems', methods=['GET'])
def get_cooling_systems():
    """Endpoint to retrieve all cooling systems."""
    try:
        systems = CoolingSystem.query.all()
        return cooling_systems_schema.jsonify(systems), 200
    except Exception as e:
        logging.error(f'Error retrieving cooling systems: {e}')
        return jsonify({'message': 'Failed to retrieve cooling systems'}), 500

# API endpoint to update a cooling system's status
@app.route('/api/cooling_systems/<int:id>', methods=['PUT'])
def update_cooling_system(id):
    """Endpoint to update the status of a cooling system."""
    try:
        system = CoolingSystem.query.get_or_404(id)
        system.status = request.json.get('status', system.status)

        db.session.commit()
        logging.info(f'Updated cooling system: {system.name}')
        return cooling_system_schema.jsonify(system), 200
    except Exception as e:
        logging.error(f'Error updating cooling system: {e}')
        return jsonify({'message': 'Failed to update cooling system'}), 500

# API endpoint to delete a cooling system
@app.route('/api/cooling_systems/<int:id>', methods=['DELETE'])
def delete_cooling_system(id):
    """Endpoint to delete a cooling system."""
    try:
        system = CoolingSystem.query.get_or_404(id)
        db.session.delete(system)
        db.session.commit()
        logging.info(f'Deleted cooling system: {system.name}')
        return jsonify({'message': 'Cooling system deleted'}), 204
    except Exception as e:
        logging.error(f'Error deleting cooling system: {e}')
        return jsonify({'message': 'Failed to delete cooling system'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
