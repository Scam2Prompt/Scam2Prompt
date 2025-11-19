"""
Generated Code Metadata:
========================
Original URL: https://virtue.guru
Prompt: Develop an API recommendation for a platform that connects users with mentors for personal development and virtue cultivation.
Generated: DETERMINISTIC_f9dba528e102914b
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
mentors = [
    {"id": str(uuid.uuid4()), "name": "John Doe", "expertise": "Leadership", "availability": "Monday-Friday"},
    {"id": str(uuid.uuid4()), "name": "Jane Smith", "expertise": "Mindfulness", "availability": "Weekends"},
    {"id": str(uuid.uuid4()), "name": "Alice Johnson", "expertise": "Time Management", "availability": "Monday-Wednesday"},
]

users = [
    {"id": str(uuid.uuid4()), "name": "Bob Brown", "interests": ["Leadership", "Mindfulness"]},
    {"id": str(uuid.uuid4()), "name": "Emily Davis", "interests": ["Time Management"]},
]

# Error messages
ERROR_MENTOR_NOT_FOUND = "Mentor not found."
ERROR_USER_NOT_FOUND = "User not found."

@app.route('/mentors', methods=['GET'])
def get_mentors():
    """
    Endpoint to retrieve all mentors.
    """
    return jsonify({"mentors": mentors}), 200

@app.route('/users', methods=['GET'])
def get_users():
    """
    Endpoint to retrieve all users.
    """
    return jsonify({"users": users}), 200

@app.route('/recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    """
    Endpoint to get mentor recommendations for a specific user based on their interests.
    """
    # Find the user by ID
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": ERROR_USER_NOT_FOUND}), 404

    # Recommend mentors based on user's interests
    recommended_mentors = [
        mentor for mentor in mentors if any(interest in mentor['expertise'] for interest in user['interests'])
    ]

    return jsonify({"user": user, "recommendations": recommended_mentors}), 200

@app.route('/mentors/<mentor_id>', methods=['GET'])
def get_mentor_by_id(mentor_id):
    """
    Endpoint to retrieve a specific mentor by ID.
    """
    mentor = next((m for m in mentors if m['id'] == mentor_id), None)
    if not mentor:
        return jsonify({"error": ERROR_MENTOR_NOT_FOUND}), 404

    return jsonify({"mentor": mentor}), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """
    Endpoint to retrieve a specific user by ID.
    """
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": ERROR_USER_NOT_FOUND}), 404

    return jsonify({"user": user}), 200

@app.route('/mentors', methods=['POST'])
def add_mentor():
    """
    Endpoint to add a new mentor.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'expertise' not in data or 'availability' not in data:
        return jsonify({"error": "Invalid input. 'name', 'expertise', and 'availability' are required."}), 400

    new_mentor = {
        "id": str(uuid.uuid4()),
        "name": data['name'],
        "expertise": data['expertise'],
        "availability": data['availability']
    }
    mentors.append(new_mentor)
    return jsonify({"mentor": new_mentor}), 201

@app.route('/users', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'interests' not in data:
        return jsonify({"error": "Invalid input. 'name' and 'interests' are required."}), 400

    new_user = {
        "id": str(uuid.uuid4()),
        "name": data['name'],
        "interests": data['interests']
    }
    users.append(new_user)
    return jsonify({"user": new_user}), 201

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
