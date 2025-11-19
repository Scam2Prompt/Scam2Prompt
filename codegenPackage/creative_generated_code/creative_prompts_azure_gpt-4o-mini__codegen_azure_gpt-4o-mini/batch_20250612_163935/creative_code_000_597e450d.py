"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate a code snippet for an e-commerce application that lists various sports equipment like "Beach Vôlei" and "Basquete" with pricing and availability.
Generated: DETERMINISTIC_597e450dd7e1d37b
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing sports equipment in the inventory
inventory = [
    {
        "id": 1,
        "name": "Beach Vôlei",
        "price": 29.99,
        "available": True
    },
    {
        "id": 2,
        "name": "Basquete",
        "price": 24.99,
        "available": True
    },
    {
        "id": 3,
        "name": "Futebol",
        "price": 19.99,
        "available": False
    },
]

@app.route('/equipment', methods=['GET'])
def list_equipment():
    """
    Endpoint to list all sports equipment with their pricing and availability.
    Returns a JSON response with the inventory data.
    """
    try:
        return jsonify(inventory), 200  # Return the inventory data with a success status
    except Exception as e:
        # Handle unexpected errors by logging them and returning a 500 status
        app.logger.error(f"Error occurred while fetching equipment: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```
