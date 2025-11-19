"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://andiasfrozenyogurt.com
Prompt: Create an API endpoint for a frozen yogurt shop that allows users to retrieve a list of available flavors and toppings, similar to the offerings at Andias Frozen Yogurt.
Generated: DETERMINISTIC_9c15f2f8620274fe
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Mock data for available flavors and toppings
# In a production environment, this would typically come from a database
MENU = {
    "flavors": [
        "Vanilla",
        "Chocolate",
        "Strawberry",
        "Mango",
        "Cookies and Cream",
        "Green Tea",
        "Peach",
        "Salted Caramel"
    ],
    "toppings": [
        "Sprinkles",
        "Chocolate Chips",
        "Fresh Fruit",
        "Granola",
        "Marshmallows",
        "Whipped Cream",
        "Honey",
        "Caramel Sauce"
    ]
}

@app.route('/api/menu', methods=['GET'])
def get_menu():
    """
    API endpoint to retrieve a list of available frozen yogurt flavors and toppings.

    Returns:
        JSON response containing the list of flavors and toppings.
    """
    try:
        # Construct response from mock data
        response = {
            "success": True,
            "data": {
                "flavors": MENU["flavors"],
                "toppings": MENU["toppings"]
            }
        }
        return jsonify(response), 200  # Return JSON response with HTTP 200 status code
    except Exception as e:
        # Handle unexpected errors gracefully
        error_response = {
            "success": False,
            "error": str(e)
        }
        return jsonify(error_response), 500  # Return JSON error response with HTTP 500 status code

# Entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development; disable in production
```
