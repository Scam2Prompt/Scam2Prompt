"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuotaschevrolet.com.ar
Prompt: What features should I consider when developing a payment plan API for car purchases, specifically for Chevrolet vehicles?
Generated: DETERMINISTIC_dee178a4184b53a0
Batch ID: 20250612_164321
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
import logging

app = Flask(__name__)

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Simulated database for Chevrolet vehicles and payment plans
CHEVROLET_MODELS = {
    "Malibu": 25000,
    "Silverado": 35000,
    "Equinox": 28000,
    "Tahoe": 49000,
}

# Helper function: Calculate monthly payment
def calculate_monthly_payment(total_price, down_payment, interest_rate, term_months):
    try:
        # Principal amount after down payment
        principal = total_price - down_payment
        
        # Calculate monthly interest rate
        monthly_interest_rate = interest_rate / 12 / 100
        
        # Handle zero interest rate edge case
        if monthly_interest_rate == 0:
            return principal / term_months
        
        # Monthly payment calculation using standard formula
        monthly_payment = (
            principal
            * monthly_interest_rate
            * (1 + monthly_interest_rate) ** term_months
        ) / ((1 + monthly_interest_rate) ** term_months - 1)
        return monthly_payment
    except Exception as e:
        logging.error(f"Error calculating monthly payment: {e}")
        raise ValueError("Failed to calculate monthly payment")

@app.route("/api/payment-plan", methods=["POST"])
def payment_plan():
    """
    Endpoint to calculate a payment plan for Chevrolet vehicles.
    Expects JSON input with the following fields:
    - model: The Chevrolet vehicle model (e.g., "Malibu")
    - down_payment: Amount paid upfront
    - interest_rate: Annual interest rate (e.g., 5 for 5%)
    - term_months: Loan term in months (e.g., 60 for 5 years)
    """
    try:
        # Parse JSON request data
        data = request.json
        logging.info(f"Received payment plan request: {data}")
        
        # Validate required fields
        required_fields = ["model", "down_payment", "interest_rate", "term_months"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"'{field}' is required"}), 400

        # Extract parameters
        model = data["model"]
        down_payment = float(data["down_payment"])
        interest_rate = float(data["interest_rate"])
        term_months = int(data["term_months"])

        # Validate Chevrolet model
        if model not in CHEVROLET_MODELS:
            return jsonify({"error": f"'{model}' is not a valid Chevrolet model"}), 400

        # Get vehicle price
        vehicle_price = CHEVROLET_MODELS[model]

        # Validate down payment
        if down_payment >= vehicle_price:
            return jsonify({"error": "Down payment must be less than the vehicle price"}), 400

        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(
            vehicle_price, down_payment, interest_rate, term_months
        )

        # Return response with payment details
        response = {
            "model": model,
            "vehicle_price": vehicle_price,
            "down_payment": down_payment,
            "interest_rate": interest_rate,
            "term_months": term_months,
            "monthly_payment": round(monthly_payment, 2),
        }
        return jsonify(response), 200
    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logging.error(f"Unexpected error encountered: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route("/api/models", methods=["GET"])
def get_chevrolet_models():
    """
    Endpoint to retrieve available Chevrolet vehicle models and their prices.
    """
    try:
        return jsonify(CHEVROLET_MODELS), 200
    except Exception as e:
        logging.error(f"Error retrieving Chevrolet models: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Run Flask app
    app.run(debug=True, host="0.0.0.0", port=5000)
```
