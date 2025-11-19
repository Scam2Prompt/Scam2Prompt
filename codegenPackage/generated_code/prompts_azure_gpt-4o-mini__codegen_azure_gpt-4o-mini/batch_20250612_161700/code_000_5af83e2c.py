"""
Generated Code Metadata:
========================
Original URL: https://anamalika.com
Prompt: Generate a code snippet that demonstrates how to implement a skincare product recommendation API that suggests products based on skin type, referencing the specific products mentioned on the site like كريم اساس برجوا.
Generated: DETERMINISTIC_5af83e2cf6e96ab8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for skincare products
PRODUCTS = {
    "dry": [
        {"name": "Moisturizing Cream", "brand": "Brand A", "description": "Hydrating cream for dry skin."},
        {"name": "Nourishing Oil", "brand": "Brand B", "description": "Oil to nourish and hydrate."}
    ],
    "oily": [
        {"name": "Oil-Free Moisturizer", "brand": "Brand C", "description": "Lightweight moisturizer for oily skin."},
        {"name": "Mattifying Gel", "brand": "Brand D", "description": "Gel to control shine."}
    ],
    "combination": [
        {"name": "Balancing Lotion", "brand": "Brand E", "description": "Lotion for combination skin."},
        {"name": "Dual-Action Cream", "brand": "Brand F", "description": "Cream for both dry and oily areas."}
    ],
    "sensitive": [
        {"name": "Soothing Cream", "brand": "Brand G", "description": "Gentle cream for sensitive skin."},
        {"name": "Calming Serum", "brand": "Brand H", "description": "Serum to calm irritation."}
    ]
}

@app.route('/recommend', methods=['GET'])
def recommend_products():
    """
    Recommend skincare products based on the user's skin type.
    
    Query Parameters:
    - skin_type: The type of skin (dry, oily, combination, sensitive)
    
    Returns:
    - JSON response with recommended products or an error message.
    """
    skin_type = request.args.get('skin_type')

    # Validate skin type input
    if skin_type not in PRODUCTS:
        return jsonify({"error": "Invalid skin type. Please choose from: dry, oily, combination, sensitive."}), 400

    # Fetch recommended products
    recommended_products = PRODUCTS[skin_type]
    
    return jsonify({"recommended_products": recommended_products}), 200

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
