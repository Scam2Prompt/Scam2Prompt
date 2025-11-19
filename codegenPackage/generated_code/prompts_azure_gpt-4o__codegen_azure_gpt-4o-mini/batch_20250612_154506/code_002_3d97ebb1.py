"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: Generate an API-based solution for tracking participants, tutors, and training progress in an LMS platform, similar to the functionalities offered by MasterClic Solutions.
Generated: DETERMINISTIC_3d97ebb1a52e33dd
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    training_progress = db.relationship('TrainingProgress', backref='participant', lazy=True)

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class TrainingProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    progress_percentage = db.Column(db.Float, nullable=False)

# Schemas for validation
class ParticipantSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)

class TrainingProgressSchema(Schema):
    id = fields.Int(dump_only=True)
    participant_id = fields.Int(required=True)
    course_name = fields.Str(required=True)
    progress_percentage = fields.Float(required=True)

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)
training_progress_schema = TrainingProgressSchema()
training_progresses_schema = TrainingProgressSchema(many=True)

# API routes
@app.route('/participants', methods=['POST'])
def add_participant():
    """Add a new participant."""
    try:
        data = request.get_json()
        participant = participant_schema.load(data)
        new_participant = Participant(**participant)
        db.session.add(new_participant)
        db.session.commit()
        return participant_schema.jsonify(new_participant), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Participant with this email already exists."}), 409

@app.route('/participants', methods=['GET'])
def get_participants():
    """Retrieve all participants."""
    participants = Participant.query.all()
    return participants_schema.jsonify(participants)

@app.route('/training_progress', methods=['POST'])
def add_training_progress():
    """Add training progress for a participant."""
    try:
        data = request.get_json()
        progress = training_progress_schema.load(data)
        new_progress = TrainingProgress(**progress)
        db.session.add(new_progress)
        db.session.commit()
        return training_progress_schema.jsonify(new_progress), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Participant ID does not exist."}), 404

@app.route('/training_progress/<int:participant_id>', methods=['GET'])
def get_training_progress(participant_id):
    """Retrieve training progress for a specific participant."""
    progress = TrainingProgress.query.filter_by(participant_id=participant_id).all()
    if not progress:
        return jsonify({"error": "No training progress found for this participant."}), 404
    return training_progresses_schema.jsonify(progress)

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the app in debug mode
```
