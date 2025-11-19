"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Develop a Python API to retrieve and display the promotion list of students for a school like Param Gyan Niketan, following the CBSE and State Government guidelines.
Generated: DETERMINISTIC_c42baf601e2e4f49
Batch ID: 20250622_212433
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
    grade = db.Column(db.String(10), nullable=False)
    promoted = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert the Student object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'grade': self.grade,
            'promoted': self.promoted
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/promotions', methods=['GET'])
def get_promotions():
    """
    Retrieve the list of students who have been promoted.
    
    Returns:
        JSON response containing the list of promoted students.
    """
    try:
        # Query the database for promoted students
        promoted_students = Student.query.filter_by(promoted=True).all()
        return jsonify([student.to_dict() for student in promoted_students]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/promote_student/<int:student_id>', methods=['PUT'])
def promote_student(student_id):
    """
    Promote a student by their ID.
    
    Args:
        student_id (int): The ID of the student to promote.
    
    Returns:
        JSON response indicating success or failure.
    """
    try:
        student = Student.query.get_or_404(student_id)
        student.promoted = True
        db.session.commit()
        return jsonify({'message': f'Student {student.name} promoted successfully.'}), 200
    except SQLAlchemyError as e:
        # Handle database errors
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
