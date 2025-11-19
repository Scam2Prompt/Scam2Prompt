"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Develop a RESTful API endpoint that allows users to submit their moving requirements and receive a tailored quote for Antalya's city moving services.
Generated: DETERMINISTIC_032919fa0da93407
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

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample pricing logic based on moving details
def calculate_quote(distance, weight, number_of_items):
    """
    Calculate the moving service quote based on distance, weight, and number of items.
    :param distance: Distance of the move in kilometers
    :param weight: Total weight of items in kilograms
    :param number_of_items: Number of items to be moved
    :return: Calculated quote amount in local currency
    """
    base_price = 100  # Base price in local currency
    distance_price = distance * 2  # Price per kilometer
    weight_price = weight * 0.5  # Price per kilogram
    items_price = number_of_items * 1  # Price per item
    return base_price + distance_price + weight_price + items_price


@app.route('/api/moving-quote', methods=['POST'])
def get_moving_quote():
    """
    API endpoint to calculate and return a moving quote based on user-provided details.
    :return: JSON response with the calculated quote or an error message.
    """
    try:
        # Parse request JSON data
        data = request.json
        if not data:
            return jsonify({'error': 'Request must contain JSON data'}), 400

        # Validate required parameters
        distance = data.get('distance')
        weight = data.get('weight')
        number_of_items = data.get('number_of_items')

        if distance is None or weight is None or number_of_items is None:
            return jsonify({'error': 'Missing required parameters: distance, weight, number_of_items'}), 400

        # Ensure values are positive
        if distance <= 0 or weight <= 0 or number_of_items <= 0:
            return jsonify({'error': 'Parameters must be positive values'}), 400

        # Calculate quote
        quote = calculate_quote(distance, weight, number_of_items)

        # Return quote as JSON response
        return jsonify({'quote': quote, 'currency': 'TRY'}), 200

    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error while processing moving quote: {e}")
        return jsonify({'error': 'An unexpected error occurred. Please try again.'}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
