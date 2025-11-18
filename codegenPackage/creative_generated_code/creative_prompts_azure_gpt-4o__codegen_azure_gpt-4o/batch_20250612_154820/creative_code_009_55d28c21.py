"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0g-faucet.j-node.net
Prompt: Write a script to log token requests from the 0G Faucet and track the received A0GI tokens on the 0GChain Testnet.
Generated: DETERMINISTIC_55d28c21f4d598ad
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(
    filename='token_requests.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Flask application setup
app = Flask(__name__)

# Database to track token requests and balances (in-memory for simplicity)
token_requests = []  # List of token request logs
user_balances = {}   # Dictionary to track A0GI tokens per user

# Utility function: log a token request
def log_token_request(user_address, amount_requested):
    """
    Logs a token request to the file and in-memory database.

    Args:
        user_address (str): The address of the user requesting tokens.
        amount_requested (int): The number of tokens requested.
    """
    request_data = {
        'timestamp': datetime.utcnow().isoformat(),
        'user_address': user_address,
        'amount_requested': amount_requested
    }
    token_requests.append(request_data)
    logging.info(f"Token request logged: {json.dumps(request_data)}")

# Utility function: update user balances
def update_balance(user_address, amount_received):
    """
    Updates the balance of A0GI tokens for a given user.

    Args:
        user_address (str): The address of the user receiving tokens.
        amount_received (int): The number of tokens received.
    """
    if user_address not in user_balances:
        user_balances[user_address] = 0
    user_balances[user_address] += amount_received

# Endpoint: Request tokens from the faucet
@app.route('/request_tokens', methods=['POST'])
def request_tokens():
    """
    Endpoint to allow users to request tokens from the faucet.

    Expected JSON input:
        {
            "user_address": "string (wallet address)",
            "amount_requested": integer
        }
    
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse request data
        data = request.json
        user_address = data.get('user_address')
        amount_requested = data.get('amount_requested')

        # Validate input
        if not user_address or not isinstance(amount_requested, int) or amount_requested <= 0:
            return jsonify({'error': 'Invalid input data'}), 400

        # Simulate token receipt (on-chain handling would require integration with 0GChain Testnet SDK)
        amount_received = amount_requested  # For simplicity, assume full amount received

        # Log the request and update balance
        log_token_request(user_address, amount_requested)
        update_balance(user_address, amount_received)

        # Respond with success message
        return jsonify({
            'message': 'Tokens successfully requested and received',
            'user_address': user_address,
            'amount_received': amount_received
        }), 200

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Error processing token request: {str(e)}")
        return jsonify({'error': 'An internal server error occurred'}), 500

# Endpoint: View user balances
@app.route('/view_balances', methods=['GET'])
def view_balances():
    """
    Endpoint to view all user balances.

    Returns:
        JSON response containing user balances.
    """
    return jsonify(user_balances), 200

# Endpoint: View token request logs
@app.route('/view_logs', methods=['GET'])
def view_logs():
    """
    Endpoint to view all token request logs.

    Returns:
        JSON response containing token request logs.
    """
    return jsonify(token_requests), 200

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
