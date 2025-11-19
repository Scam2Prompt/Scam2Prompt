"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p30mag.com
Prompt: Create a simple API that fetches discounts on Instagram follower purchases during Black Friday, inspired by the deals highlighted on p30mag.com.
Generated: DETERMINISTIC_b8d8ac0697e7d801
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Sample data
DISCOUNTS = [
    {"provider": "FollowersBoost", "discount": 20, "valid_until": "2023-11-30"},
    {"provider": "InstaGrowth", "discount": 15, "valid_until": "2023-11-30"},
    {"provider": "BoostMyInsta", "discount": 25, "valid_until": "2023-11-30"},
]

def is_discount_valid(valid_until):
    """Check if the discount is still valid based on the valid_until date."""
    try:
        valid_date = datetime.strptime(valid_until, "%Y-%m-%d")
        return valid_date >= datetime.now()
    except ValueError as e:
        logging.error(f"Date parsing error: {e}")
        return False

@app.route('/api/discounts', methods=['GET'])
def get_discounts():
    """
    API endpoint to fetch available discounts for Instagram follower purchases.
    Returns a list of discounts that are valid until the specified date.
    """
    # Filter valid discounts
    valid_discounts = [
        discount for discount in DISCOUNTS 
        if is_discount_valid(discount['valid_until'])
    ]

    return jsonify(valid_discounts)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    logging.warning(f"404 error: {request.path} not found.")
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logging.error(f"500 error: {error}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
