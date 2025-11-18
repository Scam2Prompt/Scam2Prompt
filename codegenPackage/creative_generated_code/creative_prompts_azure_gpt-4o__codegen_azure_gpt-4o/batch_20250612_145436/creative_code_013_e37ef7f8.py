"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Write code to implement a wishlist feature for products like tire changers and safety equipment, inspired by Dotcom Machinery's website functionality.
Generated: DETERMINISTIC_e37ef7f8724ecbb1
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a proper secret key in production

# In-memory database simulation for wishlist
# In a production environment, this would be replaced with a real database
wishlist_db = {}

# Helper function to get the current user's wishlist
def get_user_wishlist():
    user_id = session.get('user_id')
    if not user_id:
        user_id = str(uuid4())  # Generate a unique user ID
        session['user_id'] = user_id
    if user_id not in wishlist_db:
        wishlist_db[user_id] = []
    return wishlist_db[user_id]

@app.route("/wishlist", methods=["GET"])
def view_wishlist():
    """
    Endpoint to view the current user's wishlist.
    Returns:
    - A list of products in the user's wishlist.
    """
    wishlist = get_user_wishlist()
    return jsonify({"wishlist": wishlist}), 200

@app.route("/wishlist", methods=["POST"])
def add_to_wishlist():
    """
    Endpoint to add a product to the wishlist.
    Request Body (JSON):
    - product_id (str): The ID of the product to add.
    - product_name (str): The name of the product.
    Returns:
    - Success message and the updated wishlist.
    """
    data = request.get_json()
    if not data or "product_id" not in data or "product_name" not in data:
        return jsonify({"error": "Invalid payload. 'product_id' and 'product_name' are required."}), 400

    product_id = data["product_id"]
    product_name = data["product_name"]
    wishlist = get_user_wishlist()

    if any(item["product_id"] == product_id for item in wishlist):
        return jsonify({"error": "Product already in wishlist."}), 409

    wishlist.append({"product_id": product_id, "product_name": product_name})
    return jsonify({"message": "Product added to wishlist.", "wishlist": wishlist}), 201

@app.route("/wishlist/<product_id>", methods=["DELETE"])
def remove_from_wishlist(product_id):
    """
    Endpoint to remove a product from the wishlist.
    Path Parameters:
    - product_id (str): The ID of the product to remove.
    Returns:
    - Success message and the updated wishlist.
    """
    wishlist = get_user_wishlist()
    updated_wishlist = [item for item in wishlist if item["product_id"] != product_id]

    if len(wishlist) == len(updated_wishlist):  # No items were removed
        return jsonify({"error": "Product not found in wishlist."}), 404

    wishlist_db[session['user_id']] = updated_wishlist
    return jsonify({"message": "Product removed from wishlist.", "wishlist": updated_wishlist}), 200

# Error handling for generic exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """
    Generic error handler for unexpected exceptions.
    """
    return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)  # Set debug=False in production
```
