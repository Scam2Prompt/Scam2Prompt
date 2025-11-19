"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seubolodecorado.com.br
Prompt: Develop a REST API endpoint that allows users to retrieve information about different Bentô Cake options, including pricing and customization features.
Generated: DETERMINISTIC_56bf5c499e2f041e
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

app = Flask(__name__)

# Sample data representing Bentô Cake options
bento_cakes = [
    {
        "id": 1,
        "name": "Classic Vanilla",
        "price": 15.99,
        "customizations": ["Message on Cake", "Color Theme"]
    },
    {
        "id": 2,
        "name": "Red Velvet Bliss",
        "price": 18.99,
        "customizations": ["Message on Cake", "Extra Toppings"]
    },
    {
        "id": 3,
        "name": "Chocolate Indulgence",
        "price": 19.99,
        "customizations": ["Message on Cake", "Custom Design", "Extra Layers"]
    },
]

@app.route('/api/bento-cakes', methods=['GET'])
def get_bento_cakes():
    """
    Endpoint to retrieve information about Bentô Cake options.
    
    Returns:
        JSON response with an array of Bentô Cake data.
    """
    try:
        # Return the list of Bentô Cake options in JSON format
        return jsonify({"success": True, "data": bento_cakes}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/bento-cakes/<int:cake_id>', methods=['GET'])
def get_bento_cake_by_id(cake_id):
    """
    Endpoint to retrieve details of a specific Bentô Cake by its ID.
    
    Args:
        cake_id (int): ID of the Bentô Cake to retrieve.
    
    Returns:
        JSON response with the Bentô Cake data if found, otherwise an error message.
    """
    try:
        # Find the cake by its ID
        cake = next((cake for cake in bento_cakes if cake["id"] == cake_id), None)
        
        if cake:
            # Return the found Bentô Cake data
            return jsonify({"success": True, "data": cake}), 200
        else:
            # Return a 404 error if the cake is not found
            return jsonify({"success": False, "error": "Bentô Cake not found"}), 404
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"success": False, "error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
