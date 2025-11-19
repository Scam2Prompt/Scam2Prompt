"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://academiamedicinaestetica.cl
Prompt: Create a REST API that provides information about the different diplomas and courses in aesthetic medicine offered by Academia Medicina Estética.
Generated: DETERMINISTIC_a8dbef3e8bd2b9c2
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data for diplomas and courses
data = {
    "diplomas": [
        {
            "id": 1,
            "name": "Diploma in Advanced Aesthetic Medicine",
            "description": "A comprehensive program covering advanced techniques in aesthetic medicine.",
            "duration": "6 months"
        },
        {
            "id": 2,
            "name": "Diploma in Facial Aesthetics",
            "description": "Focuses on facial aesthetic procedures and treatments.",
            "duration": "4 months"
        }
    ],
    "courses": [
        {
            "id": 1,
            "name": "Botulinum Toxin Course",
            "description": "Learn the safe and effective use of Botulinum Toxin in aesthetic medicine.",
            "duration": "2 days"
        },
        {
            "id": 2,
            "name": "Dermal Fillers Course",
            "description": "Master techniques for administering dermal fillers.",
            "duration": "3 days"
        }
    ]
}

# Error handling for invalid routes
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

# Endpoint to retrieve all diplomas
@app.route('/api/diplomas', methods=['GET'])
def get_diplomas():
    return jsonify({"diplomas": data["diplomas"]}), 200

# Endpoint to retrieve a single diploma by ID
@app.route('/api/diplomas/<int:diploma_id>', methods=['GET'])
def get_diploma(diploma_id):
    diploma = next((d for d in data["diplomas"] if d["id"] == diploma_id), None)
    if diploma:
        return jsonify(diploma), 200
    return jsonify({"error": "Diploma not found"}), 404

# Endpoint to retrieve all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify({"courses": data["courses"]}), 200

# Endpoint to retrieve a single course by ID
@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = next((c for c in data["courses"] if c["id"] == course_id), None)
    if course:
        return jsonify(course), 200
    return jsonify({"error": "Course not found"}), 404

# Error handling for unsupported HTTP methods
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed", "message": "The requested method is not allowed for the specified endpoint."}), 405

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
