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
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for tourist attractions
tourist_attractions = [
    {
        "id": 1,
        "name": "Puncak Mentigen",
        "description": "A scenic viewpoint offering panoramic views of Mount Bromo.",
        "location": {"latitude": -7.9197, "longitude": 112.9410},
        "category": "viewpoint"
    },
    {
        "id": 2,
        "name": "Pasir Berbisik",
        "description": "A vast desert area with whispering sands near Mount Bromo.",
        "location": {"latitude": -7.9271, "longitude": 112.9387},
        "category": "desert"
    }
]

# Endpoint to get all tourist attractions
@app.route('/api/tourist-attractions', methods=['GET'])
def get_tourist_attractions():
    """
    Returns a list of all tourist attractions.
    """
    try:
        logging.info("Fetching all tourist attractions.")
        return jsonify({"status": "success", "data": tourist_attractions}), 200
    except Exception as e:
        logging.error(f"Error fetching tourist attractions: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Endpoint to get a specific tourist attraction by ID
@app.route('/api/tourist-attractions/<int:attraction_id>', methods=['GET'])
def get_tourist_attraction(attraction_id):
    """
    Returns details of a specific tourist attraction by its ID.
    """
    try:
        logging.info(f"Fetching tourist attraction with ID: {attraction_id}")
        attraction = next((a for a in tourist_attractions if a["id"] == attraction_id), None)
        if attraction:
            return jsonify({"status": "success", "data": attraction}), 200
        else:
            return jsonify({"status": "error", "message": "Attraction not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching tourist attraction: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Endpoint to add a new tourist attraction
@app.route('/api/tourist-attractions', methods=['POST'])
def add_tourist_attraction():
    """
    Adds a new tourist attraction to the list.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["name", "description", "location", "category"]):
            return jsonify({"status": "error", "message": "Invalid input"}), 400

        new_attraction = {
            "id": len(tourist_attractions) + 1,
            "name": data["name"],
            "description": data["description"],
            "location": data["location"],
            "category": data["category"]
        }
        tourist_attractions.append(new_attraction)
        logging.info(f"Added new tourist attraction: {new_attraction}")
        return jsonify({"status": "success", "data": new_attraction}), 201
    except Exception as e:
        logging.error(f"Error adding tourist attraction: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Endpoint to delete a tourist attraction by ID
@app.route('/api/tourist-attractions/<int:attraction_id>', methods=['DELETE'])
def delete_tourist_attraction(attraction_id):
    """
    Deletes a tourist attraction by its ID.
    """
    try:
        logging.info(f"Deleting tourist attraction with ID: {attraction_id}")
        attraction = next((a for a in tourist_attractions if a["id"] == attraction_id), None)
        if attraction:
            tourist_attractions.remove(attraction)
            return jsonify({"status": "success", "message": "Attraction deleted"}), 200
        else:
            return jsonify({"status": "error", "message": "Attraction not found"}), 404
    except Exception as e:
        logging.error(f"Error deleting tourist attraction: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
