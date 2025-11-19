"""
Generated Code Metadata:
========================
Original URL: https://lalitarora.in
Prompt: Develop a web application feature that facilitates initial dialogues for personalized coaching, reflecting the strategic planning process outlined by Dr. Lalit Arora.
Generated: DETERMINISTIC_e986f5dcb2669039
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coaching.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CoachingSession model
class CoachingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    goals = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Create a schema for input validation
class CoachingSessionSchema(Schema):
    user_name = fields.Str(required=True)
    goals = fields.Str(required=True)

# Initialize the schema
session_schema = CoachingSessionSchema()

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new coaching session
@app.route('/coaching_session', methods=['POST'])
def create_coaching_session():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = session_schema.load(data)

        # Create a new coaching session
        new_session = CoachingSession(
            user_name=validated_data['user_name'],
            goals=validated_data['goals']
        )
        db.session.add(new_session)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Coaching session created successfully!", "session_id": new_session.id}), 201

    except ValidationError as ve:
        # Handle validation errors
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

# Route to retrieve all coaching sessions
@app.route('/coaching_sessions', methods=['GET'])
def get_coaching_sessions():
    try:
        sessions = CoachingSession.query.all()
        result = [{"id": session.id, "user_name": session.user_name, "goals": session.goals} for session in sessions]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
