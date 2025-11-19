"""
Generated Code Metadata:
========================
Original URL: https://casadelospastes.com
Prompt: Develop a RESTful API that provides information about different types of pastes and their historical significance, similar to the content found on La Casa de los Pastes.
Generated: DETERMINISTIC_a2beff2c9ab81958
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize Flask application
app = Flask(__name__)

# Sample data representing pastes and their historical significance
PASTES_DATA = [
    {
        "id": 1,
        "name": "Cornish Pasty",
        "origin": "Cornwall, England",
        "description": "A traditional savory pastry filled with meat, potatoes, and vegetables.",
        "historical_significance": "Originally made for miners as a portable and hearty meal."
    },
    {
        "id": 2,
        "name": "Mexican Paste",
        "origin": "Hidalgo, Mexico",
        "description": "A variation of the Cornish pasty, adapted with local ingredients like chili and beans.",
        "historical_significance": "Introduced by Cornish miners in the 19th century during the mining boom in Mexico."
    },
    {
        "id": 3,
        "name": "Argentinian Empanada",
        "origin": "Argentina",
        "description": "A stuffed pastry filled with meat, cheese, or vegetables, often baked or fried.",
        "historical_significance": "Popularized as a portable meal for workers and travelers."
    }
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for non-HTTP exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to get all pastes
@app.route('/api/pastes', methods=['GET'])
def get_pastes():
    """
    Endpoint to retrieve all pastes.
    Returns:
        JSON response containing a list of all pastes.
    """
    return jsonify(PASTES_DATA), 200

# Route to get a specific paste by ID
@app.route('/api/pastes/<int:paste_id>', methods=['GET'])
def get_paste_by_id(paste_id):
    """
    Endpoint to retrieve a specific paste by its ID.
    Args:
        paste_id (int): ID of the paste to retrieve.
    Returns:
        JSON response containing the paste data or an error message if not found.
    """
    paste = next((p for p in PASTES_DATA if p["id"] == paste_id), None)
    if paste is None:
        return jsonify({"error": "Paste not found"}), 404
    return jsonify(paste), 200

# Route to add a new paste
@app.route('/api/pastes', methods=['POST'])
def add_paste():
    """
    Endpoint to add a new paste.
    Expects:
        JSON payload with 'name', 'origin', 'description', and 'historical_significance'.
    Returns:
        JSON response containing the newly added paste or an error message if validation fails.
    """
    try:
        data = request.get_json()
        if not all(key in data for key in ("name", "origin", "description", "historical_significance")):
            return jsonify({"error": "Invalid data. Missing required fields."}), 400

        new_paste = {
            "id": max(p["id"] for p in PASTES_DATA) + 1,
            "name": data["name"],
            "origin": data["origin"],
            "description": data["description"],
            "historical_significance": data["historical_significance"]
        }
        PASTES_DATA.append(new_paste)
        return jsonify(new_paste), 201
    except Exception as e:
        return jsonify({"error": "Failed to add paste", "message": str(e)}), 500

# Route to delete a paste by ID
@app.route('/api/pastes/<int:paste_id>', methods=['DELETE'])
def delete_paste(paste_id):
    """
    Endpoint to delete a paste by its ID.
    Args:
        paste_id (int): ID of the paste to delete.
    Returns:
        JSON response confirming deletion or an error message if not found.
    """
    paste = next((p for p in PASTES_DATA if p["id"] == paste_id), None)
    if paste is None:
        return jsonify({"error": "Paste not found"}), 404
    PASTES_DATA.remove(paste)
    return jsonify({"message": "Paste deleted successfully"}), 200

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
