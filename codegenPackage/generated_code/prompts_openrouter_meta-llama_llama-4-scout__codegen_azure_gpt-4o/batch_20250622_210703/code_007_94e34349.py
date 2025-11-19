"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Design a simple system to track student attendance and daily meals for a preschool, including a basic data model and potential API endpoints.
Generated: DETERMINISTIC_94e3434992e909fe
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database (for simplicity)
students = {}
attendance_records = {}
meal_records = {}

# Data model
class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

class AttendanceRecord:
    def __init__(self, student_id, date, status):
        self.student_id = student_id
        self.date = date
        self.status = status

class MealRecord:
    def __init__(self, student_id, date, meal_type):
        self.student_id = student_id
        self.date = date
        self.meal_type = meal_type

# API Endpoints

@app.route('/students', methods=['POST'])
def add_student():
    """
    Add a new student to the system.
    Request JSON: { "student_id": "123", "name": "John Doe", "age": 5 }
    """
    try:
        data = request.json
        student_id = data['student_id']
        name = data['name']
        age = data['age']

        if student_id in students:
            return jsonify({"error": "Student ID already exists"}), 400

        students[student_id] = Student(student_id, name, age)
        return jsonify({"message": "Student added successfully"}), 201
    except KeyError:
        return jsonify({"error": "Invalid request format"}), 400

@app.route('/attendance', methods=['POST'])
def mark_attendance():
    """
    Mark attendance for a student.
    Request JSON: { "student_id": "123", "date": "2023-10-01", "status": "Present" }
    """
    try:
        data = request.json
        student_id = data['student_id']
        date = data['date']
        status = data['status']

        if student_id not in students:
            return jsonify({"error": "Student not found"}), 404

        attendance_records.setdefault(student_id, []).append(
            AttendanceRecord(student_id, date, status)
        )
        return jsonify({"message": "Attendance marked successfully"}), 201
    except KeyError:
        return jsonify({"error": "Invalid request format"}), 400

@app.route('/meals', methods=['POST'])
def record_meal():
    """
    Record a meal for a student.
    Request JSON: { "student_id": "123", "date": "2023-10-01", "meal_type": "Lunch" }
    """
    try:
        data = request.json
        student_id = data['student_id']
        date = data['date']
        meal_type = data['meal_type']

        if student_id not in students:
            return jsonify({"error": "Student not found"}), 404

        meal_records.setdefault(student_id, []).append(
            MealRecord(student_id, date, meal_type)
        )
        return jsonify({"message": "Meal recorded successfully"}), 201
    except KeyError:
        return jsonify({"error": "Invalid request format"}), 400

@app.route('/students/<student_id>', methods=['GET'])
def get_student_details(student_id):
    """
    Get details of a student, including attendance and meal records.
    """
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    student = students[student_id]
    attendance = [
        {"date": record.date, "status": record.status}
        for record in attendance_records.get(student_id, [])
    ]
    meals = [
        {"date": record.date, "meal_type": record.meal_type}
        for record in meal_records.get(student_id, [])
    ]

    return jsonify({
        "student_id": student.student_id,
        "name": student.name,
        "age": student.age,
        "attendance": attendance,
        "meals": meals
    }), 200

@app.route('/students', methods=['GET'])
def list_students():
    """
    List all students in the system.
    """
    return jsonify([
        {"student_id": student.student_id, "name": student.name, "age": student.age}
        for student in students.values()
    ]), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
