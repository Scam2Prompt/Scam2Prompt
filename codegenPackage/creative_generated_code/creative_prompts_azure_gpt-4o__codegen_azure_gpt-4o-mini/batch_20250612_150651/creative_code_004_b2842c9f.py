"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globallinknext.com
Prompt: Write code to implement a roundtable discussion feature for a conference platform, inspired by the interactive demos at GlobalLink NEXT.
Generated: DETERMINISTIC_b2842c9f1c57c47c
Batch ID: 20250612_150651
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///roundtable.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for a Roundtable Discussion
class Roundtable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    participants = db.relationship('Participant', backref='roundtable', lazy=True)

# Model for Participants
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    roundtable_id = db.Column(db.Integer, db.ForeignKey('roundtable.id'), nullable=False)

# Error handling for invalid usage
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a roundtable discussion
@app.route('/roundtable', methods=['POST'])
def create_roundtable():
    data = request.get_json()
    if not data or not all(k in data for k in ('topic', 'start_time', 'end_time')):
        abort(400)

    # Validate datetime format
    try:
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
    except ValueError:
        abort(400)

    if start_time >= end_time:
        abort(400)

    new_roundtable = Roundtable(topic=data['topic'], start_time=start_time, end_time=end_time)
    db.session.add(new_roundtable)
    db.session.commit()
    
    return jsonify({'id': new_roundtable.id, 'topic': new_roundtable.topic}), 201

# Endpoint to add participants to a roundtable discussion
@app.route('/roundtable/<int:roundtable_id>/participants', methods=['POST'])
def add_participant(roundtable_id):
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400)

    roundtable = Roundtable.query.get(roundtable_id)
    if roundtable is None:
        abort(404)

    new_participant = Participant(name=data['name'], email=data['email'], roundtable_id=roundtable_id)
    db.session.add(new_participant)
    db.session.commit()

    return jsonify({'id': new_participant.id, 'name': new_participant.name}), 201

# Endpoint to fetch roundtable discussions
@app.route('/roundtables', methods=['GET'])
def get_roundtables():
    roundtables = Roundtable.query.all()
    return jsonify([{'id': rt.id, 'topic': rt.topic, 'start_time': rt.start_time.isoformat(), 'end_time': rt.end_time.isoformat()} for rt in roundtables])

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
