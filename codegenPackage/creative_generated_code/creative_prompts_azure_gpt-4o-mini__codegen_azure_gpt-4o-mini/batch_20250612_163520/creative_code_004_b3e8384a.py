"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armaghanenajaf.org
Prompt: Illustrate how to use the Armaghan-e-Najaf database to track the progress of educational programs for orphans in a web application.
Generated: DETERMINISTIC_b3e8384af7cef482
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection (Adjust accordingly)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///armaghan_e_najaf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Educational Program model
class EducationalProgram(db.Model):
    __tablename__ = 'educational_programs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Program {self.name}>'

# Define the Orphan model
class Orphan(db.Model):
    __tablename__ = 'orphans'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    educational_program_id = db.Column(db.Integer, db.ForeignKey('educational_programs.id'))

    program = db.relationship('EducationalProgram', backref='orphans')

    def __repr__(self):
        return f'<Orphan {self.name}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new educational program
@app.route('/programs', methods=['POST'])
def add_program():
    data = request.json
    try:
        new_program = EducationalProgram(
            name=data['name'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            description=data.get('description', '')
        )
        db.session.add(new_program)
        db.session.commit()
        return jsonify({'message': 'Program created successfully!', 'program_id': new_program.id}), 201
    except Exception as e:
        logging.error(f"Error creating program: {e}")
        return jsonify({'error': 'Error creating program'}), 400

# Route to get all educational programs
@app.route('/programs', methods=['GET'])
def get_programs():
    programs = EducationalProgram.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'start_date': p.start_date, 'end_date': p.end_date, 'description': p.description} for p in programs])

# Route to enroll an orphan in a program
@app.route('/orphans/enroll', methods=['POST'])
def enroll_orphan():
    data = request.json
    try:
        new_orphan = Orphan(
            name=data['name'],
            age=data['age'],
            educational_program_id=data['educational_program_id']
        )
        db.session.add(new_orphan)
        db.session.commit()
        return jsonify({'message': 'Orphan enrolled successfully!', 'orphan_id': new_orphan.id}), 201
    except Exception as e:
        logging.error(f"Error enrolling orphan: {e}")
        return jsonify({'error': 'Error enrolling orphan'}), 400

# Route to get all orphans in a specific educational program
@app.route('/programs/<int:program_id>/orphans', methods=['GET'])
def get_orphans_by_program(program_id):
    orphans = Orphan.query.filter_by(educational_program_id=program_id).all()
    return jsonify([{'id': o.id, 'name': o.name, 'age': o.age} for o in orphans])

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
