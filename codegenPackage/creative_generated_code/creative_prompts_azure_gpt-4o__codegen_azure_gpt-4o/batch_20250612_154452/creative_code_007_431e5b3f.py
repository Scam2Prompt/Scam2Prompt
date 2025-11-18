"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Create an API for managing virtual showroom environments, including options for dormitories, kitchens, living spaces, and offices, as outlined in the "Ambientes" section of the webpage.
Generated: DETERMINISTIC_431e5b3f148965c8
Batch ID: 20250612_154452
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

# Data structure to store showroom environments
showroom_environments = {
    "dormitories": [],
    "kitchens": [],
    "living_spaces": [],
    "offices": []
}


# Helper function for error response
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code


# Endpoint to list all environments
@app.route('/api/environments', methods=['GET'])
def list_environments():
    """
    List all showroom environments along with their details.
    """
    return jsonify(showroom_environments), 200


# Endpoint to add a new item to an environment
@app.route('/api/environments/<environment>', methods=['POST'])
def add_environment_item(environment):
    """
    Add a new item to a specified showroom environment.
    Request Body: { "name": "Item Name", "description": "Item Description", "features": [...] }
    """
    if environment not in showroom_environments:
        return error_response("Environment not found.")

    # Validate request data
    data = request.json
    if not all(key in data for key in ("name", "description", "features")):
        return error_response("Invalid data format. 'name', 'description', and 'features' are required.")

    # Add the new item to the specified environment
    showroom_environments[environment].append(data)
    return jsonify({"message": f"Item added to {environment} successfully.", "item": data}), 201


# Endpoint to update an item in an environment
@app.route('/api/environments/<environment>/<item_name>', methods=['PUT'])
def update_environment_item(environment, item_name):
    """
    Update an existing item in a specified showroom environment.
    Request Body: { "description": "Updated Description", "features": [...] }
    """
    if environment not in showroom_environments:
        return error_response("Environment not found.")

    # Find the item in the environment
    items = showroom_environments[environment]
    item = next((i for i in items if i["name"] == item_name), None)

    if not item:
        return error_response("Item not found in the environment.")

    # Update the item details
    data = request.json
    if "description" in data:
        item["description"] = data["description"]
    if "features" in data:
        item["features"] = data["features"]

    return jsonify({"message": f"Item '{item_name}' updated successfully.", "item": item}), 200


# Endpoint to delete an item from an environment
@app.route('/api/environments/<environment>/<item_name>', methods=['DELETE'])
def delete_environment_item(environment, item_name):
    """
    Delete an existing item from a specified showroom environment.
    """
    if environment not in showroom_environments:
        return error_response("Environment not found.")

    # Find and remove the item from the environment
    items = showroom_environments[environment]
    item = next((i for i in items if i["name"] == item_name), None)

    if not item:
        return error_response("Item not found in the environment.")

    items.remove(item)
    return jsonify({"message": f"Item '{item_name}' deleted successfully."}), 200


# Error handler for 404 routes
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors gracefully.
    """
    return error_response("Resource not found.", 404)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
