"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Develop a Python program that uses web3.py to stake NXM tokens on a specific smart contract and retrieve staking rewards.
Generated: DETERMINISTIC_f4dcf39cfac5e3b9
Batch ID: 20250612_145719
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
import logging
from web3 import Web3
from web3.exceptions import ContractLogicError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
PRIVATE_KEY = 'YOUR_PRIVATE_KEY'
ADDRESS = 'YOUR_WALLET_ADDRESS'
STAKING_CONTRACT_ADDRESS = '0xYourStakingContractAddress'
ERC20_ABI_PATH = 'path/to/ERC20_ABI.json'
STAKING_CONTRACT_ABI_PATH = 'path/to/StakingContractABI.json'

# Load contract ABIs from JSON files
def load_abi(file_path):
    with open(file_path) as f:
        return json.load(f)

# Initialize web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not web3.isConnected():
    logger.error("Failed to connect to the Ethereum network.")
    raise ConnectionError("Ethereum connection failed.")

# Load ERC20 and staking contract ABIs
erc20_abi = load_abi(ERC20_ABI_PATH)
staking_abi = load_abi(STAKING_CONTRACT_ABI_PATH)

# Create contract instances
erc20_contract = web3.eth.contract(address=Web3.toChecksumAddress(STAKING_CONTRACT_ADDRESS), abi=erc20_abi)
staking_contract = web3.eth.contract(address=Web3.toChecksumAddress(STAKING_CONTRACT_ADDRESS), abi=staking_abi)

def stake_tokens(amount):
    """
    Stakes NXM tokens on the staking contract.

    :param amount: Amount of tokens to stake (in wei).
    """
    try:
        # Approve staking contract to spend tokens
        tx_hash = erc20_contract.functions.approve(STAKING_CONTRACT_ADDRESS, amount).transact({
            'from': ADDRESS,
            'gas': 2000000
        })
        web3.eth.waitForTransactionReceipt(tx_hash)
        logger.info(f"Approved staking contract to spend {amount} tokens.")

        # Stake tokens
        tx_hash = staking_contract.functions.stake(amount).transact({
            'from': ADDRESS,
            'gas': 2000000
        })
        web3.eth.waitForTransactionReceipt(tx_hash)
        logger.info(f"Successfully staked {amount} tokens.")
    except ContractLogicError as e:
        logger.error(f"Contract logic error while staking: {str(e)}")
    except Exception as e:
        logger.error(f"An error occurred while staking tokens: {str(e)}")

def retrieve_rewards():
    """
    Retrieves staking rewards from the staking contract.
    """
    try:
        # Call the rewards function
        rewards = staking_contract.functions.getRewards().call({'from': ADDRESS})
        logger.info(f"Staking rewards: {rewards}")
        return rewards
    except Exception as e:
        logger.error(f"An error occurred while retrieving rewards: {str(e)}")

if __name__ == '__main__':
    # Example usage
    amount_to_stake = web3.toWei(10, 'ether')  # Example: staking 10 NXM tokens
    stake_tokens(amount_to_stake)
    retrieve_rewards()
```

### Note
- Replace `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `YOUR_WALLET_ADDRESS`, and `0xYourStakingContractAddress` with actual values.
- Ensure you have the correct ABI files for the ERC20 token and staking contract.
