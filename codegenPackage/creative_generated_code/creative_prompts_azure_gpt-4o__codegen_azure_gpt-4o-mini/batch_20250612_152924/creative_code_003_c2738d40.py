"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica12.vercel.app
Prompt: Create a script to display stats from Matrica for Solana, Ethereum, and Polygon networks in a web application.
Generated: DETERMINISTIC_c2738d4092f0c479
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.matrica.com/stats": {
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
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# URL for the Matrica API
MATRICA_API_URL = "https://api.matrica.com/stats"

# Supported networks
SUPPORTED_NETWORKS = ["solana", "ethereum", "polygon"]

def fetch_network_stats(network):
    """
    Fetch network statistics from Matrica API for a given network.

    Args:
        network (str): The network to fetch stats for.

    Returns:
        dict: The response data from the API if successful.

    Raises:
        ValueError: If the network is not supported.
        Exception: If an error occurs while fetching data.
    """
    if network not in SUPPORTED_NETWORKS:
        raise ValueError(f"Network '{network}' is not supported.")

    try:
        response = requests.get(f"{MATRICA_API_URL}/{network}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch stats for {network}: {str(e)}")

@app.route('/')
def index():
    """
    Render the main page of the application.
    
    Returns:
        str: Rendered HTML template for the main page.
    """
    return render_template('index.html')

@app.route('/stats/<network>', methods=['GET'])
def get_stats(network):
    """
    Endpoint to get statistics for a specific network.

    Args:
        network (str): The name of the network to fetch stats for.

    Returns:
        json: JSON response containing the network stats or an error message.
    """
    try:
        stats = fetch_network_stats(network)
        return jsonify(stats), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the Flask web application
    app.run(host='0.0.0.0', port=5000)
```

**HTML Template (`templates/index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matrica Stats</title>
</head>
<body>
    <h1>Matrica Network Statistics</h1>
    <div>
        <h2>Supported Networks:</h2>
        <ul>
            <li><a href="/stats/solana">Solana</a></li>
            <li><a href="/stats/ethereum">Ethereum</a></li>
            <li><a href="/stats/polygon">Polygon</a></li>
        </ul>
    </div>
</body>
</html>
```

**Requirements:**
- Install Flask and requests:
```bash
pip install Flask requests
```

This script sets up a simple Flask web application to fetch and display statistics from the Matrica API for the Solana, Ethereum, and Polygon networks.
