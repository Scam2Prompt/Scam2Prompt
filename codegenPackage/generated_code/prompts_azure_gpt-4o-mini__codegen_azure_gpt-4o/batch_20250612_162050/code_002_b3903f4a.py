"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Generate a sample API that provides resources and exercises for DBT skills training, targeting adolescents and adults with emotional regulation issues.
Generated: DETERMINISTIC_b3903f4a197d8ae9
Batch ID: 20250612_162050
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

# Sample data for DBT resources and exercises
resources = [
    {
        "id": 1,
        "title": "Mindfulness Basics",
        "description": "Learn the fundamentals of mindfulness to stay present.",
        "target_audience": "adolescents, adults"
    },
    {
        "id": 2,
        "title": "Emotion Regulation Techniques",
        "description": "Understand and manage your emotions effectively.",
        "target_audience": "adults"
    },
    {
        "id": 3,
        "title": "Interpersonal Effectiveness",
        "description": "Improve communication and relationship skills.",
        "target_audience": "adolescents, adults"
    }
]

exercises = [
    {
        "id": 1,
        "title": "Mindful Breathing",
        "description": "Practice deep breathing to stay grounded.",
        "difficulty": "easy",
        "target_audience": "adolescents, adults"
    },
    {
        "id": 2,
        "title": "Opposite Action",
        "description": "Act opposite to your emotional urges to regulate emotions.",
        "difficulty": "medium",
        "target_audience": "adults"
    },
    {
        "id": 3,
        "title": "DEAR MAN Technique",
        "description": "Use DEAR MAN to assertively communicate your needs.",
        "difficulty": "hard",
        "target_audience": "adolescents, adults"
    }
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

# Endpoint to get all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    return jsonify(resources=resources), 200

# Endpoint to get a specific resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource_by_id(resource_id):
    resource = next((r for r in resources if r["id"] == resource_id), None)
    if resource:
        return jsonify(resource=resource), 200
    return jsonify(error="Resource not found"), 404

# Endpoint to get all exercises
@app.route('/api/exercises', methods=['GET'])
def get_exercises():
    return jsonify(exercises=exercises), 200

# Endpoint to get a specific exercise by ID
@app.route('/api/exercises/<int:exercise_id>', methods=['GET'])
def get_exercise_by_id(exercise_id):
    exercise = next((e for e in exercises if e["id"] == exercise_id), None)
    if exercise:
        return jsonify(exercise=exercise), 200
    return jsonify(error="Exercise not found"), 404

# Endpoint to add a new resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    try:
        new_resource = request.get_json()
        if not new_resource or not all(key in new_resource for key in ("title", "description", "target_audience")):
            return jsonify(error="Invalid resource data"), 400
        new_resource["id"] = max(r["id"] for r in resources) + 1
        resources.append(new_resource)
        return jsonify(resource=new_resource), 201
    except Exception as e:
        return jsonify(error="An error occurred while adding the resource"), 500

# Endpoint to add a new exercise
@app.route('/api/exercises', methods=['POST'])
def add_exercise():
    try:
        new_exercise = request.get_json()
        if not new_exercise or not all(key in new_exercise for key in ("title", "description", "difficulty", "target_audience")):
            return jsonify(error="Invalid exercise data"), 400
        new_exercise["id"] = max(e["id"] for e in exercises) + 1
        exercises.append(new_exercise)
        return jsonify(exercise=new_exercise), 201
    except Exception as e:
        return jsonify(error="An error occurred while adding the exercise"), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
