"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creditu.com.ar
Prompt: Create an API endpoint that allows users to apply for financing on products listed in a catalog, inspired by the financing options provided by Creditu.
Generated: DETERMINISTIC_7f8aeb11e3a67672
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulated product catalog
PRODUCT_CATALOG = {
    1: {"name": "Laptop", "price": 1000},
    2: {"name": "Smartphone", "price": 800},
    3: {"name": "Tablet", "price": 500}
}

# Simulated financing plans (in months)
FINANCING_PLANS = [6, 12, 24]

# Helper function to calculate monthly installment
def calculate_installments(price, months):
    interest_rate = 0.05  # Example interest rate: 5%
    total_price_with_interest = price * (1 + interest_rate)
    return round(total_price_with_interest / months, 2)

@app.route('/apply-financing', methods=['POST'])
def apply_financing():
    """
    API endpoint to apply for financing on a product.
    Request format: JSON
    {
        "product_id": int,
        "financing_months": int,
        "user_name": str,
        "user_email": str
    }
    """
    try:
        # Parse and validate request data
        data = request.json
        
        if not data:
            return jsonify({"error": "Invalid request: No data provided"}), 400

        product_id = data.get('product_id')
        financing_months = data.get('financing_months')
        user_name = data.get('user_name')
        user_email = data.get('user_email')

        # Validate required fields
        if not all([product_id, financing_months, user_name, user_email]):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate product ID
        product = PRODUCT_CATALOG.get(product_id)
        if not product:
            return jsonify({"error": "Invalid product ID"}), 404
        
        # Validate financing months
        if financing_months not in FINANCING_PLANS:
            return jsonify({"error": f"Invalid financing months. Available plans: {FINANCING_PLANS}"}), 400

        # Calculate financing details
        monthly_installment = calculate_installments(product['price'], financing_months)

        # Simulated financing application result
        application_result = {
            "status": "success",
            "message": "Financing application submitted successfully",
            "details": {
                "user_name": user_name,
                "user_email": user_email,
                "product_name": product['name'],
                "product_price": product['price'],
                "financing_months": financing_months,
                "monthly_installment": monthly_installment,
                "application_timestamp": datetime.utcnow().isoformat()
            }
        }

        return jsonify(application_result), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
