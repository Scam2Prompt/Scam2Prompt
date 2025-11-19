"""
Generated Code Metadata:
========================
Original URL: https://joelpeekay.com
Prompt: "Generate a code snippet for a product filter on an e-commerce website, allowing users to filter men's shoes by categories like casuals, loafers, and corporate shoes."
Generated: DETERMINISTIC_4e38cde7e2eedf3f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data representing men's shoes in the database
shoes = [
    {"id": 1, "name": "Casual Sneaker", "category": "casuals", "price": 50},
    {"id": 2, "name": "Leather Loafer", "category": "loafers", "price": 80},
    {"id": 3, "name": "Corporate Derby", "category": "corporate", "price": 100},
    {"id": 4, "name": "Canvas Casual", "category": "casuals", "price": 40},
    {"id": 5, "name": "Suede Loafer", "category": "loafers", "price": 90},
]

@app.route('/filter-shoes', methods=['GET'])
def filter_shoes():
    """
    Endpoint to filter men's shoes by category.
    Query Parameters:
        category (str): The category to filter by (e.g., 'casuals', 'loafers', 'corporate').
    Returns:
        JSON response containing the filtered list of shoes.
    """
    try:
        # Get the category from query parameters
        category = request.args.get('category', '').lower()

        # Validate the category parameter
        if not category:
            return jsonify({"error": "Category parameter is required"}), 400

        # Filter shoes based on the category
        filtered_shoes = [shoe for shoe in shoes if shoe['category'] == category]

        # If no shoes match the category, return an empty list
        if not filtered_shoes:
            return jsonify({"message": "No shoes found for the given category", "shoes": []}), 200

        # Return the filtered list of shoes
        return jsonify({"shoes": filtered_shoes}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
