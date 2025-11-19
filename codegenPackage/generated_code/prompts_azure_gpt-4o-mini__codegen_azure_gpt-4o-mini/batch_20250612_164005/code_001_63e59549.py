"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Create a REST API that allows students to check their application status for the Professor Substitute selection process at IGEOG/UERJ, utilizing the data from the provided editais.
Generated: DETERMINISTIC_63e59549a3528572
Batch ID: 20250612_164005
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    application_status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Student object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'application_status': self.application_status
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student_status(student_id):
    """
    Retrieve the application status of a student by their ID.
    
    Args:
        student_id (int): The ID of the student.

    Returns:
        JSON response with student status or error message.
    """
    try:
        student = Student.query.get(student_id)
        if student is None:
            return jsonify({'error': 'Student not found'}), 404
        return jsonify(student.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/students', methods=['POST'])
def add_student():
    """
    Add a new student to the database.
    
    Returns:
        JSON response with the created student or error message.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'application_status' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_student = Student(name=data['name'], application_status=data['application_status'])
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify(new_student.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
