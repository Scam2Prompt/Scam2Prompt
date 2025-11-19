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

# Sample data for users and workouts (In a real app, this would be in a database)
users_data = {
    "1": {"name": "Alice", "goals": ["weight loss", "muscle gain"], "experience": "intermediate"},
    "2": {"name": "Bob", "goals": ["endurance", "flexibility"], "experience": "beginner"},
}

workouts_data = {
    "weight loss": ["HIIT", "Circuit Training", "Jogging"],
    "muscle gain": ["Strength Training", "Bodyweight Exercises"],
    "endurance": ["Long Distance Running", "Cycling"],
    "flexibility": ["Yoga", "Pilates"]
}

def get_user(user_id):
    """Fetch user data by user ID."""
    user = users_data.get(user_id)
    if not user:
        raise ValueError("User not found")
    return user

def get_workouts_by_goal(goal):
    """Fetch workout types based on user's goal."""
    workouts = workouts_data.get(goal)
    if workouts is None:
        raise ValueError("No workouts available for this goal")
    return workouts

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user_info(user_id):
    """API endpoint to get user information."""
    try:
        user_info = get_user(user_id)
        return jsonify(user_info), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/users/<user_id>/workouts', methods=['GET'])
def get_user_workouts(user_id):
    """API endpoint to get personalized workouts based on user goals."""
    try:
        user_info = get_user(user_id)
        workouts = []
        
        # Collect workouts for each goal
        for goal in user_info['goals']:
            workouts.extend(get_workouts_by_goal(goal))
        
        return jsonify({"workouts": workouts}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/goals', methods=['GET'])
def get_goals():
    """API endpoint to get a list of fitness goals."""
    return jsonify({"goals": list(workouts_data.keys())}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
