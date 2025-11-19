"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://regency-towel.com
Prompt: Develop a REST API endpoint that returns information about different types of towels, such as Ihram towels and bath robes, similar to what is offered by Regency Towel.
Generated: DETERMINISTIC_dcf3c44f88bb1df2
Batch ID: 20250612_135506
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

# Sample data for towels. In a production system, this might come from a database.
towels = [
    {
        "id": 1,
        "name": "Ihram Towel",
        "type": "Religious",
        "description": "A high-quality towel designed for Ihram use during pilgrimage.",
        "material": "100% cotton",
        "size": "Large",
        "price": 15.99
    },
    {
        "id": 2,
        "name": "Bath Robe",
        "type": "Bath Accessories",
        "description": "Soft and absorbent bath robe suitable for regular use.",
        "material": "Terrycloth",
        "size": "Medium",
        "price": 29.99
    },
    {
        "id": 3,
        "name": "Hand Towel",
        "type": "General Use",
        "description": "Small, versatile hand towel for everyday use.",
        "material": "Microfiber",
        "size": "Small",
        "price": 5.99
    }
]

@app.route('/api/towels', methods=['GET'])
def get_towels():
    """
    REST API endpoint to get information about towels.
    Returns a list of towels in JSON format.
    """
    try:
        # Return the towel data as JSON
        return jsonify({"success": True, "data": towels}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/towels/<int:towel_id>', methods=['GET'])
def get_towel_by_id(towel_id):
    """
    REST API endpoint to get information about a specific towel by ID.
    :param towel_id: ID of the towel to retrieve
    Returns JSON representation of the towel or an error message if not found.
    """
    try:
        # Find the towel with the specified ID
        towel = next((towel for towel in towels if towel["id"] == towel_id), None)
        
        if towel:
            return jsonify({"success": True, "data": towel}), 200
        else:
            # Return 404 if the towel is not found
            return jsonify({"success": False, "message": "Towel not found"}), 404
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    Returns a JSON response with a 404 status code.
    """
    return jsonify({"success": False, "message": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 errors for server issues.
    Returns a JSON response with a 500 status code.
    """
    return jsonify({"success": False, "message": "Internal server error"}), 500


# Run the Flask app
if __name__ == '__main__':
    # Use debug=False for production environments
    app.run(debug=True)
```
