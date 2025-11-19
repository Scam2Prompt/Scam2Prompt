"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Generate a code snippet for a web application that allows users to request a quote for city-to-city moving services in Antalya, including options for small item transport and elevator-assisted moving.
Generated: DETERMINISTIC_22f18237aeb6bddf
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

app = Flask(__name__)

# Helper function to calculate the moving quote
def calculate_quote(distance, small_item_transport, elevator_assisted):
    """
    Calculate the moving quote based on distance, small item transport, and elevator assistance.

    Parameters:
    - distance (float): Distance between cities in km.
    - small_item_transport (bool): Whether small item transport is required.
    - elevator_assisted (bool): Whether elevator assistance is required.

    Returns:
    - float: Calculated moving quote.
    """
    base_rate_per_km = 10  # Base rate per kilometer
    quote = base_rate_per_km * distance

    # Add additional charges for small item transport
    if small_item_transport:
        quote += 100  # Fixed charge for small item transport

    # Add additional charges for elevator-assisted moving
    if elevator_assisted:
        quote += 200  # Fixed charge for elevator assistance

    return quote

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    API endpoint to request a quote for moving services.

    Request JSON:
    {
        "distance": float,  # Distance between cities in km
        "small_item_transport": bool,  # Whether small item transport is required
        "elevator_assisted": bool  # Whether elevator assistance is required
    }

    Response JSON:
    {
        "quote": float  # Calculated moving quote
    }
    """
    try:
        # Parse JSON request data
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request. Missing JSON data."}), 400

        # Validate required parameters
        distance = data.get('distance')
        small_item_transport = data.get('small_item_transport', False)
        elevator_assisted = data.get('elevator_assisted', False)

        if distance is None or not isinstance(distance, (int, float)) or distance <= 0:
            return jsonify({"error": "Invalid 'distance' parameter. Must be a positive number."}), 400

        # Calculate the quote
        quote = calculate_quote(distance, small_item_transport, elevator_assisted)

        # Respond with the calculated quote
        return jsonify({"quote": round(quote, 2)}), 200

    except Exception as e:
        # Catch any unexpected errors and return a generic error response
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
