"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to search for tires by width, height, and rim size, similar to the functionality described on the GB Truck website.
Generated: DETERMINISTIC_3a1a2b24d5374227
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Sample database of tires (This would typically come from a real database)
TIRES_DATABASE = [
    {"width": 205, "height": 55, "rim_size": 16, "model": "Tire A"},
    {"width": 225, "height": 60, "rim_size": 17, "model": "Tire B"},
    {"width": 215, "height": 50, "rim_size": 18, "model": "Tire C"},
    {"width": 195, "height": 65, "rim_size": 15, "model": "Tire D"},
]

@app.route('/search_tires', methods=['GET'])
def search_tires():
    """
    Endpoint to search for tires based on width, height, and rim size.
    Example request: /search_tires?width=205&height=55&rim_size=16
    """
    try:
        # Get query parameters from the request
        width = request.args.get('width', type=int)
        height = request.args.get('height', type=int)
        rim_size = request.args.get('rim_size', type=int)

        # Validate input parameters
        if not width or not height or not rim_size:
            raise BadRequest("Missing query parameters. Please provide width, height, and rim_size.")

        # Filter tires from the database based on the search parameters
        matching_tires = [
            tire for tire in TIRES_DATABASE
            if tire["width"] == width and tire["height"] == height and tire["rim_size"] == rim_size
        ]

        # Return the response
        if matching_tires:
            return jsonify({"status": "success", "data": matching_tires}), 200
        else:
            return jsonify({"status": "success", "data": [], "message": "No matching tires found."}), 200
    except BadRequest as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        # Catch any other unexpected errors
        return jsonify({"status": "error", "message": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
