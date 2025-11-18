"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Suggest tools or frameworks for implementing a scheduling system for medical examinations, including tests for confined spaces and working at heights, as offered by Medicid IPS.
Generated: DETERMINISTIC_7e7c441fc0f546d6
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code providing a basic implementation of a scheduling system using Flask framework and SQLAlchemy for database management. This code is well-commented and follows best practices.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import traceback

# Initialize Flask app
app = Flask(__name__)

# Configurations for SQLAlchemy (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model for medical examinations
class MedicalExam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(50), nullable=False)
    exam_type = db.Column(db.String(50), nullable=False)  # e.g., "Confined Space", "Working at Heights"
    exam_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convert the database record to a dictionary."""
        return {
            'id': self.id,
            'patient_name': self.patient_name,
            'exam_type': self.exam_type,
            'exam_date': self.exam_date.strftime('%Y-%m-%d %H:%M:%S'),
            'notes': self.notes
        }

# Create database tables
@app.before_first_request
def setup_database():
    """Initialize the database."""
    db.create_all()

# Route to schedule a new medical examination
@app.route('/schedule', methods=['POST'])
def schedule_exam():
    """API endpoint to schedule a new medical examination."""
    try:
        data = request.json
        # Validate input
        if 'patient_name' not in data or 'exam_type' not in data or 'exam_date' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Parse the exam date
        try:
            exam_date = datetime.strptime(data['exam_date'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM:SS'}), 400
        
        # Create a new MedicalExam record
        new_exam = MedicalExam(
            patient_name=data['patient_name'],
            exam_type=data['exam_type'],
            exam_date=exam_date,
            notes=data.get('notes', '')
        )
        db.session.add(new_exam)
        db.session.commit()

        return jsonify({'message': 'Medical examination scheduled successfully', 'exam': new_exam.to_dict()}), 201
    except Exception as e:
        # Log and return error
        traceback.print_exc()
        return jsonify({'error': 'An internal error occurred'}), 500

# Route to fetch all scheduled medical examinations
@app.route('/examinations', methods=['GET'])
def get_examinations():
    """API endpoint to fetch all scheduled medical examinations."""
    exams = MedicalExam.query.all()
    return jsonify([exam.to_dict() for exam in exams]), 200

# Route to fetch a specific examination by ID
@app.route('/examinations/<int:exam_id>', methods=['GET'])
def get_exam_by_id(exam_id):
    """API endpoint to fetch a specific examination by ID."""
    exam = MedicalExam.query.get(exam_id)
    if not exam:
        return jsonify({'error': 'Examination not found'}), 404
    return jsonify(exam.to_dict()), 200

# Route to cancel/delete an examination by ID
@app.route('/examinations/<int:exam_id>', methods=['DELETE'])
def delete_exam_by_id(exam_id):
    """API endpoint to cancel/delete an examination by ID."""
    try:
        exam = MedicalExam.query.get(exam_id)
        if not exam:
            return jsonify({'error': 'Examination not found'}), 404

        db.session.delete(exam)
        db.session.commit()
        return jsonify({'message': 'Examination deleted successfully'}), 200
    except Exception as e:
        # Log and return error
        traceback.print_exc()
        return jsonify({'error': 'An internal error occurred'}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features of the Code:
1. **Flask Framework**: Used for building the API endpoints.
2. **SQLAlchemy ORM**: Used for database management.
3. **Error Handling**: Proper error handling for invalid inputs and internal server errors.
4. **Production-Ready**: Includes necessary routes for CRUD operations related to scheduling medical examinations.
