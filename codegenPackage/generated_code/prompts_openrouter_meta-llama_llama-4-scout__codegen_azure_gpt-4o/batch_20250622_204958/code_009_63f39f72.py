"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Create a RESTful API for retrieving information about Tanzania's national parks, including details about wildlife, climate, and tourist facilities.
Generated: DETERMINISTIC_63f39f72d53fe664
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data for Tanzania's national parks
national_parks = [
    {
        "id": 1,
        "name": "Serengeti National Park",
        "wildlife": ["Lions", "Elephants", "Cheetahs", "Zebras"],
        "climate": "Tropical savanna climate",
        "tourist_facilities": ["Lodges", "Campsites", "Guided Tours"]
    },
    {
        "id": 2,
        "name": "Ngorongoro Conservation Area",
        "wildlife": ["Rhinos", "Buffalos", "Flamingos", "Hyenas"],
        "climate": "Highland climate",
        "tourist_facilities": ["Hotels", "Viewpoints", "Cultural Tours"]
    },
    {
        "id": 3,
        "name": "Tarangire National Park",
        "wildlife": ["Elephants", "Giraffes", "Wildebeests", "Leopards"],
        "climate": "Dry tropical climate",
        "tourist_facilities": ["Luxury Tents", "Picnic Sites", "Game Drives"]
    }
]

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Route to retrieve all national parks
@app.route('/api/national_parks', methods=['GET'])
def get_national_parks():
    """
    Retrieve a list of all national parks.
    """
    logging.info("Fetching all national parks")
    return jsonify(national_parks), 200

# Route to retrieve a specific national park by ID
@app.route('/api/national_parks/<int:park_id>', methods=['GET'])
def get_national_park(park_id):
    """
    Retrieve details of a specific national park by ID.
    """
    logging.info(f"Fetching details for park ID: {park_id}")
    park = next((p for p in national_parks if p["id"] == park_id), None)
    if park:
        return jsonify(park), 200
    else:
        return jsonify({"error": "National park not found"}), 404

# Route to search national parks by name
@app.route('/api/national_parks/search', methods=['GET'])
def search_national_parks():
    """
    Search for national parks by name.
    """
    query = request.args.get('name', '').lower()
    logging.info(f"Searching for parks with name containing: {query}")
    results = [p for p in national_parks if query in p["name"].lower()]
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"error": "No parks found matching the search criteria"}), 404

# Main entry point for running the app
if __name__ == '__main__':
    app.run(debug=True)
```
