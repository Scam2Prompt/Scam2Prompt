"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pranaisland.com
Prompt: Create an API endpoint that retrieves the latest products from a jewelry shop, including details on pricing and availability for items like gold-plated copper and crystal beads.
Generated: DETERMINISTIC_ba2810074eb51ccd
Batch ID: 20250612_160804
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

app = Flask(__name__)

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

# Mock data source: Simulating a database with sample products
PRODUCTS = [
    {"id": 1, "name": "Gold-Plated Copper Necklace", "price": 129.99, "availability": True, "created_at": datetime(2023, 10, 1)},
    {"id": 2, "name": "Crystal Bead Earrings", "price": 49.99, "availability": True, "created_at": datetime(2023, 10, 2)},
    {"id": 3, "name": "Gold-Plated Copper Bracelet", "price": 89.99, "availability": False, "created_at": datetime(2023, 9, 30)},
]

@app.route('/api/products/latest', methods=['GET'])
def get_latest_products():
    """
    API endpoint to fetch the latest products from the jewelry shop.
    Returns the most recently added products along with details on pricing and availability.
    """
    try:
        # Extract query parameter for filtering (if specified)
        limit = request.args.get('limit', default=5, type=int)  # Default limit is 5
        
        # Sort products by creation date (most recent first) and apply limit
        sorted_products = sorted(PRODUCTS, key=lambda x: x['created_at'], reverse=True)
        latest_products = sorted_products[:limit]
        
        # Serialize datetime objects to strings for JSON response
        response_data = [
            {**product, "created_at": product["created_at"].strftime("%Y-%m-%d %H:%M:%S")}
            for product in latest_products
        ]

        return jsonify({"status": "success", "data": response_data}), 200
    except Exception as e:
        # Log the error and return a generic error response
        logging.error(f"Error occurred while fetching latest products: {str(e)}")
        return jsonify({"status": "error", "message": "An unexpected error occurred."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
