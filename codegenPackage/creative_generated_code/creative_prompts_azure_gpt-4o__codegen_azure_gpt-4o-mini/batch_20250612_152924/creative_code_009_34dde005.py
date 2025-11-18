"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Create a REST API for scheduling meetings and consultations for glass and aluminum project assessments, inspired by CristalesGraf's customer service model.
Generated: DETERMINISTIC_34dde005b5933de7
Batch ID: 20250612_152924
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
from datetime import datetime
import pytz

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for scheduled meetings
class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    project_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'email': self.email,
            'date_time': self.date_time.isoformat(),
            'project_type': self.project_type
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Schedule a new meeting
@app.route('/api/meetings', methods=['POST'])
def schedule_meeting():
    try:
        # Parse request data
        data = request.get_json(force=True)
        client_name = data['client_name']
        email = data['email']
        date_time_str = data['date_time']
        project_type = data['project_type']

        # Convert the date_time string to a datetime object
        date_time = datetime.fromisoformat(date_time_str).astimezone(pytz.utc)

        # Create a new meeting instance
        new_meeting = Meeting(client_name=client_name, email=email, date_time=date_time, project_type=project_type)

        # Add the meeting to the database
        db.session.add(new_meeting)
        db.session.commit()

        return jsonify(new_meeting.to_dict()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Retrieve all scheduled meetings
@app.route('/api/meetings', methods=['GET'])
def get_meetings():
    try:
        meetings = Meeting.query.all()
        return jsonify([meeting.to_dict() for meeting in meetings]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Retrieve a specific meeting by ID
@app.route('/api/meetings/<int:meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    try:
        meeting = Meeting.query.get_or_404(meeting_id)
        return jsonify(meeting.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
