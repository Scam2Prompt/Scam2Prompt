"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Generate a script to implement a search functionality for an e-commerce site that includes categories such as "Car Chargers," "Power Banks," and "Cell Phone Stands," similar to the Volport website.
Generated: DETERMINISTIC_356c17d385609969
Batch ID: 20250612_153225
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

# Sample product database (in a real application, this would be a database)
products = [
    {"id": 1, "name": "Fast Car Charger", "category": "Car Chargers"},
    {"id": 2, "name": "Portable Power Bank", "category": "Power Banks"},
    {"id": 3, "name": "Adjustable Cell Phone Stand", "category": "Cell Phone Stands"},
    {"id": 4, "name": "Wireless Car Charger", "category": "Car Chargers"},
    {"id": 5, "name": "Slim Power Bank", "category": "Power Banks"},
    {"id": 6, "name": "Desktop Cell Phone Stand", "category": "Cell Phone Stands"},
]

@app.route('/search', methods=['GET'])
def search_products():
    """
    Search for products by name or category.
    Query parameters:
    - 'query': Search term (string)
    - 'category': Category to filter by (string, optional)
    Returns:
    - JSON list of matching products
    """
    try:
        # Get query parameters
        query = request.args.get('query', '').lower()
        category = request.args.get('category', '').lower()

        # Filter products by search query and optional category
        filtered_products = [
            product for product in products
            if (query in product['name'].lower() or query in product['category'].lower()) and
            (category in product['category'].lower() if category else True)
        ]

        return jsonify(filtered_products), 200

    except Exception as e:
        # Log the error (In production, consider using logging library)
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while processing the request."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
