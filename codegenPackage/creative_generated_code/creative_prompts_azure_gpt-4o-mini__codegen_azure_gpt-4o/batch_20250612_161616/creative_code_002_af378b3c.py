"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://divinecollections.net
Prompt: Create an API endpoint that retrieves a list of Bharatanatyam costume items available for purchase, including details like price and availability.
Generated: DETERMINISTIC_af378b3cc9bb84f1
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
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing Bharatanatyam costume items
costume_items = [
    {"id": 1, "name": "Traditional Silk Costume", "price": 120.00, "availability": "In Stock"},
    {"id": 2, "name": "Temple Jewelry Set", "price": 75.00, "availability": "In Stock"},
    {"id": 3, "name": "Ankle Bells", "price": 25.00, "availability": "Out of Stock"},
    {"id": 4, "name": "Hair Accessories", "price": 15.00, "availability": "In Stock"},
]

# Error handler for custom exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.name, "message": e.description}), e.code
    return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500

@app.route('/api/costume-items', methods=['GET'])
def get_costume_items():
    """
    API endpoint to retrieve a list of Bharatanatyam costume items.
    Returns:
        JSON response containing costume items with details like price and availability.
    """
    try:
        # Returning the list of costume items as a JSON response
        return jsonify({"status": "success", "data": costume_items}), 200
    except Exception as ex:
        # Handle any unexpected exception
        return jsonify({"status": "error", "message": str(ex)}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
