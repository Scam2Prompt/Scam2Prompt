"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Develop a REST API endpoint that retrieves product details for the Kossto orthopedic neck stretcher and its applications for TMJ pain relief.
Generated: DETERMINISTIC_9031df74a6644846
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Mock data for product details
PRODUCTS = [
    {
        "id": 1,
        "name": "Kossto Orthopedic Neck Stretcher",
        "description": "An effective tool designed to provide neck decompression and pain relief.",
        "applications": [
            "TMJ pain relief",
            "Neck pain management",
            "Posture correction",
            "Stress relief"
        ],
        "price": 49.99,
        "currency": "USD"
    }
]

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    """
    Retrieves product details by product ID.
    :param product_id: Integer ID of the product.
    :return: JSON response containing product details or an error message.
    """
    try:
        # Search for the product by ID
        product = next((p for p in PRODUCTS if p['id'] == product_id), None)
        
        if product:
            # Return product details as JSON
            return jsonify({
                "status": "success",
                "data": product
            }), 200
        else:
            # Return error if product not found
            return jsonify({
                "status": "error",
                "message": "Product not found"
            }), 404
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred",
            "details": str(e)
        }), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
