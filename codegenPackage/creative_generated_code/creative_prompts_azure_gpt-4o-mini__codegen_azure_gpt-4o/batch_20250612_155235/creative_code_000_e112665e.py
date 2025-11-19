"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Generate a code snippet for an API that integrates air freight services for import and export using the logistics features described by Daimon Logistics.
Generated: DETERMINISTIC_e112665ef11c7cc9
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample mock data for air freight services (replace with actual integration later)
AIR_FREIGHT_DATA = {
    "import": [
        {"tracking_id": "IMP001", "status": "In Transit", "origin": "Shanghai", "destination": "New York"},
        {"tracking_id": "IMP002", "status": "Delivered", "origin": "London", "destination": "Los Angeles"}
    ],
    "export": [
        {"tracking_id": "EXP001", "status": "In Transit", "origin": "New York", "destination": "Tokyo"},
        {"tracking_id": "EXP002", "status": "Pending Pickup", "origin": "Los Angeles", "destination": "Dubai"}
    ],
}

@app.route('/api/airfreight', methods=['GET'])
def get_air_freight_data():
    """
    Endpoint to retrieve air freight data for import and export.
    Query params:
        type: 'import' or 'export'
    Returns:
        JSON response with air freight details.
    """
    try:
        freight_type = request.args.get('type', '').lower()
        
        if freight_type not in ['import', 'export']:
            return jsonify({"error": "Invalid type. Please specify 'import' or 'export'."}), 400
        
        return jsonify(AIR_FREIGHT_DATA[freight_type])
    except Exception as e:
        # Log the error and return an appropriate response
        logging.error(f"Error fetching air freight data: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/api/airfreight', methods=['POST'])
def add_air_freight_data():
    """
    Endpoint to add a new air freight record.
    Expecting JSON payload:
        {
            "type": "import" or "export",
            "tracking_id": "string",
            "status": "string",
            "origin": "string",
            "destination": "string"
        }
    Returns:
        JSON response with success or error message.
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Request payload is empty or invalid."}), 400
        
        # Validate required keys
        required_keys = ["type", "tracking_id", "status", "origin", "destination"]
        for key in required_keys:
            if key not in data:
                return jsonify({"error": f"Missing key: {key}"}), 400

        freight_type = data['type'].lower()
        if freight_type not in ['import', 'export']:
            return jsonify({"error": "Invalid type. Please specify 'import' or 'export'."}), 400

        # Add data to the corresponding freight type
        AIR_FREIGHT_DATA[freight_type].append({
            "tracking_id": data["tracking_id"],
            "status": data["status"],
            "origin": data["origin"],
            "destination": data["destination"]
        })

        return jsonify({"message": "Air freight data added successfully."}), 201
    except Exception as e:
        # Log the error for debugging and return an error response
        logging.error(f"Error adding air freight data: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/api/airfreight/<tracking_id>', methods=['DELETE'])
def delete_air_freight_data(tracking_id):
    """
    Endpoint to delete an air freight record by tracking ID.
    URL param:
        tracking_id: ID of the record to be deleted.
    Returns:
        JSON response with success or error message.
    """
    try:
        found = False
        for freight_type in ['import', 'export']:
            for record in AIR_FREIGHT_DATA[freight_type]:
                if record["tracking_id"] == tracking_id:
                    AIR_FREIGHT_DATA[freight_type].remove(record)
                    found = True
                    break

        if not found:
            return jsonify({"error": "Tracking ID not found."}), 404

        return jsonify({"message": "Air freight record deleted successfully."}), 200
    except Exception as e:
        # Log the error for debugging and return an error response
        logging.error(f"Error deleting air freight data: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom handler for 500 errors.
    """
    return jsonify({"error": "Internal server error."}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
