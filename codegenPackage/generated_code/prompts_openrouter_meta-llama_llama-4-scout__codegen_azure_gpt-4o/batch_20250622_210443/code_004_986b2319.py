"""
Generated Code Metadata:
========================
Original URL: https://maskatiyasgroup.com
Prompt: Design a RESTful API for retrieving information about different mobile LCD displays, including their specifications, prices, and availability, from Maskatiyas Group's product catalog.
Generated: DETERMINISTIC_986b23197b659cc1
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data for mobile LCD displays
lcd_displays = [
    {
        "id": 1,
        "name": "LCD Display A",
        "resolution": "1080x1920",
        "size": "5.5 inches",
        "price": 120.00,
        "availability": "In Stock"
    },
    {
        "id": 2,
        "name": "LCD Display B",
        "resolution": "720x1280",
        "size": "5.0 inches",
        "price": 80.00,
        "availability": "Out of Stock"
    },
    {
        "id": 3,
        "name": "LCD Display C",
        "resolution": "1440x2560",
        "size": "6.0 inches",
        "price": 200.00,
        "availability": "In Stock"
    }
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Route to retrieve all LCD displays
@app.route('/api/lcd-displays', methods=['GET'])
def get_all_lcd_displays():
    """
    Retrieve all LCD displays from the catalog.
    """
    return jsonify(lcd_displays), 200

# Route to retrieve a specific LCD display by ID
@app.route('/api/lcd-displays/<int:display_id>', methods=['GET'])
def get_lcd_display_by_id(display_id):
    """
    Retrieve a specific LCD display by its ID.
    """
    display = next((item for item in lcd_displays if item["id"] == display_id), None)
    if display is None:
        return jsonify({
            "error": "Not Found",
            "message": f"LCD display with ID {display_id} not found."
        }), 404
    return jsonify(display), 200

# Route to search LCD displays by name
@app.route('/api/lcd-displays/search', methods=['GET'])
def search_lcd_displays():
    """
    Search LCD displays by name.
    """
    query = request.args.get('name', '').lower()
    if not query:
        return jsonify({
            "error": "Bad Request",
            "message": "Query parameter 'name' is required."
        }), 400
    results = [item for item in lcd_displays if query in item["name"].lower()]
    return jsonify(results), 200

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
