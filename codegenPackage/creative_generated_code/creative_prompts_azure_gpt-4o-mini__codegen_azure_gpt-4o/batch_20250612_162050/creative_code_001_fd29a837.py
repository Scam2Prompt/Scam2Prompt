"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: How can I use the DBT approach to create a mental health app that helps users manage emotional dysregulation? Include specific features based on the DBT methodology.
Generated: DETERMINISTIC_fd29a837577bb223
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# mental_health_app.py

from flask import Flask, request, jsonify
import logging
import datetime

app = Flask(__name__)

# Setup logging for error tracking and debugging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')

# In-memory database simulation for users and DBT techniques
users = {}
dbt_techniques = [
    {"id": 1, "name": "Mindfulness", "description": "Focus on the present moment without judgment."},
    {"id": 2, "name": "Distress Tolerance", "description": "Learn tools to tolerate and survive a crisis."},
    {"id": 3, "name": "Emotion Regulation", "description": "Understand and manage intense emotions."},
    {"id": 4, "name": "Interpersonal Effectiveness", "description": "Develop and maintain healthy relationships."}
]

# ============================
# Helper Functions
# ============================

def validate_user_data(data):
    """Validate user data for required fields."""
    required_fields = ['username', 'email']
    return all(field in data for field in required_fields)

# ============================
# Routes
# ============================

@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    Expected JSON payload: {"username": "string", "email": "string"}
    """
    try:
        user_data = request.json

        if not validate_user_data(user_data):
            return jsonify({"error": "Invalid user data. 'username' and 'email' are required."}), 400

        username = user_data['username']

        if username in users:
            return jsonify({"error": "Username already exists."}), 409

        users[username] = {
            "email": user_data['email'],
            "registered_at": datetime.datetime.utcnow().isoformat(),
            "dbt_progress": {technique['name']: False for technique in dbt_techniques}  # Track progress
        }

        logging.info(f"User '{username}' registered successfully.")
        return jsonify({"message": f"User '{username}' registered successfully."}), 201
    except Exception as e:
        logging.error(f"Error during user registration: {str(e)}")
        return jsonify({"error": "An unexpected error occurred during registration."}), 500


@app.route('/dbt-techniques', methods=['GET'])
def get_dbt_techniques():
    """
    Retrieve the list of DBT techniques available in the app.
    """
    try:
        return jsonify(dbt_techniques), 200
    except Exception as e:
        logging.error(f"Error fetching DBT techniques: {str(e)}")
        return jsonify({"error": "An unexpected error occurred while fetching DBT techniques."}), 500


@app.route('/update-progress/<username>', methods=['POST'])
def update_progress(username):
    """
    Update DBT technique progress for a user.
    Expected JSON payload: {"technique": "string", "completed": true/false}
    """
    try:
        progress_data = request.json

        if username not in users:
            return jsonify({"error": "User not found."}), 404

        technique_name = progress_data.get('technique')
        completed = progress_data.get('completed')

        if not technique_name or not isinstance(completed, bool):
            return jsonify({"error": "Invalid data. 'technique' and 'completed' are required."}), 400

        if technique_name not in users[username]['dbt_progress']:
            return jsonify({"error": "Technique not found for the user."}), 404

        users[username]['dbt_progress'][technique_name] = completed
        logging.info(f"Progress updated for user '{username}' on technique '{technique_name}'.")
        return jsonify({"message": f"Progress updated for '{technique_name}'."}), 200
    except Exception as e:
        logging.error(f"Error updating progress for user '{username}': {str(e)}")
        return jsonify({"error": "An unexpected error occurred while updating progress."}), 500


@app.route('/user/<username>', methods=['GET'])
def get_user_profile(username):
    """
    Retrieve the profile and DBT progress of a user.
    """
    try:
        if username not in users:
            return jsonify({"error": "User not found."}), 404

        return jsonify(users[username]), 200
    except Exception as e:
        logging.error(f"Error fetching profile for user '{username}': {str(e)}")
        return jsonify({"error": "An unexpected error occurred while fetching the user profile."}), 500


# ============================
# Main Execution
# ============================
if __name__ == '__main__':
    app.run(debug=True)  # Use debug=True for development; set False for production
```

### Features Implemented
1. **User Registration**: Allows users to register with username and email.
2. **DBT Techniques**: Retrieves a list of DBT techniques with descriptions.
3. **Progress Tracking**: Enables users to update their progress for specific DBT techniques.
4. **User Profile**: Allows users to view their profile and DBT progress.

### Notes
- The app uses Flask as the web framework.
- In-memory data for simplicity; replace with a database (e.g., PostgreSQL) in production.
- Ensure proper authentication and validation in production environments.
