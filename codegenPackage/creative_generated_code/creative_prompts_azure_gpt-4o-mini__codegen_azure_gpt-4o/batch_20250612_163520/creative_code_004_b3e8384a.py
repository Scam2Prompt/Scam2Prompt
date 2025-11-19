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
# File: app.py
# Description: Flask-based web application to track the progress of educational programs for orphans using the Armaghan-e-Najaf database.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/armaghan_e_najaf'  # Replace with actual credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database models
class Orphan(db.Model):
    """Model for storing orphan details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

class EducationalProgram(db.Model):
    """Model for storing educational program details."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

class Progress(db.Model):
    """Model for storing progress of orphans in educational programs."""
    id = db.Column(db.Integer, primary_key=True)
    orphan_id = db.Column(db.Integer, db.ForeignKey('orphan.id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('educational_program.id'), nullable=False)
    completion_percentage = db.Column(db.Float, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    orphan = db.relationship('Orphan', backref=db.backref('progress', lazy=True))
    program = db.relationship('EducationalProgram', backref=db.backref('progress', lazy=True))

# API routes
@app.route('/add_orphan', methods=['POST'])
def add_orphan():
    """API endpoint to add a new orphan."""
    try:
        data = request.json
        new_orphan = Orphan(name=data['name'], age=data['age'], gender=data['gender'])
        db.session.add(new_orphan)
        db.session.commit()
        return jsonify({'message': 'Orphan added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/add_program', methods=['POST'])
def add_program():
    """API endpoint to add a new educational program."""
    try:
        data = request.json
        new_program = EducationalProgram(name=data['name'], description=data.get('description'))
        db.session.add(new_program)
        db.session.commit()
        return jsonify({'message': 'Program added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/record_progress', methods=['POST'])
def record_progress():
    """API endpoint to record progress for an orphan in a program."""
    try:
        data = request.json
        progress = Progress(
            orphan_id=data['orphan_id'],
            program_id=data['program_id'],
            completion_percentage=data['completion_percentage'],
            notes=data.get('notes')
        )
        db.session.add(progress)
        db.session.commit()
        return jsonify({'message': 'Progress recorded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_progress/<int:orphan_id>', methods=['GET'])
def get_progress(orphan_id):
    """API endpoint to fetch progress of an orphan."""
    try:
        progress_records = Progress.query.filter_by(orphan_id=orphan_id).all()
        if not progress_records:
            return jsonify({'message': 'No progress records found'}), 404

        result = [
            {
                'program_name': record.program.name,
                'completion_percentage': record.completion_percentage,
                'notes': record.notes
            }
            for record in progress_records
        ]
        return jsonify({'progress': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    # Ensure database tables are created
    db.create_all()
    app.run(debug=True)
```
