"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://liveonlinetv.org
Prompt: Create an API integration example for accessing live TV channels, inspired by the streaming options listed on LiveOnlineTV.org.
Generated: DETERMINISTIC_15aa3d3851a5043c
Batch ID: 20250612_161654
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/live-channels": {
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

# Configuration for the external TV channel API
API_URL = "https://api.example.com/live-channels"  # Replace with the actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Custom exception for API errors
class APIError(Exception):
    pass

def fetch_live_channels():
    """
    Fetch live TV channels from the external API.

    Returns:
        list: A list of live TV channels.

    Raises:
        APIError: If the API request fails or returns an error response.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    except requests.RequestException as e:
        raise APIError(f"Failed to fetch channels: {e}")

    return response.json()["channels"]

@app.route('/api/live-channels', methods=['GET'])
def get_live_channels():
    """
    Endpoint to retrieve live TV channels.

    Returns:
        JSON response containing a list of live TV channels.
        If an error occurs, a JSON error message is returned.
    """
    try:
        channels = fetch_live_channels()
        return jsonify({"success": True, "channels": channels}), 200
    except APIError as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
