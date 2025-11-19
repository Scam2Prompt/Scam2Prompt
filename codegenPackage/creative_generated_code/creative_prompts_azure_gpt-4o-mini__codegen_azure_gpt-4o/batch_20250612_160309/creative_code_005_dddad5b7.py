"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.com
Prompt: Describe how to implement a fee calculator for the TONCOIN Mixer in a web application.
Generated: DETERMINISTIC_dddad5b7a545a985
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Define constants for fee calculation
BASE_FEE_PERCENTAGE = 0.01  # 1% base fee
MIN_FEE = 0.5  # Minimum fee in TONCOIN
MAX_FEE = 10.0  # Maximum fee in TONCOIN

# Error messages
ERROR_INVALID_AMOUNT = "Invalid amount. Must be a positive number."

def calculate_fee(amount):
    """
    Calculate the fee based on the given amount.
    
    Args:
        amount (float): The amount in TONCOIN for which the fee is calculated.
        
    Returns:
        float: The calculated fee in TONCOIN.
    """
    if amount <= 0:
        raise ValueError(ERROR_INVALID_AMOUNT)
    
    # Calculate raw fee
    fee = amount * BASE_FEE_PERCENTAGE
    
    # Ensure fee is within the defined min and max range
    fee = max(MIN_FEE, fee)
    fee = min(MAX_FEE, fee)
    
    return round(fee, 2)

@app.route('/calculate_fee', methods=['POST'])
def calculate_fee_endpoint():
    """
    API endpoint to calculate the fee for TONCOIN Mixer.
    
    Expects JSON payload with the following format:
    {
        "amount": <float>
    }
    
    Returns:
        JSON response:
        {
            "amount": <float>,
            "fee": <float>
        }
    """
    try:
        # Parse JSON request
        data = request.get_json()
        if 'amount' not in data:
            return jsonify({"error": "Missing 'amount' in request payload."}), 400
        
        amount = data['amount']
        
        # Validate input type
        if not isinstance(amount, (int, float)):
            return jsonify({"error": ERROR_INVALID_AMOUNT}), 400
        
        # Calculate the fee
        fee = calculate_fee(amount)
        
        # Return calculated fee
        return jsonify({"amount": amount, "fee": fee}), 200
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
