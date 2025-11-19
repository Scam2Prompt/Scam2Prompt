"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Create an API endpoint for fetching user earnings and task statistics, similar to the data structure used on https://rb.itsmeplabon.xyz.
Generated: DETERMINISTIC_d1e0b88e577be6e7
Batch ID: 20250612_160246
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

# Sample data to simulate database records
users_data = {
    1: {
        "name": "John Doe",
        "earnings": 1500.50,
        "tasks": {
            "completed": 120,
            "pending": 5,
            "in_progress": 3,
        },
    },
    2: {
        "name": "Jane Smith",
        "earnings": 2200.75,
        "tasks": {
            "completed": 200,
            "pending": 10,
            "in_progress": 6,
        },
    },
    # Add more user data as needed
}

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors gracefully."""
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description
        }
    }).get_data()
    response.content_type = "application/json"
    return response

@app.route('/api/user/<int:user_id>/stats', methods=['GET'])
def get_user_stats(user_id):
    """
    API Endpoint to fetch user earnings and task statistics.
    :param user_id: Integer user ID passed in the URL.
    :return: JSON response containing earnings and task statistics for the user.
    """
    # Check if user exists in the database
    user_data = users_data.get(user_id)
    if user_data is None:
        return jsonify({
            "error": "User not found",
            "message": f"No data available for user ID {user_id}"
        }), 404

    # Return user earnings and task statistics
    return jsonify({
        "user_id": user_id,
        "name": user_data["name"],
        "earnings": user_data["earnings"],
        "tasks": user_data["tasks"]
    })

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
