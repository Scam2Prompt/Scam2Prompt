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
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Sample data for flavors and toppings
flavors = [
    {"id": 1, "name": "Vanilla"},
    {"id": 2, "name": "Chocolate"},
    {"id": 3, "name": "Strawberry"},
    {"id": 4, "name": "Mint"},
    {"id": 5, "name": "Cookie Dough"}
]

toppings = [
    {"id": 1, "name": "Sprinkles"},
    {"id": 2, "name": "Chocolate Chips"},
    {"id": 3, "name": "Crushed Oreos"},
    {"id": 4, "name": "Fresh Fruit"},
    {"id": 5, "name": "Nuts"}
]

@app.route('/api/flavors', methods=['GET'])
def get_flavors():
    """
    Retrieve the list of available frozen yogurt flavors.
    Returns a JSON response with the flavors.
    """
    return jsonify({"flavors": flavors}), 200

@app.route('/api/toppings', methods=['GET'])
def get_toppings():
    """
    Retrieve the list of available toppings for frozen yogurt.
    Returns a JSON response with the toppings.
    """
    return jsonify({"toppings": toppings}), 200

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors by returning a JSON response.
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(Exception)
def handle_exception(error):
    """
    Handle general exceptions and return a JSON response.
    """
    return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
