"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Create an API to calculate and display the consistency multiplier (1.2X volume) for wallets that transacted in at least six distinct months.
Generated: DETERMINISTIC_350d8c3575ac3645
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)

# Sample transaction data for demonstration purposes
# Each transaction contains a wallet ID, amount, and transaction date
transactions = [
    {"wallet_id": "wallet1", "amount": 100, "date": "2023-01-15"},
    {"wallet_id": "wallet1", "amount": 200, "date": "2023-02-15"},
    {"wallet_id": "wallet1", "amount": 150, "date": "2023-03-15"},
    {"wallet_id": "wallet1", "amount": 300, "date": "2023-04-15"},
    {"wallet_id": "wallet1", "amount": 50, "date": "2023-05-15"},
    {"wallet_id": "wallet1", "amount": 400, "date": "2023-06-15"},
    {"wallet_id": "wallet2", "amount": 500, "date": "2023-01-10"},
    {"wallet_id": "wallet2", "amount": 600, "date": "2023-02-10"},
    {"wallet_id": "wallet3", "amount": 700, "date": "2023-01-20"},
]

@app.route('/api/consistency-multiplier', methods=['GET'])
def get_consistency_multiplier():
    """
    Endpoint to calculate and display the consistency multiplier (1.2X volume) for wallets
    that transacted in at least six distinct months.
    """
    try:
        # Parse transactions and group them by wallet_id
        wallet_transactions = defaultdict(list)
        for transaction in transactions:
            wallet_transactions[transaction["wallet_id"]].append(transaction)
        
        # Calculate the multiplier for eligible wallets
        result = {}
        for wallet_id, txns in wallet_transactions.items():
            # Extract distinct months of transactions for this wallet
            months = set(datetime.strptime(txn["date"], "%Y-%m-%d").strftime("%Y-%m") for txn in txns)
            if len(months) >= 6:  # Wallets must have transactions in at least 6 distinct months
                total_volume = sum(txn["amount"] for txn in txns)
                consistency_multiplier = round(total_volume * 1.2, 2)
                result[wallet_id] = {
                    "total_volume": total_volume,
                    "consistency_multiplier": consistency_multiplier,
                }
        
        # Return the result as JSON
        return jsonify({"success": True, "data": result}), 200
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
