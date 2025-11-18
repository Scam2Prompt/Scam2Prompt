"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Develop a REST API that tracks a user's progress in STEPN, including their energy levels and costs for leveling up, as outlined in the blog.
Generated: DETERMINISTIC_b2b0fc6340a5b98b
Batch ID: 20250612_154756
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

# In-memory database for storing user progress
user_data = {}

# Error handler for internal server errors
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({'error': e.description}), e.code
    return jsonify({'error': 'Internal server error'}), 500

# Route: Get user progress
@app.route('/api/user/<username>', methods=['GET'])
def get_user_progress(username):
    """
    Retrieve a user's progress in STEPN by their username.
    :param username: The username of the user.
    :return: JSON containing the user's energy levels and leveling costs, or a not found error.
    """
    user = user_data.get(username)
    if not user:
        return jsonify({'error': f'User {username} not found.'}), 404
    
    return jsonify({'username': username, 'progress': user}), 200

# Route: Update user progress
@app.route('/api/user/<username>', methods=['POST'])
def update_user_progress(username):
    """
    Update a user's progress in STEPN.
    Expects JSON data with 'energy_level' and 'leveling_cost' fields.
    :param username: The username of the user.
    :return: JSON indicating success or validation errors.
    """
    data = request.json

    # Input validation
    if 'energy_level' not in data or 'leveling_cost' not in data:
        return jsonify({'error': 'Missing required fields: energy_level, leveling_cost'}), 400

    if not isinstance(data['energy_level'], (int, float)) or not isinstance(data['leveling_cost'], (int, float)):
        return jsonify({'error': 'Invalid data types: energy_level and leveling_cost must be numbers'}), 400

    # Update user data
    user_data[username] = {
        'energy_level': data['energy_level'],
        'leveling_cost': data['leveling_cost']
    }

    return jsonify({'message': f'Progress for user {username} updated successfully.'}), 200

# Route: Delete user progress
@app.route('/api/user/<username>', methods=['DELETE'])
def delete_user_progress(username):
    """
    Delete a user's progress in STEPN by their username.
    :param username: The username of the user.
    :return: JSON indicating success or a not found error.
    """
    if username not in user_data:
        return jsonify({'error': f'User {username} not found.'}), 404

    del user_data[username]
    return jsonify({'message': f'Progress for user {username} deleted successfully.'}), 200

# Route: List all users
@app.route('/api/users', methods=['GET'])
def list_users():
    """
    List all users and their progress in STEPN.
    :return: JSON containing all users and their progress.
    """
    return jsonify({'users': user_data}), 200

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
```
