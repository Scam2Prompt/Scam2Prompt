"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Suggest an API that could help automate the management of training sessions related to Coordination SPS, as mentioned in the AFCO's training initiatives.
Generated: DETERMINISTIC_6c5d8e0234d475e4
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///training_sessions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define the TrainingSession model
class TrainingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # duration in minutes
    description = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date.isoformat(),
            'duration': self.duration,
            'description': self.description
        }

# Create the database
with app.app_context():
    db.create_all()

# Endpoint to create a new training session
@app.route('/api/training_sessions', methods=['POST'])
def create_training_session():
    if not request.json or 'title' not in request.json:
        abort(400)  # Bad request if title is missing

    new_session = TrainingSession(
        title=request.json['title'],
        date=datetime.fromisoformat(request.json['date']),
        duration=request.json.get('duration', 60),
        description=request.json.get('description', '')
    )
    
    db.session.add(new_session)
    db.session.commit()
    
    return jsonify(new_session.to_dict()), 201  # Return created session with 201 status

# Endpoint to retrieve all training sessions
@app.route('/api/training_sessions', methods=['GET'])
def get_training_sessions():
    sessions = TrainingSession.query.all()
    return jsonify([session.to_dict() for session in sessions]), 200  # Return all sessions

# Endpoint to retrieve a specific training session by ID
@app.route('/api/training_sessions/<int:session_id>', methods=['GET'])
def get_training_session(session_id):
    session = TrainingSession.query.get(session_id)
    if session is None:
        abort(404)  # Not found if session does not exist
    return jsonify(session.to_dict()), 200  # Return specific session

# Endpoint to update a training session
@app.route('/api/training_sessions/<int:session_id>', methods=['PUT'])
def update_training_session(session_id):
    session = TrainingSession.query.get(session_id)
    if session is None:
        abort(404)  # Not found if session does not exist

    if not request.json:
        abort(400)  # Bad request if no data is provided

    session.title = request.json.get('title', session.title)
    session.date = datetime.fromisoformat(request.json.get('date', session.date.isoformat()))
    session.duration = request.json.get('duration', session.duration)
    session.description = request.json.get('description', session.description)

    db.session.commit()
    return jsonify(session.to_dict()), 200  # Return updated session

# Endpoint to delete a training session
@app.route('/api/training_sessions/<int:session_id>', methods=['DELETE'])
def delete_training_session(session_id):
    session = TrainingSession.query.get(session_id)
    if session is None:
        abort(404)  # Not found if session does not exist

    db.session.delete(session)
    db.session.commit()
    return jsonify({'result': True}), 204  # Return no content with 204 status

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
