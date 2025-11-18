"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Generate code using Flask to implement a "Nominate" feature where users can submit profiles for inclusion in categories like "Teacher" or "Medical" on a community-driven website.
Generated: DETERMINISTIC_1bbf99dc896d0d1d
Batch ID: 20250612_153907
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

# In-memory storage for nominations (replace with actual database in production)
nominations = []


# Custom error handler for better API error responses
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description
    }).get_data()
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "description": "An unexpected error occurred."
    }), 500


@app.route('/api/nominate', methods=['POST'])
def nominate_profile():
    """
    Endpoint for submitting nominations.
    Accepts JSON payload with 'name', 'category', and 'description'.
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Validate required fields
        if not data or 'name' not in data or 'category' not in data or 'description' not in data:
            return jsonify({
                "error": "Bad Request",
                "description": "Missing required fields: 'name', 'category', 'description'."
            }), 400

        # Validate category (for example, only 'Teacher' or 'Medical' allowed)
        valid_categories = ['Teacher', 'Medical']
        if data['category'] not in valid_categories:
            return jsonify({
                "error": "Bad Request",
                "description": f"Invalid category. Valid categories are: {', '.join(valid_categories)}."
            }), 400

        # Create nomination record
        nomination = {
            "id": len(nominations) + 1,  # Simple ID generation (replace with UUID in production)
            "name": data['name'],
            "category": data['category'],
            "description": data['description']
        }
        nominations.append(nomination)

        # Success response
        return jsonify({
            "message": "Nomination submitted successfully!",
            "nomination": nomination
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return handle_generic_exception(e)


@app.route('/api/nominations', methods=['GET'])
def get_nominations():
    """
    Endpoint for retrieving all nominations.
    Returns a list of nominations.
    """
    return jsonify({
        "nominations": nominations
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
```
