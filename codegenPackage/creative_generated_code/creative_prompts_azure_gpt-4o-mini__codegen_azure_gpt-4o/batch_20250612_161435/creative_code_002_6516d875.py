"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Create an API recommendation for managing course registrations and student notes for the programs offered at IESTP PANGOA.
Generated: DETERMINISTIC_6516d875597fcae2
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (for demonstration purposes)
courses = {}  # Format: {course_id: {"name": str, "students": {student_id: {"name": str, "notes": list}}}}
students = {}  # Format: {student_id: {"name": str, "registered_courses": list}}

# Helper function to validate course data
def validate_course_data(course_data):
    if not course_data.get("name"):
        return "Course name is required."
    return None

# Helper function to validate student data
def validate_student_data(student_data):
    if not student_data.get("name"):
        return "Student name is required."
    return None

# Route to create a new course
@app.route("/courses", methods=["POST"])
def create_course():
    try:
        course_data = request.json
        error = validate_course_data(course_data)
        if error:
            return jsonify({"error": error}), 400
        
        course_id = len(courses) + 1
        courses[course_id] = {"name": course_data["name"], "students": {}}
        
        return jsonify({"message": "Course created successfully.", "course_id": course_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to register a student
@app.route("/students", methods=["POST"])
def register_student():
    try:
        student_data = request.json
        error = validate_student_data(student_data)
        if error:
            return jsonify({"error": error}), 400
        
        student_id = len(students) + 1
        students[student_id] = {"name": student_data["name"], "registered_courses": []}
        
        return jsonify({"message": "Student registered successfully.", "student_id": student_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to enroll a student into a course
@app.route("/enroll", methods=["POST"])
def enroll_student():
    try:
        enrollment_data = request.json
        student_id = enrollment_data.get("student_id")
        course_id = enrollment_data.get("course_id")
        
        if not student_id or not course_id:
            return jsonify({"error": "Student ID and Course ID are required."}), 400

        if student_id not in students:
            return jsonify({"error": "Student not found."}), 404
        
        if course_id not in courses:
            return jsonify({"error": "Course not found."}), 404
        
        # Add student to course
        student_info = students[student_id]
        course_info = courses[course_id]
        
        if student_id in course_info["students"]:
            return jsonify({"error": "Student is already enrolled in this course."}), 400
        
        course_info["students"][student_id] = {"name": student_info["name"], "notes": []}
        student_info["registered_courses"].append(course_id)
        
        return jsonify({"message": "Student enrolled successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add notes for a student in a course
@app.route("/notes", methods=["POST"])
def add_notes():
    try:
        notes_data = request.json
        student_id = notes_data.get("student_id")
        course_id = notes_data.get("course_id")
        note = notes_data.get("note")
        
        if not student_id or not course_id or not note:
            return jsonify({"error": "Student ID, Course ID, and note are required."}), 400

        if course_id not in courses:
            return jsonify({"error": "Course not found."}), 404
        
        course_info = courses[course_id]
        if student_id not in course_info["students"]:
            return jsonify({"error": "Student is not enrolled in this course."}), 404
        
        course_info["students"][student_id]["notes"].append(note)
        
        return jsonify({"message": "Note added successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to view all courses
@app.route("/courses", methods=["GET"])
def view_courses():
    try:
        return jsonify(courses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to view all students
@app.route("/students", methods=["GET"])
def view_students():
    try:
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to view notes of a student in a course
@app.route("/notes", methods=["GET"])
def view_notes():
    try:
        student_id = request.args.get("student_id")
        course_id = request.args.get("course_id")
        
        if not student_id or not course_id:
            return jsonify({"error": "Student ID and Course ID are required."}), 400

        if course_id not in courses:
            return jsonify({"error": "Course not found."}), 404
        
        course_info = courses[course_id]
        if student_id not in course_info["students"]:
            return jsonify({"error": "Student is not enrolled in this course."}), 404
        
        notes = course_info["students"][student_id]["notes"]
        return jsonify({"notes": notes}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the application
if __name__ == "__main__":
    app.run(debug=True)
```
