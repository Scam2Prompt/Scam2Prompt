"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shahkarco.com
Prompt: Design an API endpoint that provides information on the delivery timeline and installation services for coat racks, similar to the offerings by Shahkar Industry.
Generated: DETERMINISTIC_a50b2d6847d2634c
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

# Mock database for coat racks delivery and installation information
coat_racks_data = [
    {
        "id": 1,
        "name": "Premium Wooden Coat Rack",
        "delivery_time_days": 5,
        "installation_available": True,
        "installation_cost": 50.0
    },
    {
        "id": 2,
        "name": "Metallic Coat Rack Stand",
        "delivery_time_days": 7,
        "installation_available": False,
        "installation_cost": 0.0
    },
    {
        "id": 3,
        "name": "Wall-Mounted Coat Rack",
        "delivery_time_days": 3,
        "installation_available": True,
        "installation_cost": 30.0
    }
]

@app.route('/api/coat-racks', methods=['GET'])
def get_coat_racks():
    """
    API endpoint to fetch all coat racks delivery and installation information.

    Returns:
        JSON response containing the list of coat racks and their details.
    """
    try:
        # Return the coat racks data as JSON response
        return jsonify({"coat_racks": coat_racks_data}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while fetching the data.", "details": str(e)}), 500


@app.route('/api/coat-racks/<int:coat_rack_id>', methods=['GET'])
def get_coat_rack_details(coat_rack_id):
    """
    API endpoint to fetch specific coat rack delivery and installation information.

    Args:
        coat_rack_id (int): ID of the coat rack.

    Returns:
        JSON response containing the details of the requested coat rack.
    """
    try:
        # Find the coat rack by ID
        coat_rack = next((item for item in coat_racks_data if item['id'] == coat_rack_id), None)
        
        if coat_rack is None:
            # Return a 404 response if the coat rack is not found
            return jsonify({"error": "Coat rack not found."}), 404
        
        # Return the coat rack data as JSON response
        return jsonify({"coat_rack": coat_rack}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while fetching the data.", "details": str(e)}), 500


@app.route('/api/coat-racks/estimate-delivery-date', methods=['POST'])
def estimate_delivery_date():
    """
    API endpoint to estimate the delivery date for a given coat rack.

    Request Body:
        coat_rack_id (int): ID of the coat rack.

    Returns:
        JSON response containing the estimated delivery date.
    """
    try:
        # Parse the request JSON body
        data = request.get_json()
        coat_rack_id = data.get("coat_rack_id")
        
        # Validate input
        if coat_rack_id is None:
            return jsonify({"error": "coat_rack_id is required in the request body."}), 400
        
        # Find the coat rack by ID
        coat_rack = next((item for item in coat_racks_data if item['id'] == coat_rack_id), None)
        
        if coat_rack is None:
            # Return a 404 response if the coat rack is not found
            return jsonify({"error": "Coat rack not found."}), 404
        
        # Calculate the estimated delivery date
        current_date = datetime.date.today()
        estimated_delivery_date = current_date + datetime.timedelta(days=coat_rack["delivery_time_days"])
        
        # Return the estimated delivery date as JSON response
        return jsonify({"coat_rack": coat_rack, "estimated_delivery_date": estimated_delivery_date.isoformat()}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while estimating the delivery date.", "details": str(e)}), 500


# Entry point for running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
