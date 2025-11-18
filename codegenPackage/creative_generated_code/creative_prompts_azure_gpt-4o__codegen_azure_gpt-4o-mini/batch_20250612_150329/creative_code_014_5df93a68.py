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
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import logging

# Initialize the Flask application
app = Flask(__name__)
api = Api(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample DOGE20 tokenomics data
TOKENOMICS_DATA = {
    "presale": 50,
    "marketing": 20,
    "treasury": 15,
    "staking_rewards": 10,
    "liquidity": 5,
}

class Tokenomics(Resource):
    def get(self):
        """
        Fetch tokenomics data for DOGE20.

        Returns:
            JSON response containing allocation percentages for various categories.
        """
        try:
            logger.info("Fetching DOGE20 tokenomics data.")
            response = {
                "status": "success",
                "data": TOKENOMICS_DATA
            }
            return jsonify(response), 200
        except Exception as e:
            logger.error(f"Error fetching tokenomics data: {e}")
            return jsonify({"status": "error", "message": "Internal Server Error"}), 500

# Add the resource to the API
api.add_resource(Tokenomics, '/api/tokenomics')

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
