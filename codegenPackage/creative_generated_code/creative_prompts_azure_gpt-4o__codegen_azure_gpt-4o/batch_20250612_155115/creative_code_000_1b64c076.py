"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ocuvana.com
Prompt: Write code for a product recommendation API that suggests magnetic eyelashes based on user preferences, such as "natural," "blended," or "voluminous," using the features described on Ocuvana's website.
Generated: DETERMINISTIC_1b64c0765d0e2dcf
Batch ID: 20250612_155115
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

# Hardcoded product data for demonstration purposes
PRODUCTS = [
    {"id": 1, "name": "Natural Magnetic Eyelashes", "style": "natural", "description": "Light and subtle magnetic eyelashes for a natural look."},
    {"id": 2, "name": "Blended Magnetic Eyelashes", "style": "blended", "description": "A perfect mix of natural and bold for a balanced look."},
    {"id": 3, "name": "Voluminous Magnetic Eyelashes", "style": "voluminous", "description": "Bold and dramatic magnetic eyelashes for maximum volume."},
]

@app.route('/recommend', methods=['GET'])
def recommend():
    """
    API endpoint to recommend magnetic eyelashes based on user preferences.

    Query parameters:
      - style: (string) user preference for style ("natural", "blended", "voluminous")
    
    Returns:
      - JSON response with recommended products
    """
    try:
        # Get the 'style' parameter from the request
        style = request.args.get('style')
        if not style:
            return jsonify({"error": "Missing 'style' query parameter."}), 400

        # Filter products based on user preference
        recommended_products = [product for product in PRODUCTS if product["style"] == style.lower()]

        # Handle case where no products match the preference
        if not recommended_products:
            return jsonify({"message": "No products found for the specified style."}), 404

        # Return matched products as JSON response
        return jsonify({"recommended_products": recommended_products}), 200

    except Exception as e:
        # Catch and handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
