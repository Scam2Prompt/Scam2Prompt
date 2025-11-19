"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shahkarco.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of coat racks with pricing and special offers, similar to those found on Shahkar Industry's product page.
Generated: DETERMINISTIC_8cd2199e94bb7f14
Batch ID: 20250612_155327
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

# Mock data for coat racks
coat_racks = [
    {
        "id": 1,
        "name": "Wooden Coat Rack",
        "price": 49.99,
        "special_offer": "10% off for orders above $100",
        "description": "A durable, elegant wooden coat rack perfect for any home."
    },
    {
        "id": 2,
        "name": "Metal Coat Rack",
        "price": 39.99,
        "special_offer": "Free shipping on this item",
        "description": "A sturdy metal coat rack with a modern design."
    },
    {
        "id": 3,
        "name": "Wall-Mounted Coat Rack",
        "price": 24.99,
        "special_offer": "Buy 2, get 1 free",
        "description": "Space-saving wall-mounted coat rack."
    }
]

@app.route('/coat-racks', methods=['GET'])
def get_coat_racks():
    """
    Endpoint to retrieve available coat racks with pricing and special offers.
    Returns:
        JSON response containing the list of coat racks.
    """
    try:
        # Return JSON response with coat rack data
        response = {
            "status": "success",
            "data": coat_racks
        }
        return jsonify(response), 200
    except Exception as e:
        # Log the error (production systems should use a logging framework) and return error response
        error_response = {
            "status": "error",
            "message": "Something went wrong while fetching coat racks.",
            "details": str(e)
        }
        return jsonify(error_response), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
