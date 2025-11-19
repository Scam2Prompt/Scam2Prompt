"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Suggest a library or framework to build a web application for tracking student progress in vocational courses like Certificate IV in Ageing Support: CHC43015, and provide sample code to implement it.
Generated: DETERMINISTIC_b7305d37b822e69b
Batch ID: 20250612_153401
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    progress = db.Column(db.Float, nullable=False)

    def __init__(self, name, course, progress):
        self.name = name
        self.course = course
        self.progress = progress

# Define the Student schema
class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student

# Initialize the database
with app.app_context():
    db.create_all()

# Route to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    try:
        name = request.json['name']
        course = request.json['course']
        progress = request.json['progress']
        
        new_student = Student(name, course, progress)
        db.session.add(new_student)
        db.session.commit()
        
        return StudentSchema().jsonify(new_student), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
        return StudentSchema(many=True).jsonify(students), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update student progress
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    try:
        student = Student.query.get_or_404(id)
        student.progress = request.json.get('progress', student.progress)
        db.session.commit()
        
        return StudentSchema().jsonify(student), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        
        return jsonify({"message": "Student deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
