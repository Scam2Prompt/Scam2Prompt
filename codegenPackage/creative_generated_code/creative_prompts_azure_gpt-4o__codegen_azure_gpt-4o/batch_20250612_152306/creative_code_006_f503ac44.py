"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Write code to implement an online registration system for vocational courses, including validation for fields like course type, duration, and student details.
Generated: DETERMINISTIC_f503ac4465baaa28
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Online Registration System for Vocational Courses
# Language: Python
# Framework: Flask (for web application)

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Supported course types and durations
VALID_COURSE_TYPES = ["Programming", "Design", "Marketing", "Finance"]
VALID_DURATIONS = [1, 3, 6, 12]  # Durations in months

# In-memory database for storing registrations (for demonstration purposes)
registrations = []

# Helper function for validating student details
def validate_student_details(student_details):
    required_fields = ["name", "email", "phone"]
    for field in required_fields:
        if field not in student_details or not student_details[field].strip():
            raise BadRequest(f"Missing or invalid field: {field}")
    
    # Validate email format
    if "@" not in student_details["email"] or "." not in student_details["email"]:
        raise BadRequest("Invalid email format.")
    
    # Validate phone number (must be digits and at least 10 characters)
    if not student_details["phone"].isdigit() or len(student_details["phone"]) < 10:
        raise BadRequest("Invalid phone number.")

# Helper function for validating course details
def validate_course_details(course_details):
    if "course_type" not in course_details or course_details["course_type"] not in VALID_COURSE_TYPES:
        raise BadRequest(f"Invalid course type. Valid options: {', '.join(VALID_COURSE_TYPES)}")
    
    if "duration" not in course_details or course_details["duration"] not in VALID_DURATIONS:
        raise BadRequest(f"Invalid duration. Valid options: {VALID_DURATIONS} months.")

# Endpoint for registering a student for a vocational course
@app.route('/register', methods=['POST'])
def register():
    try:
        # Parse and validate input data
        data = request.json
        if not data:
            raise BadRequest("Invalid input: JSON body is required.")
        
        student_details = data.get("student_details")
        course_details = data.get("course_details")
        
        if not student_details or not course_details:
            raise BadRequest("Missing student_details or course_details.")
        
        validate_student_details(student_details)
        validate_course_details(course_details)
        
        # Save registration (for now, we save it in memory)
        registration = {
            "student_details": student_details,
            "course_details": course_details
        }
        registrations.append(registration)
        
        # Return success response
        return jsonify({"message": "Registration successful.", "registration": registration}), 201
    
    except BadRequest as e:
        # Handle validation errors
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Endpoint to view all registrations
@app.route('/registrations', methods=['GET'])
def get_registrations():
    return jsonify({"registrations": registrations}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
