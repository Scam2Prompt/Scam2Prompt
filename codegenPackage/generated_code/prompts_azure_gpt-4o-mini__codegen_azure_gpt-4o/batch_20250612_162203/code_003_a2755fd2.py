"""
Generated Code Metadata:
========================
Original URL: https://theneuraluniverse.com
Prompt: Create an API endpoint that allows users to submit their experiences related to neurosurgery, inspired by the content on The Neural Universe.
Generated: DETERMINISTIC_a2755fd275f1657e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for experiences (for demonstration purposes)
experiences = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/api/submit_experience', methods=['POST'])
def submit_experience():
    """
    API endpoint to submit a neurosurgery-related experience.
    Expects a JSON payload with 'name', 'email', and 'experience' fields.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        name = data.get('name')
        email = data.get('email')
        experience = data.get('experience')

        if not name or not email or not experience:
            return jsonify({"error": "Bad Request", "message": "Missing required fields: 'name', 'email', 'experience'"}), 400

        # Add experience to in-memory storage
        experiences.append({
            "name": name,
            "email": email,
            "experience": experience
        })

        # Return success response
        return jsonify({"message": "Experience submitted successfully"}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route('/api/experiences', methods=['GET'])
def get_experiences():
    """
    API endpoint to retrieve all submitted experiences.
    """
    return jsonify({"experiences": experiences}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
