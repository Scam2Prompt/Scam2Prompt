"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casadelospastes.com
Prompt: Develop a RESTful API that provides information about different types of pastes and their historical significance, similar to the content found on La Casa de los Pastes.
Generated: DETERMINISTIC_a2beff2c9ab81958
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: pastes_api.py

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Create Flask application
app = Flask(__name__)

# Sample data representing different types of pastes
PASTES_DATA = [
    {
        "id": 1,
        "name": "Cornish Pasty",
        "origin": "Cornwall, England",
        "historical_significance": "Traditionally eaten by miners in the 19th century."
    },
    {
        "id": 2,
        "name": "Empanada",
        "origin": "Spain and Latin America",
        "historical_significance": "Dates back to the Middle Ages, often stuffed with meat, cheese, or vegetables."
    },
    {
        "id": 3,
        "name": "Hidalgo Pasty",
        "origin": "Hidalgo, Mexico",
        "historical_significance": "Introduced by Cornish miners in the 19th century; adapted with local ingredients."
    }
]

# Error handler for 404 (resource not found)
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

# Error handler for unexpected server errors
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify(error=str(e)).data
    response.content_type = "application/json"
    return response

# Endpoint: Get all pastes
@app.route('/api/pastes', methods=['GET'])
def get_all_pastes():
    """
    GET /api/pastes
    Returns a list of all pastes.
    """
    return jsonify(PASTES_DATA), 200

# Endpoint: Get a single paste by ID
@app.route('/api/pastes/<int:paste_id>', methods=['GET'])
def get_paste_by_id(paste_id):
    """
    GET /api/pastes/<paste_id>
    Returns the details of a specific paste by its ID.
    """
    paste = next((paste for paste in PASTES_DATA if paste['id'] == paste_id), None)
    if not paste:
        return jsonify(error="Paste not found"), 404
    return jsonify(paste), 200

# Endpoint: Add a new paste
@app.route('/api/pastes', methods=['POST'])
def add_paste():
    """
    POST /api/pastes
    Adds a new paste to the dataset.
    Expects JSON payload with 'name', 'origin', and 'historical_significance'.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'origin' not in data or 'historical_significance' not in data:
        return jsonify(error="Invalid data. 'name', 'origin', and 'historical_significance' are required."), 400
    
    new_id = max(paste['id'] for paste in PASTES_DATA) + 1
    new_paste = {
        "id": new_id,
        "name": data['name'],
        "origin": data['origin'],
        "historical_significance": data['historical_significance']
    }
    PASTES_DATA.append(new_paste)
    return jsonify(new_paste), 201

# Endpoint: Delete a paste by ID
@app.route('/api/pastes/<int:paste_id>', methods=['DELETE'])
def delete_paste(paste_id):
    """
    DELETE /api/pastes/<paste_id>
    Deletes a paste by its ID.
    """
    paste = next((paste for paste in PASTES_DATA if paste['id'] == paste_id), None)
    if not paste:
        return jsonify(error="Paste not found"), 404
    
    PASTES_DATA.remove(paste)
    return jsonify(message=f"Paste with ID {paste_id} deleted successfully."), 200

# Main entry point to run the app
if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
```
