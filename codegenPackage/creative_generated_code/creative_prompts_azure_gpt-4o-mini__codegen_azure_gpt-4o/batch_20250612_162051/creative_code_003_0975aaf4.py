"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aatmanamjewels.com
Prompt: Develop a RESTful API endpoint that retrieves best-selling jewelry items, akin to the Polki Chandbalis and diamond rings from Atmanam Jewels.
Generated: DETERMINISTIC_0975aaf4c6edf678
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data for best-selling jewelry items
BEST_SELLING_JEWELRY = [
    {"id": 1, "name": "Polki Chandbalis", "category": "Earrings", "price": 1200.00, "currency": "USD"},
    {"id": 2, "name": "Diamond Ring", "category": "Rings", "price": 2500.00, "currency": "USD"},
    {"id": 3, "name": "Gold Necklace", "category": "Necklaces", "price": 3000.00, "currency": "USD"}
]

@app.route('/api/best-selling-jewelry', methods=['GET'])
def get_best_selling_jewelry():
    """
    REST API endpoint to retrieve a list of best-selling jewelry items.

    Returns:
        JSON response containing a list of best-selling jewelry items.
    """
    try:
        # Log the incoming request
        logging.info("GET request to /api/best-selling-jewelry endpoint.")
        
        # Return the list of best-selling jewelry items
        return jsonify({
            "status": "success",
            "data": BEST_SELLING_JEWELRY
        }), 200
    
    except Exception as e:
        # Log any errors encountered
        logging.error(f"An error occurred: {str(e)}")
        
        # Return a 500 Internal Server Error response
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred while retrieving best-selling jewelry items."
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
