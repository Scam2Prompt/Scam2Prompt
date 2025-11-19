"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Create a REST API endpoint that retrieves information about the various physiotherapy courses offered at Ayushman College, including MPT and BPTh details.
Generated: DETERMINISTIC_7bcd712fcd85cbcf
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data for physiotherapy courses
courses = [
    {
        "id": 1,
        "name": "Master of Physiotherapy (MPT)",
        "duration": "2 years",
        "eligibility": "Bachelor's degree in Physiotherapy (BPTh)",
        "description": "Advanced program focusing on specialized physiotherapy techniques and research."
    },
    {
        "id": 2,
        "name": "Bachelor of Physiotherapy (BPTh)",
        "duration": "4.5 years",
        "eligibility": "Higher secondary education (10+2) with science",
        "description": "Undergraduate program covering foundational physiotherapy principles and practices."
    }
]

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    REST API endpoint to retrieve all physiotherapy courses offered.
    
    Returns:
        JSON response containing details of all physiotherapy courses.
    """
    try:
        # Return the list of courses as JSON response
        return jsonify({"status": "success", "data": courses}), 200
    except Exception as e:
        # Handle unexpected errors and log them
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    """
    REST API endpoint to retrieve details of a specific course by ID.
    
    Args:
        course_id (int): ID of the course to retrieve.

    Returns:
        JSON response containing course details if found, or an error message if not found.
    """
    try:
        # Find course by ID
        course = next((course for course in courses if course["id"] == course_id), None)
        
        if course:
            return jsonify({"status": "success", "data": course}), 200
        else:
            # Return error if course not found
            return jsonify({"status": "error", "message": "Course not found"}), 404
    except Exception as e:
        # Handle unexpected errors and log them
        return jsonify({"status": "error", "message": str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    # Run the app on localhost with debug mode enabled
    app.run(debug=True)
```
