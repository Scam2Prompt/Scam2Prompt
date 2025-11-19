"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chanorodriguez.com
Prompt: Suggest a list of API endpoints for a fitness app that could provide users with personalized training advice based on Chano Rodriguez's approach.
Generated: DETERMINISTIC_f6a676c98270ddfc
Batch ID: 20250612_162051
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

# Mock data for demonstration purposes
user_profiles = {
    1: {"name": "Alice", "age": 30, "fitness_level": "intermediate"},
    2: {"name": "Bob", "age": 25, "fitness_level": "beginner"}
}

# Sample training advice for different fitness levels
training_advice = {
    "beginner": [
        {"exercise": "Push-Ups", "reps": 10},
        {"exercise": "Squats", "reps": 15}
    ],
    "intermediate": [
        {"exercise": "Pull-Ups", "reps": 8},
        {"exercise": "Deadlift", "reps": 10}
    ],
    "advanced": [
        {"exercise": "Weighted Pull-Ups", "reps": 6},
        {"exercise": "Clean and Jerk", "reps": 5}
    ]
}

# Error-handling utility function
def get_user_profile(user_id):
    """
    Fetch a user profile by ID.
    If user ID does not exist, return None.
    """
    return user_profiles.get(user_id)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Endpoint: GET /api/users/<user_id>
    Description: Fetch user profile by ID.
    """
    user = get_user_profile(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"user": user}), 200

@app.route('/api/training-advice/<int:user_id>', methods=['GET'])
def get_training_advice(user_id):
    """
    Endpoint: GET /api/training-advice/<user_id>
    Description: Provide personalized training advice based on the user's fitness level.
    """
    user = get_user_profile(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    fitness_level = user.get('fitness_level')
    advice = training_advice.get(fitness_level, [])

    if not advice:
        return jsonify({"error": "No training advice available for this fitness level"}), 404

    return jsonify({"user": user, "training_advice": advice}), 200

@app.route('/api/training-plan', methods=['POST'])
def create_training_plan():
    """
    Endpoint: POST /api/training-plan
    Description: Generate a training plan based on user input.
    Expected JSON Input: {"age": <int>, "fitness_level": <str>}
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON input"}), 400

    age = data.get("age")
    fitness_level = data.get("fitness_level")

    if not age or not fitness_level:
        return jsonify({"error": "Missing required fields: age, fitness_level"}), 400

    advice = training_advice.get(fitness_level, [])
    if not advice:
        return jsonify({"error": "Invalid fitness level"}), 404

    return jsonify({"age": age, "fitness_level": fitness_level, "training_plan": advice}), 201

@app.route('/api/health-check', methods=['GET'])
def health_check():
    """
    Endpoint: GET /api/health-check
    Description: Health check endpoint for the API.
    """
    return jsonify({"status": "API is running"}), 200

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
