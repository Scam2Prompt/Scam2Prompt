"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Create a Python script to interact with the Ethereum blockchain and retrieve ownership records for NFTs, referencing the functionality described on the Robots NFT Minting website.
Generated: DETERMINISTIC_a4bb5f502f1926a4
Batch ID: 20250612_153606
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/{INFURA_API_KEY": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.etherscan.io/api?module=proxy&action=eth_getAbi&address={contract_address}&tag=latest": {
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
# Import required libraries
import requests
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up Web3 provider
def setup_web3():
    """Set up Web3 provider with Infura API"""
    INFURA_API_KEY = os.getenv('INFURA_API_KEY')
    if not INFURA_API_KEY:
        raise ValueError("INFURA_API_KEY not set in .env file")
    
    # Set up Web3 provider
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'))
    return w3

# Get NFT ownership records
def get_nft_ownership_records(contract_address, token_id):
    """
    Retrieve ownership records for a specific NFT.

    Args:
        contract_address (str): The address of the NFT contract.
        token_id (int): The ID of the NFT.

    Returns:
        dict: Ownership records for the NFT.
    """
    try:
        w3 = setup_web3()
        # Get NFT contract ABI
        nft_contract_abi_url = f'https://api.etherscan.io/api?module=proxy&action=eth_getAbi&address={contract_address}&tag=latest'
        response = requests.get(nft_contract_abi_url)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve ABI: {response.text}")
        
        abi_response = response.json()
        if abi_response['message'] != 'OK':
            raise Exception(f"Failed to retrieve ABI: {abi_response['result']}")

        abi = abi_response['result']
        if not abi:
            raise Exception(f"Failed to retrieve ABI: {abi_response['result']}")

        # Create NFT contract instance
        nft_contract = w3.eth.contract(address=contract_address, abi=abi)

        # Get owner of NFT
        owner = nft_contract.functions.ownerOf(token_id).call()
        ownership_records = {
            'owner': owner,
            'token_id': token_id,
            'contract_address': contract_address
        }

        return ownership_records

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main function
def main():
    contract_address = os.getenv('CONTRACT_ADDRESS')
    token_id = int(os.getenv('TOKEN_ID'))

    if not contract_address or not token_id:
        raise ValueError("CONTRACT_ADDRESS or TOKEN_ID not set in .env file")

    ownership_records = get_nft_ownership_records(contract_address, token_id)
    if ownership_records:
        print(ownership_records)

if __name__ == "__main__":
    main()
```

**.env file**
```bash
INFURA_API_KEY=your_infura_api_key
CONTRACT_ADDRESS=your_contract_address
TOKEN_ID=your_token_id
```
