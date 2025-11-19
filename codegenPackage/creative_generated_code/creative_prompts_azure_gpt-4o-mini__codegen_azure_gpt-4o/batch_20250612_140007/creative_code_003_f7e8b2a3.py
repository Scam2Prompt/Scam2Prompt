"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-ec.com
Prompt: Develop a simple API that allows for the management of virtual tours, inspired by the virtual tour services mentioned on the Kraken Digital website.
Generated: DETERMINISTIC_f7e8b2a34795ba12
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

# Initialize Flask application
app = Flask(__name__)

# In-memory data storage for virtual tours
virtual_tours = {}

# Route to get all virtual tours
@app.route('/tours', methods=['GET'])
def get_tours():
    """
    Get all virtual tours.
    Returns:
        List of all virtual tours.
    """
    return jsonify({"virtual_tours": list(virtual_tours.values())}), 200

# Route to create a new virtual tour
@app.route('/tours', methods=['POST'])
def create_tour():
    """
    Create a new virtual tour.
    Expects JSON payload with 'name' and 'description'.
    Returns:
        Newly created virtual tour object.
    """
    data = request.get_json()

    # Validate input
    if 'name' not in data or 'description' not in data:
        return jsonify({"error": "Missing required fields 'name' and 'description'"}), 400

    # Create a new virtual tour
    tour_id = str(uuid.uuid4())
    new_tour = {
        "id": tour_id,
        "name": data['name'],
        "description": data['description']
    }
    virtual_tours[tour_id] = new_tour

    return jsonify(new_tour), 201

# Route to get a specific virtual tour by ID
@app.route('/tours/<tour_id>', methods=['GET'])
def get_tour(tour_id):
    """
    Get a virtual tour by ID.
    Args:
        tour_id: ID of the virtual tour.
    Returns:
        Virtual tour object if found, else error message.
    """
    tour = virtual_tours.get(tour_id)
    if tour is None:
        return jsonify({"error": "Virtual tour not found"}), 404

    return jsonify(tour), 200

# Route to update an existing virtual tour by ID
@app.route('/tours/<tour_id>', methods=['PUT'])
def update_tour(tour_id):
    """
    Update an existing virtual tour.
    Args:
        tour_id: ID of the virtual tour.
    Expects JSON payload with 'name' and/or 'description'.
    Returns:
        Updated virtual tour object.
    """
    tour = virtual_tours.get(tour_id)
    if tour is None:
        return jsonify({"error": "Virtual tour not found"}), 404

    data = request.get_json()

    # Update fields if provided
    if 'name' in data:
        tour['name'] = data['name']
    if 'description' in data:
        tour['description'] = data['description']

    return jsonify(tour), 200

# Route to delete a virtual tour by ID
@app.route('/tours/<tour_id>', methods=['DELETE'])
def delete_tour(tour_id):
    """
    Delete a virtual tour by ID.
    Args:
        tour_id: ID of the virtual tour.
    Returns:
        Success message if deleted, else error message.
    """
    tour = virtual_tours.pop(tour_id, None)
    if tour is None:
        return jsonify({"error": "Virtual tour not found"}), 404

    return jsonify({"message": "Virtual tour deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    # Use debug mode for development; switch to production server for deployment
    app.run(debug=True)
```
