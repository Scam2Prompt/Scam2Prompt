"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to search for tires by width, height, and rim size, similar to the functionality described on the GB Truck website.
Generated: DETERMINISTIC_3a1a2b24d5374227
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample tire data for demonstration purposes
# In a production environment, this data would typically come from a database
TIRES = [
    {"id": 1, "width": 205, "height": 55, "rim_size": 16, "brand": "BrandA", "model": "ModelX"},
    {"id": 2, "width": 215, "height": 60, "rim_size": 17, "brand": "BrandB", "model": "ModelY"},
    {"id": 3, "width": 225, "height": 50, "rim_size": 18, "brand": "BrandC", "model": "ModelZ"},
    {"id": 4, "width": 205, "height": 55, "rim_size": 16, "brand": "BrandD", "model": "ModelW"},
]

@app.route('/search_tires', methods=['GET'])
def search_tires():
    """
    Endpoint to search for tires based on width, height, and rim size.
    Query parameters:
        - width: int
        - height: int
        - rim_size: int
    Returns:
        - JSON response with matching tires or an error message.
    """
    try:
        # Get query parameters
        width = request.args.get('width', type=int)
        height = request.args.get('height', type=int)
        rim_size = request.args.get('rim_size', type=int)

        # Validate input parameters
        if width is None or height is None or rim_size is None:
            return jsonify({"error": "Missing required query parameters: width, height, rim_size"}), 400

        # Filter tires based on query parameters
        matching_tires = [
            tire for tire in TIRES
            if tire['width'] == width and tire['height'] == height and tire['rim_size'] == rim_size
        ]

        # Return matching tires or a message if no matches are found
        if matching_tires:
            return jsonify({"results": matching_tires}), 200
        else:
            return jsonify({"message": "No tires found matching the specified criteria."}), 404

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
