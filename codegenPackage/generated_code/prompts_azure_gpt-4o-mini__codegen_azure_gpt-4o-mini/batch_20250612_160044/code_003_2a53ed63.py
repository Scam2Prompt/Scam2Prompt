"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Develop an API that allows users to retrieve information about tennis coaches and their training programs, inspired by the coaching details provided by TC Harsewinkel.
Generated: DETERMINISTIC_2a53ed635ede20e5
Batch ID: 20250612_160044
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coaches.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Coach model
class Coach(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    training_programs = db.relationship('TrainingProgram', backref='coach', lazy=True)

# Define the TrainingProgram model
class TrainingProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(100), nullable=False)
    duration_weeks = db.Column(db.Integer, nullable=False)
    coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to retrieve all coaches
@app.route('/api/coaches', methods=['GET'])
def get_coaches():
    try:
        coaches = Coach.query.all()
        return jsonify([{'id': coach.id, 'name': coach.name, 'experience_years': coach.experience_years} for coach in coaches]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to retrieve a specific coach by ID
@app.route('/api/coaches/<int:coach_id>', methods=['GET'])
def get_coach(coach_id):
    try:
        coach = Coach.query.get_or_404(coach_id)
        return jsonify({
            'id': coach.id,
            'name': coach.name,
            'experience_years': coach.experience_years,
            'training_programs': [{'id': program.id, 'program_name': program.program_name, 'duration_weeks': program.duration_weeks} for program in coach.training_programs]
        }), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to add a new coach
@app.route('/api/coaches', methods=['POST'])
def add_coach():
    data = request.get_json()
    try:
        new_coach = Coach(name=data['name'], experience_years=data['experience_years'])
        db.session.add(new_coach)
        db.session.commit()
        return jsonify({'id': new_coach.id, 'name': new_coach.name}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to add a training program for a coach
@app.route('/api/coaches/<int:coach_id>/programs', methods=['POST'])
def add_training_program(coach_id):
    data = request.get_json()
    try:
        coach = Coach.query.get_or_404(coach_id)
        new_program = TrainingProgram(program_name=data['program_name'], duration_weeks=data['duration_weeks'], coach=coach)
        db.session.add(new_program)
        db.session.commit()
        return jsonify({'id': new_program.id, 'program_name': new_program.program_name}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
