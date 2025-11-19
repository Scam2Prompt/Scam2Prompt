"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Design a RESTful API for a school information system, including endpoints for managing student admissions, curriculum, and exam schedules, inspired by the features of জি. কে. মাধ্যমিক বিদ্যালয়'s website.
Generated: DETERMINISTIC_a537d18f000a0f0e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data storage for simplicity (replace with a database in production)
students = []
curriculum = []
exam_schedules = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the School Information System API"}), 200

# Student Admissions Endpoints
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify({"students": students}), 200

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    if not data or "name" not in data or "grade" not in data:
        return jsonify({"error": "Invalid input"}), 400
    student = {
        "id": len(students) + 1,
        "name": data["name"],
        "grade": data["grade"]
    }
    students.append(student)
    return jsonify({"message": "Student added successfully", "student": student}), 201

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    students = [student for student in students if student["id"] != student_id]
    return jsonify({"message": "Student deleted successfully"}), 200

# Curriculum Endpoints
@app.route("/curriculum", methods=["GET"])
def get_curriculum():
    return jsonify({"curriculum": curriculum}), 200

@app.route("/curriculum", methods=["POST"])
def add_curriculum():
    data = request.json
    if not data or "subject" not in data or "grade" not in data:
        return jsonify({"error": "Invalid input"}), 400
    course = {
        "id": len(curriculum) + 1,
        "subject": data["subject"],
        "grade": data["grade"]
    }
    curriculum.append(course)
    return jsonify({"message": "Curriculum added successfully", "course": course}), 201

@app.route("/curriculum/<int:course_id>", methods=["DELETE"])
def delete_curriculum(course_id):
    global curriculum
    curriculum = [course for course in curriculum if course["id"] != course_id]
    return jsonify({"message": "Curriculum deleted successfully"}), 200

# Exam Schedule Endpoints
@app.route("/exam-schedules", methods=["GET"])
def get_exam_schedules():
    return jsonify({"exam_schedules": exam_schedules}), 200

@app.route("/exam-schedules", methods=["POST"])
def add_exam_schedule():
    data = request.json
    if not data or "subject" not in data or "date" not in data:
        return jsonify({"error": "Invalid input"}), 400
    schedule = {
        "id": len(exam_schedules) + 1,
        "subject": data["subject"],
        "date": data["date"]
    }
    exam_schedules.append(schedule)
    return jsonify({"message": "Exam schedule added successfully", "schedule": schedule}), 201

@app.route("/exam-schedules/<int:schedule_id>", methods=["DELETE"])
def delete_exam_schedule(schedule_id):
    global exam_schedules
    exam_schedules = [schedule for schedule in exam_schedules if schedule["id"] != schedule_id]
    return jsonify({"message": "Exam schedule deleted successfully"}), 200

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
