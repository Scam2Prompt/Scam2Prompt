"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coworkingcomercio.com.br
Prompt: Create an API endpoint for a coworking space management system that lists monthly and hourly plans, inspired by the offerings at Coworking Comércio.
Generated: DETERMINISTIC_f1c6bd4127fc9564
Batch ID: 20250612_160946
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

# Mock data: List of coworking plans
plans = [
    {
        "type": "Monthly",
        "name": "Basic Plan",
        "price": 150.00,
        "features": [
            "Unlimited access during working hours",
            "Free coffee",
            "High-speed internet"
        ]
    },
    {
        "type": "Monthly",
        "name": "Premium Plan",
        "price": 300.00,
        "features": [
            "24/7 access",
            "Dedicated desk",
            "Free coffee and snacks",
            "High-speed internet",
            "Meeting room access"
        ]
    },
    {
        "type": "Hourly",
        "name": "Hourly Access",
        "price_per_hour": 5.00,
        "features": [
            "Flexible access",
            "High-speed internet",
            "Free coffee"
        ]
    }
]

# API endpoint to list coworking plans
@app.route('/api/coworking-plans', methods=['GET'])
def get_coworking_plans():
    """
    Endpoint to retrieve the list of coworking space plans.
    Returns:
        JSON response containing the list of plans.
    """
    try:
        # Return the list of plans as a JSON response
        return jsonify({"plans": plans}), 200
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask application only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production use
```
