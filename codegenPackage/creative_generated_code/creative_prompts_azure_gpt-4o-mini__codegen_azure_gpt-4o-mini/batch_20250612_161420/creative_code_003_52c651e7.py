"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://del-pinar.com.ar
Prompt: Develop a RESTful API endpoint that provides information about check-in and check-out times for an apart hotel located in a forested area by the sea.
Generated: DETERMINISTIC_52c651e713222665
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data structure to hold check-in and check-out information
APART_HOTEL_INFO = {
    "location": "Forested area by the sea",
    "check_in": "15:00",  # 3 PM
    "check_out": "11:00"  # 11 AM
}

@app.route('/api/checkin-checkout', methods=['GET'])
def get_check_in_checkout():
    """
    Endpoint to retrieve check-in and check-out times for the apart hotel.
    
    Returns:
        JSON response containing check-in and check-out times along with location.
    """
    try:
        # Prepare the response data
        response_data = {
            "location": APART_HOTEL_INFO["location"],
            "check_in": APART_HOTEL_INFO["check_in"],
            "check_out": APART_HOTEL_INFO["check_out"]
        }
        return jsonify(response_data), 200  # HTTP 200 OK
    except Exception as e:
        # Log the error (in a real application, use a logging framework)
        print(f"Error retrieving check-in and check-out information: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500  # HTTP 500 Internal Server Error

if __name__ == '__main__':
    # Run the Flask application on the default port 5000
    app.run(debug=False)  # Set debug to False for production
```
