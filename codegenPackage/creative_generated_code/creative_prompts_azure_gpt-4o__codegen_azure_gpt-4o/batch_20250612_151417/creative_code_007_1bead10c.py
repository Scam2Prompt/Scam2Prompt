"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://excelwithsmart.com
Prompt: Create a dashboard for tracking the progress of placement training programs across multiple colleges, inspired by SMART Training Resources' widespread operations.
Generated: DETERMINISTIC_1bead10cf0868502
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI (adjust to your database settings)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///placement_training.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the College model
class College(db.Model):
    __tablename__ = 'colleges'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False, unique=True)

# Define the TrainingProgram model
class TrainingProgram(db.Model):
    __tablename__ = 'training_programs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

# Define the Progress model
class Progress(db.Model):
    __tablename__ = 'progress'
    id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.Integer, db.ForeignKey('colleges.id'), nullable=False)
    training_program_id = db.Column(db.Integer, db.ForeignKey('training_programs.id'), nullable=False)
    progress_percentage = db.Column(db.Float, nullable=False, default=0.0)  # Progress in percentage (0.0 to 100.0)
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    college = db.relationship('College', backref='progress_records')
    training_program = db.relationship('TrainingProgram', backref='progress_records')

# Route: Home/Dashboard
@app.route('/')
def home():
    """Render the dashboard page."""
    try:
        colleges = College.query.all()
        training_programs = TrainingProgram.query.all()
        progress_records = Progress.query.all()
        return render_template('dashboard.html', colleges=colleges, training_programs=training_programs, progress_records=progress_records)
    except SQLAlchemyError as e:
        return f"Database Error: {str(e)}", 500

# Route: Add College
@app.route('/add_college', methods=['POST'])
def add_college():
    """Add a new college to the database."""
    try:
        data = request.json
        college = College(name=data['name'], location=data['location'], contact_email=data['contact_email'])
        db.session.add(college)
        db.session.commit()
        return jsonify({'message': 'College added successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except KeyError:
        return jsonify({'error': 'Invalid data format'}), 400

# Route: Add Training Program
@app.route('/add_training_program', methods=['POST'])
def add_training_program():
    """Add a new training program to the database."""
    try:
        data = request.json
        training_program = TrainingProgram(
            name=data['name'],
            description=data.get('description', ''),
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d')
        )
        db.session.add(training_program)
        db.session.commit()
        return jsonify({'message': 'Training program added successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except KeyError:
        return jsonify({'error': 'Invalid data format'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

# Route: Update Progress
@app.route('/update_progress', methods=['POST'])
def update_progress():
    """Update progress for a specific college and training program."""
    try:
        data = request.json
        progress = Progress.query.filter_by(
            college_id=data['college_id'], training_program_id=data['training_program_id']
        ).first()
        if not progress:
            progress = Progress(
                college_id=data['college_id'],
                training_program_id=data['training_program_id'],
                progress_percentage=data['progress_percentage']
            )
            db.session.add(progress)
        else:
            progress.progress_percentage = data['progress_percentage']
            progress.last_updated = datetime.utcnow()
        db.session.commit()
        return jsonify({'message': 'Progress updated successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except KeyError:
        return jsonify({'error': 'Invalid data format'}), 400

# Route: Get Summary
@app.route('/summary', methods=['GET'])
def summary():
    """Provide a summary of all colleges, training programs, and progress."""
    try:
        colleges = College.query.all()
        training_programs = TrainingProgram.query.all()
        progress_records = Progress.query.all()
        summary_data = {
            'colleges': [{'id': c.id, 'name': c.name, 'location': c.location, 'contact_email': c.contact_email} for c in colleges],
            'training_programs': [
                {'id': t.id, 'name': t.name, 'description': t.description, 'start_date': t.start_date.strftime('%Y-%m-%d'),
                 'end_date': t.end_date.strftime('%Y-%m-%d')} for t in training_programs
            ],
            'progress_records': [
                {'college_id': p.college_id, 'training_program_id': p.training_program_id, 'progress_percentage': p.progress_percentage,
                 'last_updated': p.last_updated.strftime('%Y-%m-%d %H:%M:%S')} for p in progress_records
            ]
        }
        return jsonify(summary_data), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Run the Flask development server
    app.run(debug=True)
```

This code assumes that you will use a frontend template for the `dashboard.html` file to render the dashboard correctly. It also includes RESTful API endpoints for managing colleges, training programs, and progress.
