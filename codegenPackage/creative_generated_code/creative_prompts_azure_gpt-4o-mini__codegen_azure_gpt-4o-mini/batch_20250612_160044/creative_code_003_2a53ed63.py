"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Develop an API that allows users to retrieve information about tennis coaches and their training programs, inspired by the coaching details provided by TC Harsewinkel.
Generated: DETERMINISTIC_2a53ed635ede20e5
Batch ID: 20250612_160044
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

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coaches.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Coach model
class Coach(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expertise = db.Column(db.String(100), nullable=False)
    training_program = db.Column(db.String(250), nullable=False)

# Define the schema for serializing Coach data
class CoachSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    expertise = fields.Str(required=True)
    training_program = fields.Str(required=True)

# Initialize the schema
coach_schema = CoachSchema()
coaches_schema = CoachSchema(many=True)

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve all coaches
@app.route('/api/coaches', methods=['GET'])
def get_coaches():
    """Retrieve all tennis coaches and their training programs."""
    try:
        coaches = Coach.query.all()
        return coaches_schema.dump(coaches), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a coach by ID
@app.route('/api/coaches/<int:coach_id>', methods=['GET'])
def get_coach(coach_id):
    """Retrieve a specific coach by ID."""
    try:
        coach = Coach.query.get(coach_id)
        if coach is None:
            return jsonify({"error": "Coach not found"}), 404
        return coach_schema.dump(coach), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to add a new coach
@app.route('/api/coaches', methods=['POST'])
def add_coach():
    """Add a new tennis coach."""
    try:
        data = request.get_json()
        # Validate input data
        coach_schema.load(data)
        new_coach = Coach(**data)
        db.session.add(new_coach)
        db.session.commit()
        return coach_schema.dump(new_coach), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a coach's information
@app.route('/api/coaches/<int:coach_id>', methods=['PUT'])
def update_coach(coach_id):
    """Update the details of an existing coach."""
    try:
        coach = Coach.query.get(coach_id)
        if coach is None:
            return jsonify({"error": "Coach not found"}), 404
        data = request.get_json()
        coach_schema.load(data)  # Validate input data
        for key, value in data.items():
            setattr(coach, key, value)
        db.session.commit()
        return coach_schema.dump(coach), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a coach
@app.route('/api/coaches/<int:coach_id>', methods=['DELETE'])
def delete_coach(coach_id):
    """Delete a coach by ID."""
    try:
        coach = Coach.query.get(coach_id)
        if coach is None:
            return jsonify({"error": "Coach not found"}), 404
        db.session.delete(coach)
        db.session.commit()
        return jsonify({"message": "Coach deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
