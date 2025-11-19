"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.gay
Prompt: Create a simple API that logs financial transparency data as described on the blur.gay site, detailing income and expenditures related to public endeavors.
Generated: DETERMINISTIC_8d0a30c67b1ee18a
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging
import datetime
import os

# Flask app instance
app = Flask(__name__)

# Configure logging
LOG_FILE = 'financial_transparency.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()


# Helper function to write to log file
def log_transaction(transaction_type, data):
    """
    Logs a financial transaction (income or expenditure).
    :param transaction_type: Type of transaction (income or expenditure).
    :param data: Dictionary containing transaction details.
    """
    log_entry = f"{transaction_type.upper()} | Amount: {data['amount']} | Source: {data['source']} | Description: {data.get('description', 'N/A')}"
    logging.info(log_entry)


# Endpoint to log income
@app.route('/api/log/income', methods=['POST'])
def log_income():
    """
    Logs income data.
    Request JSON Example:
    {
        "amount": 1000,
        "source": "Donation",
        "description": "Monthly donor contribution"
    }
    """
    try:
        data = request.get_json()
        # Validate input
        if not data or 'amount' not in data or 'source' not in data:
            return jsonify({"error": "Invalid input. 'amount' and 'source' are required."}), 400

        # Log the transaction
        log_transaction("income", data)

        return jsonify({"message": "Income logged successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to log expenditure
@app.route('/api/log/expenditure', methods=['POST'])
def log_expenditure():
    """
    Logs expenditure data.
    Request JSON Example:
    {
        "amount": 500,
        "source": "Purchase",
        "description": "Office supplies"
    }
    """
    try:
        data = request.get_json()
        # Validate input
        if not data or 'amount' not in data or 'source' not in data:
            return jsonify({"error": "Invalid input. 'amount' and 'source' are required."}), 400

        # Log the transaction
        log_transaction("expenditure", data)

        return jsonify({"message": "Expenditure logged successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Endpoint to retrieve logs (for transparency purposes)
@app.route('/api/logs', methods=['GET'])
def get_logs():
    """
    Retrieves all logged financial transactions.
    Returns a list of log entries.
    """
    try:
        if not os.path.exists(LOG_FILE):
            return jsonify({"error": "Log file not found."}), 404

        with open(LOG_FILE, 'r') as file:
            logs = file.readlines()

        return jsonify({"logs": logs}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Application entry point
if __name__ == '__main__':
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)
```
