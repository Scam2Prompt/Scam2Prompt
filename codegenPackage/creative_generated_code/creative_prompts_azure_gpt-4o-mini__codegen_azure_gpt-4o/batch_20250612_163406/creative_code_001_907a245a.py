"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: How can I implement a payment plan feature in a web application for selling automotive products, similar to the one described on Itamarati Online?
Generated: DETERMINISTIC_907a245a8cfede28
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Mock database for simplicity
products = {
    1: {"name": "Car Engine", "price": 1200},
    2: {"name": "Tires Set", "price": 800},
}
payment_plans = {
    "monthly": {"installments": 12, "interest_rate": 0.02},
    "quarterly": {"installments": 4, "interest_rate": 0.05},
}

# Error handling utility function
def create_error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to list all available products.
    """
    return jsonify(products)

@app.route('/payment-plans', methods=['POST'])
def create_payment_plan():
    """
    Endpoint to create a payment plan for a product.
    """
    try:
        # Parse request payload
        data = request.json
        product_id = data.get("product_id")
        plan_type = data.get("plan_type")
        
        # Validate product ID
        if product_id not in products:
            return create_error_response(f"Product with ID {product_id} not found.")
        
        # Validate plan type
        if plan_type not in payment_plans:
            return create_error_response(f"Payment plan '{plan_type}' not available.")
        
        # Retrieve product and payment plan details
        product = products[product_id]
        plan = payment_plans[plan_type]
        
        # Calculate payment details
        total_price = product["price"] * (1 + plan["interest_rate"])
        installment_amount = round(total_price / plan["installments"], 2)
        next_due_date = datetime.now() + timedelta(days=30)
        
        # Build payment schedule
        schedule = [
            {
                "installment_number": i + 1,
                "amount_due": installment_amount,
                "due_date": (next_due_date + timedelta(days=30 * i)).strftime("%Y-%m-%d"),
            }
            for i in range(plan["installments"])
        ]
        
        # Response payload
        response = {
            "product": product,
            "plan_type": plan_type,
            "total_price": total_price,
            "installments": plan["installments"],
            "schedule": schedule,
        }
        
        return jsonify(response)
    
    except Exception as e:
        # Handle unexpected errors
        return create_error_response(f"An error occurred: {str(e)}", status_code=500)

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
