"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plataforma-aceess.blogspot.com
Prompt: Develop a RESTful API endpoint that allows users to search for wholesale clothing items, specifically targeting colorful shirts and blouses.
Generated: DETERMINISTIC_b209fd2320e75bf6
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data: Sample inventory of colorful clothing items
inventory = [
    {"id": 1, "type": "shirt", "color": "red", "size": "M", "price": 15.99},
    {"id": 2, "type": "blouse", "color": "blue", "size": "L", "price": 18.99},
    {"id": 3, "type": "shirt", "color": "green", "size": "S", "price": 12.99},
    {"id": 4, "type": "blouse", "color": "yellow", "size": "M", "price": 16.99},
    {"id": 5, "type": "shirt", "color": "purple", "size": "XL", "price": 20.99},
]

@app.route('/search', methods=['GET'])
def search_clothing():
    """
    Endpoint to search for colorful shirts and blouses.
    Query parameters:
        - type: Filter by clothing type (e.g., 'shirt' or 'blouse')
        - color: Filter by color (e.g., 'red', 'blue', etc.)
    Returns:
        JSON response containing matching clothing items.
    """
    try:
        # Get query parameters
        clothing_type = request.args.get('type', '').lower()
        color = request.args.get('color', '').lower()

        # Validate query parameters
        if not clothing_type and not color:
            return jsonify({"error": "At least one filter ('type' or 'color') must be provided."}), 400

        # Filter inventory based on query parameters
        results = [
            item for item in inventory
            if (not clothing_type or item['type'] == clothing_type)
            and (not color or item['color'] == color)
        ]

        # Return results
        return jsonify({"results": results, "count": len(results)}), 200

    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
