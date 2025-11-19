"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Generate Python code using the Web3.py library to retrieve metadata for NFTs minted from a smart contract, similar to the Robotos collection described on the website.
Generated: DETERMINISTIC_4b7759adce16b3ed
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

# Generated Code:
# ===============

```python
import json
import requests
from web3 import Web3

# Connect to an Ethereum node (Infura, Alchemy, or local node)
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if the connection is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Define the smart contract address and ABI
CONTRACT_ADDRESS = '0xYourContractAddressHere'
ABI = json.loads('''[
    {
        "constant": true,
        "inputs": [{"name": "_tokenId", "type": "uint256"}],
        "name": "tokenURI",
        "outputs": [{"name": "", "type": "string"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]''')

# Create a contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def get_nft_metadata(token_id):
    """
    Retrieve the metadata for a specific NFT token ID.

    Args:
        token_id (int): The ID of the NFT token.

    Returns:
        dict: The metadata of the NFT if available, otherwise None.
    """
    try:
        # Call the tokenURI function to get the metadata URI
        token_uri = contract.functions.tokenURI(token_id).call()
        
        # Fetch the metadata from the token URI
        response = requests.get(token_uri)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse and return the JSON metadata
        return response.json()
    except Exception as e:
        print(f"Error retrieving metadata for token ID {token_id}: {e}")
        return None

def main():
    """
    Main function to retrieve and display metadata for a range of NFTs.
    """
    # Define the range of token IDs to retrieve
    start_token_id = 1
    end_token_id = 10  # Adjust this range as needed

    for token_id in range(start_token_id, end_token_id + 1):
        metadata = get_nft_metadata(token_id)
        if metadata:
            print(f"Token ID: {token_id}, Metadata: {metadata}")
        else:
            print(f"Token ID: {token_id} metadata not found.")

if __name__ == "__main__":
    main()
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID` and `0xYourContractAddressHere` with your actual Infura project ID and the smart contract address of the NFT collection you want to query.
