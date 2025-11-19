"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acess-wallet-stream.blogspot.com
Prompt: Generate a code snippet using Flask to build a simple API that serves details about Cervejaria Montez's location and operating hours.
Generated: DETERMINISTIC_b80d4285dcfb72db
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Data for Cervejaria Montez
cervejaria_details = {
    "name": "Cervejaria Montez",
    "location": "123 Beer Street, Porto Alegre, RS, Brazil",
    "operating_hours": {
        "Monday-Friday": "5:00 PM - 12:00 AM",
        "Saturday": "3:00 PM - 1:00 AM",
        "Sunday": "Closed"
    }
}

@app.route('/api/cervejaria', methods=['GET'])
def get_cervejaria_details():
    """
    Endpoint to get details about Cervejaria Montez.
    Returns JSON data containing the name, location, and operating hours.
    """
    return jsonify({
        "status": "success",
        "data": cervejaria_details
    }), 200  # HTTP 200 OK for successful response

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 - Not Found.
    """
    return jsonify({
        "status": "error",
        "message": "Resource not found"
    }), 404  # HTTP 404 Not Found

@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 - Internal Server Error.
    """
    return jsonify({
        "status": "error",
        "message": "An internal server error occurred"
    }), 500  # HTTP 500 Internal Server Error

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)  # Host and port can be configured as needed
```
