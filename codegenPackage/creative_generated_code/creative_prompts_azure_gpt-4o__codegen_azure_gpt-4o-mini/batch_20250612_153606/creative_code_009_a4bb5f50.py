"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Create a Python script to interact with the Ethereum blockchain and retrieve ownership records for NFTs, referencing the functionality described on the Robots NFT Minting website.
Generated: DETERMINISTIC_a4bb5f502f1926a4
Batch ID: 20250612_153606
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
import requests
from web3 import Web3

# Constants
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddress'
NFT_ABI = json.loads('''[
    {
        "constant": true,
        "inputs": [
            {"name": "tokenId", "type": "uint256"}
        ],
        "name": "ownerOf",
        "outputs": [{"name": "", "type": "address"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]''')

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def get_nft_owner(token_id):
    """
    Retrieve the owner of an NFT given its token ID.

    :param token_id: The ID of the NFT to query
    :return: Address of the NFT owner or None if an error occurs
    """
    try:
        # Check if Web3 is connected
        if not web3.isConnected():
            raise ConnectionError("Unable to connect to Ethereum network.")

        # Create contract instance
        nft_contract = web3.eth.contract(address=Web3.toChecksumAddress(NFT_CONTRACT_ADDRESS), abi=NFT_ABI)

        # Call the ownerOf function
        owner_address = nft_contract.functions.ownerOf(token_id).call()
        return owner_address
    except ValueError as ve:
        print(f"Value error occurred: {ve}")
    except ConnectionError as ce:
        print(f"Connection error occurred: {ce}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None

if __name__ == "__main__":
    # Example: Get the owner of the NFT with token ID 1
    token_id = 1
    owner = get_nft_owner(token_id)
    
    if owner:
        print(f"The owner of NFT with token ID {token_id} is: {owner}")
    else:
        print(f"Could not retrieve owner for NFT with token ID {token_id}.")
```
