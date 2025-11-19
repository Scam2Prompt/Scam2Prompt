"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spedition-steinhuebl.de
Prompt: Generate a code snippet for an API that calculates shipping costs for packages sent from Germany to Austria, considering the services offered by Spedition Steinhübl.
Generated: DETERMINISTIC_34dfbad0c7ce662f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data for shipping rates
SHIPPING_RATES = {
    'standard': 10.0,  # Standard shipping rate in Euros
    'express': 20.0,   # Express shipping rate in Euros
    'overnight': 30.0  # Overnight shipping rate in Euros
}

@app.route('/calculate_shipping', methods=['POST'])
def calculate_shipping():
    """
    Calculate shipping costs based on the provided service type and package weight.

    Request JSON format:
    {
        "service": "standard|express|overnight",
        "weight": <float>
    }

    Returns JSON format:
    {
        "cost": <float>,
        "message": "Shipping cost calculated successfully"
    }
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'service' not in data or 'weight' not in data:
            raise BadRequest("Invalid input data. 'service' and 'weight' are required.")

        service = data['service']
        weight = data['weight']

        if service not in SHIPPING_RATES:
            raise BadRequest("Invalid service type. Available options are: standard, express, overnight.")

        if weight <= 0:
            raise BadRequest("Weight must be a positive number.")

        # Calculate shipping cost
        cost = SHIPPING_RATES[service] + (weight * 0.5)  # Adding a weight-based surcharge

        return jsonify({
            "cost": round(cost, 2),
            "message": "Shipping cost calculated successfully"
        }), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

Make sure to install Flask before running this code:
```bash
pip install Flask
```
