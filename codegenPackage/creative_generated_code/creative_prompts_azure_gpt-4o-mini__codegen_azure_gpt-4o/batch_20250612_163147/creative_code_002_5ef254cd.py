"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Create an API that provides information about the different occupational medical exams available at Medicid IPS, including details on exams for high-altitude work and confined spaces.
Generated: DETERMINISTIC_5ef254cdc9b6acad
Batch ID: 20250612_163147
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

# Sample data representing occupational medical exams
medical_exams = [
    {
        "id": 1,
        "name": "High-Altitude Work Medical Exam",
        "description": "A comprehensive evaluation to ensure workers are fit for high-altitude tasks.",
        "requirements": [
            "Physical examination",
            "Respiratory function test",
            "Cardiac stress test"
        ]
    },
    {
        "id": 2,
        "name": "Confined Spaces Medical Exam",
        "description": "Assessment to verify workers’ capability to operate safely in confined spaces.",
        "requirements": [
            "Physical examination",
            "Respiratory function test",
            "Psychological evaluation"
        ]
    }
]

@app.route("/api/medical-exams", methods=["GET"])
def get_medical_exams():
    """
    Endpoint to retrieve all available occupational medical exams.
    Returns:
        JSON response containing a list of medical exams.
    """
    return jsonify({"success": True, "data": medical_exams}), 200

@app.route("/api/medical-exams/<int:exam_id>", methods=["GET"])
def get_medical_exam_by_id(exam_id):
    """
    Endpoint to retrieve details about a specific medical exam by ID.
    Parameters:
        exam_id: ID of the medical exam to retrieve.
    Returns:
        JSON response containing the requested medical exam details, 
        or an error message if the exam is not found.
    """
    # Find the medical exam with the matching ID
    exam = next((exam for exam in medical_exams if exam["id"] == exam_id), None)
    
    if exam:
        return jsonify({"success": True, "data": exam}), 200
    else:
        return jsonify({
            "success": False,
            "error": "Medical exam not found."
        }), 404

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 errors.
    Returns:
        JSON response with error message for not-found resources.
    """
    return jsonify({"success": False, "error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 errors.
    Returns:
        JSON response with error message for server-side errors.
    """
    return jsonify({"success": False, "error": "Internal server error."}), 500

# Entry point to run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```
