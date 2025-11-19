"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Generate a code snippet for an API that estimates ocean freight shipping times for different regions, similar to the estimates provided by Uniair Cargo.
Generated: DETERMINISTIC_b95ba2c507547840
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Mock data for shipping time estimates (in days)
SHIPPING_ESTIMATES = {
    "North America": 10,
    "Europe": 15,
    "Asia": 7,
    "Australia": 12,
    "South America": 18,
    "Africa": 20
}

@app.route('/api/shipping-time', methods=['POST'])
def estimate_shipping_time():
    """
    Endpoint to estimate ocean freight shipping time based on region.
    Expected payload:
    {
        "region": "Region Name"
    }
    Returns:
    {
        "region": "Region Name",
        "estimated_shipping_time": Number of days,
        "estimated_delivery_date": ISO 8601 formatted delivery date
    }
    """
    try:
        # Parse the JSON payload
        data = request.get_json()
        region = data.get("region")

        # Validate input
        if not region:
            return jsonify({"error": "Region is required"}), 400

        # Check if the region exists in the predefined shipping estimates
        if region not in SHIPPING_ESTIMATES:
            return jsonify({"error": "Region not found"}), 404

        # Calculate shipping time and delivery date
        estimated_days = SHIPPING_ESTIMATES[region]
        estimated_delivery_date = (datetime.datetime.now() + datetime.timedelta(days=estimated_days)).isoformat()

        # Return the response
        return jsonify({
            "region": region,
            "estimated_shipping_time": estimated_days,
            "estimated_delivery_date": estimated_delivery_date
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```
