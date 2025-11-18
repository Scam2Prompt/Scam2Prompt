"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smkn1kadipaten.sch.id
Prompt: Develop a web application using Flask or Django that replicates the exam schedule management system described on SMKN 1 Kadipaten's website. Include features for adding, updating, and viewing exam schedules.
Generated: DETERMINISTIC_2e718f754c4396a0
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Flask-based implementation for an Exam Schedule Management System. To simplify, we'll use SQLite as the database. Make sure Flask is installed (`pip install flask`).

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam_schedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ExamSchedule model
class ExamSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    subject = db.Column(db.String(100), nullable=False)  # Subject name
    date = db.Column(db.DateTime, nullable=False)  # Exam date and time
    classroom = db.Column(db.String(50), nullable=False)  # Classroom location

    # Return a dictionary representation for easy JSON conversion
    def to_dict(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "classroom": self.classroom
        }

# Route: Home page
@app.route('/')
def index():
    return render_template('index.html')  # HTML template for front-end

# Route: Get all exam schedules
@app.route('/schedules', methods=['GET'])
def get_schedules():
    schedules = ExamSchedule.query.all()  # Fetch all records
    return jsonify([schedule.to_dict() for schedule in schedules])  # Return as JSON

# Route: Add a new exam schedule
@app.route('/schedules', methods=['POST'])
def add_schedule():
    try:
        data = request.json  # Parse JSON data from the request
        subject = data.get('subject')
        date = datetime.strptime(data.get('date'), "%Y-%m-%d %H:%M:%S")  # Parse date
        classroom = data.get('classroom')

        # Input validation
        if not subject or not classroom or not date:
            return jsonify({"error": "Invalid data"}), 400

        # Create a new schedule entry
        new_schedule = ExamSchedule(subject=subject, date=date, classroom=classroom)
        db.session.add(new_schedule)
        db.session.commit()  # Save to the database

        return jsonify(new_schedule.to_dict()), 201  # Return the new record
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Update an existing exam schedule
@app.route('/schedules/<int:id>', methods=['PUT'])
def update_schedule(id):
    try:
        schedule = ExamSchedule.query.get(id)  # Fetch the record by ID
        if not schedule:
            return jsonify({"error": "Schedule not found"}), 404

        data = request.json  # Parse JSON data from the request
        schedule.subject = data.get('subject', schedule.subject)  # Update subject
        schedule.classroom = data.get('classroom', schedule.classroom)  # Update classroom
        if 'date' in data:
            schedule.date = datetime.strptime(data.get('date'), "%Y-%m-%d %H:%M:%S")  # Update date

        db.session.commit()  # Save to the database
        return jsonify(schedule.to_dict()), 200  # Return the updated record
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete an exam schedule
@app.route('/schedules/<int:id>', methods=['DELETE'])
def delete_schedule(id):
    try:
        schedule = ExamSchedule.query.get(id)  # Fetch the record by ID
        if not schedule:
            return jsonify({"error": "Schedule not found"}), 404

        db.session.delete(schedule)
        db.session.commit()  # Remove from the database
        return jsonify({"message": "Schedule deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initial setup: Create database tables
@app.before_first_request
def create_tables():
    db.create_all()  # Create tables based on the models

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. **Database Initialization**: Run the app once to create the `exam_schedule.db` database file.
2. **Front-End**: You can create an `index.html` file in a `templates` folder for front-end functionality.
3. **API Testing**: Use tools like `Postman` or `curl` to test the API endpoints for adding, updating, and viewing schedules.
