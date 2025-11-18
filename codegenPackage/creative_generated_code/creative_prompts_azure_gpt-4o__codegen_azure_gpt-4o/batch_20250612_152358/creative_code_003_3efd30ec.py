"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftgoldcoin.com
Prompt: Develop a secure web application that uses EVSSL certificates and anti-DDoS hosting features, as described on swiftgoldcoin.com, to manage cryptocurrency investment transactions.
Generated: DETERMINISTIC_3efd30ec894621ec
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sslify import SSLify
import logging
from werkzeug.exceptions import HTTPException
import os

# Initialize Flask application
app = Flask(__name__)

# Enforce HTTPS with SSLify. This assumes EV SSL certificates are configured at the server level.
SSLify(app)

# Set up logging for debugging and error monitoring
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Placeholder database for cryptocurrency transactions (to be replaced with a secure, production-ready database)
transactions_db = []

# Environment variables for secure configurations
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")

# Anti-DDoS settings are assumed to be handled by hosting provider (e.g., Cloudflare or similar).
# This code assumes a secure web hosting environment.

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    """
    logging.error(f"HTTP Exception: {e.code} - {e.description}")
    response = e.get_response()
    response.data = jsonify({
        "error": e.description,
        "code": e.code
    })
    response.content_type = "application/json"
    return response


@app.route('/api/transactions', methods=['POST'])
def create_transaction():
    """
    API endpoint to create a cryptocurrency transaction.
    """
    try:
        data = request.json

        # Validate request data
        if not data or 'amount' not in data or 'currency' not in data or 'investor_id' not in data:
            logging.warning("Invalid transaction data received.")
            return jsonify({"error": "Invalid transaction data"}), 400

        # Simulate creating a transaction
        transaction = {
            "id": len(transactions_db) + 1,
            "amount": data['amount'],
            "currency": data['currency'],
            "investor_id": data['investor_id']
        }
        transactions_db.append(transaction)
        logging.info(f"Transaction created: {transaction}")
        return jsonify({"transaction": transaction}), 201

    except Exception as ex:
        logging.error(f"Error creating transaction: {str(ex)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/api/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """
    API endpoint to retrieve a cryptocurrency transaction by its ID.
    """
    try:
        # Find transaction by ID
        transaction = next((t for t in transactions_db if t['id'] == transaction_id), None)

        if not transaction:
            logging.warning(f"Transaction ID {transaction_id} not found.")
            return jsonify({"error": "Transaction not found"}), 404

        logging.info(f"Transaction retrieved: {transaction}")
        return jsonify({"transaction": transaction}), 200

    except Exception as ex:
        logging.error(f"Error retrieving transaction: {str(ex)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/api/transactions', methods=['GET'])
def list_transactions():
    """
    API endpoint to list all cryptocurrency transactions.
    """
    try:
        logging.info("Listing all transactions.")
        return jsonify({"transactions": transactions_db}), 200

    except Exception as ex:
        logging.error(f"Error listing transactions: {str(ex)}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    # Run the Flask application
    # EV SSL certificates should be configured at the server level (e.g., nginx or apache).
    app.run(ssl_context=('cert.pem', 'key.pem'))
```

### Notes:
1. **EV SSL Certificates**: This code assumes that the server hosting the application is configured with EV SSL certificates. Flask's `ssl_context` ensures HTTPS locally.
2. **Anti-DDoS Hosting**: Hosting providers like Cloudflare should be used to implement anti-DDoS features. This is not handled directly in the application code.
3. Replace the placeholder database (`transactions_db`) with a production-ready, secure database solution like PostgreSQL or MongoDB.
4. Configure environment variables securely for production deployment.
