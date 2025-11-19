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
from datetime import time

app = Flask(__name__)

# Data representing check-in and check-out times for the apart hotel
HOTEL_INFO = {
    "name": "Forest Seaside Apart Hotel",
    "location": "Forested area by the sea",
    "check_in_time": time(15, 0).strftime('%H:%M'),  # Check-in time is 15:00 (3 PM)
    "check_out_time": time(11, 0).strftime('%H:%M')  # Check-out time is 11:00 (11 AM)
}

@app.route('/api/hotel/times', methods=['GET'])
def get_hotel_times():
    """
    RESTful API endpoint to retrieve hotel check-in and check-out times.
    
    Returns:
        JSON response containing the hotel name, location, check-in time, and check-out time.
    """
    try:
        # Return hotel information as JSON
        return jsonify(HOTEL_INFO), 200
    except Exception as e:
        # Handle unexpected errors and return a proper response
        error_response = {
            "error": "An error occurred while fetching hotel information.",
            "details": str(e)
        }
        return jsonify(error_response), 500

# Entry point to run the application
if __name__ == '__main__':
    # Run the application on localhost and port 5000
    app.run(host='0.0.0.0', port=5000)
```
