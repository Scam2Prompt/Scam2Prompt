"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocket-pool.xyz
Prompt: Write a script in Python to query Rocket Pool's node staking APR and calculate potential rewards for staking ETH by running an Ethereum node. Use web3.py to fetch real-time data from Rocket Pool's smart contracts.
Generated: DETERMINISTIC_40845913fbd8074d
Batch ID: 20250612_153821
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
import json
from web3 import Web3
from decimal import Decimal

# Define constants
RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID or preferred Ethereum node RPC URL
ROCKET_POOL_CONTRACT_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with Rocket Pool smart contract address
ROCKET_POOL_ABI_PATH = "rocket_pool_abi.json"  # Path to the contract ABI JSON file

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Check connection
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum network. Check your RPC URL.")

# Load Rocket Pool contract ABI
try:
    with open(ROCKET_POOL_ABI_PATH, 'r') as abi_file:
        rocket_pool_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError(f"ABI file not found at path: {ROCKET_POOL_ABI_PATH}")
except json.JSONDecodeError:
    raise ValueError(f"Invalid ABI JSON format in file: {ROCKET_POOL_ABI_PATH}")

# Instantiate Rocket Pool contract
rocket_pool_contract = web3.eth.contract(address=ROCKET_POOL_CONTRACT_ADDRESS, abi=rocket_pool_abi)

# Define function to fetch node operator APR
def fetch_node_operator_apr():
    try:
        # Call the Rocket Pool smart contract function to get APR
        apr = rocket_pool_contract.functions.getNodeOperatorStakingAPR().call()
        return Decimal(apr) / 100  # Convert APR to a percentage (assuming the contract returns APR in basis points)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch APR from Rocket Pool contract: {e}")

# Define function to calculate staking rewards
def calculate_rewards(eth_amount, apr, duration_years):
    """
    Calculate potential staking rewards for running an Ethereum node.
    
    :param eth_amount: Amount of ETH staked.
    :param apr: Annual Percentage Rate (APR) as a decimal.
    :param duration_years: Duration of staking in years.
    :return: Potential rewards in ETH.
    """
    try:
        if eth_amount <= 0 or duration_years <= 0:
            raise ValueError("ETH amount and duration must be positive numbers.")
        
        # Calculate rewards using simple interest formula: rewards = principal * rate * time
        rewards = eth_amount * apr * duration_years
        return rewards
    except Exception as e:
        raise RuntimeError(f"Error calculating rewards: {e}")

# Main function
def main():
    try:
        print("Connecting to Ethereum network...")
        apr = fetch_node_operator_apr()
        print(f"Rocket Pool Node Operator Staking APR: {apr:.2%}")
        
        # Example usage: Calculate rewards for staking 32 ETH for 1 year
        eth_staked = Decimal(32)  # Example staking amount
        staking_duration = Decimal(1)  # Staking period in years
        
        rewards = calculate_rewards(eth_staked, apr, staking_duration)
        print(f"Potential rewards for staking {eth_staked} ETH for {staking_duration} year(s): {rewards:.4f} ETH")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```

**Note:** Replace placeholders (`YOUR_INFURA_PROJECT_ID`, `ROCKET_POOL_CONTRACT_ADDRESS`, and `ROCKET_POOL_ABI_PATH`) with actual values for the script to run successfully. Ensure that the ABI JSON file matches the Rocket Pool smart contract's ABI.
