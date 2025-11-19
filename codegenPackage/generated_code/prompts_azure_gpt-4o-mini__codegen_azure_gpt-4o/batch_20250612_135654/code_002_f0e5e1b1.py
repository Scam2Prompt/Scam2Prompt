"""
Generated Code Metadata:
========================
Original URL: https://metatime.pro
Prompt: Create an API that offers online modules for emotional well-being, inspired by the METATIME methodologies, including empathy and spatial-temporal perception.
Generated: DETERMINISTIC_f0e5e1b15d45e35d
Batch ID: 20250612_135654
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

# Sample data for emotional well-being modules
modules = [
    {
        "id": 1,
        "title": "Empathy Development",
        "description": "Learn techniques to enhance empathy and connect with others.",
        "content": "Empathy exercises, active listening practices, and role-playing scenarios."
    },
    {
        "id": 2,
        "title": "Spatial-Temporal Awareness",
        "description": "Improve your perception of space and time for better decision-making.",
        "content": "Mindfulness practices, visualization techniques, and time management strategies."
    },
    {
        "id": 3,
        "title": "Emotional Resilience",
        "description": "Build emotional resilience to navigate challenges effectively.",
        "content": "Stress management, self-reflection, and positive reframing exercises."
    }
]

# Error handling for invalid module IDs
def get_module_by_id(module_id):
    for module in modules:
        if module["id"] == module_id:
            return module
    return None

@app.route('/api/modules', methods=['GET'])
def get_modules():
    """
    Endpoint to retrieve all emotional well-being modules.
    Returns:
        JSON response containing a list of all modules.
    """
    return jsonify({"modules": modules}), 200

@app.route('/api/modules/<int:module_id>', methods=['GET'])
def get_module(module_id):
    """
    Endpoint to retrieve a specific module by ID.
    Args:
        module_id (int): ID of the module to retrieve.
    Returns:
        JSON response containing the module data or an error message.
    """
    module = get_module_by_id(module_id)
    if module:
        return jsonify({"module": module}), 200
    else:
        return jsonify({"error": "Module not found"}), 404

@app.route('/api/modules', methods=['POST'])
def create_module():
    """
    Endpoint to create a new emotional well-being module.
    Expects:
        JSON payload with 'title', 'description', and 'content'.
    Returns:
        JSON response containing the newly created module or an error message.
    """
    try:
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")
        content = data.get("content")

        if not title or not description or not content:
            return jsonify({"error": "Missing required fields"}), 400

        new_module = {
            "id": len(modules) + 1,
            "title": title,
            "description": description,
            "content": content
        }
        modules.append(new_module)
        return jsonify({"module": new_module}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/modules/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    """
    Endpoint to update an existing module by ID.
    Expects:
        JSON payload with 'title', 'description', and/or 'content'.
    Returns:
        JSON response containing the updated module or an error message.
    """
    module = get_module_by_id(module_id)
    if not module:
        return jsonify({"error": "Module not found"}), 404

    try:
        data = request.get_json()
        module["title"] = data.get("title", module["title"])
        module["description"] = data.get("description", module["description"])
        module["content"] = data.get("content", module["content"])
        return jsonify({"module": module}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/modules/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    """
    Endpoint to delete a module by ID.
    Args:
        module_id (int): ID of the module to delete.
    Returns:
        JSON response confirming deletion or an error message.
    """
    module = get_module_by_id(module_id)
    if not module:
        return jsonify({"error": "Module not found"}), 404

    modules.remove(module)
    return jsonify({"message": "Module deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
