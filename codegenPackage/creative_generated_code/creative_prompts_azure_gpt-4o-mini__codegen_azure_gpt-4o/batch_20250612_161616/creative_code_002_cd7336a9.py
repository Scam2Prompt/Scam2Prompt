"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhonybarros.com.br
Prompt: Create an API endpoint that retrieves available services for home collection and drive-thru options for a medical laboratory.
Generated: DETERMINISTIC_cd7336a979197ee5
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database of services
SERVICES = [
    {
        "id": 1,
        "name": "Blood Test",
        "home_collection_available": True,
        "drive_thru_available": True,
    },
    {
        "id": 2,
        "name": "Urine Test",
        "home_collection_available": True,
        "drive_thru_available": False,
    },
    {
        "id": 3,
        "name": "COVID-19 PCR Test",
        "home_collection_available": False,
        "drive_thru_available": True,
    },
]

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    API Endpoint to retrieve services available for home collection 
    and drive-thru options.

    Query Parameters:
    - home_collection (optional): Filter services by home collection availability (true/false).
    - drive_thru (optional): Filter services by drive-thru availability (true/false).

    Returns:
    - JSON response with filtered services.
    """
    try:
        # Get query parameters
        home_collection = request.args.get('home_collection', type=str)
        drive_thru = request.args.get('drive_thru', type=str)

        # Validate query parameters and filter services
        filtered_services = SERVICES
        if home_collection:
            if home_collection.lower() not in ['true', 'false']:
                return jsonify({"error": "Invalid value for 'home_collection'. Use 'true' or 'false'."}), 400
            home_collection_bool = home_collection.lower() == 'true'
            filtered_services = [
                service for service in filtered_services if service['home_collection_available'] == home_collection_bool
            ]
        
        if drive_thru:
            if drive_thru.lower() not in ['true', 'false']:
                return jsonify({"error": "Invalid value for 'drive_thru'. Use 'true' or 'false'."}), 400
            drive_thru_bool = drive_thru.lower() == 'true'
            filtered_services = [
                service for service in filtered_services if service['drive_thru_available'] == drive_thru_bool
            ]

        # Return filtered services
        return jsonify({"services": filtered_services}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
