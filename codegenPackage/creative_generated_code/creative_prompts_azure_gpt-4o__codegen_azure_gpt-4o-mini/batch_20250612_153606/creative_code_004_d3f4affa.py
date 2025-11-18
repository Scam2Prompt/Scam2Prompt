"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Provide a step-by-step guide in code for integrating the OpenSea API to display Robotos NFT assets, including animated GIFs, PNGs, and SVGs, as described on the Robots NFT Minting website.
Generated: DETERMINISTIC_d3f4affa001dbfd4
Batch ID: 20250612_153606
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/assets": {
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
from flask import Flask, render_template

app = Flask(__name__)

# Constants for OpenSea API access
OPENSEA_API_URL = "https://api.opensea.io/api/v1/assets"
CONTRACT_ADDRESS = "YOUR_ROBOTS_CONTRACT_ADDRESS"
API_KEY = "YOUR_OPENSEA_API_KEY"  # Replace with your OpenSea API key

def fetch_nft_assets():
    """
    Fetches NFT assets from the OpenSea API for the specified contract address.

    Returns:
        list: A list of NFT assets.
    """
    try:
        response = requests.get(OPENSEA_API_URL, 
                                params={'asset_contract_address': CONTRACT_ADDRESS,
                                        'order_direction': 'desc',
                                        'offset': '0',
                                        'limit': '20'},
                                headers={'X-API-KEY': API_KEY})
        response.raise_for_status()  # Raises an HTTPError for bad responses
        assets = response.json().get('assets', [])
        return assets
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []

@app.route('/')
def index():
    """
    Renders the main page with NFT assets.
    """
    assets = fetch_nft_assets()
    return render_template('index.html', assets=assets)

if __name__ == '__main__':
    # Running the application
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Robots NFT Assets</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .assets { display: flex; flex-wrap: wrap; }
        .asset { margin: 10px; border: 1px solid #ddd; padding: 10px; border-radius: 4px; }
        img { max-width: 100%; height: auto; }
    </style>
</head>
<body>
    <h1>Robots NFT Assets</h1>
    <div class="assets">
        {% for asset in assets %}
            <div class="asset">
                <h2>{{ asset.name }}</h2>
                {% if asset.image_url %}
                    <img src="{{ asset.image_url }}" alt="{{ asset.name }}">
                {% endif %}
                <p>Token ID: {{ asset.token_id }}</p>
                <p>
                    <a href="{{ asset.permalink }}" target="_blank">View on OpenSea</a>
                </p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

**Note:** Make sure to replace `YOUR_ROBOTS_CONTRACT_ADDRESS` and `YOUR_OPENSEA_API_KEY` with your actual contract address and API key.
