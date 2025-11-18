"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-nyanheroes.pages.dev
Prompt: Suggest tools or frameworks for building a gamified mission tracking system like the one used in Nyan Heroes.
Generated: DETERMINISTIC_0219fdc1609e3cce
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sqlite3
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Create a Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Mission model
class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

# Create the schema for validation
class MissionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    is_completed = fields.Bool()

# Initialize the schema
mission_schema = MissionSchema()
missions_schema = MissionSchema(many=True)

# Error handling for validation
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({'error': error.messages}), 400

# Endpoint to create a new mission
@app.route('/missions', methods=['POST'])
def create_mission():
    try:
        # Validate and deserialize input
        mission_data = mission_schema.load(request.json)
        new_mission = Mission(**mission_data)
        db.session.add(new_mission)
        db.session.commit()
        return mission_schema.jsonify(new_mission), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all missions
@app.route('/missions', methods=['GET'])
def get_missions():
    missions = Mission.query.all()
    return missions_schema.jsonify(missions), 200

# Endpoint to update a mission's status
@app.route('/missions/<int:mission_id>', methods=['PUT'])
def update_mission(mission_id):
    mission = Mission.query.get(mission_id)
    if not mission:
        return jsonify({'error': 'Mission not found'}), 404
    
    try:
        # Update mission details
        mission_data = mission_schema.load(request.json)
        for key, value in mission_data.items():
            setattr(mission, key, value)
        db.session.commit()
        return mission_schema.jsonify(mission), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a mission
@app.route('/missions/<int:mission_id>', methods=['DELETE'])
def delete_mission(mission_id):
    mission = Mission.query.get(mission_id)
    if not mission:
        return jsonify({'error': 'Mission not found'}), 404
    
    try:
        db.session.delete(mission)
        db.session.commit()
        return jsonify({'message': 'Mission deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```
