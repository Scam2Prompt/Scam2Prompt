"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Develop an API that allows users to receive customized workout routines based on their fitness goals, similar to the personalized training approach of Carol Crespo.
Generated: DETERMINISTIC_8e4bf1d7f4062cb5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Setting up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example workout database (mocked for demo purposes)
WORKOUT_DATABASE = {
    "weight_loss": [
        {"name": "Cardio Session", "duration": "30 minutes", "intensity": "High"},
        {"name": "Strength Training", "duration": "20 minutes", "intensity": "Moderate"}
    ],
    "muscle_gain": [
        {"name": "Heavy Lifting", "duration": "45 minutes", "intensity": "High"},
        {"name": "Protein Recovery Stretch", "duration": "10 minutes", "intensity": "Low"}
    ],
    "general_fitness": [
        {"name": "Yoga", "duration": "30 minutes", "intensity": "Low"},
        {"name": "Bodyweight Exercises", "duration": "20 minutes", "intensity": "Moderate"}
    ]
}

def get_workout_routine(goal):
    """
    Retrieve workout routines based on the user's fitness goal.
    :param goal: Fitness goal (e.g., 'weight_loss', 'muscle_gain', 'general_fitness')
    :return: List of workout routines or None if the goal is not found.
    """
    return WORKOUT_DATABASE.get(goal)

@app.route('/workout', methods=['POST'])
def generate_workout():
    """
    API endpoint to generate a workout routine based on user fitness goals.
    Expects a JSON payload with the key `fitness_goal`.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data or 'fitness_goal' not in data:
            return jsonify({"error": "Invalid request. Please provide a 'fitness_goal'."}), 400

        fitness_goal = data['fitness_goal'].lower()
        workout_routine = get_workout_routine(fitness_goal)

        if workout_routine:
            return jsonify({
                "fitness_goal": fitness_goal,
                "workout_routine": workout_routine
            }), 200
        else:
            return jsonify({"error": f"No workout routine found for goal '{fitness_goal}'."}), 404

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

@app.route('/')
def health_check():
    """
    Health check endpoint to ensure the server is running.
    """
    return jsonify({"status": "ok", "message": "Workout API is running!"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
