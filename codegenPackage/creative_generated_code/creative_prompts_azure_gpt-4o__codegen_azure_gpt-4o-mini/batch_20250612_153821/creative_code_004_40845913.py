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
  "https://api.etherscan.io/api": {
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
import os
import json
import requests
from web3 import Web3

# Constants
ROCKET_POOL_CONTRACT_ADDRESS = "0xYourRocketPoolContractAddress"
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
RPC_PROVIDER_URL = os.getenv("ETH_RPC_PROVIDER_URL")

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(RPC_PROVIDER_URL))

# ABI for the Rocket Pool contract (simplified for the example, you should use the actual ABI)
rocket_pool_abi = json.loads("""
[
    {
        "constant": true,
        "inputs": [],
        "name": "getAPR",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
""")

def get_apr():
    """Fetch the annual percentage rate (APR) for staking from the Rocket Pool contract."""
    try:
        # Create a contract instance
        rocket_pool_contract = web3.eth.contract(address=ROCKET_POOL_CONTRACT_ADDRESS, abi=rocket_pool_abi)

        # Call the getAPR function from the contract
        apr = rocket_pool_contract.functions.getAPR().call()
        return apr / 1e18  # Adjust for wei-to-ether conversion
    except Exception as e:
        print(f"Error fetching APR: {e}")
        return None

def calculate_rewards(staked_amount, apr, duration_years):
    """Calculate potential rewards for staking ETH based on APR and duration.
    
    Args:
        staked_amount (float): Amount of ETH staked.
        apr (float): Annual percentage rate as a decimal.
        duration_years (float): Duration in years for staking.
        
    Returns:
        float: Potential rewards in ETH.
    """
    return staked_amount * apr * duration_years

def main():
    """Main function to execute the script."""
    # Retrieve APR
    apr = get_apr()
    if apr is None:
        print("Could not retrieve APR. Exiting.")
        return

    # Define staking parameters
    staked_amount_eth = 10  # Amount of ETH to stake
    duration_years = 1      # Duration for staking in years

    # Calculate potential rewards
    potential_rewards = calculate_rewards(staked_amount_eth, apr, duration_years)

    # Output the results
    print(f"Staked Amount: {staked_amount_eth} ETH")
    print(f"APR: {apr:.2%}")
    print(f"Potential Rewards in {duration_years} year(s): {potential_rewards:.4f} ETH")

if __name__ == "__main__":
    main()
```

**Note**: Ensure to replace `0xYourRocketPoolContractAddress` with the actual Rocket Pool contract address and set the environment variables `ETHERSCAN_API_KEY` and `ETH_RPC_PROVIDER_URL` to your respective values before running the script.
