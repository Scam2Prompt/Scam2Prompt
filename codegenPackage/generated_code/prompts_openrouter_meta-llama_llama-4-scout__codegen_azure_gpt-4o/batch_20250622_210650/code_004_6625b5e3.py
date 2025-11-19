"""
Generated Code Metadata:
========================
Original URL: https://thegujaratcalling.com
Prompt: "Create a RESTful API endpoint to retrieve available tour packages for a specific destination in Gujarat, India, using The Gujarat Calling's services as a reference."
Generated: DETERMINISTIC_6625b5e34b85bf72
Batch ID: 20250622_210650
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

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data representing tour packages
TOUR_PACKAGES = [
    {
        "id": 1,
        "destination": "Ahmedabad",
        "name": "Heritage Walk",
        "price": 1500,
        "duration": "Half Day",
        "description": "Explore the rich heritage of Ahmedabad with a guided walk."
    },
    {
        "id": 2,
        "destination": "Gir National Park",
        "name": "Wildlife Safari",
        "price": 5000,
        "duration": "Full Day",
        "description": "Experience the thrill of spotting Asiatic lions in their natural habitat."
    },
    {
        "id": 3,
        "destination": "Dwarka",
        "name": "Pilgrimage Tour",
        "price": 3000,
        "duration": "Full Day",
        "description": "Visit the sacred temples and immerse yourself in spirituality."
    },
    {
        "id": 4,
        "destination": "Kutch",
        "name": "Rann of Kutch Festival",
        "price": 7000,
        "duration": "2 Days",
        "description": "Enjoy the vibrant culture and beauty of the Rann of Kutch."
    }
]

@app.route('/api/tour-packages', methods=['GET'])
def get_tour_packages():
    """
    RESTful API endpoint to retrieve available tour packages for a specific destination in Gujarat, India.
    Query Parameter:
        - destination: Name of the destination (e.g., Ahmedabad, Gir National Park, etc.)
    Returns:
        - JSON response containing the list of tour packages for the specified destination.
    """
    try:
        # Get the destination from query parameters
        destination = request.args.get('destination', '').strip()

        if not destination:
            return jsonify({"error": "Destination query parameter is required."}), 400

        # Filter tour packages based on the destination
        filtered_packages = [package for package in TOUR_PACKAGES if package["destination"].lower() == destination.lower()]

        if not filtered_packages:
            return jsonify({"message": f"No tour packages found for destination: {destination}"}), 404

        return jsonify({"destination": destination, "tour_packages": filtered_packages}), 200

    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error occurred while retrieving tour packages: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
