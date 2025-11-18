"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Create a web-based documentation page for a smart contract built with Código's CIDL, including all exposed methods, input parameters, and account structures for Solana.
Generated: DETERMINISTIC_d7dd89f9a40f37fe
Batch ID: 20250612_150946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Required imports for the web server and interacting with the Solana blockchain
from flask import Flask, jsonify, render_template
from solana.rpc.api import Client
import json

# Initialize Flask app
app = Flask(__name__)

# Solana RPC endpoint (mainnet-beta by default, can be changed for devnet or testnet)
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

# Initialize Solana client
solana_client = Client(SOLANA_RPC_URL)

# Path to the CIDL (Código Interface Definition Language) file containing the smart contract specification
CIDL_FILE_PATH = "./smart_contract.cidl"

# Load the CIDL file and parse contract details
def load_cidl_data(file_path):
    """
    Load and parse CIDL file to retrieve contract methods, parameters, and structures.
    :param file_path: Path to the CIDL file
    :return: Parsed CIDL data as a dictionary
    """
    try:
        with open(file_path, 'r') as file:
            cidl_data = json.load(file)
        return cidl_data
    except FileNotFoundError:
        return {"error": "CIDL file not found"}
    except json.JSONDecodeError:
        return {"error": "Failed to parse CIDL file"}

# Route to display the documentation page
@app.route('/')
def documentation():
    """
    Main route to load the documentation page.
    It renders an HTML template displaying contract methods and details.
    """
    cidl_data = load_cidl_data(CIDL_FILE_PATH)
    if "error" in cidl_data:
        return jsonify(cidl_data)  # Return the error message if file loading fails.
    return render_template('documentation.html', cidl_data=cidl_data)

# Route to fetch contract methods and details via API
@app.route('/api/contract')
def contract_api():
    """
    API endpoint to fetch smart contract methods and input parameters.
    Returns the parsed CIDL data as a JSON response.
    """
    cidl_data = load_cidl_data(CIDL_FILE_PATH)
    return jsonify(cidl_data)

# Route to fetch account structures from the blockchain
@app.route('/api/accounts/<public_key>')
def fetch_account(public_key):
    """
    API endpoint to fetch account details given a public key.
    :param public_key: Public key of the account
    :return: Account details as a JSON response
    """
    try:
        account_info = solana_client.get_account_info(public_key)
        return jsonify(account_info)
    except Exception as e:
        return jsonify({"error": str(e)})

# HTML template for documentation (stored as documentation.html)
# This should be placed in a templates folder within the project directory.
"""
<!DOCTYPE html>
<html>
<head>
    <title>Smart Contract Documentation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        pre { background: #f8f8f8; padding: 10px; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <h1>Smart Contract Documentation</h1>
    <h2>Contract Methods</h2>
    {% for method in cidl_data.methods %}
        <h3>{{ method.name }}</h3>
        <p><strong>Description:</strong> {{ method.description }}</p>
        <pre><strong>Inputs:</strong> {{ method.inputs | tojson }}</pre>
        <pre><strong>Outputs:</strong> {{ method.outputs | tojson }}</pre>
    {% endfor %}
    <h2>Account Structures</h2>
    {% for structure in cidl_data.structures %}
        <h3>{{ structure.name }}</h3>
        <pre>{{ structure.fields | tojson }}</pre>
    {% endfor %}
</body>
</html>
"""

# Error handling for Flask routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Error handler for 404 - Page Not Found.
    :param e: Exception object
    :return: JSON error message
    """
    return jsonify({"error": "Page not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Error handler for 500 - Internal Server Error.
    :param e: Exception object
    :return: JSON error message
    """
    return jsonify({"error": "Internal server error"}), 500

# Main entry point for the application
if __name__ == "__main__":
    # Run the Flask app on port 5000
    app.run(debug=True, port=5000)
```
