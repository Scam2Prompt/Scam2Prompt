"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://questsmisten.pw
Prompt: Create an API endpoint for users to request their data in accordance with privacy regulations.
Generated: DETERMINISTIC_9abf11e5f3c6a1ff
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, make_response
from werkzeug.exceptions import NotFound, BadRequest
import json

app = Flask(__name__)

# Simulated user database
USER_DATA = {
    "user1": {"name": "Alice", "email": "alice@example.com"},
    "user2": {"name": "Bob", "email": "bob@example.com"}
}

@app.route('/api/userdata', methods=['GET'])
def get_user_data():
    """
    API endpoint to retrieve user data based on the provided user ID.
    This complies with privacy regulations for data access.
    
    Query Parameters:
    - user_id: The ID of the user requesting their data.
    
    Returns:
    - JSON object containing user data or an error message.
    """
    try:
        # Extract user_id from query parameters
        user_id = request.args.get('user_id')

        # Validate user_id presence
        if not user_id:
            raise BadRequest("Missing 'user_id' query parameter.")

        # Retrieve user data from the simulated database
        user_data = USER_DATA.get(user_id)

        # If user data not found, raise a NotFound error
        if user_data is None:
            raise NotFound(f"No data found for user ID: {user_id}")

        # Return user data as JSON response
        return jsonify(user_data), 200

    except BadRequest as e:
        # Handle bad request errors
        return make_response(jsonify({"error": str(e)}), 400)
    
    except NotFound as e:
        # Handle not found errors
        return make_response(jsonify({"error": str(e)}), 404)

    except Exception as e:
        # Handle unexpected errors
        return make_response(jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500)

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
