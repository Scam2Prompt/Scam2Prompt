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

# Sample product database
PRODUCTS = [
    {"id": 1, "name": "كريم اساس برجوا", "skin_type": "dry", "description": "A foundation suitable for dry skin."},
    {"id": 2, "name": "كريم اساس برجوا مات", "skin_type": "oily", "description": "A matte foundation for oily skin."},
    {"id": 3, "name": "مرطب للبشرة الحساسة", "skin_type": "sensitive", "description": "A moisturizer for sensitive skin."},
    {"id": 4, "name": "كريم اساس برجوا للبشرة المختلطة", "skin_type": "combination", "description": "A foundation for combination skin."},
]

@app.route('/recommend', methods=['GET'])
def recommend_products():
    """
    API endpoint to recommend skincare products based on skin type.
    Query parameter: skin_type (e.g., 'dry', 'oily', 'sensitive', 'combination')
    Returns: JSON response with recommended products.
    """
    try:
        # Get the skin type from query parameters
        skin_type = request.args.get('skin_type', '').lower()
        
        if not skin_type:
            return jsonify({"error": "Missing 'skin_type' query parameter."}), 400
        
        # Filter products based on skin type
        recommended_products = [product for product in PRODUCTS if product['skin_type'] == skin_type]
        
        if not recommended_products:
            return jsonify({"message": f"No products found for skin type '{skin_type}'."}), 404
        
        return jsonify({"recommended_products": recommended_products}), 200
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
