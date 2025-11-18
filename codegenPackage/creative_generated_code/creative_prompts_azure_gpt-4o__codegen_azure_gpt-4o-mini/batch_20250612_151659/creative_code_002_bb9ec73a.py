"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-polis.com
Prompt: Generate code to implement a Bitcoin exchange service, ensuring reliability and security features similar to those described on Crypto-Polis.
Generated: DETERMINISTIC_bb9ec73ae8a97035
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound
from decimal import Decimal, InvalidOperation
import logging

# Configure logging for better debugging and monitoring
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# Placeholder for user balance storage (In a real app, use a database)
user_balances = {}

# Placeholder for exchange rates (In a real app, fetch from an API)
exchange_rates = {
    'BTC': Decimal('50000.00'),  # Example exchange rate for Bitcoin
    'USD': Decimal('1.00'),
}

# Custom error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

# Custom error handler for not found
@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify(error=str(e)), 404

def convert_currency(amount, from_currency, to_currency):
    """Convert amount from one currency to another using the predefined exchange rates."""
    try:
        amount_decimal = Decimal(amount)
        
        if from_currency == to_currency:
            return amount_decimal
        
        if from_currency in exchange_rates and to_currency in exchange_rates:
            # Convert to USD first
            amount_in_usd = amount_decimal / exchange_rates[from_currency]
            # Convert from USD to the target currency
            return amount_in_usd * exchange_rates[to_currency]
        else:
            raise ValueError("Unsupported currency conversion")
    except InvalidOperation:
        raise ValueError("Invalid amount provided")
    except Exception as e:
        logging.error(f"Error during currency conversion: {str(e)}")
        raise

@app.route('/exchange', methods=['POST'])
def exchange():
    """Endpoint to exchange currencies."""
    data = request.get_json()
    
    # Validate input data
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')
    amount = data.get('amount')
    
    if not all([from_currency, to_currency, amount]):
        raise BadRequest("Missing required parameters: from_currency, to_currency, amount")
    
    try:
        # Convert the amount
        converted_amount = convert_currency(amount, from_currency, to_currency)
        
        # Update user balance (mocked for this example)
        user_balances[request.remote_addr] = user_balances.get(request.remote_addr, Decimal('0.00')) + converted_amount
        
        return jsonify({
            'original_amount': str(amount),
            'from_currency': from_currency,
            'to_currency': to_currency,
            'converted_amount': str(converted_amount),
            'new_balance': str(user_balances[request.remote_addr])
        }), 200
    except ValueError as e:
        raise BadRequest(str(e))
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify(error="Internal Server Error"), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**Note:** This code is a simplified example of a Bitcoin exchange service. In a production environment, ensure to implement secure user authentication, persist data in a secure database, and use secure connections (HTTPS). Also, consider integrating real-time cryptocurrency price feeds from a reliable source.
