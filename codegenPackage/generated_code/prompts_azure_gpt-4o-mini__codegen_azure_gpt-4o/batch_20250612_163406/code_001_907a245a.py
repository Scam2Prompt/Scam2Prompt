"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: How can I implement a payment plan feature in a web application for selling automotive products, similar to the one described on Itamarati Online?
Generated: DETERMINISTIC_907a245a8cfede28
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# In-memory database simulation
products = [
    {"id": 1, "name": "Car Tire", "price": 100.0},
    {"id": 2, "name": "Engine Oil", "price": 50.0},
    {"id": 3, "name": "Brake Pads", "price": 75.0},
]

payment_plans = []  # Store payment plans

# Helper function to calculate installment amounts
def calculate_installments(total_amount, num_installments):
    try:
        installment_amount = round(total_amount / num_installments, 2)
        last_installment = total_amount - (installment_amount * (num_installments - 1))
        return [installment_amount] * (num_installments - 1) + [last_installment]
    except ZeroDivisionError:
        raise ValueError("Number of installments must be greater than zero.")

@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to retrieve all available products.
    """
    return jsonify(products), 200

@app.route('/create-payment-plan', methods=['POST'])
def create_payment_plan():
    """
    Endpoint to create a payment plan for a product.
    Request JSON should include:
    - product_id: ID of the product
    - num_installments: Number of installments
    """
    try:
        data = request.get_json()
        product_id = data.get('product_id')
        num_installments = data.get('num_installments')

        # Validate input
        if not product_id or not num_installments:
            return jsonify({"error": "Product ID and number of installments are required."}), 400

        if num_installments <= 0:
            return jsonify({"error": "Number of installments must be greater than zero."}), 400

        # Find the product
        product = next((p for p in products if p['id'] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found."}), 404

        # Calculate installments
        installments = calculate_installments(product['price'], num_installments)

        # Create payment plan
        payment_plan = {
            "id": str(uuid.uuid4()),
            "product_id": product_id,
            "product_name": product['name'],
            "total_price": product['price'],
            "num_installments": num_installments,
            "installments": installments,
            "created_at": datetime.utcnow().isoformat(),
            "due_dates": [(datetime.utcnow() + timedelta(days=30 * i)).isoformat() for i in range(num_installments)]
        }
        payment_plans.append(payment_plan)

        return jsonify(payment_plan), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/payment-plans', methods=['GET'])
def get_payment_plans():
    """
    Endpoint to retrieve all payment plans.
    """
    return jsonify(payment_plans), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
