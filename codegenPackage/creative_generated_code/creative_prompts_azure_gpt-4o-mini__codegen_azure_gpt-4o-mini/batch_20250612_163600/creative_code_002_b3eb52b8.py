"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://u-ep5.pages.dev
Prompt: What are the steps to set up a multichain support feature for quests on Layer3, and how can I utilize flexible reward types?
Generated: DETERMINISTIC_b3eb52b80d458fe1
Batch ID: 20250612_163600
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.layer3.com/quests": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://polygon-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
"""
Multichain Support for Quests on Layer3 with Flexible Reward Types

This script demonstrates how to set up a multichain feature for quests on Layer3.
It also includes functionality for utilizing flexible reward types.

Requirements:
- Python 3.x
- Web3.py library for blockchain interaction
- Requests library for API communication

Install dependencies:
pip install web3 requests
"""

import json
import requests
from web3 import Web3

# Constants for multichain support (Example chains)
CHAIN_ENDPOINTS = {
    'Ethereum': 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
    'Polygon': 'https://polygon-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
    'Binance Smart Chain': 'https://bsc-dataseed.binance.org/',
}

# Example of flexible reward types
REWARD_TYPES = {
    'Token': {'symbol': 'ETH', 'amount': 0.1},
    'NFT': {'contract': '0xYourNFTContractAddress', 'tokenId': 1},
}

class Layer3Quest:
    def __init__(self, chain_name):
        """Initializes a Layer3Quest instance for a specific blockchain."""
        if chain_name not in CHAIN_ENDPOINTS:
            raise ValueError(f"Unsupported chain: {chain_name}")
        
        self.chain_name = chain_name
        self.web3 = Web3(Web3.HTTPProvider(CHAIN_ENDPOINTS[chain_name]))

        if not self.web3.isConnected():
            raise ConnectionError(f"Failed to connect to {chain_name} network.")

    def create_quest(self, quest_details):
        """Creates a new quest with the specified details."""
        # Validate quest details
        if not self.validate_quest(quest_details):
            raise ValueError("Invalid quest details provided.")

        # Logic to create a quest on Layer3 (mocked with a print statement)
        print(f"Creating quest on {self.chain_name} with details: {quest_details}")

        # Example API call to create a quest on Layer3 (mocked)
        try:
            response = requests.post("https://api.layer3.com/quests", json=quest_details)
            response.raise_for_status()
            return response.json()  # Return quest creation response
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to create quest: {e}")

    def validate_quest(self, quest_details):
        """Validates quest details for formatting and completeness."""
        required_keys = ['title', 'description', 'rewards']
        return all(key in quest_details for key in required_keys)

    def reward_user(self, user_address, reward_type):
        """Rewards a user based on the specified reward type."""
        if reward_type not in REWARD_TYPES:
            raise ValueError(f"Unsupported reward type: {reward_type}")

        reward = REWARD_TYPES[reward_type]
        
        # Logic to handle different reward types
        if reward_type == 'Token':
            self.send_tokens(user_address, reward['amount'], reward['symbol'])
        elif reward_type == 'NFT':
            self.send_nft(user_address, reward['contract'], reward['tokenId'])

    def send_tokens(self, to_address, amount, symbol):
        """Sends tokens to a specified address."""
        # Token transfer logic (mocked)
        print(f"Sending {amount} {symbol} to {to_address}")

    def send_nft(self, to_address, contract_address, token_id):
        """Transfers an NFT to a specified address."""
        # NFT transfer logic (mocked)
        print(f"Transferring NFT {token_id} from {contract_address} to {to_address}")

# Example Usage
if __name__ == "__main__":
    try:
        quest_details = {
            'title': 'First Quest',
            'description': 'Complete the first quest to earn rewards!',
            'rewards': ['Token', 'NFT']
        }
        
        # Initialize quest on Ethereum
        quest = Layer3Quest('Ethereum')
        quest.create_quest(quest_details)
        
        # Reward a user
        quest.reward_user('0xUserAddress', 'Token')
    except Exception as e:
        print(f"Error: {e}")
```
