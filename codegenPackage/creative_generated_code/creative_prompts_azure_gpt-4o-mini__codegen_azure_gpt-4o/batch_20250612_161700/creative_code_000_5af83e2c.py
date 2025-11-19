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

# Initialize Flask app
app = Flask(__name__)

# Sample product database
PRODUCTS = [
    {"id": 1, "name": "كريم اساس برجوا", "skin_types": ["oily", "combination"]},
    {"id": 2, "name": "Moisturizing Cream A", "skin_types": ["dry", "sensitive"]},
    {"id": 3, "name": "Oil-Free Face Wash", "skin_types": ["oily"]},
    {"id": 4, "name": "Hydrating Serum", "skin_types": ["dry", "combination"]},
]

# API route for product recommendations
@app.route('/recommend', methods=['POST'])
def recommend_products():
    try:
        # Parse input JSON data
        data = request.get_json()
        if not data or 'skin_type' not in data:
            return jsonify({"error": "Invalid input. Please provide a skin_type."}), 400

        skin_type = data['skin_type'].lower()

        # Validate skin type
        valid_skin_types = {"oily", "dry", "combination", "sensitive"}
        if skin_type not in valid_skin_types:
            return jsonify({"error": f"Invalid skin_type. Must be one of {valid_skin_types}."}), 400

        # Filter products based on skin type
        recommended_products = [
            product for product in PRODUCTS if skin_type in product["skin_types"]
        ]

        # Return recommendations
        return jsonify({"recommended_products": recommended_products}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False)
```

This code snippet implements a skincare product recommendation API that filters products based on the provided skin type. It includes proper error handling and is suitable for production use when integrated into a larger system.
