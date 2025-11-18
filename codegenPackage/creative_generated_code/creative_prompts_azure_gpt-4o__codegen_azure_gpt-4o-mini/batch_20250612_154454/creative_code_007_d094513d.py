"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Suggest a framework or tool for building a school management system that supports features like those described on SMKN 1 Kadipaten's site (e.g., academic schedules, character education tracking). Provide implementation details.
Generated: DETERMINISTIC_d094513dc1a3188e
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# school_management_system.py

"""
School Management System

This system provides functionalities for managing academic schedules, tracking character education, and supporting administrative tasks.

Framework: Flask
Database: SQLite (for simplicity in development)
"""

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model for Academic Schedule
class AcademicSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    day = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Schedule {self.subject} on {self.day} at {self.time}>'

# Model for Character Education Tracking
class CharacterEducation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    character_trait = db.Column(db.String(100), nullable=False)
    evaluation_date = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<CharacterEducation {self.student_name} - {self.character_trait} on {self.evaluation_date}>'

# Route to create a new academic schedule
@app.route('/schedule', methods=['POST'])
def create_schedule():
    data = request.json
    try:
        new_schedule = AcademicSchedule(subject=data['subject'], day=data['day'], time=data['time'])
        db.session.add(new_schedule)
        db.session.commit()
        return jsonify({"message": "Schedule created successfully!"}), 201
    except (KeyError, TypeError) as e:
        return jsonify({"error": str(e), "message": "Invalid input"}), 400

# Route to retrieve all academic schedules
@app.route('/schedules', methods=['GET'])
def get_schedules():
    schedules = AcademicSchedule.query.all()
    return jsonify([{"id": s.id, "subject": s.subject, "day": s.day, "time": s.time} for s in schedules])

# Route to create new character education entry
@app.route('/character-education', methods=['POST'])
def create_character_entry():
    data = request.json
    try:
        new_entry = CharacterEducation(student_name=data['student_name'],
                                       character_trait=data['character_trait'],
                                       evaluation_date=data['evaluation_date'])
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({"message": "Character education entry created successfully!"}), 201
    except (KeyError, TypeError) as e:
        return jsonify({"error": str(e), "message": "Invalid input"}), 400

# Route to retrieve all character education entries
@app.route('/character-entries', methods=['GET'])
def get_character_entries():
    entries = CharacterEducation.query.all()
    return jsonify([{"id": e.id, "student_name": e.student_name, "character_trait": e.character_trait,
                     "evaluation_date": e.evaluation_date} for e in entries])

# Error handler for 404 errors
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Main entry point for the application
if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Set debug to False in production
```
