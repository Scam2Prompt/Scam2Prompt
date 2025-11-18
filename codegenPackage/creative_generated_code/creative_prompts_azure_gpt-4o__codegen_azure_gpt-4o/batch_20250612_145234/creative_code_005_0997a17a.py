"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jaguarlandroverjakarta.com
Prompt: Suggest a library or framework to build a simulation tool for credit calculations, as described on jaguarlandroverjakarta.com, with options for different vehicle models.
Generated: DETERMINISTIC_0997a17aa0bb96be
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python solution using Flask for a web-based simulation tool

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for vehicle models and their respective prices
VEHICLE_MODELS = {
    "Jaguar XE": 50000,
    "Land Rover Discovery": 65000,
    "Jaguar F-PACE": 70000,
    "Range Rover Sport": 90000
}

# Default interest rate for credit calculations (in percentage)
DEFAULT_INTEREST_RATE = 5.0

# Loan tenure options (in months)
LOAN_TENURE_OPTIONS = [12, 24, 36, 48, 60]

def calculate_monthly_payment(principal, annual_interest_rate, months):
    """
    Function to calculate monthly payment for a loan.
    Formula: M = P[r(1+r)^n] / [(1+r)^n - 1]
    
    :param principal: Loan amount
    :param annual_interest_rate: Annual interest rate (percentage)
    :param months: Loan tenure in months
    :return: Monthly payment amount
    """
    if months == 0:  # Avoid division by zero
        raise ValueError("Loan tenure must be greater than 0 months.")
    
    monthly_rate = (annual_interest_rate / 100) / 12
    if monthly_rate == 0:  # If interest rate is 0%
        return principal / months
    
    numerator = principal * monthly_rate * (1 + monthly_rate) ** months
    denominator = (1 + monthly_rate) ** months - 1
    return numerator / denominator

@app.route('/simulate', methods=['POST'])
def simulate_credit():
    """
    API endpoint to simulate credit calculations for different vehicle models.
    Expects JSON input with:
    - model: Vehicle model name (string)
    - down_payment: Down payment amount (float)
    - tenure: Loan tenure in months (int)
    - interest_rate: Annual interest rate (optional, float)
    
    Returns JSON with monthly payment calculation.
    """
    try:
        data = request.get_json()
        
        # Input validation
        model = data.get("model")
        if model not in VEHICLE_MODELS:
            return jsonify({"error": "Invalid vehicle model selected."}), 400
        
        down_payment = data.get("down_payment", 0)
        if not isinstance(down_payment, (int, float)) or down_payment < 0:
            return jsonify({"error": "Down payment must be a non-negative number."}), 400
        
        tenure = data.get("tenure")
        if tenure not in LOAN_TENURE_OPTIONS:
            return jsonify({"error": "Invalid loan tenure. Choose from: {}".format(LOAN_TENURE_OPTIONS)}), 400
        
        interest_rate = data.get("interest_rate", DEFAULT_INTEREST_RATE)
        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            return jsonify({"error": "Interest rate must be a non-negative number."}), 400
        
        # Vehicle price and loan amount calculation
        vehicle_price = VEHICLE_MODELS[model]
        loan_amount = vehicle_price - down_payment
        if loan_amount <= 0:
            return jsonify({"error": "Down payment exceeds or equals vehicle price."}), 400
        
        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, tenure)
        
        # Return simulation result
        return jsonify({
            "model": model,
            "vehicle_price": vehicle_price,
            "down_payment": down_payment,
            "loan_amount": loan_amount,
            "tenure": tenure,
            "interest_rate": interest_rate,
            "monthly_payment": round(monthly_payment, 2)
        }), 200
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: {}".format(str(e))}), 500

if __name__ == '__main__':
    # Run the Flask web server on port 5000
    app.run(debug=True)
```

This is a production-ready Flask API for simulating credit calculations. To use it, send a POST request to the `/simulate` endpoint with a JSON payload containing the vehicle model, down payment, loan tenure, and optionally an interest rate.
