"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Create a REST API endpoint that retrieves information about the "Dermal Fillers: Facial Anatomy and Injection Techniques" course, including pricing and access details.
Generated: DETERMINISTIC_dd719d180e513728
Batch ID: 20250612_162945
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

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock database (typically this would connect to an actual database)
COURSES = {
    "Dermal Fillers: Facial Anatomy and Injection Techniques": {
        "description": "A comprehensive course on facial anatomy and injection techniques for dermal fillers.",
        "price": 299.99,
        "access_details": "Lifetime access with downloadable resources and certification upon completion."
    }
}

@app.route('/api/course', methods=['GET'])
def get_course_info():
    """
    REST API endpoint to retrieve course information.
    URL: /api/course
    Method: GET
    Query Params: course_name (optional)
    Response: JSON object containing course details
    """
    try:
        # Extract course name from query params (defaulting to our example course)
        course_name = request.args.get('course_name', "Dermal Fillers: Facial Anatomy and Injection Techniques")

        # Validate if the course exists
        if course_name in COURSES:
            course_info = COURSES[course_name]
            response = {
                "success": True,
                "course_name": course_name,
                "details": course_info
            }
            return jsonify(response), 200
        else:
            # Course not found error
            response = {
                "success": False,
                "error": "Course not found."
            }
            return jsonify(response), 404

    except Exception as e:
        # Log the exception and return an error response
        logger.error(f"An error occurred: {str(e)}")
        response = {
            "success": False,
            "error": "An internal server error occurred."
        }
        return jsonify(response), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
