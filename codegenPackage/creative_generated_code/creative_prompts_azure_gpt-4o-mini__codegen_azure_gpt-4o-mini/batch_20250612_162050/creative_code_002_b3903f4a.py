"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Generate a sample API that provides resources and exercises for DBT skills training, targeting adolescents and adults with emotional regulation issues.
Generated: DETERMINISTIC_b3903f4a197d8ae9
Batch ID: 20250612_162050
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/emotional-regulation": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/dbt-intro": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/mindfulness-exercises": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for DBT resources and exercises
dbt_resources = [
    {
        "id": 1,
        "title": "Understanding DBT",
        "description": "An introductory guide to Dialectical Behavior Therapy.",
        "link": "https://www.example.com/dbt-intro"
    },
    {
        "id": 2,
        "title": "Emotional Regulation Skills",
        "description": "Learn techniques to manage your emotions.",
        "link": "https://www.example.com/emotional-regulation"
    },
    {
        "id": 3,
        "title": "Mindfulness Exercises",
        "description": "Practice mindfulness to improve emotional awareness.",
        "link": "https://www.example.com/mindfulness-exercises"
    }
]

# Error handling for invalid requests
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route('/resources', methods=['GET'])
def get_resources():
    """
    Retrieve a list of DBT resources.
    Returns:
        JSON list of resources.
    """
    return jsonify(dbt_resources), 200

@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """
    Retrieve a specific DBT resource by ID.
    Args:
        resource_id (int): ID of the resource to retrieve.
    Returns:
        JSON resource object or 404 error if not found.
    """
    resource = next((res for res in dbt_resources if res["id"] == resource_id), None)
    if resource is None:
        return not_found(404)
    return jsonify(resource), 200

@app.route('/resources', methods=['POST'])
def add_resource():
    """
    Add a new DBT resource.
    Returns:
        JSON of the created resource with status code 201.
    """
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "Bad request: 'title' is required"}), 400

    new_resource = {
        "id": dbt_resources[-1]["id"] + 1,
        "title": request.json['title'],
        "description": request.json.get('description', ""),
        "link": request.json.get('link', "")
    }
    dbt_resources.append(new_resource)
    return jsonify(new_resource), 201

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
```
