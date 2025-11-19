"""
Generated Code Metadata:
========================
Original URL: https://everyworld-started.pages.dev
Prompt: Design a web3 rewarded ads platform using a dual incentivization economic model that supports environmental charities.
Generated: DETERMINISTIC_c2ab49f2f32e1cd3
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
from web3 import Web3
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import hashlib

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Web3 Configuration
INFURA_URL = os.getenv('INFURA_URL')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Load contract ABI
with open('RewardAdPlatform.json') as f:
    contract_abi = json.load(f)

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# Database simulation (in production, use a real database)
ads_db = {}
users_db = {}
charities_db = {
    '1': {'name': 'Ocean Cleanup', 'wallet': '0x123...'},
    '2': {'name': 'Forest Foundation', 'wallet': '0x456...'}
}

# Helper functions
def generate_ad_id(ad_data):
    """Generate unique ad ID from ad data"""
    data_str = json.dumps(ad_data, sort_keys=True) + str(datetime.now())
    return hashlib.sha256(data_str.encode()).hexdigest()

def validate_user_wallet(wallet_address):
    """Validate Ethereum wallet address"""
    return Web3.is_address(wallet_address)

def send_transaction(to_address, amount_wei):
    """Send ETH transaction"""
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': amount_wei,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    }
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

# Routes
@app.route('/api/ads', methods=['POST'])
def create_ad():
    """Create a new ad campaign"""
    try:
        data = request.get_json()
        
        # Validate input
        required_fields = ['title', 'description', 'image_url', 'advertiser_wallet', 'reward_per_view', 'charity_percentage']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if not validate_user_wallet(data['advertiser_wallet']):
            return jsonify({'error': 'Invalid wallet address'}), 400
        
        # Generate ad ID
        ad_id = generate_ad_id(data)
        
        # Store ad
        ads_db[ad_id] = {
            **data,
            'id': ad_id,
            'created_at': datetime.now().isoformat(),
            'total_views': 0,
            'total_rewards': 0,
            'total_charity': 0,
            'active': True
        }
        
        return jsonify({'ad_id': ad_id}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ads/<ad_id>/view', methods=['POST'])
def record_ad_view(ad_id):
    """Record an ad view and distribute rewards"""
    try:
        data = request.get_json()
        
        if 'user_wallet' not in data:
            return jsonify({'error': 'User wallet required'}), 400
        
        if not validate_user_wallet(data['user_wallet']):
            return jsonify({'error': 'Invalid wallet address'}), 400
        
        if ad_id not in ads_db:
            return jsonify({'error': 'Ad not found'}), 404
        
        ad = ads_db[ad_id]
        if not ad['active']:
            return jsonify({'error': 'Ad campaign not active'}), 400
        
        # Calculate rewards
        reward = ad['reward_per_view']
        charity_amount = reward * ad['charity_percentage'] / 100
        user_amount = reward - charity_amount
        
        # Update totals
        ad['total_views'] += 1
        ad['total_rewards'] += user_amount
        ad['total_charity'] += charity_amount
        
        # Distribute rewards
        charity_wallet = charities_db[ad['charity_id']]['wallet']
        
        # In production, these would be blockchain transactions
        user_tx_hash = send_transaction(data['user_wallet'], web3.to_wei(user_amount, 'ether'))
        charity_tx_hash = send_transaction(charity_wallet, web3.to_wei(charity_amount, 'ether'))
        
        # Update user stats
        if data['user_wallet'] not in users_db:
            users_db[data['user_wallet']] = {'total_rewards': 0, 'ads_viewed': []}
        
        users_db[data['user_wallet']]['total_rewards'] += user_amount
        users_db[data['user_wallet']]['ads_viewed'].append({
            'ad_id': ad_id,
            'timestamp': datetime.now().isoformat(),
            'reward': user_amount
        })
        
        return jsonify({
            'user_reward': user_amount,
            'charity_donation': charity_amount,
            'user_tx_hash': user_tx_hash,
            'charity_tx_hash': charity_tx_hash
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ads', methods=['GET'])
def get_active_ads():
    """Get all active ads"""
    try:
        active_ads = [ad for ad in ads_db.values() if ad['active']]
        return jsonify(active_ads), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/<wallet_address>', methods=['GET'])
def get_user_stats(wallet_address):
    """Get user statistics"""
    try:
        if not validate_user_wallet(wallet_address):
            return jsonify({'error': 'Invalid wallet address'}), 400
        
        if wallet_address not in users_db:
            return jsonify({'total_rewards': 0, 'ads_viewed': []}), 200
        
        return jsonify(users_db[wallet_address]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/charities', methods=['GET'])
def get_charities():
    """Get list of supported charities"""
    try:
        return jsonify(list(charities_db.values())), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RewardAdPlatform is Ownable {
    struct AdCampaign {
        address advertiser;
        string title;
        string description;
        string imageUrl;
        uint256 rewardPerView;
        uint256 charityPercentage;
        uint256 totalViews;
        uint256 totalRewards;
        uint256 totalCharity;
        bool active;
    }

    struct Charity {
        string name;
        address wallet;
    }

    IERC20 public rewardToken;
    mapping(bytes32 => AdCampaign) public adCampaigns;
    mapping(uint256 => Charity) public charities;
    mapping(address => uint256) public userRewards;
    mapping(address => mapping(bytes32 => uint256)) public userAdViews;

    event AdCampaignCreated(bytes32 adId, address advertiser);
    event AdViewed(bytes32 adId, address viewer, uint256 userReward, uint256 charityDonation);
    event RewardsClaimed(address user, uint256 amount);
    event CharityAdded(uint256 charityId, string name, address wallet);

    constructor(address _rewardToken) {
        rewardToken = IERC20(_rewardToken);
    }

    function createAdCampaign(
        string memory title,
        string memory description,
        string memory imageUrl,
        uint256 rewardPerView,
        uint256 charityPercentage,
        uint256 charityId
    ) external payable returns (bytes32) {
        require(charityPercentage <= 100, "Charity percentage must be <= 100");
        require(charities[charityId].wallet != address(0), "Invalid charity");
        require(msg.value >= rewardPerView, "Insufficient funds for initial reward pool");

        bytes32 adId = keccak
