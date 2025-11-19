"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Develop a RESTful API endpoint that lists all available aviation security courses, including the Avsec Management Course and Risk Management Course, as offered by Welwitschia Aviation.
Generated: DETERMINISTIC_79288b154b00f025
Batch ID: 20250612_155233
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

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock data for aviation security courses
COURSES = [
    {"id": 1, "name": "Avsec Management Course", "description": "Learn advanced aviation security management techniques."},
    {"id": 2, "name": "Risk Management Course", "description": "Understand and mitigate risks in aviation security."},
    {"id": 3, "name": "Basic Aviation Security Course", "description": "Introduction to aviation security principles."},
    {"id": 4, "name": "Advanced Screening Techniques Course", "description": "Master advanced screening methods for airport security."},
]

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    RESTful API endpoint to list all available aviation security courses.

    Returns:
        JSON response containing course details.
    """
    try:
        # Log the incoming request
        logger.info("Received request to list all courses.")
        
        # Return all courses as a JSON response
        return jsonify({"status": "success", "data": COURSES}), 200
    except Exception as e:
        # Log the error
        logger.error(f"Error occurred while fetching courses: {str(e)}")
        
        # Return an error response
        return jsonify({"status": "error", "message": "An error occurred while fetching courses."}), 500

# Error handling for invalid routes
@app.errorhandler(404)
def handle_404(error):
    """
    Handle invalid routes gracefully.
    
    Returns:
        JSON response for 404 errors.
    """
    return jsonify({"status": "error", "message": "Endpoint not found."}), 404

# Run the application
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)
```
