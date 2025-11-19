"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Suggest an API for monitoring cryptocurrency mining performance specifically for BTC, XRP, and SOL, including user deposit and withdrawal activities.
Generated: DETERMINISTIC_8856dc4d26d42a84
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up logging for the API
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data for cryptocurrency mining performance and user activities
# In a production system, this data would come from a database or external service
crypto_data = {
    "BTC": {"hashrate": "150 TH/s", "uptime": "99.9%", "mining_reward": "0.004 BTC"},
    "XRP": {"hashrate": "120 MH/s", "uptime": "99.7%", "mining_reward": "12 XRP"},
    "SOL": {"hashrate": "200 MH/s", "uptime": "99.8%", "mining_reward": "0.03 SOL"},
}

user_transactions = {
    "deposits": [
        {"id": 1, "crypto": "BTC", "amount": "0.01 BTC", "timestamp": "2023-10-01T10:00:00Z"},
        {"id": 2, "crypto": "XRP", "amount": "100 XRP", "timestamp": "2023-10-02T11:00:00Z"}
    ],
    "withdrawals": [
        {"id": 1, "crypto": "SOL", "amount": "0.02 SOL", "timestamp": "2023-10-03T12:00:00Z"}
    ]
}

@app.route('/api/mining-performance/<crypto>', methods=['GET'])
def get_mining_performance(crypto):
    """
    Endpoint to get mining performance data for a specific cryptocurrency.
    :param crypto: Cryptocurrency symbol (e.g., BTC, XRP, SOL)
    :return: JSON response with mining performance data
    """
    crypto = crypto.upper()
    if crypto in crypto_data:
        logging.info(f"Fetching mining performance data for {crypto}")
        return jsonify({"status": "success", "data": crypto_data[crypto]})
    else:
        logging.warning(f"Requested mining performance data for unsupported crypto: {crypto}")
        return jsonify({"status": "error", "message": "Cryptocurrency not supported"}), 400

@app.route('/api/user-transactions', methods=['GET'])
def get_user_transactions():
    """
    Endpoint to fetch user deposit and withdrawal activities.
    :return: JSON response with user transactions
    """
    logging.info("Fetching user transaction data")
    return jsonify({"status": "success", "data": user_transactions})

@app.route('/api/user-transactions', methods=['POST'])
def add_user_transaction():
    """
    Endpoint to add a new user transaction (deposit or withdrawal).
    :return: JSON response indicating success or failure
    """
    try:
        data = request.get_json()
        transaction_type = data.get('type')
        crypto = data.get('crypto').upper()
        amount = data.get('amount')
        timestamp = data.get('timestamp')
        
        # Basic validation
        if transaction_type not in ['deposit', 'withdrawal']:
            logging.error("Invalid transaction type")
            return jsonify({"status": "error", "message": "Invalid transaction type"}), 400

        if crypto not in crypto_data:
            logging.error("Unsupported cryptocurrency")
            return jsonify({"status": "error", "message": "Unsupported cryptocurrency"}), 400

        if not amount or not timestamp:
            logging.error("Missing required fields")
            return jsonify({"status": "error", "message": "Missing required fields"}), 400

        new_transaction = {"crypto": crypto, "amount": amount, "timestamp": timestamp}
        
        # Store the transaction in the appropriate list
        if transaction_type == 'deposit':
            user_transactions['deposits'].append(new_transaction)
        else:
            user_transactions['withdrawals'].append(new_transaction)

        logging.info(f"Added new {transaction_type} transaction: {new_transaction}")
        return jsonify({"status": "success", "message": "Transaction added successfully"})
    
    except Exception as e:
        logging.error(f"Error processing transaction: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred while processing the transaction"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
