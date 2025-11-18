"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.ilmaweb.com
Prompt: Suggest an API for mapping tourist attractions like Puncak Mentigen and Pasir Berbisik, as described on the Budi Bromo Tour website.
Generated: DETERMINISTIC_93f24b5cf5536b37
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Sample data representing tourist attractions
attractions = [
    {
        "id": 1,
        "name": "Puncak Mentigen",
        "location": {"latitude": -7.9772, "longitude": 112.6305},
        "description": "A beautiful viewpoint perfect for sunrise.",
        "category": "Nature"
    },
    {
        "id": 2,
        "name": "Pasir Berbisik",
        "location": {"latitude": -7.9470, "longitude": 112.6443},
        "description": "A serene sand dune area with stunning landscapes.",
        "category": "Nature"
    }
]

@app.route('/api/attractions', methods=['GET'])
def get_attractions():
    """
    Retrieve a list of all tourist attractions.
    Returns:
        JSON response containing a list of attractions.
    """
    return jsonify(attractions), 200

@app.route('/api/attractions/<int:attraction_id>', methods=['GET'])
def get_attraction(attraction_id):
    """
    Retrieve a specific tourist attraction by ID.
    Args:
        attraction_id (int): The ID of the attraction to retrieve.
    Returns:
        JSON response containing the attraction details.
    Raises:
        NotFound: If the attraction ID does not exist.
    """
    attraction = next((attr for attr in attractions if attr['id'] == attraction_id), None)
    if attraction is None:
        raise NotFound(f'Attraction with ID {attraction_id} not found.')
    return jsonify(attraction), 200

@app.route('/api/attractions', methods=['POST'])
def add_attraction():
    """
    Add a new tourist attraction.
    Expects a JSON payload with attraction details.
    Returns:
        JSON response with the newly created attraction.
    Raises:
        BadRequest: If the request data is invalid.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'location' not in data:
        raise BadRequest('Invalid input. Must include name and location.')

    new_id = max(attraction['id'] for attraction in attractions) + 1
    new_attraction = {
        "id": new_id,
        "name": data['name'],
        "location": data['location'],
        "description": data.get('description', ''),
        "category": data.get('category', 'General')
    }
    attractions.append(new_attraction)
    return jsonify(new_attraction), 201

@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
