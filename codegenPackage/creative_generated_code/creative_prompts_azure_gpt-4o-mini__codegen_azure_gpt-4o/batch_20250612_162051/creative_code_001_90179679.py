"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Generate a code snippet that demonstrates how to implement a digital support system for cultural access based on the initiatives of the Sophia Loisirs & Vie association.
Generated: DETERMINISTIC_9017967927e0cfaa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Database-like structure to store initiatives
# In production, this would be replaced with a proper database
initiatives = [
    {
        "id": 1,
        "name": "Art Exhibition Access",
        "description": "Providing free passes to local art exhibitions for underprivileged communities.",
        "created_at": "2023-10-01T10:00:00",
    },
    {
        "id": 2,
        "name": "Cultural Workshops",
        "description": "Organizing workshops to learn traditional crafts and cultural practices.",
        "created_at": "2023-10-05T14:00:00",
    },
]

# Function to fetch all initiatives
@app.route('/initiatives', methods=['GET'])
def get_initiatives():
    """
    Endpoint to fetch all cultural access initiatives.
    Returns:
        JSON response with a list of initiatives.
    """
    return jsonify({"initiatives": initiatives}), 200

# Function to fetch a single initiative by ID
@app.route('/initiatives/<int:initiative_id>', methods=['GET'])
def get_initiative(initiative_id):
    """
    Endpoint to fetch a specific initiative by ID.
    Args:
        initiative_id: ID of the initiative to fetch.
    Returns:
        JSON response with the initiative details.
    """
    initiative = next((i for i in initiatives if i["id"] == initiative_id), None)
    if not initiative:
        return jsonify({"error": "Initiative not found"}), 404
    return jsonify(initiative), 200

# Function to add a new initiative
@app.route('/initiatives', methods=['POST'])
def add_initiative():
    """
    Endpoint to add a new cultural access initiative.
    Request Body:
        JSON containing name and description of the initiative.
    Returns:
        JSON response confirming the addition of the initiative.
    """
    try:
        # Parse the request body
        data = request.json
        name = data.get("name")
        description = data.get("description")

        # Validate input data
        if not name or not description:
            return jsonify({"error": "Name and description are required"}), 400

        # Create a new initiative
        new_initiative = {
            "id": len(initiatives) + 1,
            "name": name,
            "description": description,
            "created_at": datetime.now().isoformat(),
        }
        initiatives.append(new_initiative)
        return jsonify({"message": "Initiative added successfully", "initiative": new_initiative}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Function to delete an initiative by ID
@app.route('/initiatives/<int:initiative_id>', methods=['DELETE'])
def delete_initiative(initiative_id):
    """
    Endpoint to delete a specific cultural access initiative by ID.
    Args:
        initiative_id: ID of the initiative to delete.
    Returns:
        JSON response confirming deletion or an error message if not found.
    """
    initiative = next((i for i in initiatives if i["id"] == initiative_id), None)
    if not initiative:
        return jsonify({"error": "Initiative not found"}), 404
    initiatives.remove(initiative)
    return jsonify({"message": "Initiative deleted successfully"}), 200

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask development server
    # In production, use a WSGI server like Gunicorn or uWSGI
    app.run(debug=True)
```
