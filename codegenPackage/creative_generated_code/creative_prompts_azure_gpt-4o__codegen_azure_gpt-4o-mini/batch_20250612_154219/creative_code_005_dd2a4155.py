"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applecoin-49f.pages.dev
Prompt: Develop a Solana blockchain explorer tool that highlights community-owned tokens like $SILLY and their decentralized distribution model.
Generated: DETERMINISTIC_dd2a41551c2cadfa
Batch ID: 20250612_154219
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
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration Constants
SOLANA_API_URL = "https://api.mainnet-beta.solana.com"
TOKEN_CONFIG = {
    "SILLY": {
        "name": "$SILLY",
        "symbol": "SILLY",
        "decimals": 9,
    },
    # Additional tokens can be added here
}

def fetch_token_info(token_address):
    """
    Fetch token information from Solana API using the specified token address.

    Args:
        token_address (str): The public key of the token.

    Returns:
        dict: The token information if successful, None otherwise.
    """
    try:
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenSupply",
            "params": [token_address]
        }

        response = requests.post(SOLANA_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad HTTP response

        data = response.json()
        if "result" in data:
            return data["result"]
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching token info: {e}")
        return None

@app.route('/tokens', methods=['GET'])
def get_tokens():
    """
    Endpoint to retrieve community-owned tokens and their distribution info.

    Returns:
        JSON: A list of community-owned tokens with their distribution info.
    """
    tokens_info = []

    for token_key, token_value in TOKEN_CONFIG.items():
        token_address = get_token_address(token_key)  # Function to resolve the token address
        token_supply_info = fetch_token_info(token_address)

        if token_supply_info:
            tokens_info.append({
                "name": token_value["name"],
                "symbol": token_value["symbol"],
                "total_supply": token_supply_info.get("value", {}).get("amount", 0),
                "decimals": token_value["decimals"],
            })

    return jsonify(tokens_info)

def get_token_address(token_key):
    """
    Resolves the token address based on the token key.

    Args:
        token_key (str): The key representing the token.

    Returns:
        str: The corresponding token address or None if not found.
    """
    # Replace with actual token address lookup logic
    token_addresses = {
        "SILLY": "TokenAddressHere",  # Replace with actual token address
    }
    return token_addresses.get(token_key)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
