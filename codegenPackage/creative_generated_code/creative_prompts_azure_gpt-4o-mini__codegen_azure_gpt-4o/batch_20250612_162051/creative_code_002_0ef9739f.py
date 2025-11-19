"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Create a RESTful API endpoint that retrieves information about luxury villas, including details like maximum guest capacity, check-in/check-out times, and nearby attractions, inspired by the Diamond Villa in Corfu.
Generated: DETERMINISTIC_0ef9739f3d8dc253
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO)

# Mock data for luxury villas
villas = [
    {
        "id": 1,
        "name": "Diamond Villa",
        "location": "Corfu, Greece",
        "max_guest_capacity": 10,
        "check_in_time": "3:00 PM",
        "check_out_time": "11:00 AM",
        "nearby_attractions": [
            "Corfu Old Town",
            "Paleokastritsa Beach",
            "Achilleion Palace"
        ]
    },
    {
        "id": 2,
        "name": "Emerald Villa",
        "location": "Zakynthos, Greece",
        "max_guest_capacity": 8,
        "check_in_time": "2:00 PM",
        "check_out_time": "10:00 AM",
        "nearby_attractions": [
            "Navagio Beach",
            "Blue Caves",
            "Keri Cliffs"
        ]
    }
]

@app.route('/api/villas', methods=['GET'])
def get_villas():
    """
    Endpoint to retrieve information about all luxury villas.
    Returns:
        JSON: List of villas with details.
    """
    try:
        return jsonify({"success": True, "data": villas}), 200
    except Exception as e:
        logging.error(f"Error fetching villas: {str(e)}")
        return jsonify({"success": False, "error": "An error occurred while fetching villa data"}), 500

@app.route('/api/villas/<int:villa_id>', methods=['GET'])
def get_villa_by_id(villa_id):
    """
    Endpoint to retrieve information about a specific villa by ID.
    Args:
        villa_id (int): ID of the villa to retrieve.
    Returns:
        JSON: Details of the specific villa or error message.
    """
    try:
        villa = next((villa for villa in villas if villa["id"] == villa_id), None)
        if villa:
            return jsonify({"success": True, "data": villa}), 200
        else:
            return jsonify({"success": False, "error": "Villa not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching villa by ID ({villa_id}): {str(e)}")
        return jsonify({"success": False, "error": "An error occurred while fetching villa data"}), 500

@app.route('/api/villas/search', methods=['GET'])
def search_villas():
    """
    Endpoint to search villas by name or location.
    Query Parameters:
        name (str): Name of the villa (optional).
        location (str): Location of the villa (optional).
    Returns:
        JSON: Filtered list of villas or a message if no match is found.
    """
    try:
        name = request.args.get('name', None)
        location = request.args.get('location', None)

        filtered_villas = villas

        if name:
            filtered_villas = [villa for villa in filtered_villas if name.lower() in villa["name"].lower()]
        
        if location:
            filtered_villas = [villa for villa in filtered_villas if location.lower() in villa["location"].lower()]
        
        if filtered_villas:
            return jsonify({"success": True, "data": filtered_villas}), 200
        else:
            return jsonify({"success": False, "message": "No villas matched the search criteria"}), 404
    except Exception as e:
        logging.error(f"Error searching villas: {str(e)}")
        return jsonify({"success": False, "error": "An error occurred while searching for villas"}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
