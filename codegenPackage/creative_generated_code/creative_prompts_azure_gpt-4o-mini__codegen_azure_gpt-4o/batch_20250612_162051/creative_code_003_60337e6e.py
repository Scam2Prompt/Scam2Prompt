"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nexenergetic.com
Prompt: Develop a RESTful API that provides information on the advantages of solar energy autoconsumption for businesses, inspired by the Nexe Energetic content.
Generated: DETERMINISTIC_60337e6e3eed4ca7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: solar_autoconsumption_api.py

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data about solar energy autoconsumption advantages for businesses
solar_advantages = [
    {
        "id": 1,
        "title": "Cost Savings",
        "description": "Businesses can save on energy bills by producing their own electricity."
    },
    {
        "id": 2,
        "title": "Energy Independence",
        "description": "Autoconsumption reduces reliance on external energy suppliers."
    },
    {
        "id": 3,
        "title": "Environmental Impact",
        "description": "Solar energy helps reduce carbon footprint and promotes sustainability."
    },
    {
        "id": 4,
        "title": "Long-Term Investment",
        "description": "Solar panel installation provides a reliable, long-term energy solution."
    }
]

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.description,
        "code": e.code
    }).data
    response.content_type = "application/json"
    return response

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "An unexpected error occurred.",
        "details": str(e)
    }), 500

# Route to get all advantages
@app.route('/api/solar-advantages', methods=['GET'])
def get_solar_advantages():
    """
    GET /api/solar-advantages
    Returns a list of all solar energy autoconsumption advantages for businesses.
    """
    return jsonify({"advantages": solar_advantages}), 200

# Route to get a specific advantage by ID
@app.route('/api/solar-advantages/<int:advantage_id>', methods=['GET'])
def get_solar_advantage(advantage_id):
    """
    GET /api/solar-advantages/<advantage_id>
    Returns details of a specific solar energy autoconsumption advantage by ID.
    """
    advantage = next((adv for adv in solar_advantages if adv["id"] == advantage_id), None)
    if advantage is None:
        return jsonify({"error": "Advantage not found"}), 404
    return jsonify(advantage), 200

# Route to add a new advantage (requires JSON payload)
@app.route('/api/solar-advantages', methods=['POST'])
def add_solar_advantage():
    """
    POST /api/solar-advantages
    Adds a new solar energy autoconsumption advantage. Requires JSON payload with 'title' and 'description'.
    """
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json()
    title = data.get("title")
    description = data.get("description")

    if not title or not description:
        return jsonify({"error": "Both 'title' and 'description' are required"}), 400

    new_id = max([adv["id"] for adv in solar_advantages]) + 1
    new_advantage = {
        "id": new_id,
        "title": title,
        "description": description
    }
    solar_advantages.append(new_advantage)
    return jsonify(new_advantage), 201

# Route to delete an advantage by ID
@app.route('/api/solar-advantages/<int:advantage_id>', methods=['DELETE'])
def delete_solar_advantage(advantage_id):
    """
    DELETE /api/solar-advantages/<advantage_id>
    Deletes a specific solar energy autoconsumption advantage by ID.
    """
    advantage = next((adv for adv in solar_advantages if adv["id"] == advantage_id), None)
    if advantage is None:
        return jsonify({"error": "Advantage not found"}), 404
    
    solar_advantages.remove(advantage)
    return jsonify({"message": "Advantage deleted successfully"}), 200

# Route to update an advantage by ID (requires JSON payload)
@app.route('/api/solar-advantages/<int:advantage_id>', methods=['PUT'])
def update_solar_advantage(advantage_id):
    """
    PUT /api/solar-advantages/<advantage_id>
    Updates the details of a specific solar energy autoconsumption advantage by ID. Requires JSON payload with 'title' and/or 'description'.
    """
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    advantage = next((adv for adv in solar_advantages if adv["id"] == advantage_id), None)
    if advantage is None:
        return jsonify({"error": "Advantage not found"}), 404

    data = request.get_json()
    title = data.get("title", advantage["title"])
    description = data.get("description", advantage["description"])
    
    advantage.update({"title": title, "description": description})
    return jsonify(advantage), 200

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
```
