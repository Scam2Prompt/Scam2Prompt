"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claimm.pages.dev
Prompt: Develop an API endpoint to fetch DOGE20 tokenomics data, including the allocation percentages for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_5df93a688f196183
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
from flask import Flask, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)

# Define DOGE20 tokenomics data
TOKENOMICS_DATA = {
    "presale": 40.0,      # Percentage allocated for presale
    "marketing": 20.0,    # Percentage allocated for marketing
    "treasury": 15.0,     # Percentage allocated for treasury
    "staking_rewards": 15.0,  # Percentage allocated for staking rewards
    "liquidity": 10.0     # Percentage allocated for liquidity
}

@app.route('/api/tokenomics', methods=['GET'])
def get_tokenomics():
    """
    API Endpoint to fetch DOGE20 tokenomics data.
    Returns:
        JSON response containing allocation percentages for DOGE20 tokenomics.
    """
    try:
        # Log the request for tracking purposes
        logging.info("Fetching DOGE20 tokenomics data.")
        
        # Respond with the tokenomics data
        return jsonify({
            "success": True,
            "data": TOKENOMICS_DATA
        }), 200
    except Exception as e:
        # Log the error
        logging.error(f"An error occurred while fetching tokenomics data: {e}")
        
        # Return an error response
        return jsonify({
            "success": False,
            "message": "An error occurred while fetching tokenomics data."
        }), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False in production
```

This code defines a Flask API endpoint that provides DOGE20 tokenomics data in a clean, efficient, and well-documented manner.
