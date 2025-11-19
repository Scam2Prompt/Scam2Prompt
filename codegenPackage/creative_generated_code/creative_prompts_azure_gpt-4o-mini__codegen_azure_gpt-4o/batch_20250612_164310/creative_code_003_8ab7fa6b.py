"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Develop a REST API endpoint that allows users to fetch details about the "Diplomado de Auditoria Gubernamental" course from AulaContable.
Generated: DETERMINISTIC_8ab7fa6b9f65683f
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configuring logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock database for course details
COURSES = {
    "Diplomado de Auditoria Gubernamental": {
        "id": 1,
        "name": "Diplomado de Auditoria Gubernamental",
        "description": "Curso especializado para auditores gubernamentales.",
        "duration": "6 months",
        "price": "1200 USD",
        "institution": "AulaContable"
    }
}

@app.route('/api/courses/<course_name>', methods=['GET'])
def get_course_details(course_name):
    """
    REST API endpoint to fetch details of a specific course.
    :param course_name: Name of the course passed as a URL parameter.
    :return: JSON response with course details or error message.
    """
    try:
        # Fetch course details from the mock database
        course_details = COURSES.get(course_name)
        
        # If the course is not found, return a 404 error
        if not course_details:
            logger.warning(f"Course '{course_name}' not found.")
            return jsonify({"error": "Course not found"}), 404
        
        # Return the course details
        logger.info(f"Course details for '{course_name}' fetched successfully.")
        return jsonify(course_details), 200
    
    except Exception as e:
        # Log unexpected errors and return a 500 error
        logger.error(f"Error fetching course details: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
