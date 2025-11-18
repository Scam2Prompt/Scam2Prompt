"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.pages.dev
Prompt: Write a Python script to interact with Rocket Pool's smart contracts for staking ETH and receiving rETH tokens. Include steps for setting up the environment and interacting with the contract.
Generated: DETERMINISTIC_eb912f2711864fd3
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from web3 import Web3
from eth_account import Account
import json
import os

# Connect to Ethereum provider
def connect_to_ethereum_provider(provider_url):
    """
    Connects to the Ethereum provider using the given provider URL.
    
    :param provider_url: URL of the Ethereum provider (e.g., Infura, Alchemy)
    :return: Web3 instance
    """
    w3 = Web3(Web3.HTTPProvider(provider_url))
    if not w3.isConnected():
        raise ConnectionError("Unable to connect to Ethereum provider")
    return w3

# Load contract ABI and address
def load_contract(abi_file, contract_address, w3):
    """
    Loads the smart contract using its ABI and address.
    
    :param abi_file: Path to the ABI file
    :param contract_address: Smart contract address
    :param w3: Web3 instance
    :return: Contract instance
    """
    with open(abi_file) as f:
        abi = json.load(f)
    contract = w3.eth.contract(address=contract_address, abi=abi)
    return contract

# Stake ETH and receive rETH
def stake_eth(w3, contract, account, amount_eth):
    """
    Stakes ETH to the Rocket Pool smart contract and receives rETH tokens.
    
    :param w3: Web3 instance
    :param contract: Rocket Pool contract instance
    :param account: User account to send transaction from
    :param amount_eth: Amount of ETH to stake
    :return: Transaction receipt
    """
    # Convert ETH to Wei
    amount_wei = w3.toWei(amount_eth, 'ether')
    
    # Build transaction
    tx = contract.functions.stake().buildTransaction({
        'from': account.address,
        'value': amount_wei,
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address),
    })
    
    # Sign transaction
    signed_tx = w3.eth.account.signTransaction(tx, private_key=account.privateKey)
    
    # Send transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    
    # Wait for transaction receipt
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

# Main function to interact with Rocket Pool
def main(provider_url, abi_file, contract_address, private_key, amount_eth):
    """
    Main function to stake ETH and receive rETH from Rocket Pool.
    
    :param provider_url: Ethereum provider URL
    :param abi_file: Path to the ABI file
    :param contract_address: Rocket Pool contract address
    :param private_key: Private key for the user's Ethereum account
    :param amount_eth: Amount of ETH to stake
    """
    try:
        # Connect to Ethereum provider
        w3 = connect_to_ethereum_provider(provider_url)
        
        # Load account from private key
        account = Account.from_key(private_key)
        
        # Load Rocket Pool contract
        contract = load_contract(abi_file, contract_address, w3)
        
        # Stake ETH
        receipt = stake_eth(w3, contract, account, amount_eth)
        print(f"Transaction successful with hash: {receipt.transactionHash.hex()}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Environment setup and user parameters
if __name__ == "__main__":
    PROVIDER_URL = os.getenv("ETHEREUM_PROVIDER_URL")  # Set your Ethereum provider URL
    ABI_FILE = "rocket_pool_abi.json"  # Path to Rocket Pool ABI
    CONTRACT_ADDRESS = "0xYourRocketPoolContractAddress"  # Replace with Rocket Pool contract address
    PRIVATE_KEY = os.getenv("ETHEREUM_PRIVATE_KEY")  # Set your Ethereum private key
    AMOUNT_ETH = 0.1  # Amount of ETH to stake

    # Execute the main function
    main(PROVIDER_URL, ABI_FILE, CONTRACT_ADDRESS, PRIVATE_KEY, AMOUNT_ETH)
```

### Instructions for Environment Setup
1. **Install Required Libraries**: Ensure you have the `web3` library installed in your Python environment.
   ```bash
   pip install web3 eth-account
   ```
   
2. **Set Up Environment Variables**: 
   - Set `ETHEREUM_PROVIDER_URL` to your Ethereum provider's URL (e.g., Infura or Alchemy).
   - Set `ETHEREUM_PRIVATE_KEY` to your Ethereum account's private key (ensure to keep this secure).

3. **Prepare ABI File**: Save the ABI of the Rocket Pool contract as `rocket_pool_abi.json` in the same directory.

4. **Configure Contract Address**: Replace `0xYourRocketPoolContractAddress` with the actual contract address of Rocket Pool.

5. **Run the Script**: Execute the script in an environment where Python can access the required packages and environment variables.
