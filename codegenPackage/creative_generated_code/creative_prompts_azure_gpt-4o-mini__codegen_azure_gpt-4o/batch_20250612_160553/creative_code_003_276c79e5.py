"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logingalagames-io.blogspot.com
Prompt: Create an API endpoint for fetching furniture items with specific attributes like color and type, inspired by the product listings on Móveis Campo Largo.
Generated: DETERMINISTIC_276c79e501dccd1a
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing furniture items
furniture_items = [
    {"id": 1, "name": "Wooden Chair", "type": "chair", "color": "brown"},
    {"id": 2, "name": "Metal Table", "type": "table", "color": "black"},
    {"id": 3, "name": "Leather Sofa", "type": "sofa", "color": "white"},
    {"id": 4, "name": "Plastic Stool", "type": "stool", "color": "red"},
    {"id": 5, "name": "Glass Coffee Table", "type": "table", "color": "transparent"},
]

@app.route('/api/furniture', methods=['GET'])
def get_furniture():
    """
    API endpoint to fetch furniture items filtered by specific attributes.
    Query parameters:
        - type: Type of furniture (e.g., chair, table, sofa, etc.)
        - color: Color of the furniture (e.g., brown, black, white, etc.)
    Response:
        - JSON list of furniture items matching the filters.
    """
    try:
        # Get query parameters for filtering
        furniture_type = request.args.get('type')
        furniture_color = request.args.get('color')

        # Filter based on the provided parameters
        filtered_items = [
            item for item in furniture_items
            if (not furniture_type or item['type'].lower() == furniture_type.lower()) and
               (not furniture_color or item['color'].lower() == furniture_color.lower())
        ]

        # Return the filtered list as JSON response
        return jsonify(filtered_items), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    """
    return jsonify({"error": e.description}), e.code

@app.errorhandler(404)
def handle_not_found_error(e):
    """
    Handle 404 errors with a custom message.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def handle_internal_server_error(e):
    """
    Handle 500 errors with a custom message.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code provides a production-ready API endpoint for filtering furniture items based on type and color attributes. It includes error handling, comments, and adheres to best practices for Flask development.
