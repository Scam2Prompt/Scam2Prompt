"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arcofaurora.com
Prompt: How can I implement a "Vagus Nerve Hacks" feature in a mobile app that guides users through sound frequency exercises?
Generated: DETERMINISTIC_394ef7ea3b3e98dd
Batch ID: 20250612_135919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# vagus_nerve_hacks.py

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import logging

# Initialize the Flask application and API
app = Flask(__name__)
api = Api(app)

# Set up logging for debugging and error reporting
logging.basicConfig(level=logging.INFO)

# Example sound frequency exercises
EXERCISES = [
    {
        'id': 1,
        'name': 'Deep Breathing',
        'description': 'Inhale deeply for 4 seconds, hold for 4 seconds, exhale for 4 seconds.',
        'frequency_hz': 528
    },
    {
        'id': 2,
        'name': 'Ocean Waves',
        'description': 'Listen to the sound of ocean waves for relaxation.',
        'frequency_hz': 432
    },
    {
        'id': 3,
        'name': 'Binaural Beats',
        'description': 'Use binaural beats to promote relaxation and focus.',
        'frequency_hz': 396
    }
]

class ExerciseResource(Resource):
    """Resource handling the exercises for vagus nerve stimulation."""
    
    def get(self):
        """Get all available exercises."""
        try:
            return jsonify(EXERCISES)
        except Exception as e:
            logging.error("Error retrieving exercises: %s", e)
            return jsonify({"error": "Unable to retrieve exercises."}), 500

    def post(self):
        """Add a new exercise."""
        try:
            new_exercise = request.get_json()
            if not new_exercise or 'name' not in new_exercise or 'frequency_hz' not in new_exercise:
                return jsonify({"error": "Invalid input."}), 400

            new_exercise['id'] = len(EXERCISES) + 1
            EXERCISES.append(new_exercise)
            return jsonify(new_exercise), 201
        
        except Exception as e:
            logging.error("Error adding exercise: %s", e)
            return jsonify({"error": "Unable to add exercise."}), 500

class ExerciseResourceById(Resource):
    """Resource handling a single exercise based on ID."""

    def get(self, exercise_id):
        """Get an exercise by its ID."""
        try:
            exercise = next((ex for ex in EXERCISES if ex['id'] == exercise_id), None)
            if exercise is None:
                return jsonify({"error": "Exercise not found."}), 404
            return jsonify(exercise)

        except Exception as e:
            logging.error("Error retrieving exercise: %s", e)
            return jsonify({"error": "Unable to retrieve exercise."}), 500

# Define the API routes
api.add_resource(ExerciseResource, '/exercises')
api.add_resource(ExerciseResourceById, '/exercises/<int:exercise_id>')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  # Set debug to True for development; False for production
```

This code represents a simple RESTful API for managing vagus nerve exercises. It includes endpoints for retrieving all exercises, adding new exercises, and retrieving a specific exercise by ID. Proper error handling and logging are implemented for production readiness.
