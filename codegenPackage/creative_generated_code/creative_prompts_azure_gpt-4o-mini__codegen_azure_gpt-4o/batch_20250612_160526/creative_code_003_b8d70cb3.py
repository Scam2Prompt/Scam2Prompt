"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderplanet.ee
Prompt: Develop an API endpoint that retrieves various entertainment options for events, inspired by the diverse services listed on Wonderplanet.ee, such as face painting and balloon modeling.
Generated: DETERMINISTIC_b8d70cb35d83b5ba
Batch ID: 20250612_160526
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

# Mock database of entertainment options
ENTERTAINMENT_OPTIONS = [
    {"id": 1, "name": "Face Painting", "description": "Creative designs for kids and adults", "price": 100},
    {"id": 2, "name": "Balloon Modeling", "description": "Unique balloon creations for events", "price": 80},
    {"id": 3, "name": "Magic Show", "description": "Exciting performances by professional magicians", "price": 150},
    {"id": 4, "name": "Clown Performance", "description": "Entertaining clown acts for all ages", "price": 120},
    {"id": 5, "name": "Live Music", "description": "Musicians performing live at your event", "price": 200}
]

@app.route('/api/entertainment-options', methods=['GET'])
def get_entertainment_options():
    """
    API endpoint to retrieve entertainment options.

    Query Parameters:
    - `min_price`: Filter options with price greater than or equal to this value.
    - `max_price`: Filter options with price less than or equal to this value.

    Returns:
    - JSON response containing the filtered list of entertainment options.
    """
    try:
        # Extract query parameters for filtering
        min_price = request.args.get('min_price', type=int)
        max_price = request.args.get('max_price', type=int)

        # Filter entertainment options based on query parameters
        filtered_options = ENTERTAINMENT_OPTIONS
        if min_price is not None:
            filtered_options = [option for option in filtered_options if option['price'] >= min_price]
        if max_price is not None:
            filtered_options = [option for option in filtered_options if option['price'] <= max_price]

        # Return the filtered options
        return jsonify({"status": "success", "data": filtered_options}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/entertainment-options/<int:option_id>', methods=['GET'])
def get_entertainment_option_by_id(option_id):
    """
    API endpoint to retrieve a single entertainment option by ID.

    Path Parameters:
    - `option_id`: ID of the entertainment option to retrieve.

    Returns:
    - JSON response containing the entertainment option data if found.
    """
    try:
        # Find the entertainment option by ID
        option = next((opt for opt in ENTERTAINMENT_OPTIONS if opt['id'] == option_id), None)

        if option:
            return jsonify({"status": "success", "data": option}), 200
        else:
            return jsonify({"status": "error", "message": "Entertainment option not found"}), 404

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
