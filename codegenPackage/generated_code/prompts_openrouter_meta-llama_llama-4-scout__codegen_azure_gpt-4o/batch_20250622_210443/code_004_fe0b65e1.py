"""
Generated Code Metadata:
========================
Original URL: https://safargenie.com
Prompt: "Create a RESTful API for retrieving information about tour packages in Nepal, including Muktinath tour packages and Chardham Yatra packages, with filtering and sorting capabilities."
Generated: DETERMINISTIC_fe0b65e1adc4c452
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data for tour packages
TOUR_PACKAGES = [
    {"id": 1, "name": "Muktinath Tour Package", "location": "Nepal", "price": 500, "duration": 5},
    {"id": 2, "name": "Chardham Yatra Package", "location": "India", "price": 800, "duration": 10},
    {"id": 3, "name": "Everest Base Camp Trek", "location": "Nepal", "price": 1200, "duration": 14},
    {"id": 4, "name": "Annapurna Circuit Trek", "location": "Nepal", "price": 1000, "duration": 12},
]

@app.route('/api/tour-packages', methods=['GET'])
def get_tour_packages():
    """
    Endpoint to retrieve tour packages with optional filtering and sorting.
    Query Parameters:
        - location: Filter by location (e.g., 'Nepal')
        - min_price: Filter by minimum price
        - max_price: Filter by maximum price
        - sort_by: Sort by a field (e.g., 'price', 'duration')
        - order: Sort order ('asc' or 'desc')
    """
    try:
        # Get query parameters
        location = request.args.get('location')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        sort_by = request.args.get('sort_by')
        order = request.args.get('order', 'asc')

        # Filter tour packages
        filtered_packages = TOUR_PACKAGES
        if location:
            filtered_packages = [pkg for pkg in filtered_packages if pkg['location'].lower() == location.lower()]
        if min_price is not None:
            filtered_packages = [pkg for pkg in filtered_packages if pkg['price'] >= min_price]
        if max_price is not None:
            filtered_packages = [pkg for pkg in filtered_packages if pkg['price'] <= max_price]

        # Sort tour packages
        if sort_by:
            reverse = (order == 'desc')
            filtered_packages = sorted(filtered_packages, key=lambda x: x.get(sort_by, 0), reverse=reverse)

        return jsonify({"status": "success", "data": filtered_packages}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Handle HTTP exceptions and return JSON responses.
    """
    return jsonify({"status": "error", "message": e.description}), e.code

@app.errorhandler(404)
def handle_404(e):
    """
    Handle 404 errors specifically.
    """
    return jsonify({"status": "error", "message": "Resource not found"}), 404

@app.errorhandler(500)
def handle_500(e):
    """
    Handle 500 errors specifically.
    """
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
