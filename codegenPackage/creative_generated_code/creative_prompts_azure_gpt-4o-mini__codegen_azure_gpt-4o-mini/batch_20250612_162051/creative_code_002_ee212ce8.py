"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: Generate a REST API specification for a personal development program that includes features like self-assessment and virtual mentoring, inspired by the services of Nesha Group.
Generated: DETERMINISTIC_ee212ce84519bd6b
Batch ID: 20250612_162051
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class SelfAssessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    feedback = db.Column(db.String(200), nullable=True)

class MentorSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    mentor_id = db.Column(db.Integer, nullable=False)
    session_date = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.String(200), nullable=True)

# Define schemas for input validation
class SelfAssessmentSchema(Schema):
    user_id = fields.Int(required=True)
    score = fields.Float(required=True)
    feedback = fields.Str(required=False)

class MentorSessionSchema(Schema):
    user_id = fields.Int(required=True)
    mentor_id = fields.Int(required=True)
    session_date = fields.Str(required=True)
    notes = fields.Str(required=False)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# Route for self-assessment submission
@app.route('/api/self-assessments', methods=['POST'])
def create_self_assessment():
    json_data = request.json
    try:
        # Validate and deserialize input
        data = SelfAssessmentSchema().load(json_data)
        new_assessment = SelfAssessment(**data)
        db.session.add(new_assessment)
        db.session.commit()
        return jsonify({'message': 'Self-assessment created', 'id': new_assessment.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for scheduling mentor sessions
@app.route('/api/mentor-sessions', methods=['POST'])
def create_mentor_session():
    json_data = request.json
    try:
        # Validate and deserialize input
        data = MentorSessionSchema().load(json_data)
        new_session = MentorSession(**data)
        db.session.add(new_session)
        db.session.commit()
        return jsonify({'message': 'Mentor session created', 'id': new_session.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for retrieving all self-assessments
@app.route('/api/self-assessments', methods=['GET'])
def get_self_assessments():
    try:
        assessments = SelfAssessment.query.all()
        return jsonify([{'id': a.id, 'user_id': a.user_id, 'score': a.score, 'feedback': a.feedback} for a in assessments]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for retrieving all mentor sessions
@app.route('/api/mentor-sessions', methods=['GET'])
def get_mentor_sessions():
    try:
        sessions = MentorSession.query.all()
        return jsonify([{'id': s.id, 'user_id': s.user_id, 'mentor_id': s.mentor_id, 'session_date': s.session_date, 'notes': s.notes} for s in sessions]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
