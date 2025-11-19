"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Develop an API that allows users to retrieve information about tennis coaches and their training programs, inspired by the coaching details provided by TC Harsewinkel.
Generated: DETERMINISTIC_2a53ed635ede20e5
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing tennis coaches and their training programs
coaches_data = [
    {
        "id": 1,
        "name": "John Doe",
        "experience": "10 years",
        "specialization": "Beginner and Intermediate players",
        "training_programs": [
            {
                "program_id": 101,
                "name": "Beginner Basics",
                "duration": "6 weeks",
                "description": "Learn the fundamentals of tennis, including grip, stance, and basic strokes."
            },
            {
                "program_id": 102,
                "name": "Intermediate Skills",
                "duration": "8 weeks",
                "description": "Improve your game with advanced techniques and strategies."
            }
        ]
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "experience": "15 years",
        "specialization": "Advanced players",
        "training_programs": [
            {
                "program_id": 201,
                "name": "Advanced Tactics",
                "duration": "10 weeks",
                "description": "Master advanced tactics and mental strategies for competitive play."
            },
            {
                "program_id": 202,
                "name": "Fitness and Agility",
                "duration": "4 weeks",
                "description": "Enhance your physical fitness and agility for peak performance."
            }
        ]
    }
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Endpoint to retrieve all coaches
@app.route('/api/coaches', methods=['GET'])
def get_coaches():
    """
    Retrieve a list of all tennis coaches.
    """
    return jsonify(coaches_data), 200

# Endpoint to retrieve a specific coach by ID
@app.route('/api/coaches/<int:coach_id>', methods=['GET'])
def get_coach_by_id(coach_id):
    """
    Retrieve details of a specific coach by their ID.
    """
    coach = next((coach for coach in coaches_data if coach["id"] == coach_id), None)
    if coach:
        return jsonify(coach), 200
    else:
        return jsonify({"error": "Coach not found"}), 404

# Endpoint to retrieve training programs for a specific coach
@app.route('/api/coaches/<int:coach_id>/programs', methods=['GET'])
def get_training_programs(coach_id):
    """
    Retrieve training programs for a specific coach by their ID.
    """
    coach = next((coach for coach in coaches_data if coach["id"] == coach_id), None)
    if coach:
        return jsonify(coach["training_programs"]), 200
    else:
        return jsonify({"error": "Coach not found"}), 404

# Endpoint to retrieve a specific training program by program ID
@app.route('/api/coaches/<int:coach_id>/programs/<int:program_id>', methods=['GET'])
def get_training_program_by_id(coach_id, program_id):
    """
    Retrieve details of a specific training program by program ID for a given coach.
    """
    coach = next((coach for coach in coaches_data if coach["id"] == coach_id), None)
    if coach:
        program = next((program for program in coach["training_programs"] if program["program_id"] == program_id), None)
        if program:
            return jsonify(program), 200
        else:
            return jsonify({"error": "Training program not found"}), 404
    else:
        return jsonify({"error": "Coach not found"}), 404

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
