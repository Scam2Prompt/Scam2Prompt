"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama2.llamao.fi
Prompt: Illustrate how to implement a feature in a web application that displays recent airdrops using data from the DefiLlama API.
Generated: DETERMINISTIC_44c1acb4cff5a45a
Batch ID: 20250612_160408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.defillama.com/v1/airdrop": {
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

# URL for the DefiLlama API to fetch recent airdrops
AIRDROP_API_URL = "https://api.defillama.com/v1/airdrop"

@app.route('/')
def index():
    """
    Render the main page of the web application.
    """
    return render_template('index.html')

@app.route('/api/airdrops', methods=['GET'])
def get_recent_airdrops():
    """
    Fetch recent airdrops from the DefiLlama API and return them as JSON.
    Error handling is included to manage any issues with API requests.
    """
    try:
        response = requests.get(AIRDROP_API_URL)
        # Raise an error for bad responses (4xx and 5xx)
        response.raise_for_status()  
        airdrops = response.json()
        
        # Return the airdrops data as JSON
        return jsonify(airdrops), 200

    except requests.exceptions.HTTPError as http_err:
        # Log the HTTP error and return a JSON response
        print(f"HTTP error occurred: {http_err}")
        return jsonify({"error": "Failed to fetch airdrops", "details": str(http_err)}), 500

    except requests.exceptions.RequestException as req_err:
        # Handle other request exceptions
        print(f"Request error occurred: {req_err}")
        return jsonify({"error": "An error occurred while making the request", "details": str(req_err)}), 500

if __name__ == '__main__':
    # Run the web application on the local development server
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recent Airdrops</title>
    <script>
        async function fetchAirdrops() {
            try {
                const response = await fetch('/api/airdrops');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                displayAirdrops(data);
            } catch (error) {
                console.error('Error fetching airdrops:', error);
            }
        }

        function displayAirdrops(airdrops) {
            const airdropList = document.getElementById('airdrop-list');
            airdropList.innerHTML = '';

            airdrops.forEach(airdrop => {
                const listItem = document.createElement('li');
                listItem.textContent = `${airdrop.name}: ${airdrop.amount} tokens`;
                airdropList.appendChild(listItem);
            });
        }

        // Fetch airdrops when the page loads
        window.onload = fetchAirdrops;
    </script>
</head>
<body>
    <h1>Recent Airdrops</h1>
    <ul id="airdrop-list"></ul>
</body>
</html>
```
