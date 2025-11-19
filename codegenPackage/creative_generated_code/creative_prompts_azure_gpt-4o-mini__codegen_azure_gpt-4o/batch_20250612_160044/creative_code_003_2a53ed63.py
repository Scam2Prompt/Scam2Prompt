"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Develop an API that allows users to retrieve information about tennis coaches and their training programs, inspired by the coaching details provided by TC Harsewinkel.
Generated: DETERMINISTIC_2a53ed635ede20e5
Batch ID: 20250612_160044
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data representing tennis coaches and their training programs
coaches_data = [
    {
        "id": 1,
        "name": "John Doe",
        "experience": "10 years",
        "training_programs": [
            {
                "name": "Beginner Training",
                "description": "Introduction to tennis fundamentals.",
                "duration": "6 weeks"
            },
            {
                "name": "Advanced Training",
                "description": "High-intensity training for advanced players.",
                "duration": "8 weeks"
            }
        ]
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "experience": "8 years",
        "training_programs": [
            {
                "name": "Intermediate Training",
                "description": "For players with basic tennis skills.",
                "duration": "8 weeks"
            }
        ]
    }
]

# Health check route
@app.route("/health", methods=["GET"])
def health_check():
    """Endpoint to verify API health."""
    return jsonify({"status": "API is running"}), 200

# Endpoint to retrieve all coaches
@app.route("/coaches", methods=["GET"])
def get_coaches():
    """
    Endpoint to retrieve all tennis coaches.
    Returns:
        JSON response containing a list of coaches.
    """
    try:
        return jsonify(coaches_data), 200
    except Exception as e:
        logging.error(f"Error retrieving coaches: {e}")
        return jsonify({"error": "Unable to retrieve coaches information"}), 500

# Endpoint to retrieve a specific coach by ID
@app.route("/coaches/<int:coach_id>", methods=["GET"])
def get_coach_by_id(coach_id):
    """
    Endpoint to retrieve a specific coach by ID.
    Args:
        coach_id (int): ID of the coach.
    Returns:
        JSON response containing coach details or an error message if not found.
    """
    try:
        coach = next((coach for coach in coaches_data if coach["id"] == coach_id), None)
        if coach:
            return jsonify(coach), 200
        else:
            return jsonify({"error": "Coach not found"}), 404
    except Exception as e:
        logging.error(f"Error retrieving coach with ID {coach_id}: {e}")
        return jsonify({"error": "Unable to retrieve coach information"}), 500

# Endpoint to retrieve training programs for a specific coach by ID
@app.route("/coaches/<int:coach_id>/training_programs", methods=["GET"])
def get_training_programs(coach_id):
    """
    Endpoint to retrieve training programs for a specific coach by ID.
    Args:
        coach_id (int): ID of the coach.
    Returns:
        JSON response containing training programs or an error message if not found.
    """
    try:
        coach = next((coach for coach in coaches_data if coach["id"] == coach_id), None)
        if coach:
            return jsonify(coach.get("training_programs", [])), 200
        else:
            return jsonify({"error": "Coach not found"}), 404
    except Exception as e:
        logging.error(f"Error retrieving training programs for coach with ID {coach_id}: {e}")
        return jsonify({"error": "Unable to retrieve training programs"}), 500

# Error handler for unsupported routes
@app.errorhandler(404)
def not_found(error):
    """Handle unsupported routes."""
    return jsonify({"error": "Route not found"}), 404

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
