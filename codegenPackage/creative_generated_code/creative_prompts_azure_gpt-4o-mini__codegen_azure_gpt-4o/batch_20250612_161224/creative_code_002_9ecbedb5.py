"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherealspamassagetherapist.com
Prompt: Create an API endpoint that retrieves the price list for different massage services offered at Ethereal Spa, including Swedish and sports massage.
Generated: DETERMINISTIC_9ecbedb54064e867
Batch ID: 20250612_161224
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

# Predefined list of massage services and their prices
MASSAGE_SERVICES = [
    {"service": "Swedish Massage", "price": 80},
    {"service": "Sports Massage", "price": 100},
    {"service": "Deep Tissue Massage", "price": 90},
    {"service": "Aromatherapy Massage", "price": 85},
]

@app.route('/api/massage_prices', methods=['GET'])
def get_massage_prices():
    """
    API endpoint to retrieve the price list for massage services.
    :return: JSON object containing massage services and their prices.
    """
    try:
        # Return the massage services and prices as a JSON response
        return jsonify({"massage_prices": MASSAGE_SERVICES}), 200
    except Exception as e:
        # Handle any unexpected errors and return a JSON error response
        error_message = {"error": "An unexpected error occurred.", "details": str(e)}
        return jsonify(error_message), 500

if __name__ == '__main__':
    # Run the Flask app on the default port (5000)
    app.run(debug=False)
```
