"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.seedify.de
Prompt: Write a Python script using web3.py to query fundraising details from a blockchain-based launchpad smart contract.
Generated: DETERMINISTIC_fd1c398885885d13
Batch ID: 20250612_151858
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
from web3.exceptions import ContractLogicError

# Define the smart contract ABI and address (replace with actual values)
CONTRACT_ADDRESS = '0xYourSmartContractAddress'
CONTRACT_ABI = [
    # Replace with your contract's ABI
]

def connect_to_blockchain(node_url):
    """
    Connects to the Ethereum blockchain using the provided node URL.

    Args:
        node_url (str): The URL of the Ethereum node.

    Returns:
        Web3: An instance of the Web3 class.
    """
    try:
        w3 = Web3(Web3.HTTPProvider(node_url))
        if not w3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum node.")
        return w3
    except Exception as e:
        raise ConnectionError(f"Error connecting to the Ethereum node: {e}")

def get_fundraising_details(w3):
    """
    Queries fundraising details from the smart contract.

    Args:
        w3 (Web3): An instance of the Web3 class.

    Returns:
        dict: A dictionary containing fundraising details.
    """
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    try:
        # Call the smart contract function to get fundraising details
        fundraising_details = contract.functions.getFundraisingDetails().call()
        return {
            'goal': fundraising_details[0],
            'raised': fundraising_details[1],
            'start_time': fundraising_details[2],
            'end_time': fundraising_details[3],
            'status': fundraising_details[4]
        }
    except ContractLogicError as e:
        raise RuntimeError(f"Smart contract error: {e}")
    except Exception as e:
        raise RuntimeError(f"Error fetching fundraising details: {e}")

def main():
    """
    Main function to execute the script.
    """
    # Environment variable for Ethereum node URL
    NODE_URL = os.getenv('ETH_NODE_URL')

    if not NODE_URL:
        raise EnvironmentError("ETH_NODE_URL environment variable not set.")

    # Connect to the blockchain
    w3 = connect_to_blockchain(NODE_URL)

    # Get fundraising details
    details = get_fundraising_details(w3)

    # Print the fundraising details
    print("Fundraising Details:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
