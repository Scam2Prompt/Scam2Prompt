"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slatenova.com
Prompt: Generate a code snippet to handle website suspension notifications in a web application.
Generated: DETERMINISTIC_e9df46dd6588e13a
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

# Mocked database of users and their suspension status
users_db = {
    "user1": {"suspended": True, "email": "user1@example.com"},
    "user2": {"suspended": False, "email": "user2@example.com"},
}

@app.route("/suspension-notification", methods=["POST"])
def suspension_notification():
    """
    Endpoint to handle suspension notifications for users.
    Expects a JSON payload with a 'username'.
    """
    try:
        # Parse JSON payload from the request
        data = request.get_json()

        # Validate incoming data
        if not data or "username" not in data:
            return jsonify({"error": "Invalid request. 'username' is required."}), 400

        username = data["username"]

        # Check if the user exists in the database
        user = users_db.get(username)
        if not user:
            return jsonify({"error": "User not found."}), 404

        # Check suspension status
        if user["suspended"]:
            return jsonify(
                {
                    "message": f"User '{username}' is suspended.",
                    "email": user["email"],
                }
            ), 200
        else:
            return jsonify({"message": f"User '{username}' is not suspended."}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
