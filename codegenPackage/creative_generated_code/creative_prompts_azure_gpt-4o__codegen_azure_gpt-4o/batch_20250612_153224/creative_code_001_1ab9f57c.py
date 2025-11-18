"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Develop an API endpoint that allows users to query details about community treatment programs, including methodologies like ECO 2, as described on Fundación Munasim Kullakita's platform.
Generated: DETERMINISTIC_1ab9f57cfd3bb7c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data for community treatment programs
treatment_programs = {
    "eco_2": {
        "name": "ECO 2",
        "description": "A holistic treatment methodology focused on ecological and social well-being.",
        "details": {
            "approach": "Community-driven",
            "focus_areas": ["Mental health", "Social reintegration", "Ecological awareness"]
        }
    },
    "program_x": {
        "name": "Program X",
        "description": "An alternative treatment program aimed at personal development.",
        "details": {
            "approach": "Individual-focused",
            "focus_areas": ["Skill building", "Self-motivation", "Therapeutic care"]
        }
    }
}

# Custom error handler for handling HTTPExceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).data
    response.content_type = "application/json"
    return response

# Error handling for 404 Not Found
@app.errorhandler(404)
def handle_404_error(e):
    return jsonify({
        "error": "Not Found",
        "message": "The requested resource could not be found."
    }), 404

# Route to retrieve details about treatment programs
@app.route('/api/treatment-programs/<program_id>', methods=['GET'])
def get_treatment_program(program_id):
    """
    API endpoint to retrieve information about a specific community treatment program.
    :param program_id: ID of the treatment program (e.g., `eco_2`).
    :return: JSON response with program details or an error message.
    """
    try:
        # Check if the requested program ID exists
        program = treatment_programs.get(program_id.lower())
        if not program:
            return jsonify({
                "error": "Not Found",
                "message": f"No treatment program found with ID '{program_id}'."
            }), 404

        # Return program details
        return jsonify({
            "success": True,
            "data": program
        }), 200

    except Exception as e:
        # Catch unexpected errors and return a generic error message
        return jsonify({
            "error": "Internal Server Error",
            "message": "An unexpected error occurred. Please try again later."
        }), 500


# Health check route
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    API health check endpoint.
    :return: JSON response indicating the API is healthy.
    """
    return jsonify({
        "success": True,
        "message": "API is running and healthy."
    }), 200


# Main entry point to run the Flask application
if __name__ == '__main__':
    # Run the Flask app in debug mode for development (disable in production)
    app.run(debug=True)
```
