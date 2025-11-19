"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khaptadtours.com
Prompt: Generate a code snippet for a travel booking API that includes options for trekking the Everest Base Camp, highlighting its challenging nature and stunning views.
Generated: DETERMINISTIC_5a1f8563453214e8
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data for trekking packages
TREKKING_PACKAGES = [
    {
        "id": 1,
        "name": "Everest Base Camp Trek",
        "duration": "14 days",
        "difficulty": "Challenging",
        "highlights": [
            "Stunning views of Mount Everest",
            "Visit to Namche Bazaar",
            "Experience Sherpa culture",
            "Explore picturesque villages"
        ],
        "price": 1200.00
    }
]

@app.route('/api/treks', methods=['GET'])
def get_trekking_options():
    """
    Endpoint to retrieve a list of trekking packages.
    Returns a JSON response with trekking details.
    """
    return jsonify(TREKKING_PACKAGES), 200

@app.route('/api/treks/<int:trek_id>', methods=['GET'])
def get_trek_by_id(trek_id):
    """
    Retrieve details of a specific trekking package by its ID.
    Args:
        trek_id (int): The ID of the trek to retrieve.
    Returns:
        JSON response with trek details or 404 if not found.
    """
    trek = next((trek for trek in TREKKING_PACKAGES if trek["id"] == trek_id), None)
    
    if trek is None:
        return jsonify({"error": "Trek not found"}), 404
    
    return jsonify(trek), 200

@app.route('/api/treks', methods=['POST'])
def create_trek():
    """
    Endpoint to create a new trekking package.
    Expects JSON body with trek details.
    Returns:
        JSON response with the created trek or 400 if input is invalid.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'duration' not in data or 'difficulty' not in data:
            raise BadRequest("Missing required fields: name, duration, difficulty.")
        
        new_trek = {
            "id": len(TREKKING_PACKAGES) + 1,
            "name": data['name'],
            "duration": data['duration'],
            "difficulty": data['difficulty'],
            "highlights": data.get('highlights', []),
            "price": data.get('price', 0.0)
        }
        
        TREKKING_PACKAGES.append(new_trek)
        return jsonify(new_trek), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for unexpected exceptions.
    Returns a JSON response with error details.
    """
    return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False)
```
