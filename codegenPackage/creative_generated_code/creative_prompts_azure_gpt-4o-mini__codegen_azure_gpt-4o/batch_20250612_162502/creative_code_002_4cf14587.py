"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Create an API endpoint that provides details about the courses and workshops offered by Instituto de Especialidades Odontológicas, including their accreditation by the SEP.
Generated: DETERMINISTIC_4cf14587749abb4a
Batch ID: 20250612_162502
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

# Sample data representing courses and workshops
courses_and_workshops = [
    {
        "id": 1,
        "name": "Advanced Orthodontics Workshop",
        "description": "Hands-on workshop focused on advanced orthodontics techniques.",
        "duration": "3 days",
        "accredited_by_SEP": True
    },
    {
        "id": 2,
        "name": "Dental Implantology Course",
        "description": "Comprehensive course about dental implants and surgical procedures.",
        "duration": "2 weeks",
        "accredited_by_SEP": True
    },
    {
        "id": 3,
        "name": "Oral Surgery Workshop",
        "description": "Focused training in oral surgery methods and practices.",
        "duration": "5 days",
        "accredited_by_SEP": False
    }
]

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to ensure the API is running.
    """
    logger.info("Health check endpoint accessed.")
    return jsonify({"status": "API is running"}), 200

# Endpoint to get all courses and workshops
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    Get details of all courses and workshops offered by Instituto de Especialidades Odontológicas.
    """
    logger.info("Fetching list of courses and workshops.")
    try:
        return jsonify(courses_and_workshops), 200
    except Exception as e:
        logger.error(f"Failed to fetch courses and workshops: {str(e)}")
        return jsonify({"error": "Failed to fetch courses and workshops"}), 500

# Endpoint to get a specific course or workshop by ID
@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    """
    Get details of a specific course or workshop by ID.
    :param course_id: The ID of the course or workshop.
    """
    logger.info(f"Fetching details for course ID: {course_id}")
    try:
        course = next((c for c in courses_and_workshops if c['id'] == course_id), None)
        if course:
            return jsonify(course), 200
        else:
            logger.warning(f"Course with ID {course_id} not found.")
            return jsonify({"error": "Course not found"}), 404
    except Exception as e:
        logger.error(f"Failed to fetch course details: {str(e)}")
        return jsonify({"error": "Failed to fetch course details"}), 500

# Error handling for unsupported routes
@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors for unsupported routes.
    """
    logger.warning("Unsupported route accessed.")
    return jsonify({"error": "Endpoint not found"}), 404

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
