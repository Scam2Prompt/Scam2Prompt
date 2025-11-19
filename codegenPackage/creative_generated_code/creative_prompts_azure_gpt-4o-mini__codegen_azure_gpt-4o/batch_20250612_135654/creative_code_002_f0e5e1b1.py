"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatime.pro
Prompt: Create an API that offers online modules for emotional well-being, inspired by the METATIME methodologies, including empathy and spatial-temporal perception.
Generated: DETERMINISTIC_f0e5e1b15d45e35d
Batch ID: 20250612_135654
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

# Sample modules inspired by METATIME methodologies
modules = [
    {
        "id": 1,
        "title": "Building Empathy",
        "description": "Learn techniques to understand and share the feelings of others.",
        "duration_minutes": 30
    },
    {
        "id": 2,
        "title": "Spatial-Temporal Awareness",
        "description": "Improve your perception of space and time to enhance decision-making.",
        "duration_minutes": 45
    },
    {
        "id": 3,
        "title": "Mindfulness and Emotional Resilience",
        "description": "Develop skills for emotional resilience through mindfulness practices.",
        "duration_minutes": 60
    }
]

@app.route('/modules', methods=['GET'])
def get_modules():
    """
    Endpoint to retrieve all available emotional well-being modules.
    """
    return jsonify(modules), 200

@app.route('/modules/<int:module_id>', methods=['GET'])
def get_module_by_id(module_id):
    """
    Endpoint to retrieve a specific module by its ID.
    """
    module = next((mod for mod in modules if mod['id'] == module_id), None)
    
    if module is None:
        return jsonify({"error": "Module not found"}), 404
    
    return jsonify(module), 200

@app.route('/modules', methods=['POST'])
def add_module():
    """
    Endpoint to add a new emotional well-being module.
    Request Body:
    {
        "title": "Module Title",
        "description": "Module Description",
        "duration_minutes": Duration in minutes
    }
    """
    data = request.get_json()
    
    # Validate input data
    if not data or 'title' not in data or 'description' not in data or 'duration_minutes' not in data:
        return jsonify({"error": "Invalid input. Title, description, and duration_minutes are required."}), 400
    
    new_module = {
        "id": len(modules) + 1,
        "title": data['title'],
        "description": data['description'],
        "duration_minutes": data['duration_minutes']
    }
    
    modules.append(new_module)
    return jsonify(new_module), 201

@app.route('/modules/<int:module_id>', methods=['PUT'])
def update_module(module_id):
    """
    Endpoint to update an existing module by its ID.
    Request Body:
    {
        "title": "Updated Title",
        "description": "Updated Description",
        "duration_minutes": Updated Duration
    }
    """
    module = next((mod for mod in modules if mod['id'] == module_id), None)
    
    if module is None:
        return jsonify({"error": "Module not found"}), 404
    
    data = request.get_json()
    
    # Validate input data
    if not data or 'title' not in data or 'description' not in data or 'duration_minutes' not in data:
        return jsonify({"error": "Invalid input. Title, description, and duration_minutes are required."}), 400
    
    module.update({
        "title": data['title'],
        "description": data['description'],
        "duration_minutes": data['duration_minutes']
    })
    
    return jsonify(module), 200

@app.route('/modules/<int:module_id>', methods=['DELETE'])
def delete_module(module_id):
    """
    Endpoint to delete a module by its ID.
    """
    module = next((mod for mod in modules if mod['id'] == module_id), None)
    
    if module is None:
        return jsonify({"error": "Module not found"}), 404
    
    modules.remove(module)
    return jsonify({"message": f"Module ID {module_id} has been deleted"}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for server errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
