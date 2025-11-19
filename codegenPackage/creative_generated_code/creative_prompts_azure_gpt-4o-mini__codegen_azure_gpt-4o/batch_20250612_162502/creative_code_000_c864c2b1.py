"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Generate a code snippet for a web application that allows users to enroll in the "Especialidad en Ortodoncia" program at Instituto de Especialidades Odontológicas, including fields for start date and class schedule.
Generated: DETERMINISTIC_c864c2b13d604534
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for enrolled students (for simplicity; use a database in production)
enrolled_students = []

@app.route('/enroll', methods=['POST'])
def enroll():
    """
    Endpoint to enroll a user in the "Especialidad en Ortodoncia" program.
    Expects JSON data with name, email, start_date, and class_schedule fields.
    """
    try:
        # Parse incoming JSON data
        data = request.json
        
        # Validate required fields
        if not all(field in data for field in ['name', 'email', 'start_date', 'class_schedule']):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate start_date format
        try:
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid start_date format. Use YYYY-MM-DD."}), 400
        
        # Format data for storage
        enrollment = {
            "name": data['name'],
            "email": data['email'],
            "start_date": start_date.strftime('%Y-%m-%d'),
            "class_schedule": data['class_schedule']
        }
        
        # Save enrollment
        enrolled_students.append(enrollment)
        
        return jsonify({"message": "Enrollment successful", "data": enrollment}), 201
    
    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/enrollments', methods=['GET'])
def get_enrollments():
    """
    Endpoint to retrieve all enrollments for the "Especialidad en Ortodoncia" program.
    """
    return jsonify({"enrollments": enrolled_students}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```
