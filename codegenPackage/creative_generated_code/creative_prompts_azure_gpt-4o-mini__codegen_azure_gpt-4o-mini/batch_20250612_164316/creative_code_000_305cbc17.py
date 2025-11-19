"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45hy45y45y54.pages.dev
Prompt: How can I implement a registration feature for a web application that tracks participants and their connection status, similar to the functionality described on the Sophon Time webpage?
Generated: DETERMINISTIC_305cbc1711e7ca5a
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# registration.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for participants
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False)

# Schema for validation of input data
class ParticipantSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    status = fields.String(required=True)

participant_schema = ParticipantSchema()

# Route to register a new participant
@app.route('/register', methods=['POST'])
def register():
    try:
        # Validate and deserialize the input data
        data = request.get_json()
        participant_data = participant_schema.load(data)

        # Check if participant already exists
        if Participant.query.filter_by(email=participant_data['email']).first():
            return jsonify({"error": "Participant already registered."}), 400

        # Create a new participant and add to the database
        new_participant = Participant(
            name=participant_data['name'],
            email=participant_data['email'],
            status=participant_data['status']
        )
        db.session.add(new_participant)
        db.session.commit()

        logging.info(f"Registered participant: {new_participant.name}")
        return jsonify({"message": "Registration successful."}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error registering participant: {e}")
        return jsonify({"error": "Internal server error."}), 500

# Route to get all participants and their statuses
@app.route('/participants', methods=['GET'])
def get_participants():
    try:
        participants = Participant.query.all()
        result = [{"name": p.name, "email": p.email, "status": p.status} for p in participants]
        return jsonify(result), 200
    except Exception as e:
        logging.error(f"Error fetching participants: {e}")
        return jsonify({"error": "Internal server error."}), 500

# Function to create the database
def create_db():
    with app.app_context():
        db.create_all()

# Main entry point
if __name__ == '__main__':
    create_db()  # Create the database tables
    app.run(debug=False)  # Run the Flask application
```

**Note**: Ensure you have Flask, Flask-SQLAlchemy, and marshmallow installed in your environment to run this code:

```bash
pip install Flask Flask-SQLAlchemy marshmallow
```
