"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-api.pages.dev
Prompt: Generate a script to display the tokenomics breakdown of $MK, including presale allocation, staking rewards, DEX liquidity, and community rewards.
Generated: DETERMINISTIC_3b456de8d9b4e8c7
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Tokenomics data for $MK
TOKENOMICS_DATA = {
    "total_supply": 1000000,  # Total supply of $MK tokens
    "allocation": {
        "presale": 0.25,  # 25% for presale
        "staking_rewards": 0.20,  # 20% for staking rewards
        "dex_liquidity": 0.30,  # 30% for DEX liquidity
        "community_rewards": 0.25  # 25% for community rewards
    }
}

@app.route('/tokenomics', methods=['GET'])
def get_tokenomics():
    """
    GET endpoint to retrieve the tokenomics breakdown of $MK.
    Returns a JSON response with total supply and allocation percentages.
    """
    try:
        # Prepare the response data
        response_data = {
            "total_supply": TOKENOMICS_DATA["total_supply"],
            "allocation": {
                "presale": TOKENOMICS_DATA["allocation"]["presale"] * 100,
                "staking_rewards": TOKENOMICS_DATA["allocation"]["staking_rewards"] * 100,
                "dex_liquidity": TOKENOMICS_DATA["allocation"]["dex_liquidity"] * 100,
                "community_rewards": TOKENOMICS_DATA["allocation"]["community_rewards"] * 100
            }
        }
        return jsonify(response_data), 200  # Return JSON response with status code 200 (OK)
    
    except Exception as e:
        # Log the error (this could be improved with proper logging)
        print(f"Error retrieving tokenomics: {e}")
        return jsonify({"error": "Internal Server Error"}), 500  # Return an error response with status code 500

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)  # Avoid debug mode in production
    except Exception as e:
        print(f"Error starting the server: {e}")  # Handle server start errors
```
