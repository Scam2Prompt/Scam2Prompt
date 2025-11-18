"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockprocurator.pages.dev
Prompt: Develop a dashboard that uses Multichain’s Explorer API to display cross-chain transaction details for multiple supported chains.
Generated: DETERMINISTIC_ea69f40cf39045bb
Batch ID: 20250612_150946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://explorer.multichain.com/api": {
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
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Multichain Explorer API base URL
API_BASE_URL = "https://explorer.multichain.com/api"

# Supported chains
SUPPORTED_CHAINS = [
    "Ethereum",
    "Binance Smart Chain",
    "Polygon",
    "Avalanche",
    "Fantom"
]

def fetch_transaction_details(chain, transaction_id):
    """
    Fetches transaction details from Multichain's Explorer API.

    Args:
        chain (str): Name of the blockchain.
        transaction_id (str): Transaction ID.

    Returns:
        dict: Transaction details if found, else an error message.
    """
    url = f"{API_BASE_URL}/{chain}/transaction/{transaction_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}

@app.route('/')
def index():
    """
    Renders the main dashboard page.
    
    Returns:
        str: Rendered HTML template for the dashboard.
    """
    return render_template('dashboard.html', chains=SUPPORTED_CHAINS)

@app.route('/transaction/<chain>/<transaction_id>', methods=['GET'])
def transaction_info(chain, transaction_id):
    """
    Endpoint to fetch transaction information based on the chain and transaction ID.
    
    Args:
        chain (str): Name of the blockchain.
        transaction_id (str): Transaction ID.

    Returns:
        JSON: Transaction details or error message.
    """
    if chain not in SUPPORTED_CHAINS:
        return jsonify({"error": "Chain not supported."}), 400

    transaction_details = fetch_transaction_details(chain, transaction_id)
    return jsonify(transaction_details)

if __name__ == '__main__':
    # Run the Flask application on the specified host and port
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### HTML Template (dashboard.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multichain Dashboard</title>
</head>
<body>
    <h1>Multichain Dashboard</h1>
    <h2>Supported Chains</h2>
    <ul>
        {% for chain in chains %}
            <li>{{ chain }}</li>
        {% endfor %}
    </ul>
    <h2>Transaction Lookup</h2>
    <form action="" method="get">
        <label for="chain">Chain:</label>
        <select id="chain" name="chain">
            {% for chain in chains %}
                <option value="{{ chain }}">{{ chain }}</option>
            {% endfor %}
        </select>
        <label for="transaction_id">Transaction ID:</label>
        <input type="text" id="transaction_id" name="transaction_id">
        <button type="submit">Fetch Transaction</button>
    </form>
</body>
</html>
```

### Notes 
- Make sure you have Flask installed in your Python environment.
- The above code assumes an HTML template is saved as `dashboard.html` in a `templates` folder within the same directory as the Python script.
- The application will run in a Flask development server; for production, consider using a WSGI server like Gunicorn.
