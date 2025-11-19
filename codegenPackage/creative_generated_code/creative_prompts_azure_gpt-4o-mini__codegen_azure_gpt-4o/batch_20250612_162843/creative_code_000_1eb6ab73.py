"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.coinsend.top
Prompt: Generate a code snippet for an e-commerce platform that allows users to filter track cycling products by category, such as "Track Bikes/Frames" or "Track Wheels/Tyres."
Generated: DETERMINISTIC_1eb6ab7375f44c3a
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize the Flask Application
app = Flask(__name__)

# Mock Data: Track Cycling Products
PRODUCTS = [
    {"id": 1, "name": "Track Bike - Model X", "category": "Track Bikes/Frames", "price": 1200},
    {"id": 2, "name": "Track Frame - Model Y", "category": "Track Bikes/Frames", "price": 800},
    {"id": 3, "name": "Track Wheelset - UltraSpeed", "category": "Track Wheels/Tyres", "price": 500},
    {"id": 4, "name": "Track Tyres - GripMax", "category": "Track Wheels/Tyres", "price": 120},
    {"id": 5, "name": "Track Pedals - ProRide", "category": "Accessories", "price": 80},
]

# Error Handling Middleware for JSON Responses
@app.errorhandler(Exception)
def handle_exception(error):
    """Global error handler for the application."""
    response = {
        "error": str(error)
    }
    if isinstance(error, HTTPException):
        response["status_code"] = error.code
    else:
        response["status_code"] = 500
    return jsonify(response), response["status_code"]

# Route to Filter Products by Category
@app.route("/filter-products", methods=["GET"])
def filter_products():
    """
    Filters track cycling products based on the 'category' query parameter.
    Returns a JSON list of matching products.
    """
    # Get the 'category' from query parameters
    category = request.args.get("category", None)
    
    # Validate the 'category' parameter
    if not category:
        return jsonify({"error": "Category parameter is required."}), 400
    
    # Filter products by category
    filtered_products = [product for product in PRODUCTS if product["category"] == category]
    
    # Return the filtered products
    return jsonify({"products": filtered_products}), 200

# Run the Flask Application
if __name__ == "__main__":
    app.run(debug=True)
```
