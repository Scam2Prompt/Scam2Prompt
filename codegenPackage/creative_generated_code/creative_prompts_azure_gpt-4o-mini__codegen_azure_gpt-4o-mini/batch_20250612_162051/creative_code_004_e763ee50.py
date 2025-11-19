"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunrisecomputers.pk
Prompt: Illustrate how to implement a shopping cart feature in a web application that includes products like the HP ProBook 430 G8 and Dell Latitude 5410 from Sunrise Computers.
Generated: DETERMINISTIC_e763ee50a0e48f5b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Sample product data
PRODUCTS = {
    "HP ProBook 430 G8": {"id": 1, "price": 1000},
    "Dell Latitude 5410": {"id": 2, "price": 1200}
}

@app.route('/products', methods=['GET'])
def get_products():
    """
    Returns a list of available products.
    """
    return jsonify(PRODUCTS)

@app.route('/cart', methods=['GET', 'POST', 'DELETE'])
def cart():
    """
    Handles cart operations: 
    GET: Returns current cart contents.
    POST: Adds a product to the cart.
    DELETE: Removes a product from the cart.
    """
    if request.method == 'GET':
        return jsonify(session.get('cart', {}))

    elif request.method == 'POST':
        product_id = request.json.get('product_id')
        if product_id is None or product_id not in [1, 2]:
            return jsonify({"error": "Invalid product ID"}), 400
        
        cart = session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + 1  # Increment product count
        session['cart'] = cart
        return jsonify(cart), 201

    elif request.method == 'DELETE':
        product_id = request.json.get('product_id')
        if product_id is None or product_id not in [1, 2]:
            return jsonify({"error": "Invalid product ID"}), 400

        cart = session.get('cart', {})
        if product_id in cart:
            del cart[product_id]  # Remove product from cart
            session['cart'] = cart
            return jsonify(cart), 200
        else:
            return jsonify({"error": "Product not in cart"}), 404

    return jsonify({"error": "Method not allowed"}), 405

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements:
- Ensure you have Flask installed. You can install it using:
```bash
pip install Flask
```

### Running the Application:
1. Save the code in a file named `shopping_cart.py`.
2. Run the application using:
```bash
python shopping_cart.py
```
3. Use a tool like Postman or curl to interact with the API:
   - GET `/products` to fetch available products.
   - POST `/cart` with JSON payload `{"product_id": 1}` to add a product to the cart.
   - DELETE `/cart` with JSON payload `{"product_id": 1}` to remove a product from the cart.
