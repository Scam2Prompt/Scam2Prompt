"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank.cz
Prompt: Create an API endpoint that returns the latest furniture collections and promotional offers from an online furniture store.
Generated: DETERMINISTIC_55a0237fcdf3e6dc
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

# Mock data for furniture collections and promotional offers
furniture_collections = [
    {
        "id": 1,
        "name": "Modern Living Room Set",
        "description": "A sleek and stylish living room set perfect for urban homes.",
        "price": 1499.99,
        "available": True
    },
    {
        "id": 2,
        "name": "Rustic Dining Table",
        "description": "Crafted from reclaimed wood, ideal for family dinners.",
        "price": 799.99,
        "available": True
    }
]

promotional_offers = [
    {
        "id": 1,
        "title": "Spring Sale",
        "description": "Get 20% off on all dining tables!",
        "valid_until": "2023-12-31"
    },
    {
        "id": 2,
        "title": "Furniture Combo Discount",
        "description": "Buy any living room set and get a coffee table for free.",
        "valid_until": "2023-11-15"
    }
]

@app.route('/api/v1/furniture-store/latest', methods=['GET'])
def get_latest_furniture_and_offers():
    """
    API endpoint to return the latest furniture collections and promotional offers.
    """
    try:
        # Current date for reference
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Response object
        response = {
            "success": True,
            "data": {
                "furnitureCollections": furniture_collections,
                "promotionalOffers": [
                    offer for offer in promotional_offers
                    if offer["valid_until"] >= current_date
                ]
            },
            "timestamp": current_date
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        error_response = {
            "success": False,
            "message": "An error occurred while processing your request.",
            "error": str(e)
        }
        return jsonify(error_response), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
