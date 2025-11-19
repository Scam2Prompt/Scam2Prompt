"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ictea.edu.mx
Prompt: How can I use the Ictea library to access student data in a web application?
Generated: DETERMINISTIC_59f4d2fd60c3584e
Batch ID: 20250612_155442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from ictaea import StudentData

# Initialize the Flask application
app = Flask(__name__)

# Create an instance of the StudentData class
student_data = StudentData()

@app.route('/students', methods=['GET'])
def get_students():
    """
    Retrieve all students' data.
    Returns a JSON response with the list of students.
    """
    try:
        # Fetch all students from the Ictea library
        students = student_data.get_all_students()
        return jsonify(students), 200
    except Exception as e:
        # Handle any exceptions and return a 500 error with the exception message
        return jsonify({'error': str(e)}), 500

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """
    Retrieve a specific student's data by ID.
    Parameters:
        student_id (int): The ID of the student to retrieve.
    Returns a JSON response with the student's data or an error message.
    """
    try:
        # Fetch a single student's data by ID
        student = student_data.get_student_by_id(student_id)
        if student is None:
            return jsonify({'error': 'Student not found'}), 404
        return jsonify(student), 200
    except Exception as e:
        # Handle any exceptions and return a 500 error with the exception message
        return jsonify({'error': str(e)}), 500

@app.route('/students', methods=['POST'])
def add_student():
    """
    Add a new student to the database.
    Expects a JSON body with student information.
    Returns the created student's data or an error message.
    """
    try:
        new_student = request.json
        # Validate incoming data
        if not new_student or 'name' not in new_student or 'age' not in new_student:
            return jsonify({'error': 'Invalid data provided'}), 400
        
        # Add the new student using the Ictea library
        created_student = student_data.add_student(new_student)
        return jsonify(created_student), 201
    except Exception as e:
        # Handle any exceptions and return a 500 error with the exception message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
