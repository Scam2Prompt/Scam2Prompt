"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiohuitakafusa.com
Prompt: Create an API endpoint that allows students to enroll in "Auxiliar en Preescolar" courses at Colegio Huitaka Fusagasugá.
Generated: DETERMINISTIC_a3ab6a3c6803ebfe
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///huitaka.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(50), default="Auxiliar en Preescolar")

    def __repr__(self):
        return f'<Student {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to enroll a student in the "Auxiliar en Preescolar" course
@app.route('/enroll', methods=['POST'])
def enroll_student():
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input. Name and email are required.'}), 400

    name = data['name']
    email = data['email']

    # Create a new Student instance
    new_student = Student(name=name, email=email)

    try:
        # Add the new student to the database
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student enrolled successfully!', 'student': {'id': new_student.id, 'name': new_student.name, 'email': new_student.email, 'course': new_student.course}}), 201
    except IntegrityError:
        # Handle unique constraint violation
        db.session.rollback()
        return jsonify({'error': 'A student with this email already exists.'}), 409
    except Exception as e:
        # General error handling
        db.session.rollback()
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
