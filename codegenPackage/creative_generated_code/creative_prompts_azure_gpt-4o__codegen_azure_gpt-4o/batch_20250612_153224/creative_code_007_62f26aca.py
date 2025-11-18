"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Develop a REST API endpoint for retrieving store locations and contact details, formatted like the addresses provided on Navkar Furniture's website.
Generated: DETERMINISTIC_62f26acae7f73d84
Batch ID: 20250612_153224
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

# Initialize the Flask app
app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)

# Sample data for store locations and contact details
STORE_LOCATIONS = [
    {
        "id": 1,
        "name": "Navkar Furniture - Main Branch",
        "address": "1234 Elm Street, Springfield, IL, 62704",
        "phone": "+1 234-567-890",
        "email": "info@navkarfurniture.com"
    },
    {
        "id": 2,
        "name": "Navkar Furniture - Downtown",
        "address": "5678 Oak Drive, Springfield, IL, 62705",
        "phone": "+1 345-678-901",
        "email": "support@navkarfurniture.com"
    },
    {
        "id": 3,
        "name": "Navkar Furniture - Westside",
        "address": "9101 Pine Avenue, Springfield, IL, 62706",
        "phone": "+1 456-789-012",
        "email": "sales@navkarfurniture.com"
    }
]

@app.route('/api/store-locations', methods=['GET'])
def get_store_locations():
    """
    Endpoint to retrieve all store locations and contact details.

    Returns:
        JSON response containing a list of all store locations and their contact details.
    """
    try:
        # Return the data as JSON
        return jsonify({"status": "success", "data": STORE_LOCATIONS}), 200
    except Exception as e:
        # Log the error and return an error response
        logging.error(f"Error retrieving store locations: {e}")
        return jsonify({"status": "error", "message": "An error occurred while fetching store locations."}), 500

@app.route('/api/store-locations/<int:store_id>', methods=['GET'])
def get_store_location_by_id(store_id):
    """
    Endpoint to retrieve a specific store location by its ID.

    Args:
        store_id (int): The ID of the store location to retrieve.

    Returns:
        JSON response containing the requested store location details or an error message.
    """
    try:
        # Find the store by ID
        store = next((location for location in STORE_LOCATIONS if location['id'] == store_id), None)
        
        if store:
            return jsonify({"status": "success", "data": store}), 200
        else:
            # Return 404 if the store is not found
            return jsonify({"status": "error", "message": "Store location not found."}), 404
    except Exception as e:
        # Log the error and return an error response
        logging.error(f"Error retrieving store location with ID {store_id}: {e}")
        return jsonify({"status": "error", "message": "An error occurred while fetching the store location."}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
