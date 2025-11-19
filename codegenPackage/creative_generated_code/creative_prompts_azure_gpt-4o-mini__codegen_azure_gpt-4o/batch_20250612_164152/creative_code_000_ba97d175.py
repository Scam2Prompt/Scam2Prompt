"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: Generate a code snippet for an e-commerce website that allows users to purchase comic volumes, specifically for a series like "Top G" that features complex narratives and character development.
Generated: DETERMINISTIC_ba97d175d2348222
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask app for handling comic volume purchases for an e-commerce website

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Logging setup for production
logging.basicConfig(level=logging.INFO)

# Sample comic database (mocked for demonstration purposes)
COMIC_SERIES = {
    "Top G": {
        "volumes": {
            1: {"title": "Origins", "price": 10.99, "stock": 5},
            2: {"title": "Rise of Legends", "price": 12.99, "stock": 3},
            3: {"title": "Endgame", "price": 15.99, "stock": 0},  # Out of stock
        }
    }
}

@app.route('/purchase', methods=['POST'])
def purchase_comic_volume():
    """
    Endpoint to purchase a comic volume.
    Expects JSON input with 'series_name', 'volume_number', and 'quantity'.
    Example request:
    {
        "series_name": "Top G",
        "volume_number": 2,
        "quantity": 1
    }
    """
    try:
        # Parse request JSON
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. JSON data expected."}), 400
        
        series_name = data.get('series_name')
        volume_number = data.get('volume_number')
        quantity = data.get('quantity', 1)

        # Validate input
        if not series_name or not volume_number or quantity < 1:
            return jsonify({"error": "Invalid input. Please provide 'series_name', 'volume_number', and a valid 'quantity'."}), 400

        # Check if series exists
        series = COMIC_SERIES.get(series_name)
        if not series:
            return jsonify({"error": f"Series '{series_name}' not found."}), 404

        # Check if volume exists
        volume = series['volumes'].get(volume_number)
        if not volume:
            return jsonify({"error": f"Volume {volume_number} not found in series '{series_name}'."}), 404

        # Check stock availability
        if volume['stock'] < quantity:
            if volume['stock'] == 0:
                return jsonify({"error": f"Volume {volume_number} of '{series_name}' is out of stock."}), 400
            return jsonify({"error": f"Only {volume['stock']} copies of Volume {volume_number} are available."}), 400

        # Process purchase
        volume['stock'] -= quantity
        total_price = volume['price'] * quantity

        logging.info(f"User purchased {quantity} copy/copies of '{series_name}' Volume {volume_number}. Total: ${total_price:.2f}")
        
        return jsonify({
            "message": f"Successfully purchased {quantity} copy/copies of '{series_name}' Volume {volume_number}.",
            "total_price": f"${total_price:.2f}",
            "remaining_stock": volume['stock']
        }), 200

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the Flask app
if __name__ == '__main__':
    # Production server would use a WSGI server like Gunicorn or uWSGI
    app.run(debug=False, host='0.0.0.0', port=5000)
```
