"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rawcakesandcandy.ro
Prompt: Create an API endpoint for an online bakery that allows users to customize their vegan cake orders, including size, flavor, and decorations, inspired by the offerings of Raw Cakes And Candy SRL.
Generated: DETERMINISTIC_6dc4d1528d0c306e
Batch ID: 20250612_161520
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/customize-cake`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# List of valid options for customization
VALID_SIZES = ["small", "medium", "large"]
VALID_FLAVORS = ["chocolate", "vanilla", "strawberry", "lemon", "carrot"]
VALID_DECORATIONS = ["nuts", "berries", "frosting", "edible flowers", "chocolate shavings"]

@app.route('/customize-cake', methods=['POST'])
def customize_cake():
    """
    API endpoint to customize a vegan cake order.
    Accepts 'size', 'flavor', and 'decorations' as parameters in the request JSON.
    Returns the details of the custom cake if valid, otherwise returns an error.
    """

    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid input. Please provide a JSON object."}), 400

        size = data.get("size")
        flavor = data.get("flavor")
        decorations = data.get("decorations")

        # Validate 'size'
        if size not in VALID_SIZES:
            return jsonify({"error": f"Invalid size. Valid options are {VALID_SIZES}."}), 400

        # Validate 'flavor'
        if flavor not in VALID_FLAVORS:
            return jsonify({"error": f"Invalid flavor. Valid options are {VALID_FLAVORS}."}), 400

        # Validate 'decorations'
        if decorations:
            if not isinstance(decorations, list):
                return jsonify({"error": "Decorations must be a list of strings."}), 400

            invalid_decorations = [decor for decor in decorations if decor not in VALID_DECORATIONS]
            if invalid_decorations:
                return jsonify({"error": f"Invalid decorations: {invalid_decorations}. Valid options are {VALID_DECORATIONS}."}), 400

        # If validation is passed, return the customized cake details
        cake_details = {
            "size": size,
            "flavor": flavor,
            "decorations": decorations if decorations else []
        }

        return jsonify({
            "message": "Your vegan cake has been successfully customized!",
            "cake_details": cake_details
        }), 200

    except Exception as e:
        # Catch unexpected errors and return a message
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5000)
```

To use this endpoint:
1. Start the Flask server by running the script.
2. Send a POST request to `http://localhost:5000/customize-cake` with a JSON body containing `size`, `flavor`, and optional `decorations`. Example:

```json
{
    "size": "medium",
    "flavor": "chocolate",
    "decorations": ["nuts", "berries"]
}
```
