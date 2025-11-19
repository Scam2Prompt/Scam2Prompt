"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anamalika.com
Prompt: Generate a code snippet that demonstrates how to implement a skincare product recommendation API that suggests products based on skin type, referencing the specific products mentioned on the site like كريم اساس برجوا.
Generated: DETERMINISTIC_5af83e2cf6e96ab8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

# Sample data representing skincare products
PRODUCTS = {
    "dry": [
        {"name": "Moisturizing Cream", "brand": "Brand A"},
        {"name": "Hydrating Lotion", "brand": "Brand B"}
    ],
    "oily": [
        {"name": "Oil-Free Gel", "brand": "Brand C"},
        {"name": "Clay Mask", "brand": "Brand D"}
    ],
    "combination": [
        {"name": "Balancing Moisturizer", "brand": "Brand E"},
        {"name": "Hydrating Serum", "brand": "Brand F"}
    ],
    "sensitive": [
        {"name": "Gentle Cream", "brand": "Brand G"},
        {"name": "Soothing Gel", "brand": "Brand H"}
    ],
    "normal": [
        {"name": "Daily Lotion", "brand": "Brand I"},
        {"name": "Nourishing Cream", "brand": "Brand J"}
    ],
}

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend_products():
    """
    Endpoint to recommend skincare products based on skin type.

    Query Parameters:
    - skin_type: The type of skin (e.g., dry, oily, combination, sensitive, normal)

    Returns:
    - A JSON response with recommended products or an error message.
    """
    skin_type = request.args.get('skin_type')

    # Validate skin_type input
    if not skin_type:
        return jsonify({"error": "skin_type parameter is required."}), 400

    skin_type = skin_type.lower()

    # Check if the skin_type is valid
    if skin_type not in PRODUCTS:
        return jsonify({"error": "Invalid skin_type. Must be one of: dry, oily, combination, sensitive, normal."}), 400

    # Fetch the recommended products
    recommended_products = PRODUCTS[skin_type]

    return jsonify({
        "skin_type": skin_type,
        "recommended_products": recommended_products
    }), 200

if __name__ == '__main__':
    # Start the Flask application
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
