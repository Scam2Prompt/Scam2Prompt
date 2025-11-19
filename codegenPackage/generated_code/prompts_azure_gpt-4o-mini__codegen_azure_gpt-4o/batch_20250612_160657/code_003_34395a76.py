"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Develop an API endpoint that provides details about the types of cookware available at Varejão das Louças, including options for restaurants and hotels.
Generated: DETERMINISTIC_34395a76dd3887cd
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing cookware options
cookware_data = [
    {
        "id": 1,
        "name": "Non-stick Frying Pan",
        "type": "restaurant",
        "material": "aluminum",
        "price": 25.99
    },
    {
        "id": 2,
        "name": "Cast Iron Skillet",
        "type": "hotel",
        "material": "cast iron",
        "price": 45.50
    },
    {
        "id": 3,
        "name": "Stainless Steel Saucepan",
        "type": "restaurant",
        "material": "stainless steel",
        "price": 30.00
    },
    {
        "id": 4,
        "name": "Ceramic Baking Dish",
        "type": "hotel",
        "material": "ceramic",
        "price": 20.75
    }
]

@app.route('/api/cookware', methods=['GET'])
def get_cookware():
    """
    API endpoint to retrieve cookware details.
    Query parameters:
        type (optional): Filter cookware by type (e.g., 'restaurant', 'hotel').
    Returns:
        JSON response containing cookware details.
    """
    try:
        # Get optional query parameter 'type'
        cookware_type = request.args.get('type', None)

        # Filter cookware data based on type if provided
        if cookware_type:
            filtered_cookware = [item for item in cookware_data if item['type'] == cookware_type.lower()]
        else:
            filtered_cookware = cookware_data

        # Return the filtered cookware data as JSON
        return jsonify({
            "success": True,
            "data": filtered_cookware
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "success": False,
            "error": "An error occurred while processing your request.",
            "details": str(e)
        }), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
