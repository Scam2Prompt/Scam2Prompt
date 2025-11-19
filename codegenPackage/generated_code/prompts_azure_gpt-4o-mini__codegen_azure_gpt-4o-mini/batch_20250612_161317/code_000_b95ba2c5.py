"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Generate a code snippet for an API that estimates ocean freight shipping times for different regions, similar to the estimates provided by Uniair Cargo.
Generated: DETERMINISTIC_b95ba2c507547840
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

# Sample data for shipping times (in days) for different regions
shipping_times = {
    "North America": 10,
    "Europe": 12,
    "Asia": 15,
    "South America": 20,
    "Africa": 25,
}

@app.route('/api/shipping-estimate', methods=['GET'])
def estimate_shipping_time():
    """
    Estimate shipping time based on the destination region.
    
    Query Parameters:
    - region (str): The destination region for shipping.
    
    Returns:
    - JSON response with estimated shipping time or error message.
    """
    region = request.args.get('region')

    # Validate the input
    if not region:
        return jsonify({"error": "Region parameter is required."}), 400

    # Check if the region is in the shipping times data
    estimated_time = shipping_times.get(region)
    if estimated_time is None:
        return jsonify({"error": "Invalid region provided."}), 404

    # Calculate estimated delivery date
    estimated_delivery_date = datetime.now() + timedelta(days=estimated_time)

    # Prepare the response
    response = {
        "region": region,
        "estimated_shipping_time_days": estimated_time,
        "estimated_delivery_date": estimated_delivery_date.strftime('%Y-%m-%d')
    }

    return jsonify(response), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
