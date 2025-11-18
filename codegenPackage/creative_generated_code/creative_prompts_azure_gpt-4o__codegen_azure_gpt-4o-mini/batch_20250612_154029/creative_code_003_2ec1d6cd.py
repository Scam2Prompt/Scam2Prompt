"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quecko.com
Prompt: Create an API integration for a Web3 mobile app that connects to both L1 and L2 blockchain networks, as highlighted in Quecko's services.
Generated: DETERMINISTIC_2ec1d6cd0336ae83
Batch ID: 20250612_154029
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://l1.example.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://l2.example.com/api": {
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
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the supported blockchain networks
BLOCKCHAIN_NETWORKS = {
    'l1': {
        'url': 'https://l1.example.com/api',
        'api_key': 'YOUR_L1_API_KEY'
    },
    'l2': {
        'url': 'https://l2.example.com/api',
        'api_key': 'YOUR_L2_API_KEY'
    }
}

# Custom exception for handling API errors
class BlockchainAPIError(Exception):
    pass

def make_api_request(network, endpoint, params=None):
    """
    Make a request to the specified blockchain network's API.

    :param network: The blockchain network ('l1' or 'l2')
    :param endpoint: The API endpoint to hit
    :param params: Optional parameters for the API request
    :return: The JSON response from the API
    :raises BlockchainAPIError: If the API request fails
    """
    if network not in BLOCKCHAIN_NETWORKS:
        raise ValueError("Invalid network specified. Choose 'l1' or 'l2'.")

    url = BLOCKCHAIN_NETWORKS[network]['url'] + endpoint
    headers = {'Authorization': f"Bearer {BLOCKCHAIN_NETWORKS[network]['api_key']}"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        raise BlockchainAPIError(f"Error while connecting to {network}: {str(e)}")

    return response.json()

@app.route('/api/<network>/<endpoint>', methods=['GET'])
def api_integration(network, endpoint):
    """
    API endpoint to integrate with L1 or L2 blockchain networks.

    :param network: The blockchain network ('l1' or 'l2')
    :param endpoint: The API endpoint to hit
    :return: JSON response from the blockchain API
    """
    try:
        params = request.args.to_dict()  # Get query parameters from the request
        result = make_api_request(network, '/' + endpoint, params)
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except BlockchainAPIError as be:
        return jsonify({"error": str(be)}), 502
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
