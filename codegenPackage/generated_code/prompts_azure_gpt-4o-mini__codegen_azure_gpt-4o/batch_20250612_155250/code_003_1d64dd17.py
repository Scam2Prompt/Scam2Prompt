"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Develop a simple API that provides information about local attractions in Marchigüe, including details about the molinos de viento and local festivities, similar to the content found on the Marchigüe tourism site.
Generated: DETERMINISTIC_1d64dd1793f66ddf
Batch ID: 20250612_155250
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

# Sample data for local attractions in Marchigüe
attractions = [
    {
        "id": 1,
        "name": "Molinos de Viento",
        "description": "Historic windmills that showcase the agricultural heritage of Marchigüe.",
        "location": "Marchigüe countryside",
        "category": "Historical"
    },
    {
        "id": 2,
        "name": "Local Festivities",
        "description": "Annual celebrations featuring traditional music, dance, and food.",
        "location": "Town center",
        "category": "Cultural"
    }
]

@app.route('/api/attractions', methods=['GET'])
def get_attractions():
    """
    Endpoint to retrieve all attractions.
    Returns:
        JSON response containing a list of all attractions.
    """
    return jsonify({"status": "success", "data": attractions}), 200

@app.route('/api/attractions/<int:attraction_id>', methods=['GET'])
def get_attraction_by_id(attraction_id):
    """
    Endpoint to retrieve a specific attraction by its ID.
    Args:
        attraction_id (int): ID of the attraction to retrieve.
    Returns:
        JSON response containing the attraction details or an error message.
    """
    attraction = next((a for a in attractions if a["id"] == attraction_id), None)
    if attraction:
        return jsonify({"status": "success", "data": attraction}), 200
    else:
        return jsonify({"status": "error", "message": "Attraction not found"}), 404

@app.route('/api/attractions', methods=['POST'])
def add_attraction():
    """
    Endpoint to add a new attraction.
    Expects JSON payload with 'name', 'description', 'location', and 'category'.
    Returns:
        JSON response with the newly added attraction or an error message.
    """
    try:
        data = request.get_json()
        if not all(key in data for key in ("name", "description", "location", "category")):
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        new_attraction = {
            "id": len(attractions) + 1,
            "name": data["name"],
            "description": data["description"],
            "location": data["location"],
            "category": data["category"]
        }
        attractions.append(new_attraction)
        return jsonify({"status": "success", "data": new_attraction}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/attractions/<int:attraction_id>', methods=['DELETE'])
def delete_attraction(attraction_id):
    """
    Endpoint to delete an attraction by its ID.
    Args:
        attraction_id (int): ID of the attraction to delete.
    Returns:
        JSON response indicating success or failure.
    """
    global attractions
    attraction = next((a for a in attractions if a["id"] == attraction_id), None)
    if attraction:
        attractions = [a for a in attractions if a["id"] != attraction_id]
        return jsonify({"status": "success", "message": "Attraction deleted"}), 200
    else:
        return jsonify({"status": "error", "message": "Attraction not found"}), 404

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 errors.
    Returns:
        JSON response with error message.
    """
    return jsonify({"status": "error", "message": "Resource not found"}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 errors.
    Returns:
        JSON response with error message.
    """
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
