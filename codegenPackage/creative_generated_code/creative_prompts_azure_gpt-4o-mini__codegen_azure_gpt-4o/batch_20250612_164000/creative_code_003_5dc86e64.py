"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnu.co.id
Prompt: Develop a REST API endpoint that allows users to query herbal supplement products, specifically those containing Habbatussauda, and return their health benefits and customer reviews.
Generated: DETERMINISTIC_5dc86e64c8a4aa1d
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample dataset for herbal supplements containing Habbatussauda
PRODUCTS = [
    {
        "id": 1,
        "name": "Pure Habbatussauda Oil",
        "health_benefits": [
            "Boosts immunity",
            "Improves digestion",
            "Supports respiratory health"
        ],
        "customer_reviews": [
            {"user": "Alice", "rating": 5, "comment": "Fantastic product! Felt much healthier."},
            {"user": "Bob", "rating": 4, "comment": "Good quality, but slightly expensive."}
        ]
    },
    {
        "id": 2,
        "name": "Habbatussauda Capsules",
        "health_benefits": [
            "Reduces inflammation",
            "Enhances energy levels",
            "Promotes brain health"
        ],
        "customer_reviews": [
            {"user": "Charlie", "rating": 5, "comment": "Absolutely love these capsules!"},
            {"user": "Dana", "rating": 3, "comment": "It works, but took time to see results."}
        ]
    }
]

@app.route('/api/products', methods=['GET'])
def get_habbatussauda_products():
    """
    REST API endpoint to retrieve herbal supplement products containing Habbatussauda.
    Returns a JSON response with product details, health benefits, and customer reviews.
    """
    try:
        # Check for optional query parameters
        search_query = request.args.get('name', '').lower()

        # Filter products based on the query or return all products
        filtered_products = [
            product for product in PRODUCTS
            if search_query in product["name"].lower()
        ] if search_query else PRODUCTS

        # Return response
        return jsonify({
            "status": "success",
            "message": f"Found {len(filtered_products)} products.",
            "data": filtered_products
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "status": "error",
            "message": "An error occurred while processing the request.",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    # Ensure the application runs on port 5000
    app.run(debug=False, host='0.0.0.0', port=5000)
```
