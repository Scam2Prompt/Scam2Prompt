"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Generate a code snippet for a web application that allows users to request a quote for Ataköy Evden Eve Nakliyat services, including options for city and intercity moves.
Generated: DETERMINISTIC_11154b4e2460c8cb
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample pricing data for city and intercity moves
PRICING = {
    "city": 500,  # Base price for city moves
    "intercity": 1500  # Base price for intercity moves
}

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to request a quote for Ataköy Evden Eve Nakliyat services.
    Accepts JSON payload with 'move_type' and 'details'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request. Please provide JSON data."}), 400

        # Validate required fields
        move_type = data.get('move_type')
        details = data.get('details')  # Additional details about the move (optional)

        if move_type not in ['city', 'intercity']:
            return jsonify({"error": "Invalid move_type. Must be 'city' or 'intercity'."}), 400

        # Calculate the quote based on move type
        base_price = PRICING[move_type]
        quote = {
            "move_type": move_type,
            "base_price": base_price,
            "details": details or "No additional details provided."
        }

        return jsonify({"quote": quote}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
