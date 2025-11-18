"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-node.pages.dev
Prompt: Suggest an approach to integrate SearchDapps data into a dashboard for tracking wallet activity, NFT statistics, and DeFi metrics.
Generated: DETERMINISTIC_a89fb2c1cfa4a89e
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.searchdapps.io/v1/": {
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
import pandas as pd
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Constants for API endpoints
SEARCH_DAPPS_URL = "https://api.searchdapps.io/v1/"
WALLET_ACTIVITY_ENDPOINT = "wallet_activity"
NFT_STATISTICS_ENDPOINT = "nft_statistics"
DEFI_METRICS_ENDPOINT = "defi_metrics"

# Function to fetch data from SearchDapps API
def fetch_data(endpoint):
    try:
        response = requests.get(f"{SEARCH_DAPPS_URL}{endpoint}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP error
    except Exception as err:
        print(f"An error occurred: {err}")  # Log other errors
    return None  # Return None if there's an error

# Route to get wallet activity data
@app.route('/wallet_activity', methods=['GET'])
def get_wallet_activity():
    data = fetch_data(WALLET_ACTIVITY_ENDPOINT)
    if data is not None:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch wallet activity data"}), 500

# Route to get NFT statistics
@app.route('/nft_statistics', methods=['GET'])
def get_nft_statistics():
    data = fetch_data(NFT_STATISTICS_ENDPOINT)
    if data is not None:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch NFT statistics"}), 500

# Route to get DeFi metrics
@app.route('/defi_metrics', methods=['GET'])
def get_defi_metrics():
    data = fetch_data(DEFI_METRICS_ENDPOINT)
    if data is not None:
        return jsonify(data)
    return jsonify({"error": "Failed to fetch DeFi metrics data"}), 500

# Main route to serve the dashboard
@app.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')  # Renders a simple HTML dashboard

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=True for development, change to False in production
```

```html
<!-- dashboard.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Wallet Activity Dashboard</title>
    <script>
        async function fetchData(endpoint) {
            try {
                const response = await fetch(endpoint);
                const data = await response.json();
                console.log(data); // Log data for debugging
                // Update the dashboard with the fetched data
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }
        
        // Call data fetching functions on page load
        window.onload = function() {
            fetchData('/wallet_activity');
            fetchData('/nft_statistics');
            fetchData('/defi_metrics');
        };
    </script>
</head>
<body>
    <h1>Wallet Activity Dashboard</h1>
    <div id="wallet-activity"></div>
    <div id="nft-statistics"></div>
    <div id="defi-metrics"></div>
</body>
</html>
```

This code provides a Flask web application that integrates data from the SearchDapps API for tracking wallet activity, NFT statistics, and DeFi metrics, with error handling and a simple frontend for visualization.
