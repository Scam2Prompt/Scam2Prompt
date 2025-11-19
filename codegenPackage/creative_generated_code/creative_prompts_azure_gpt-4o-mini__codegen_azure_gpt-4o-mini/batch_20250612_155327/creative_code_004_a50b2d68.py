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
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)

# Sample data for coat racks delivery timeline and installation services
coat_racks_info = {
    1: {
        "name": "Classic Coat Rack",
        "delivery_timeline": "3-5 business days",
        "installation_service": True,
        "installation_details": "Professional installation available for $50."
    },
    2: {
        "name": "Modern Coat Rack",
        "delivery_timeline": "5-7 business days",
        "installation_service": True,
        "installation_details": "Self-installation guide provided. Professional installation for $75."
    },
    3: {
        "name": "Vintage Coat Rack",
        "delivery_timeline": "7-10 business days",
        "installation_service": False,
        "installation_details": "No installation service available."
    }
}

@app.route('/api/coat_racks/<int:coat_rack_id>', methods=['GET'])
def get_coat_rack_info(coat_rack_id):
    """
    Retrieve information about a specific coat rack's delivery timeline and installation services.

    :param coat_rack_id: ID of the coat rack
    :return: JSON response containing coat rack details
    """
    # Error handling for invalid coat rack ID
    if coat_rack_id not in coat_racks_info:
        raise NotFound(f"Coat rack with ID {coat_rack_id} not found.")

    # Retrieve the coat rack information
    coat_rack = coat_racks_info[coat_rack_id]

    return jsonify(coat_rack)

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle bad request errors."""
    response = jsonify({'error': 'Bad Request', 'message': str(error)})
    response.status_code = 400
    return response

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle not found errors."""
    response = jsonify({'error': 'Not Found', 'message': str(error)})
    response.status_code = 404
    return response

if __name__ == '__main__':
    # Run the application on the default Flask port
    app.run(debug=True)
```
