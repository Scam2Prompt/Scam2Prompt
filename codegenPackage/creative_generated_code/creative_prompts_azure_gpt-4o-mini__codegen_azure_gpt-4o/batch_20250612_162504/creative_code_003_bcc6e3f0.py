"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gematria.com
Prompt: Develop a RESTful API endpoint that allows users to retrieve details about hormone and immune support supplements offered by Gematria.
Generated: DETERMINISTIC_bcc6e3f080f398c0
Batch ID: 20250612_162504
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

# Sample data to simulate a database
SUPPLEMENTS = [
    {
        "id": 1,
        "name": "Hormone Support",
        "description": "Supports hormonal balance for overall wellness.",
        "ingredients": ["Ashwagandha", "Maca Root", "Vitamin B6"],
        "price": 29.99
    },
    {
        "id": 2,
        "name": "Immune Support",
        "description": "Boosts immune system health and performance.",
        "ingredients": ["Vitamin C", "Zinc", "Elderberry"],
        "price": 25.99
    }
]

# Error handler for invalid routes or methods
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions with a JSON response."""
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

@app.route('/api/supplements', methods=['GET'])
def get_supplements():
    """
    API endpoint to retrieve the list of hormone and immune support supplements.
    """
    try:
        # Return the full list of supplements
        return jsonify({"success": True, "data": SUPPLEMENTS}), 200
    except Exception as e:
        # Catch any unexpected errors and return a generic error response
        return jsonify({"success": False, "error": "Internal Server Error", "message": str(e)}), 500

@app.route('/api/supplements/<int:supplement_id>', methods=['GET'])
def get_supplement_by_id(supplement_id):
    """
    API endpoint to retrieve details of a specific supplement by ID.
    """
    try:
        # Find the supplement with the matching ID in the sample data
        supplement = next((s for s in SUPPLEMENTS if s["id"] == supplement_id), None)
        if supplement:
            return jsonify({"success": True, "data": supplement}), 200
        else:
            # Return a 404 error if the supplement ID is not found
            return jsonify({"success": False, "error": "Not Found", "message": "Supplement not found"}), 404
    except Exception as e:
        # Catch any unexpected errors and return a generic error response
        return jsonify({"success": False, "error": "Internal Server Error", "message": str(e)}), 500

# Main entry point for running the Flask application
if __name__ == '__main__':
    # Use debug mode during development; disable it in production
    app.run(debug=True)
```
