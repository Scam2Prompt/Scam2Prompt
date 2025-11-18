"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofinance.blogspot.com
Prompt: Write a script to query and display the list of node operators and reward distribution records from Lido Finance's staking pool smart contract.
Generated: DETERMINISTIC_c8d5232bf0d3011e
Batch ID: 20250612_142640
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://raw.githubusercontent.com/lidofinance/lido-dao/main/contracts/abi/Lido.json": {
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
import requests
from web3 import Web3
from web3.exceptions import ContractLogicError

# Configuration
RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
LIDO_CONTRACT_ADDRESS = "0x7eDb476bE6Ccb6C663C7a9c4cAe5dACb0b7604bD"  # Lido staking pool contract address
ABI_URL = "https://raw.githubusercontent.com/lidofinance/lido-dao/main/contracts/abi/Lido.json"  # ABI file URL

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(RPC_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Fetch the contract ABI from the provided URL
try:
    response = requests.get(ABI_URL)
    response.raise_for_status()
    lido_abi = response.json()
except requests.exceptions.RequestException as e:
    raise RuntimeError(f"Failed to fetch contract ABI: {e}")

# Initialize the Lido contract instance
lido_contract = web3.eth.contract(address=LIDO_CONTRACT_ADDRESS, abi=lido_abi)

def get_node_operators():
    """
    Fetch the list of node operators from the Lido contract.
    """
    try:
        node_operator_count = lido_contract.functions.getNodeOperatorsCount().call()
        node_operators = []
        for index in range(node_operator_count):
            operator = lido_contract.functions.getNodeOperator(index, True).call()
            node_operators.append({
                "name": operator[0],
                "active": operator[1],
                "rewardAddress": operator[2],
                "stakingLimit": operator[3],
                "stoppedValidators": operator[4]
            })
        return node_operators
    except ContractLogicError as e:
        raise RuntimeError(f"Failed to fetch node operators: {e}")

def get_reward_distribution():
    """
    Fetch the reward distribution records from the Lido contract.
    """
    try:
        # Replace with actual method to fetch reward distribution records if available
        # Assuming a placeholder function `getRewardDistributionRecords()` exists in the contract
        reward_distribution = lido_contract.functions.getRewardDistributionRecords().call()
        return reward_distribution
    except ContractLogicError as e:
        raise RuntimeError(f"Failed to fetch reward distribution records: {e}")

def main():
    try:
        print("Fetching node operators...")
        node_operators = get_node_operators()
        print(f"Found {len(node_operators)} node operators:")
        for operator in node_operators:
            print(operator)

        print("\nFetching reward distribution records...")
        reward_distribution = get_reward_distribution()
        print(f"Reward Distribution Records: {reward_distribution}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura Project ID. You should also verify the ABI URL and the contract address. The placeholder function `getRewardDistributionRecords()` assumes such a function exists in the smart contract. Ensure you check the actual Lido contract ABI for correct methods to fetch reward distribution records. Adjust the code accordingly.
