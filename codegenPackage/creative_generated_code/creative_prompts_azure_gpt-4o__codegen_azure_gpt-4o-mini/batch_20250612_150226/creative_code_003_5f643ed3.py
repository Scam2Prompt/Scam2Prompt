"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Create a Python script using Web3.py to connect a wallet and calculate potential returns for MAMO token purchases based on presale stage pricing.
Generated: DETERMINISTIC_5f643ed39bf8387d
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from collections import namedtuple

# Define constants for MAMO token sale stages
SaleStage = namedtuple('SaleStage', ['name', 'price_per_token', 'token_supply'])

# Configuration for the MAMO token presale
presale_stages = [
    SaleStage('Stage 1', Web3.toWei(0.01, 'ether'), 1000000),  # Price for Stage 1
    SaleStage('Stage 2', Web3.toWei(0.02, 'ether'), 2000000),  # Price for Stage 2
    SaleStage('Stage 3', Web3.toWei(0.03, 'ether'), 3000000),  # Price for Stage 3
]

# Connect to Ethereum network
def connect_to_blockchain(infura_url):
    """ Connects to Ethereum network using Web3. """
    try:
        w3 = Web3(Web3.HTTPProvider(infura_url))
        if not w3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum network.")
        return w3
    except Exception as e:
        print(f"Error connecting to blockchain: {e}")
        return None

# Calculate potential returns based on tokens purchased
def calculate_returns(tokens_purchased, current_stage):
    """ Calculate potential returns based on tokens purchased. """
    if tokens_purchased < 0:
        raise ValueError("Tokens purchased cannot be negative.")
    return tokens_purchased * current_stage.price_per_token

def main():
    # Set your Infura URL here (ensure to replace it with your actual Infura project URL)
    infura_url = os.getenv('INFURA_URL')  # Load Infura URL from environment variables

    # Connect to the Ethereum blockchain
    w3 = connect_to_blockchain(infura_url)
    if w3 is None:
        return

    # Example: Specify the presale stage and amount of tokens to purchase
    current_stage = presale_stages[0]  # Change index to select different stage
    tokens_to_purchase = 100  # Change this value for different calculations

    try:
        # Calculate the potential returns
        potential_investment = calculate_returns(tokens_to_purchase, current_stage)
        
        print(f"Stage: {current_stage.name}")
        print(f"Price per Token: {Web3.fromWei(current_stage.price_per_token, 'ether')} ETH")
        print(f"Tokens Purchased: {tokens_to_purchase}")
        print(f"Potential Investment: {Web3.fromWei(potential_investment, 'ether')} ETH")
    except ValueError as ve:
        print(f"Value Error: {ve}")

if __name__ == "__main__":
    main()
```
