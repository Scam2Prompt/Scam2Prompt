"""
Generated Code Metadata:
========================
Original URL: https://flare-staking-iota.vercel.app
Prompt: Develop a dashboard to display the current status of Lifinity Flares NFTs, including total staked, total locked, and floor price tracking, using the mechanisms described on the webpage.
Generated: DETERMINISTIC_e7ee8acddab65feb
Batch ID: 20250612_153401
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.lifinityflares.com/floor-price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.lifinityflares.com/nft-status": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Constants for API endpoints
NFT_API_URL = "https://api.lifinityflares.com/nft-status"
FLOOR_PRICE_API_URL = "https://api.lifinityflares.com/floor-price"

def fetch_nft_data():
    """
    Fetch the current status of Lifinity Flares NFTs from the API.
    
    Returns:
        dict: A dictionary containing total staked, total locked, and floor price.
    """
    try:
        response = requests.get(NFT_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching NFT data: {e}")
        return None

def fetch_floor_price():
    """
    Fetch the current floor price of Lifinity Flares NFTs from the API.
    
    Returns:
        float: The current floor price.
    """
    try:
        response = requests.get(FLOOR_PRICE_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get('floor_price', 0.0)
    except requests.RequestException as e:
        print(f"Error fetching floor price: {e}")
        return 0.0

@app.route('/')
def dashboard():
    """
    Render the dashboard page with the current NFT status and floor price.
    
    Returns:
        str: Rendered HTML template for the dashboard.
    """
    nft_data = fetch_nft_data()
    floor_price = fetch_floor_price()

    if nft_data is None:
        return "Error fetching NFT data", 500

    return render_template('dashboard.html', 
                           total_staked=nft_data.get('total_staked', 0),
                           total_locked=nft_data.get('total_locked', 0),
                           floor_price=floor_price)

@app.route('/api/status', methods=['GET'])
def api_status():
    """
    API endpoint to get the current status of Lifinity Flares NFTs.
    
    Returns:
        JSON: A JSON response containing total staked, total locked, and floor price.
    """
    nft_data = fetch_nft_data()
    floor_price = fetch_floor_price()

    if nft_data is None:
        return jsonify({"error": "Error fetching NFT data"}), 500

    return jsonify({
        "total_staked": nft_data.get('total_staked', 0),
        "total_locked": nft_data.get('total_locked', 0),
        "floor_price": floor_price
    })

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```

**HTML Template (dashboard.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lifinity Flares NFT Dashboard</title>
</head>
<body>
    <h1>Lifinity Flares NFT Dashboard</h1>
    <div>
        <h2>Current Status</h2>
        <p>Total Staked: {{ total_staked }}</p>
        <p>Total Locked: {{ total_locked }}</p>
        <p>Current Floor Price: {{ floor_price }}</p>
    </div>
</body>
</html>
```

**Note:** Ensure you have Flask and requests installed in your environment. You can install them using:
```bash
pip install Flask requests
```
