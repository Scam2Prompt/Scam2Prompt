"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Create a team management system for the Team Mathematics Competition using a Python library or framework, allowing schools to register teams and track student participation.
Generated: DETERMINISTIC_2bdef599548d437a
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# team_management.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Team model
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100), nullable=False)
    members = db.relationship('Student', backref='team', lazy=True)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/teams', methods=['POST'])
def register_team():
    """Register a new team."""
    data = request.get_json()
    school_name = data.get('school_name')

    if not school_name:
        return jsonify({'error': 'School name is required'}), 400

    new_team = Team(school_name=school_name)
    db.session.add(new_team)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Team already exists'}), 400

    return jsonify({'message': 'Team registered successfully', 'team_id': new_team.id}), 201

@app.route('/teams/<int:team_id>/students', methods=['POST'])
def add_student(team_id):
    """Add a student to a team."""
    data = request.get_json()
    student_name = data.get('name')

    if not student_name:
        return jsonify({'error': 'Student name is required'}), 400

    team = Team.query.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404

    new_student = Student(name=student_name, team=team)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({'message': 'Student added successfully', 'student_id': new_student.id}), 201

@app.route('/teams/<int:team_id>', methods=['GET'])
def get_team_info(team_id):
    """Retrieve information about a team and its members."""
    team = Team.query.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404

    members = [{'id': member.id, 'name': member.name} for member in team.members]
    return jsonify({'team_id': team.id, 'school_name': team.school_name, 'members': members}), 200

@app.route('/teams/<int:team_id>/students/<int:student_id>', methods=['DELETE'])
def remove_student(team_id, student_id):
    """Remove a student from a team."""
    student = Student.query.filter_by(id=student_id, team_id=team_id).first()
    if not student:
        return jsonify({'error': 'Student not found in this team'}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({'message': 'Student removed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions to Run the Code
1. Ensure you have Python and Flask installed. You can install Flask and SQLAlchemy using pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Save the code in a file named `team_management.py`.
3. Run the application:
   ```bash
   python team_management.py
   ```
4. Use a tool like Postman or curl to interact with the API endpoints.
