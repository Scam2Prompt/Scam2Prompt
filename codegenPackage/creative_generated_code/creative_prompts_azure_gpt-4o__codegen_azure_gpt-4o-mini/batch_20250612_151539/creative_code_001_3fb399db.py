"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Generate an API endpoint for retrieving furniture details (e.g., sofas, beds, tables) with attributes like dimensions, color, and price, as described on the Joss Home website.
Generated: DETERMINISTIC_3fb399dbdc3d24e5
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Sample data representing furniture details
furniture_data = [
    {
        "id": 1,
        "type": "sofa",
        "attributes": {
            "dimensions": "78 x 34 x 30 inches",
            "color": "blue",
            "price": 799.99
        }
    },
    {
        "id": 2,
        "type": "bed",
        "attributes": {
            "dimensions": "60 x 80 inches",
            "color": "gray",
            "price": 499.99
        }
    },
    {
        "id": 3,
        "type": "table",
        "attributes": {
            "dimensions": "48 x 30 x 30 inches",
            "color": "brown",
            "price": 299.99
        }
    }
]

@app.route('/api/furniture/<int:furniture_id>', methods=['GET'])
def get_furniture(furniture_id):
    """
    Retrieve furniture details by ID.

    Args:
        furniture_id (int): The ID of the furniture item.

    Returns:
        JSON response with furniture details or an error message.
    """
    # Validate the request ID
    if furniture_id < 1:
        raise BadRequest("Invalid furniture ID. It must be a positive integer.")

    # Search for the furniture item by ID
    furniture_item = next((f for f in furniture_data if f['id'] == furniture_id), None)
    
    if furniture_item is None:
        raise NotFound(f"Furniture with ID {furniture_id} not found.")

    return jsonify(furniture_item)

if __name__ == '__main__':
    # Run the application in debug mode for development purposes
    app.run(debug=True)
```
