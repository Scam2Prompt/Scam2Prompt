"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Recommend a library or API to create a parental portal for a school, similar to the one mentioned on the Deepti Convent Higher Secondary School website, and provide sample code for integration.
Generated: DETERMINISTIC_cbca219b4fcc9b88
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Students
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    parent_email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"

# Create the database
with app.app_context():
    db.create_all()

# Route to add a new student
@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        data = request.json
        new_student = Student(name=data['name'], grade=data['grade'], parent_email=data['parent_email'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
        return jsonify([{"id": student.id, "name": student.name, "grade": student.grade} for student in students]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a student's information
@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        return jsonify({"id": student.id, "name": student.name, "grade": student.grade, "parent_email": student.parent_email}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions for Integration:
1. Ensure you have Flask and Flask-SQLAlchemy installed:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-CORS
   ```

2. Save the code in a file, for instance, `app.py`.

3. Run the application using:
   ```bash
   python app.py
   ```

4. Use REST client tools like Postman to interact with the API:
   - To add a student, make a POST request to `/add_student` with JSON body:
     ```json
     {
       "name": "John Doe",
       "grade": "10",
       "parent_email": "parent@example.com"
     }
     ```

   - To retrieve all students, make a GET request to `/students`.

   - To get a specific student's information, make a GET request to `/student/{student_id}`.
