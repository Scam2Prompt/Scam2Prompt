"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Create a REST API endpoint that provides pricing quotes for densified EPS Styrofoam based on the specifications of the XT400 densifier.
Generated: DETERMINISTIC_e66b92779a04863c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define pricing constants based on densified EPS Styrofoam properties
PRICE_PER_KG = 1.75  # Example rate ($ per kg)
DENSITY = 400  # XT400 densifier density in kg/m^3

@app.route('/api/v1/quote', methods=['GET'])
def get_pricing_quote():
    """
    REST API endpoint to get pricing quotes for densified EPS Styrofoam.
    Example request: /api/v1/quote?volume=5
    """
    try:
        # Extract 'volume' parameter from query string
        volume = request.args.get('volume', type=float)

        # Validate input
        if volume is None or volume <= 0:
            return jsonify({
                "error": "Invalid volume parameter. It must be a positive number."
            }), 400

        # Calculate weight based on volume and density
        weight = volume * DENSITY

        # Calculate pricing
        total_price = weight * PRICE_PER_KG

        # Return the quote
        response = {
            "volume_m3": volume,
            "weight_kg": weight,
            "price_usd": round(total_price, 2)
        }
        logging.info(f"Quote generated: {response}")
        return jsonify(response), 200
    except Exception as e:
        logging.error(f"Error generating quote: {str(e)}")
        return jsonify({
            "error": "An unexpected error occurred while calculating the quote."
        }), 500

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for invalid routes.
    """
    return jsonify({
        "error": "Endpoint not found."
    }), 404

# Run the Flask application (for development purposes only)
if __name__ == '__main__':
    app.run(debug=True)  # Note: Disable debug mode in production
```
