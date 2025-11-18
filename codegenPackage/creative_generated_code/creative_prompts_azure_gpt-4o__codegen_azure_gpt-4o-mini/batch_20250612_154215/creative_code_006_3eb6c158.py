"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipad.club
Prompt: Write code for a mentorship scheduling tool that connects advanced AI users with beginners, inspired by AiPAD Club's mentorship opportunities.
Generated: DETERMINISTIC_3eb6c1585a158cbe
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    """Model representing a user in the mentorship system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.String(10), nullable=False)  # 'mentor' or 'mentee'

    def __repr__(self):
        return f'<User {self.name}, Type: {self.user_type}>'

class Meeting(db.Model):
    """Model representing a mentorship meeting."""
    id = db.Column(db.Integer, primary_key=True)
    mentor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mentee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meeting_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Meeting {self.id}, Mentor: {self.mentor_id}, Mentee: {self.mentee_id}, Time: {self.meeting_time}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    """Endpoint to create a new user (mentor or mentee)."""
    try:
        data = request.json
        new_user = User(name=data['name'], user_type=data['user_type'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully.", "user": data}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route('/meetings', methods=['POST'])
def schedule_meeting():
    """Endpoint to schedule a mentorship meeting."""
    try:
        data = request.json
        mentor = User.query.get(data['mentor_id'])
        mentee = User.query.get(data['mentee_id'])
        
        if not mentor or not mentee:
            return jsonify({"error": "Invalid mentor or mentee ID."}), 404
        
        meeting_time = datetime.strptime(data['meeting_time'], '%Y-%m-%d %H:%M:%S')
        new_meeting = Meeting(mentor_id=mentor.id, mentee_id=mentee.id, meeting_time=meeting_time)
        db.session.add(new_meeting)
        db.session.commit()
        
        return jsonify({"message": "Meeting scheduled successfully.", "meeting": new_meeting.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except ValueError:
        return jsonify({"error": "Invalid date format. Use 'YYYY-MM-DD HH:MM:SS'."}), 400

@app.route('/meetings/<int:user_id>', methods=['GET'])
def get_meetings(user_id):
    """Endpoint to get all meetings for a specific user."""
    try:
        meetings = Meeting.query.filter((Meeting.mentor_id == user_id) | (Meeting.mentee_id == user_id)).all()
        return jsonify({"meetings": [meeting.id for meeting in meetings]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/meetings/<int:meeting_id>', methods=['DELETE'])
def cancel_meeting(meeting_id):
    """Endpoint to cancel a scheduled meeting."""
    try:
        meeting = Meeting.query.get(meeting_id)
        if not meeting:
            return jsonify({"error": "Meeting not found."}), 404

        db.session.delete(meeting)
        db.session.commit()
        return jsonify({"message": "Meeting canceled successfully."}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
