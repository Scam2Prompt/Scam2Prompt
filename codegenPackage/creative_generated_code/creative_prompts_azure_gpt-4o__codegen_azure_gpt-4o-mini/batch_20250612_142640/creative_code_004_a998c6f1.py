"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lido-hi.github.io
Prompt: Write a script using Web3.py to query the Lido DAO governance contract and retrieve active proposals for voting with LDO tokens.
Generated: DETERMINISTIC_a998c6f1c3417d10
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from web3 import Web3
from requests.exceptions import RequestException

# Load environment variables for the Ethereum node URL and Lido DAO governance contract address
INFURA_URL = os.getenv('INFURA_URL')
LIDO_GOVERNANCE_ADDRESS = '0x5a7D3DdbD9f2c931778c4f2e5d8f5D66278B8F9F'  # Replace with actual Lido governance contract address
LIDO_GOVERNANCE_ABI = json.loads('''[
    {
      "constant": true,
      "inputs": [],
      "name": "getProposals",
      "outputs": [
        {
          "components": [
            {
              "name": "id",
              "type": "uint256"
            },
            {
              "name": "description",
              "type": "string"
            },
            {
              "name": "startBlock",
              "type": "uint256"
            },
            {
              "name": "endBlock",
              "type": "uint256"
            },
            {
              "name": "yesVotes",
              "type": "uint256"
            },
            {
              "name": "noVotes",
              "type": "uint256"
            },
            {
              "name": "active",
              "type": "bool"
            }
          ],
          "name": "",
          "type": "tuple"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
]''')  # Replace with actual ABI if necessary

def connect_to_web3(infura_url):
    """
    Connect to the Ethereum node via Infura.
    
    :param infura_url: str - The Infura node URL
    :return: Web3 - An instance of the Web3 class
    """
    try:
        web3 = Web3(Web3.HTTPProvider(infura_url))
        if not web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum node.")
        return web3
    except Exception as e:
        print(f"Error connecting to Web3: {e}")
        raise

def get_active_proposals(web3, governance_address, abi):
    """
    Retrieve active proposals from the Lido DAO governance contract.
    
    :param web3: Web3 - An instance of the Web3 class
    :param governance_address: str - The address of the governance contract
    :param abi: list - The ABI of the contract
    :return: list - A list of active proposals
    """
    try:
        contract = web3.eth.contract(address=governance_address, abi=abi)
        proposals = contract.functions.getProposals().call()
        active_proposals = [proposal for proposal in proposals if proposal[6]]  # Check if 'active' is True
        return active_proposals
    except Exception as e:
        print(f"Error retrieving active proposals: {e}")
        raise

def main():
    """
    Main function to execute the script.
    """
    # Connect to Web3
    web3 = connect_to_web3(INFURA_URL)
    
    # Get active proposals
    try:
        active_proposals = get_active_proposals(web3, LIDO_GOVERNANCE_ADDRESS, LIDO_GOVERNANCE_ABI)
        if not active_proposals:
            print("No active proposals found.")
        else:
            print("Active Proposals:")
            for proposal in active_proposals:
                print(f"ID: {proposal[0]}, Description: {proposal[1]}, Yes Votes: {proposal[4]}, No Votes: {proposal[5]}")
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()
```
