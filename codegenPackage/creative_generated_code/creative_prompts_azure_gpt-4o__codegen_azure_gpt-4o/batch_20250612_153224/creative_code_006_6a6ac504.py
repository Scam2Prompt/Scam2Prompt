"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.stellarviewrealty.com
Prompt: Suggest an API for integrating a real estate comparison tool that matches the "Compare listings" feature on the StellarView Realty website.
Generated: DETERMINISTIC_6a6ac504fab3af16
Batch ID: 20250612_153224
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data for demonstration purposes
mock_listings = [
    {
        "id": 1,
        "address": "123 Maple Street",
        "price": 250000,
        "beds": 3,
        "baths": 2,
        "sqft": 1500
    },
    {
        "id": 2,
        "address": "456 Oak Avenue",
        "price": 350000,
        "beds": 4,
        "baths": 3,
        "sqft": 2200
    },
    {
        "id": 3,
        "address": "789 Pine Drive",
        "price": 150000,
        "beds": 2,
        "baths": 1,
        "sqft": 1000
    }
]

@app.route('/api/compare', methods=['POST'])
def compare_listings():
    """
    Endpoint for comparing real estate listings.
    Accepts a JSON payload with an array of listing IDs to compare.
    Returns a JSON object with the details of the requested listings.
    
    Request format:
    {
        "listing_ids": [1, 2, 3]
    }
    """
    try:
        # Parse request data
        data = request.get_json()
        if not data or 'listing_ids' not in data:
            return jsonify({"error": "Invalid request format. 'listing_ids' is required."}), 400
        
        listing_ids = data['listing_ids']
        if not isinstance(listing_ids, list) or not all(isinstance(id, int) for id in listing_ids):
            return jsonify({"error": "Invalid format for 'listing_ids'. Must be an array of integers."}), 400
        
        # Filter listings based on requested IDs
        matched_listings = [listing for listing in mock_listings if listing['id'] in listing_ids]
        
        if not matched_listings:
            return jsonify({"error": "No listings found for the provided IDs."}), 404
        
        return jsonify({"listings": matched_listings}), 200
    
    except Exception as e:
        logging.error(f"An error occurred while processing the request: {e}")
        return jsonify({"error": "Internal server error. Please try again later."}), 500

if __name__ == '__main__':
    # Run Flask app
    app.run(debug=True)
```

### Key Features:
- **Dynamic API**: Accepts listing IDs and returns matching data.
- **Error Handling**: Graceful handling of invalid input and unexpected errors.
- **Mock Listings**: Simulates a real-world use case with static data for demonstration.
