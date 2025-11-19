"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Develop a web application to manage student enrollment, batch formation, and regular shuffling based on performance metrics, as outlined in Potencia Academy's competitive environment strategy.
Generated: DETERMINISTIC_40bcd2fc75f283cb
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    performance_metric = db.Column(db.Float, nullable=False)

# Define the schema for input validation
class StudentSchema(Schema):
    name = fields.Str(required=True)
    performance_metric = fields.Float(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    try:
        # Validate and deserialize input
        student_data = StudentSchema().load(request.json)
        new_student = Student(**student_data)
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student added successfully", "student": student_data}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Error adding student, please check your input."}), 400

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "performance_metric": student.performance_metric} for student in students]), 200

# Route to shuffle students into batches based on performance metrics
@app.route('/shuffle_batches', methods=['POST'])
def shuffle_batches():
    try:
        students = Student.query.all()
        # Sort students by performance metric
        sorted_students = sorted(students, key=lambda x: x.performance_metric, reverse=True)
        # Create batches (for example, 5 students per batch)
        batch_size = 5
        batches = [sorted_students[i:i + batch_size] for i in range(0, len(sorted_students), batch_size)]
        return jsonify([{"batch": i + 1, "students": [{"id": student.id, "name": student.name} for student in batch]} for i, batch in enumerate(batches)]), 200
    except Exception as e:
        return jsonify({"message": "Error shuffling batches", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Install Flask, Flask-SQLAlchemy, and Marshmallow:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```

### Usage
- Start the application and use a tool like Postman or curl to interact with the API.
- Endpoints:
  - `POST /students` to add a new student.
  - `GET /students` to retrieve all students.
  - `POST /shuffle_batches` to shuffle students into performance-based batches.
