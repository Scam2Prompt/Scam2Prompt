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
from flask import Flask, request, jsonify
from decimal import Decimal, InvalidOperation

app = Flask(__name__)

# Constants for fee calculation
BASE_FEE_RATE = Decimal('0.01')  # 1% base fee for mixer
MINIMUM_FEE = Decimal('0.0001')   # Minimum fee to ensure minimum transaction cost

def calculate_fee(amount: Decimal) -> Decimal:
    """
    Calculate the fee based on a given amount.
    
    :param amount: The amount for which the fee is being calculated
    :return: The calculated fee
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    
    # Calculate fee based on the base fee rate
    fee = amount * BASE_FEE_RATE
    # Ensure the fee is at least the minimum fee
    return max(fee, MINIMUM_FEE)

@app.route('/calculate_fee', methods=['POST'])
def fee_calculator():
    """
    API endpoint to calculate the fee for the TONCOIN Mixer.
    
    Expected JSON body:
    {
        "amount": "amount_in_toncoin"
    }
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        if not data or 'amount' not in data:
            return jsonify({"error": "Invalid input. 'amount' is required."}), 400
        
        # Convert amount to Decimal for accurate financial calculations
        amount = Decimal(data['amount'])
        
        # Calculate the fee
        fee = calculate_fee(amount)
        
        # Return the calculated fee in JSON format
        return jsonify({
            "amount": str(amount),
            "calculated_fee": str(fee)
        }), 200
    
    except InvalidOperation:
        return jsonify({"error": "Invalid amount format. Please provide a valid decimal number."}), 400
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
