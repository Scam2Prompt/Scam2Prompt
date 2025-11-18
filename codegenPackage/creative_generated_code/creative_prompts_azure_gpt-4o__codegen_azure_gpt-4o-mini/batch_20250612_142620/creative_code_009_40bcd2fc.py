"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Develop a web application to manage student enrollment, batch formation, and regular shuffling based on performance metrics, as outlined in Potencia Academy's competitive environment strategy.
Generated: DETERMINISTIC_40bcd2fc75f283cb
Batch ID: 20250612_142620
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    performance_metric = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to enroll a new student
@app.route('/enroll', methods=['POST'])
def enroll_student():
    data = request.json
    try:
        new_student = Student(name=data['name'], performance_metric=data['performance_metric'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"message": "Student enrolled successfully", "student": new_student.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Student enrollment failed, check the input data"}), 400

# API endpoint to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "performance_metric": student.performance_metric} for student in students]), 200

# API endpoint to shuffle students into batches based on performance metrics
@app.route('/shuffle-batches', methods=['POST'])
def shuffle_batches():
    try:
        students = Student.query.order_by(Student.performance_metric).all()
        batch_size = request.json.get('batch_size', 5)
        batches = [students[i:i + batch_size] for i in range(0, len(students), batch_size)]
        return jsonify([{"batch": i + 1, "students": [{"id": student.id, "name": student.name} for student in batch]} for i, batch in enumerate(batches)]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update student performance metric
@app.route('/update-performance/<int:student_id>', methods=['PUT'])
def update_performance(student_id):
    data = request.json
    try:
        student = Student.query.get_or_404(student_id)
        student.performance_metric = data['performance_metric']
        db.session.commit()
        return jsonify({"message": "Performance updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
