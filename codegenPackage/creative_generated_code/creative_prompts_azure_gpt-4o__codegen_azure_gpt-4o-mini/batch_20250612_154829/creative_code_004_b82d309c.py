"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad-og-tnymxw.nfts2.me
Prompt: Implement a script to track and display the number of NFTs minted through a referral link on the Monad OG Chain, using data provided by NFTs2Me.com.
Generated: DETERMINISTIC_b82d309c825019fc
Batch ID: 20250612_154829
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nfts2me.com/minted-nfts": {
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

# Configuration for the NFTs2Me API
NFTS2ME_API_URL = "https://api.nfts2me.com/minted-nfts"
REFERRAL_QUERY_PARAM = "referral"

def fetch_minted_nfts(referral_link):
    """
    Fetch the number of NFTs minted through a specific referral link.

    Parameters:
    - referral_link (str): The referral link to track.

    Returns:
    - int: The number of NFTs minted through the referral link.
    """
    try:
        response = requests.get(NFTS2ME_API_URL, params={REFERRAL_QUERY_PARAM: referral_link})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Assuming the API returns a JSON object with a key 'minted_count'
        return data.get('minted_count', 0)
    except requests.RequestException as e:
        # Log the error (in production, consider using a logging framework)
        print(f"Error fetching data from NFTs2Me.com: {e}")
        return 0  # Return 0 if there's an error

@app.route('/track_nfts', methods=['GET'])
def track_nfts():
    """
    API endpoint to track NFTs minted through a referral link.

    Returns:
    - JSON response with the count of minted NFTs.
    """
    referral_link = request.args.get('referral')
    
    if not referral_link:
        # Return an error response if the referral link is missing
        return jsonify({"error": "Missing referral link"}), 400

    # Fetch the number of minted NFTs
    minted_count = fetch_minted_nfts(referral_link)
    
    # Return the result as a JSON response
    return jsonify({"referral_link": referral_link, "minted_count": minted_count})

if __name__ == '__main__':
    # Run the Flask application on localhost with debugging disabled for production
    app.run(host='0.0.0.0', port=5000, debug=False)
```
