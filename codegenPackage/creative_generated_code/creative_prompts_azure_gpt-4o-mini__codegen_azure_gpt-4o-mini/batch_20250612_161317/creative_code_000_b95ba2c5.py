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
from datetime import datetime, timedelta
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants for estimated shipping times (in days) per region
SHIPPING_ESTIMATES = {
    'Asia': 10,
    'North America': 15,
    'Europe': 12,
    'South America': 20,
    'Africa': 25,
    'Australia': 18
}

@app.route('/api/shipping-estimate', methods=['GET'])
def get_shipping_estimate():
    """
    API endpoint to estimate ocean freight shipping times based on destination region.
    
    Query Parameters:
        - region (str): The region to which the goods are being shipped. 
                        Must be one of the predefined regions.
    
    Returns:
        JSON response containing the estimated shipping time in days or an error message.
    """
    region = request.args.get('region')

    # Validate the input
    if not region:
        logging.error("Region parameter is missing.")
        return jsonify({"error": "Region parameter is required."}), 400
    
    region = region.capitalize()  # Capitalize the first letter for consistency

    # Check if the region is valid
    if region not in SHIPPING_ESTIMATES:
        logging.error(f"Invalid region: {region}.")
        return jsonify({"error": "Invalid region. Valid options are: Asia, North America, Europe, South America, Africa, Australia."}), 400

    # Retrieve estimated shipping time
    estimated_days = SHIPPING_ESTIMATES[region]
    
    # Calculate estimated arrival date
    estimated_arrival_date = datetime.now() + timedelta(days=estimated_days)

    # Prepare the response
    response = {
        "region": region,
        "estimated_shipping_days": estimated_days,
        "estimated_arrival_date": estimated_arrival_date.strftime('%Y-%m-%d')
    }
    
    logging.info(f"Estimated shipping for {region}: {estimated_days} days, arrival on {response['estimated_arrival_date']}.")
    
    return jsonify(response), 200

if __name__ == '__main__':
    # Run the Flask app in production mode
    app.run(host='0.0.0.0', port=5000, debug=False)
```
