"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amarparasanar.com.mx
Prompt: Develop an API endpoint that retrieves information about available online therapy modalities, including individual and couple therapy options.
Generated: DETERMINISTIC_143b37d1afc53f15
Batch ID: 20250612_155829
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

# Sample data representing available therapy modalities
THERAPY_MODALITIES = [
    {
        "id": 1,
        "type": "Individual Therapy",
        "description": "One-on-one therapy sessions tailored to personal needs.",
        "available_online": True
    },
    {
        "id": 2,
        "type": "Couple Therapy",
        "description": "Joint sessions to address relationship challenges.",
        "available_online": True
    },
    {
        "id": 3,
        "type": "Group Therapy",
        "description": "Therapy conducted in a group setting for shared experiences.",
        "available_online": False
    }
]

# API endpoint to retrieve available online therapy modalities
@app.route('/api/therapy-modalities', methods=['GET'])
def get_therapy_modalities():
    """
    Endpoint to fetch information about online therapy modalities.
    Returns:
        JSON: List of therapy modalities available online.
    """
    try:
        # Filter the modalities to only include those available online
        available_online = [
            modality for modality in THERAPY_MODALITIES if modality["available_online"]
        ]
        
        # Return the filtered list as JSON response
        return jsonify({
            "success": True,
            "data": available_online
        }), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "success": False,
            "message": "An error occurred while processing your request.",
            "error": str(e)
        }), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handler for 404 errors.
    Returns:
        JSON: Error message for resource not found.
    """
    return jsonify({
        "success": False,
        "message": "The requested resource was not found."
    }), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handler for 500 errors.
    Returns:
        JSON: Error message for server errors.
    """
    return jsonify({
        "success": False,
        "message": "An internal server error occurred."
    }), 500

# Entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
