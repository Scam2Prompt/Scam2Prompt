"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alicebeauty.bg
Prompt: Illustrate how to implement a promotional discount feature in a web application for Alice Beauty's gift cards and special offers.
Generated: DETERMINISTIC_942ff271102cf34e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data structure to hold gift cards and their associated discounts
gift_cards = {
    'GC001': {'value': 100, 'discount': 0.10},  # 10% discount
    'GC002': {'value': 50, 'discount': 0.05},   # 5% discount
}

@app.route('/apply_discount', methods=['POST'])
def apply_discount():
    """
    Apply a promotional discount to a gift card.

    Request Example:
    {
        "gift_card_id": "GC001"
    }

    Returns:
    JSON response with the final value after discount.
    """
    try:
        # Extract JSON data from request
        data = request.get_json()
        if not data or 'gift_card_id' not in data:
            raise BadRequest("Missing gift_card_id in request data.")

        gift_card_id = data['gift_card_id']

        # Validate gift card ID
        if gift_card_id not in gift_cards:
            return jsonify({'error': 'Invalid gift card ID'}), 404

        gift_card = gift_cards[gift_card_id]
        
        # Calculate discounted value
        discount_amount = gift_card['value'] * gift_card['discount']
        final_value = gift_card['value'] - discount_amount

        # Return the final value after applying the discount
        return jsonify({
            'gift_card_id': gift_card_id,
            'original_value': gift_card['value'],
            'discount_amount': discount_amount,
            'final_value': final_value
        }), 200

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
