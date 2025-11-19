"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Create an API that provides resources and exercises for women looking to improve their emotional stability, as outlined in the "5 atitudes que destroem o seu emocional."
Generated: DETERMINISTIC_2f1bffdc22fd6a3b
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/meditation": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/emotional-stability": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for resources and exercises
resources = [
    {
        "id": 1,
        "title": "Understanding Emotional Stability",
        "description": "Learn the basics of emotional stability and how to cultivate it.",
        "link": "https://example.com/emotional-stability"
    },
    {
        "id": 2,
        "title": "Meditation for Emotional Balance",
        "description": "A guided meditation to help you stay emotionally grounded.",
        "link": "https://example.com/meditation"
    }
]

exercises = [
    {
        "id": 1,
        "title": "Daily Gratitude Journal",
        "description": "Write down three things you're grateful for every day.",
        "instructions": "Take 5 minutes each morning to reflect and write in your journal."
    },
    {
        "id": 2,
        "title": "Breathing Exercise",
        "description": "Practice deep breathing to reduce stress and improve focus.",
        "instructions": "Inhale deeply for 4 seconds, hold for 4 seconds, exhale for 4 seconds. Repeat 5 times."
    }
]

# Error handling for invalid resource or exercise IDs
def get_item_by_id(item_list, item_id):
    try:
        item_id = int(item_id)
        for item in item_list:
            if item["id"] == item_id:
                return item
        return None
    except ValueError:
        return None

# API endpoint to get all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    return jsonify({"resources": resources}), 200

# API endpoint to get a specific resource by ID
@app.route('/api/resources/<resource_id>', methods=['GET'])
def get_resource_by_id(resource_id):
    resource = get_item_by_id(resources, resource_id)
    if resource:
        return jsonify(resource), 200
    return jsonify({"error": "Resource not found"}), 404

# API endpoint to get all exercises
@app.route('/api/exercises', methods=['GET'])
def get_exercises():
    return jsonify({"exercises": exercises}), 200

# API endpoint to get a specific exercise by ID
@app.route('/api/exercises/<exercise_id>', methods=['GET'])
def get_exercise_by_id(exercise_id):
    exercise = get_item_by_id(exercises, exercise_id)
    if exercise:
        return jsonify(exercise), 200
    return jsonify({"error": "Exercise not found"}), 404

# API endpoint to add a new resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    try:
        new_resource = request.json
        if not new_resource.get("title") or not new_resource.get("description") or not new_resource.get("link"):
            return jsonify({"error": "Invalid resource data"}), 400
        new_resource["id"] = len(resources) + 1
        resources.append(new_resource)
        return jsonify(new_resource), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to add a new exercise
@app.route('/api/exercises', methods=['POST'])
def add_exercise():
    try:
        new_exercise = request.json
        if not new_exercise.get("title") or not new_exercise.get("description") or not new_exercise.get("instructions"):
            return jsonify({"error": "Invalid exercise data"}), 400
        new_exercise["id"] = len(exercises) + 1
        exercises.append(new_exercise)
        return jsonify(new_exercise), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
