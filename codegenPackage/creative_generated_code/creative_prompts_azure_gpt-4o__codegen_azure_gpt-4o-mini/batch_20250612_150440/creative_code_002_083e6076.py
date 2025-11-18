"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.github.io
Prompt: Provide a step-by-step guide to programmatically query Rocket Pool's smart contracts for staking statistics, including the total amount staked and node operator rewards.
Generated: DETERMINISTIC_083e60769a1305d0
Batch ID: 20250612_150440
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://raw.githubusercontent.com/rocket-pool/rocketpool/master/build/contracts/RocketPool.json": {
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
import json
import requests
from web3 import Web3

# Define constants for the Ethereum network and Rocket Pool smart contracts
ETHEREUM_RPC_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'  # Replace with your Infura Project ID
ROCKET_POOL_CONTRACT_ADDRESS = '0xYourRocketPoolContractAddressHere'  # Replace with the actual contract address
ABI_URL = 'https://raw.githubusercontent.com/rocket-pool/rocketpool/master/build/contracts/RocketPool.json'

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))

# Check if Web3 is connected
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network")

# Load Rocket Pool contract ABI
def load_rocket_pool_abi():
    try:
        response = requests.get(ABI_URL)
        response.raise_for_status()
        abi = json.loads(response.text)
        return abi['abi']
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch ABI: {e}")

# Get total amount staked from the Rocket Pool contract
def get_total_staked(contract):
    try:
        total_staked = contract.functions.totalStaked().call()
        return w3.fromWei(total_staked, 'ether')  # Convert from wei to ether
    except Exception as e:
        raise RuntimeError(f"Error retrieving total staked: {e}")

# Get node operator rewards from the Rocket Pool contract
def get_node_operator_rewards(contract, operator_address):
    try:
        rewards = contract.functions.getNodeOperatorRewards(operator_address).call()
        return w3.fromWei(rewards, 'ether')  # Convert from wei to ether
    except Exception as e:
        raise RuntimeError(f"Error retrieving rewards for {operator_address}: {e}")

# Main function to query staking statistics
def query_staking_statistics(node_operator_address):
    # Load the Rocket Pool contract ABI
    abi = load_rocket_pool_abi()
    
    # Create a contract instance
    rocket_pool_contract = w3.eth.contract(address=ROCKET_POOL_CONTRACT_ADDRESS, abi=abi)

    # Get total amount staked
    total_staked = get_total_staked(rocket_pool_contract)
    
    # Get node operator rewards
    node_rewards = get_node_operator_rewards(rocket_pool_contract, node_operator_address)

    return {
        'total_staked': total_staked,
        'node_operator_rewards': node_rewards
    }

if __name__ == '__main__':
    try:
        # Replace with the actual node operator address
        node_operator_address = '0xYourNodeOperatorAddressHere'
        statistics = query_staking_statistics(node_operator_address)

        print(f"Total Amount Staked: {statistics['total_staked']} ETH")
        print(f"Node Operator Rewards: {statistics['node_operator_rewards']} ETH")
    except Exception as e:
        print(f"An error occurred: {e}")
```
