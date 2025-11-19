"""
Generated Code Metadata:
========================
Original URL: https://bigwaveinfotech.net
Prompt: "Write a Python code snippet for a simple mobile app using a custom application development approach, as described on the BigWaveInfotech website."
Generated: DETERMINISTIC_acec2f913905a049
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define a simple in-memory database (dictionary) to store user data
user_data = {}

# Route: Home page
@app.route('/')
def home():
    """
    Home route to display a welcome message.
    """
    return jsonify({"message": "Welcome to the Simple Mobile App API!"})

# Route: Add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Route to add a new user to the in-memory database.
    Expects JSON payload with 'username' and 'email'.
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        # Validate input
        if not username or not email:
            return jsonify({"error": "Both 'username' and 'email' are required."}), 400

        # Check if the user already exists
        if username in user_data:
            return jsonify({"error": "User already exists."}), 409

        # Add user to the database
        user_data[username] = {"email": email}
        return jsonify({"message": f"User '{username}' added successfully!"}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Get user details
@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    """
    Route to retrieve user details by username.
    """
    try:
        # Check if the user exists
        if username not in user_data:
            return jsonify({"error": "User not found."}), 404

        # Return user details
        return jsonify({"username": username, "email": user_data[username]['email']}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Delete a user
@app.route('/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
    """
    Route to delete a user by username.
    """
    try:
        # Check if the user exists
        if username not in user_data:
            return jsonify({"error": "User not found."}), 404

        # Delete the user
        del user_data[username]
        return jsonify({"message": f"User '{username}' deleted successfully!"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point to run the application
if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
```
