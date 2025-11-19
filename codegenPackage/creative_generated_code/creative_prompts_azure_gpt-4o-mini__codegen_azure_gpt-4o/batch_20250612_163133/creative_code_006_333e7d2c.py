"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Design a RESTful API in Python Flask that provides information about the various online degrees offered by California National University, including program details and admission requirements.
Generated: DETERMINISTIC_333e7d2ced7ae8d3
Batch ID: 20250612_163133
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

# Sample data for online degrees offered by California National University
degrees = [
    {
        "id": 1,
        "name": "Bachelor of Science in Computer Science",
        "description": "An undergraduate program focused on computer programming, algorithms, and systems.",
        "admission_requirements": [
            "High school diploma or equivalent",
            "Minimum GPA: 2.5",
            "SAT/ACT scores (optional)"
        ]
    },
    {
        "id": 2,
        "name": "Master of Business Administration (MBA)",
        "description": "A graduate program designed to develop leadership and business management skills.",
        "admission_requirements": [
            "Bachelor's degree from an accredited institution",
            "Minimum GPA: 3.0",
            "GMAT/GRE scores (optional)"
        ]
    },
    {
        "id": 3,
        "name": "Master of Science in Data Science",
        "description": "A graduate program focusing on data analysis, machine learning, and statistical modeling.",
        "admission_requirements": [
            "Bachelor's degree in STEM or related field",
            "Minimum GPA: 3.0",
            "Prior coursework in programming and statistics"
        ]
    }
]

# Route to get information about all degrees
@app.route('/api/degrees', methods=['GET'])
def get_degrees():
    """
    Endpoint to fetch all online degrees offered by the university.
    Returns JSON containing information about degrees.
    """
    return jsonify(degrees), 200

# Route to get information about a specific degree by ID
@app.route('/api/degrees/<int:degree_id>', methods=['GET'])
def get_degree_by_id(degree_id):
    """
    Endpoint to fetch a specific degree by its ID.
    Returns JSON containing information if degree is found, else 404 error.
    """
    degree = next((degree for degree in degrees if degree["id"] == degree_id), None)
    if degree:
        return jsonify(degree), 200
    return jsonify({"error": "Degree not found"}), 404

# Route to add a new degree program
@app.route('/api/degrees', methods=['POST'])
def add_degree():
    """
    Endpoint to add a new degree program.
    Expects JSON payload with 'name', 'description', and 'admission_requirements'.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'admission_requirements' not in data:
            return jsonify({"error": "Invalid request payload"}), 400
        
        new_degree = {
            "id": len(degrees) + 1,
            "name": data['name'],
            "description": data['description'],
            "admission_requirements": data['admission_requirements']
        }
        degrees.append(new_degree)
        return jsonify(new_degree), 201
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500

# Route to update an existing degree program
@app.route('/api/degrees/<int:degree_id>', methods=['PUT'])
def update_degree(degree_id):
    """
    Endpoint to update an existing degree program based on its ID.
    Expects JSON payload with updated fields.
    """
    degree = next((degree for degree in degrees if degree["id"] == degree_id), None)
    if not degree:
        return jsonify({"error": "Degree not found"}), 404
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request payload"}), 400
        
        degree.update({key: value for key, value in data.items() if key in degree})
        return jsonify(degree), 200
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500

# Route to delete a degree program by ID
@app.route('/api/degrees/<int:degree_id>', methods=['DELETE'])
def delete_degree(degree_id):
    """
    Endpoint to delete a degree program by ID.
    Returns success message if deletion is successful, else 404 error.
    """
    degree = next((degree for degree in degrees if degree["id"] == degree_id), None)
    if not degree:
        return jsonify({"error": "Degree not found"}), 404
    
    degrees.remove(degree)
    return jsonify({"message": "Degree deleted successfully"}), 200

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handles 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles 500 errors for server issues.
    """
    return jsonify({"error": "Internal server error"}), 500

# Main entry point for the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
