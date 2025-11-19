"""
Generated Code Metadata:
========================
Original URL: https://amarparasanar.com.mx
Prompt: Develop an API endpoint that retrieves information about available online therapy modalities, including individual and couple therapy options.
Generated: DETERMINISTIC_143b37d1afc53f15
Batch ID: 20250612_155829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing available therapy modalities
THERAPY_MODALITIES = [
    {
        "id": 1,
        "type": "Individual Therapy",
        "description": "One-on-one sessions with a licensed therapist.",
        "availability": "Online and In-Person"
    },
    {
        "id": 2,
        "type": "Couple Therapy",
        "description": "Therapy sessions for couples to improve communication and resolve conflicts.",
        "availability": "Online Only"
    },
    {
        "id": 3,
        "type": "Group Therapy",
        "description": "Therapy sessions conducted in a group setting.",
        "availability": "In-Person Only"
    }
]

@app.route('/api/therapy-modalities', methods=['GET'])
def get_therapy_modalities():
    """
    API endpoint to retrieve information about available therapy modalities.
    Returns:
        JSON response containing a list of therapy modalities.
    """
    try:
        # Return the list of therapy modalities as a JSON response
        return jsonify({
            "success": True,
            "data": THERAPY_MODALITIES
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "success": False,
            "error": "An error occurred while retrieving therapy modalities.",
            "details": str(e)
        }), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({
        "success": False,
        "error": "Endpoint not found."
    }), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({
        "success": False,
        "error": "Internal server error."
    }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
