"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomgardi-sunland.com
Prompt: Generate an API that allows users to explore unique experiences at an eco-lodge, such as nature walks and art workshops, similar to those offered by the Boomgardi Sunland accommodation.
Generated: DETERMINISTIC_ad37975156956863
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Mock database of experiences
experiences = [
    {"id": 1, "name": "Nature Walk", "description": "A guided tour through lush greenery.", "availability": "Daily"},
    {"id": 2, "name": "Art Workshop", "description": "Learn and create art using natural materials.", "availability": "Weekends"},
    {"id": 3, "name": "Bird Watching", "description": "Spot exotic birds in their natural habitat.", "availability": "Mornings"},
]

# Error handling for unexpected issues
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = 'application/json'
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Route to list all experiences
@app.route('/api/experiences', methods=['GET'])
def get_experiences():
    """
    Endpoint to retrieve all available experiences at the eco-lodge.
    Returns:
        JSON response containing a list of experiences.
    """
    return jsonify({"experiences": experiences}), 200

# Route to retrieve a specific experience by ID
@app.route('/api/experiences/<int:experience_id>', methods=['GET'])
def get_experience_by_id(experience_id):
    """
    Endpoint to retrieve details of a specific experience by ID.
    Parameters:
        experience_id (int): ID of the experience to retrieve.
    Returns:
        JSON response containing experience details or an error message.
    """
    experience = next((exp for exp in experiences if exp["id"] == experience_id), None)
    if experience:
        return jsonify({"experience": experience}), 200
    return jsonify({"error": "Experience not found"}), 404

# Route to add a new experience
@app.route('/api/experiences', methods=['POST'])
def add_experience():
    """
    Endpoint to add a new experience to the eco-lodge.
    Expects:
        JSON payload with 'name', 'description', and 'availability' fields.
    Returns:
        JSON response with the newly created experience or an error message.
    """
    try:
        data = request.get_json()
        if not data or "name" not in data or "description" not in data or "availability" not in data:
            return jsonify({"error": "Invalid input. 'name', 'description', and 'availability' are required fields."}), 400

        new_experience = {
            "id": len(experiences) + 1,
            "name": data["name"],
            "description": data["description"],
            "availability": data["availability"],
        }
        experiences.append(new_experience)
        return jsonify({"experience": new_experience}), 201
    except Exception as e:
        return jsonify({"error": "Failed to add experience. Please check your input."}), 500

# Route to update an existing experience
@app.route('/api/experiences/<int:experience_id>', methods=['PUT'])
def update_experience(experience_id):
    """
    Endpoint to update an existing experience by ID.
    Expects:
        JSON payload with 'name', 'description', and/or 'availability' fields.
    Parameters:
        experience_id (int): ID of the experience to update.
    Returns:
        JSON response with the updated experience or an error message.
    """
    experience = next((exp for exp in experiences if exp["id"] == experience_id), None)
    if not experience:
        return jsonify({"error": "Experience not found"}), 404

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. Please provide at least one field to update."}), 400

        experience.update({key: value for key, value in data.items() if key in experience})
        return jsonify({"experience": experience}), 200
    except Exception as e:
        return jsonify({"error": "Failed to update experience. Please check your input."}), 500

# Route to delete an experience
@app.route('/api/experiences/<int:experience_id>', methods=['DELETE'])
def delete_experience(experience_id):
    """
    Endpoint to delete an experience by ID.
    Parameters:
        experience_id (int): ID of the experience to delete.
    Returns:
        JSON response confirming deletion or an error message.
    """
    global experiences
    experience = next((exp for exp in experiences if exp["id"] == experience_id), None)
    if not experience:
        return jsonify({"error": "Experience not found"}), 404

    experiences = [exp for exp in experiences if exp["id"] != experience_id]
    return jsonify({"message": "Experience deleted successfully"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
