"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-daop.web.app
Prompt: Develop a dashboard interface to show NFT collection details such as floor price, trading volume, and total sales using Tensor's API data.
Generated: DETERMINISTIC_c95ffe29f9356488
Batch ID: 20250612_153648
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.tensornft.com/v1/": {
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
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Base URL for Tensor's API
BASE_URL = "https://api.tensornft.com/v1/"

# Function to fetch NFT collection data
def fetch_nft_collection_data(collection_id):
    """
    Fetches NFT collection data from Tensor's API.

    :param collection_id: str - The ID of the NFT collection.
    :return: dict - The collection data including floor price, trading volume, and total sales.
    :raises ValueError: If the API response is not successful.
    """
    try:
        response = requests.get(f"{BASE_URL}collections/{collection_id}")
        response.raise_for_status()  # Raise an error for HTTP errors
        data = response.json()
        
        # Check if required fields are present in the response
        if not all(key in data for key in ('floor_price', 'trading_volume', 'total_sales')):
            raise ValueError("Incomplete data received from API.")
        
        return {
            "floor_price": data['floor_price'],
            "trading_volume": data['trading_volume'],
            "total_sales": data['total_sales']
        }
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Network error occurred: {e}")
        return {"error": "Network error occurred while fetching data."}
    except ValueError as e:
        # Handle value errors
        print(f"Value error: {e}")
        return {"error": str(e)}

@app.route('/nft_dashboard/<collection_id>', methods=['GET'])
def nft_dashboard(collection_id):
    """
    Dashboard route to display NFT collection details.

    :param collection_id: str - The ID of the NFT collection.
    :return: JSON response with NFT collection details or error message.
    """
    nft_data = fetch_nft_collection_data(collection_id)
    return jsonify(nft_data)

@app.route('/')
def index():
    """
    Render the main dashboard interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>NFT Dashboard</h1>
        <form id="nftForm">
            <div class="form-group">
                <label for="collectionId">Enter NFT Collection ID:</label>
                <input type="text" class="form-control" id="collectionId" required>
            </div>
            <button type="submit" class="btn btn-primary">Get Collection Data</button>
        </form>
        <div id="nftData" class="mt-4"></div>
    </div>

    <script>
        document.getElementById('nftForm').addEventListener('submit', function (event) {
            event.preventDefault();
            const collectionId = document.getElementById('collectionId').value;
            fetch(`/nft_dashboard/${collectionId}`)
                .then(response => response.json())
                .then(data => {
                    const nftDataDiv = document.getElementById('nftData');
                    nftDataDiv.innerHTML = '';
                    if (data.error) {
                        nftDataDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
                    } else {
                        nftDataDiv.innerHTML = `
                            <div class="alert alert-success">
                                <strong>Floor Price:</strong> ${data.floor_price}<br>
                                <strong>Trading Volume:</strong> ${data.trading_volume}<br>
                                <strong>Total Sales:</strong> ${data.total_sales}
                            </div>`;
                    }
                })
                .catch(error => {
                    console.error('Error fetching NFT data:', error);
                });
        });
    </script>
</body>
</html>
```
