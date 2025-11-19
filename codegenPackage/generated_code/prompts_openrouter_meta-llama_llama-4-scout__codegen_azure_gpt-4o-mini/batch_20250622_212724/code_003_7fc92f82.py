"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: "Design a RESTful API for a cloud-based time-tracking service targeting legal professionals, with a pricing model under $10 per month."
Generated: DETERMINISTIC_7fc92f82cab4ab99
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///time_tracking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the TimeEntry model
class TimeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'description': self.description,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'duration': (self.end_time - self.start_time).total_seconds() / 3600  # Duration in hours
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Create a new time entry
@app.route('/api/time_entries', methods=['POST'])
def create_time_entry():
    data = request.get_json()
    if not data or 'user_id' not in data or 'description' not in data or 'start_time' not in data or 'end_time' not in data:
        abort(400)  # Bad request

    try:
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
    except ValueError:
        abort(400)  # Bad request

    if start_time >= end_time:
        abort(400)  # Bad request

    new_entry = TimeEntry(
        user_id=data['user_id'],
        description=data['description'],
        start_time=start_time,
        end_time=end_time
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify(new_entry.to_dict()), 201

# Retrieve all time entries for a user
@app.route('/api/users/<int:user_id>/time_entries', methods=['GET'])
def get_time_entries(user_id):
    entries = TimeEntry.query.filter_by(user_id=user_id).all()
    return jsonify([entry.to_dict() for entry in entries]), 200

# Retrieve a specific time entry by ID
@app.route('/api/time_entries/<int:entry_id>', methods=['GET'])
def get_time_entry(entry_id):
    entry = TimeEntry.query.get(entry_id)
    if entry is None:
        abort(404)  # Not found
    return jsonify(entry.to_dict()), 200

# Update a time entry
@app.route('/api/time_entries/<int:entry_id>', methods=['PUT'])
def update_time_entry(entry_id):
    entry = TimeEntry.query.get(entry_id)
    if entry is None:
        abort(404)  # Not found

    data = request.get_json()
    if not data:
        abort(400)  # Bad request

    if 'description' in data:
        entry.description = data['description']
    if 'start_time' in data:
        try:
            entry.start_time = datetime.fromisoformat(data['start_time'])
        except ValueError:
            abort(400)  # Bad request
    if 'end_time' in data:
        try:
            entry.end_time = datetime.fromisoformat(data['end_time'])
        except ValueError:
            abort(400)  # Bad request

    db.session.commit()
    return jsonify(entry.to_dict()), 200

# Delete a time entry
@app.route('/api/time_entries/<int:entry_id>', methods=['DELETE'])
def delete_time_entry(entry_id):
    entry = TimeEntry.query.get(entry_id)
    if entry is None:
        abort(404)  # Not found

    db.session.delete(entry)
    db.session.commit()
    return jsonify({'result': 'Entry deleted'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
