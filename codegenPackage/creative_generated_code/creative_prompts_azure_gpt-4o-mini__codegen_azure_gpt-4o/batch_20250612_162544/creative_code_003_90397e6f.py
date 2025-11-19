"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chibiheadnft.com
Prompt: Create an API call to check the availability of Chibi Head NFTs and display the results on a webpage.
Generated: DETERMINISTIC_90397e6f97a9589b
Batch ID: 20250612_162544
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/chibi-head-nfts": {
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
from flask import Flask, jsonify, render_template, request
import requests

# Flask application setup
app = Flask(__name__)

# API endpoint and configuration
CHIBI_NFT_API_URL = "https://api.example.com/chibi-head-nfts"  # Replace with the actual API URL
TIMEOUT = 10  # Timeout for API requests in seconds

@app.route('/')
def home():
    """
    Renders the homepage.
    """
    return render_template('index.html')  # Ensure `index.html` exists in the templates folder

@app.route('/check-chibi-nfts', methods=['GET'])
def check_chibi_nfts():
    """
    Endpoint to check the availability of Chibi Head NFTs.
    Makes an API call to fetch the data and returns it to the client.
    """
    try:
        # Make the API call
        response = requests.get(CHIBI_NFT_API_URL, timeout=TIMEOUT)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        
        # Parse the JSON response
        nft_data = response.json()
        
        # Return the data as JSON
        return jsonify({
            "success": True,
            "data": nft_data
        })
    except requests.exceptions.RequestException as e:
        # Handle API errors
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# HTML template for the webpage
# Save this as 'templates/index.html'
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chibi Head NFTs Availability</title>
    <script>
        async function fetchNFTs() {
            try {
                const response = await fetch('/check-chibi-nfts');
                const result = await response.json();
                
                const outputDiv = document.getElementById('output');
                
                if (result.success) {
                    outputDiv.innerHTML = JSON.stringify(result.data, null, 2);
                } else {
                    outputDiv.innerHTML = `Error: ${result.error}`;
                }
            } catch (error) {
                console.error("Error fetching NFTs:", error);
                document.getElementById('output').innerHTML = "An error occurred while fetching NFT data.";
            }
        }
    </script>
</head>
<body>
    <h1>Chibi Head NFTs Availability</h1>
    <button onclick="fetchNFTs()">Check Availability</button>
    <pre id="output"></pre>
</body>
</html>
"""

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)  # Use debug=True only in development; change to False in production
```
