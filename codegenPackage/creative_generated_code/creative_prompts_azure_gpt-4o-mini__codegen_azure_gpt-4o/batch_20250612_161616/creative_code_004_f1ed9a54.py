"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld2.pages.dev
Prompt: What libraries or APIs would you recommend for building a web3 application that supports rewarded ads and environmental initiatives, as seen in Everyworld?
Generated: DETERMINISTIC_f1ed9a54f0820b77
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for a Web3 application with rewarded ads and environmental initiatives

# Flask for backend API development
from flask import Flask, jsonify, request

# web3.py for blockchain interaction
from web3 import Web3

# dotenv for environment variable management
from dotenv import load_dotenv
import os

# pymongo for database management (storing user rewards, ad data, and environmental impact records)
from pymongo import MongoClient

# Requests for making HTTP requests (if needed for external API interaction)
import requests

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize Web3 connection
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint for Ethereum network access
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Verify Web3 connection
if web3.isConnected():
    print("Connected to Ethereum network")
else:
    raise ConnectionError("Failed to connect to Ethereum network")

# MongoDB connection setup
MONGO_URI = os.getenv("MONGO_URI")  # MongoDB connection string
client = MongoClient(MONGO_URI)
db = client['web3_app']  # Database name
collection_rewards = db['rewards']  # Collection for storing user rewards
collection_ads = db['ads']  # Collection for storing ads data
collection_environment = db['environment']  # Collection for storing environmental initiative data

# Route for serving rewarded ads
@app.route('/api/rewarded_ad', methods=['GET'])
def serve_rewarded_ad():
    try:
        # Fetch an ad from the database
        ad = collection_ads.find_one()
        if ad:
            return jsonify({"success": True, "ad": ad}), 200
        else:
            return jsonify({"success": False, "message": "No ads available"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Route for registering user rewards after ad interaction
@app.route('/api/reward', methods=['POST'])
def register_reward():
    try:
        user_data = request.json
        # Validate input data
        if not user_data.get("user_id") or not user_data.get("ad_id"):
            return jsonify({"success": False, "message": "Missing user_id or ad_id"}), 400
        
        # Store reward record in database
        reward_record = {
            "user_id": user_data["user_id"],
            "ad_id": user_data["ad_id"],
            "reward_amount": user_data.get("reward_amount", 0),  # Default reward amount if not provided
            "timestamp": web3.eth.get_block('latest')['timestamp']
        }
        collection_rewards.insert_one(reward_record)
        
        return jsonify({"success": True, "message": "Reward registered successfully"}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Route for supporting environmental initiatives
@app.route('/api/environment', methods=['POST'])
def support_environment():
    try:
        initiative = request.json
        # Validate input data
        if not initiative.get("initiative_name") or not initiative.get("contribution_amount"):
            return jsonify({"success": False, "message": "Missing initiative_name or contribution_amount"}), 400
        
        # Store environmental initiative record in database
        initiative_record = {
            "initiative_name": initiative["initiative_name"],
            "contribution_amount": initiative["contribution_amount"],
            "timestamp": web3.eth.get_block('latest')['timestamp']
        }
        collection_environment.insert_one(initiative_record)
        
        return jsonify({"success": True, "message": "Environmental initiative supported successfully"}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
1. Set up a `.env` file with keys like `INFURA_URL` and `MONGO_URI` for secure configuration.
2. MongoDB collections (`rewards`, `ads`, `environment`) need to be pre-structured.
3. This script is a basic starting point and may need additional features like user authentication, ad targeting logic, blockchain smart contract integration, and more for a production-ready system.
