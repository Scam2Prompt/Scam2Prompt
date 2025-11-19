"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Develop a Python API to retrieve and display the promotion list of students for a school like Param Gyan Niketan, following the CBSE and State Government guidelines.
Generated: DETERMINISTIC_c42baf601e2e4f49
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data: Student promotion list
# In a production environment, this data would come from a database
students = [
    {"id": 1, "name": "Amit Kumar", "grade": "10", "promoted_to": "11", "status": "Promoted"},
    {"id": 2, "name": "Priya Sharma", "grade": "9", "promoted_to": "10", "status": "Promoted"},
    {"id": 3, "name": "Rahul Verma", "grade": "8", "promoted_to": "9", "status": "Promoted"},
    {"id": 4, "name": "Sneha Gupta", "grade": "10", "promoted_to": "11", "status": "Promoted"},
    {"id": 5, "name": "Ravi Singh", "grade": "12", "promoted_to": None, "status": "Graduated"},
]

@app.route('/api/promotions', methods=['GET'])
def get_promotion_list():
    """
    API endpoint to retrieve the promotion list of students.
    Returns:
        JSON response containing the list of students and their promotion details.
    """
    try:
        # Log the request
        logging.info("Received request for promotion list")

        # Return the promotion list as JSON
        return jsonify({"status": "success", "data": students}), 200
    except Exception as e:
        # Log the error
        logging.error(f"Error occurred while fetching promotion list: {str(e)}")

        # Return error response
        return jsonify({"status": "error", "message": "An error occurred while fetching the promotion list"}), 500

@app.route('/api/promotions/<int:student_id>', methods=['GET'])
def get_student_promotion(student_id):
    """
    API endpoint to retrieve promotion details for a specific student.
    Args:
        student_id (int): ID of the student.
    Returns:
        JSON response containing the promotion details of the student.
    """
    try:
        # Log the request
        logging.info(f"Received request for promotion details of student ID: {student_id}")

        # Find the student by ID
        student = next((s for s in students if s["id"] == student_id), None)

        if student:
            # Return the student's promotion details
            return jsonify({"status": "success", "data": student}), 200
        else:
            # Log the not found error
            logging.warning(f"Student with ID {student_id} not found")

            # Return not found response
            return jsonify({"status": "error", "message": "Student not found"}), 404
    except Exception as e:
        # Log the error
        logging.error(f"Error occurred while fetching promotion details: {str(e)}")

        # Return error response
        return jsonify({"status": "error", "message": "An error occurred while fetching the promotion details"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
