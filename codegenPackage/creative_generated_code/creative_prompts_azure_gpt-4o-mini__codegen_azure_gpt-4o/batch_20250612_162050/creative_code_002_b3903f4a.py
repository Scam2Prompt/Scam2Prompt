"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Generate a sample API that provides resources and exercises for DBT skills training, targeting adolescents and adults with emotional regulation issues.
Generated: DETERMINISTIC_b3903f4a197d8ae9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up logging for debugging and monitoring
logging.basicConfig(level=logging.INFO)


# Sample data: Resources and exercises for DBT skills training
dbt_resources = [
    {
        "id": 1,
        "name": "Mindfulness Exercise",
        "description": "Practice being present in the moment.",
        "target_audience": ["adolescents", "adults"]
    },
    {
        "id": 2,
        "name": "Emotion Regulation Worksheet",
        "description": "Learn techniques to manage intense emotions.",
        "target_audience": ["adults"]
    },
    {
        "id": 3,
        "name": "Distress Tolerance Practice",
        "description": "Develop coping strategies for challenging situations.",
        "target_audience": ["adolescents", "adults"]
    }
]


# Error handler for 404
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({"error": "Resource not found"}), 404


# Error handler for 500
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500


# Route to fetch all DBT resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    """
    Returns all DBT resources.
    """
    try:
        logging.info("Fetching all DBT resources.")
        return jsonify(dbt_resources), 200
    except Exception as e:
        logging.error(f"Error fetching resources: {e}")
        return jsonify({"error": "Unable to fetch resources"}), 500


# Route to fetch a single resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """
    Returns a DBT resource by its ID.
    """
    try:
        logging.info(f"Fetching resource with ID: {resource_id}")
        resource = next((res for res in dbt_resources if res["id"] == resource_id), None)
        if resource:
            return jsonify(resource), 200
        else:
            return jsonify({"error": "Resource not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching resource with ID {resource_id}: {e}")
        return jsonify({"error": "Unable to fetch resource"}), 500


# Route to filter resources by target audience
@app.route('/api/resources/filter', methods=['GET'])
def filter_resources():
    """
    Filters DBT resources by target audience.
    Query parameter: audience (e.g., 'adolescents', 'adults')
    """
    try:
        audience = request.args.get('audience', None)
        if audience:
            logging.info(f"Filtering resources for target audience: {audience}")
            filtered_resources = [res for res in dbt_resources if audience in res["target_audience"]]
            return jsonify(filtered_resources), 200
        else:
            return jsonify({"error": "No audience specified"}), 400
    except Exception as e:
        logging.error(f"Error filtering resources: {e}")
        return jsonify({"error": "Unable to filter resources"}), 500


# Route to add a new resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    """
    Adds a new DBT resource.
    Expects JSON payload with 'name', 'description', and 'target_audience'.
    """
    try:
        logging.info("Adding a new DBT resource.")
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'target_audience' not in data:
            return jsonify({"error": "Invalid data provided"}), 400

        new_resource = {
            "id": len(dbt_resources) + 1,
            "name": data["name"],
            "description": data["description"],
            "target_audience": data["target_audience"]
        }
        dbt_resources.append(new_resource)
        return jsonify(new_resource), 201
    except Exception as e:
        logging.error(f"Error adding resource: {e}")
        return jsonify({"error": "Unable to add resource"}), 500


# Route to delete a resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    Deletes a DBT resource by its ID.
    """
    try:
        logging.info(f"Deleting resource with ID: {resource_id}")
        resource = next((res for res in dbt_resources if res["id"] == resource_id), None)
        if resource:
            dbt_resources.remove(resource)
            return jsonify({"message": "Resource deleted successfully"}), 200
        else:
            return jsonify({"error": "Resource not found"}), 404
    except Exception as e:
        logging.error(f"Error deleting resource with ID {resource_id}: {e}")
        return jsonify({"error": "Unable to delete resource"}), 500


# Main entry point to run the application
if __name__ == '__main__':
    # Run the Flask server
    app.run(debug=True)
```
