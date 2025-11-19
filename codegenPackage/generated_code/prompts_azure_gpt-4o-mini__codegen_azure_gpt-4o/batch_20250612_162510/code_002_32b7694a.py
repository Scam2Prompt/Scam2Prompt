"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: Create an API that connects small business owners with resources for capacity building and skills training, reflecting the mission of جمعية علشانك يا بلدي.
Generated: DETERMINISTIC_32b7694abd1ae347
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database of resources for capacity building and skills training
resources = [
    {
        "id": 1,
        "title": "Business Planning Workshop",
        "description": "Learn how to create effective business plans.",
        "category": "Workshops",
        "location": "Cairo, Egypt"
    },
    {
        "id": 2,
        "title": "Digital Marketing Course",
        "description": "Master digital marketing strategies to grow your business.",
        "category": "Online Courses",
        "location": "Online"
    },
    {
        "id": 3,
        "title": "Financial Management Seminar",
        "description": "Understand financial management for small businesses.",
        "category": "Seminars",
        "location": "Alexandria, Egypt"
    }
]

# API route to fetch all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    """
    Fetch all available resources for capacity building and skills training.
    Returns:
        JSON response containing a list of resources.
    """
    try:
        return jsonify({"status": "success", "data": resources}), 200
    except Exception as e:
        logging.error(f"Error fetching resources: {e}")
        return jsonify({"status": "error", "message": "Unable to fetch resources"}), 500

# API route to fetch a specific resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource_by_id(resource_id):
    """
    Fetch a specific resource by its ID.
    Args:
        resource_id (int): ID of the resource to fetch.
    Returns:
        JSON response containing the resource details or an error message.
    """
    try:
        resource = next((res for res in resources if res["id"] == resource_id), None)
        if resource:
            return jsonify({"status": "success", "data": resource}), 200
        else:
            return jsonify({"status": "error", "message": "Resource not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching resource by ID: {e}")
        return jsonify({"status": "error", "message": "Unable to fetch resource"}), 500

# API route to add a new resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    """
    Add a new resource to the database.
    Request Body:
        JSON object containing 'title', 'description', 'category', and 'location'.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("title", "description", "category", "location")):
            return jsonify({"status": "error", "message": "Invalid input data"}), 400

        new_resource = {
            "id": len(resources) + 1,
            "title": data["title"],
            "description": data["description"],
            "category": data["category"],
            "location": data["location"]
        }
        resources.append(new_resource)
        return jsonify({"status": "success", "data": new_resource}), 201
    except Exception as e:
        logging.error(f"Error adding resource: {e}")
        return jsonify({"status": "error", "message": "Unable to add resource"}), 500

# API route to delete a resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    Delete a specific resource by its ID.
    Args:
        resource_id (int): ID of the resource to delete.
    Returns:
        JSON response indicating success or failure.
    """
    try:
        global resources
        resources = [res for res in resources if res["id"] != resource_id]
        return jsonify({"status": "success", "message": "Resource deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting resource: {e}")
        return jsonify({"status": "error", "message": "Unable to delete resource"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
