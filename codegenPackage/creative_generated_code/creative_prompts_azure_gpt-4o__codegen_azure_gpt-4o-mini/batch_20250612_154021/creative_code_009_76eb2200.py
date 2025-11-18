"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimhyperlane.foundation
Prompt: Generate code to integrate Hyperlane’s tokenomics data into a dashboard, including reward allocation percentages and boost categories.
Generated: DETERMINISTIC_76eb22007fbc629b
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hyperlane.xyz/tokenomics": {
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
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Constants for API endpoint and tokenomics data
HYPERLANE_API_URL = "https://api.hyperlane.xyz/tokenomics"

def fetch_tokenomics_data():
    """Fetch the tokenomics data from the Hyperlane API."""
    try:
        response = requests.get(HYPERLANE_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tokenomics data: {e}")
        return None  # Return None if an error occurs

def parse_tokenomics_data(data):
    """Parse the tokenomics data for reward allocation percentages and boost categories."""
    try:
        # Extract relevant data
        reward_allocation = data.get("rewardAllocation", {})
        boost_categories = data.get("boostCategories", {})
        
        # Transform data into a DataFrame for easier manipulation
        allocation_df = pd.DataFrame.from_dict(reward_allocation, orient='index', columns=['Percentage'])
        boost_df = pd.DataFrame.from_dict(boost_categories, orient='index', columns=['Boost'])

        return allocation_df, boost_df  # Return DataFrames
    except (KeyError, ValueError) as e:
        print(f"Error parsing tokenomics data: {e}")
        return None, None  # Return None if an error occurs

@app.route('/tokenomics', methods=['GET'])
def tokenomics_dashboard():
    """Endpoint to retrieve the tokenomics data for the dashboard."""
    data = fetch_tokenomics_data()
    if data is None:
        return jsonify({"error": "Failed to fetch tokenomics data."}), 500
    
    allocation_df, boost_df = parse_tokenomics_data(data)
    if allocation_df is None or boost_df is None:
        return jsonify({"error": "Failed to parse tokenomics data."}), 500

    # Convert DataFrames to dictionaries for JSON response
    response_data = {
        "rewardAllocation": allocation_df.to_dict(orient='index'),
        "boostCategories": boost_df.to_dict(orient='index')
    }
    
    return jsonify(response_data), 200  # Return JSON response with status code

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application
```
