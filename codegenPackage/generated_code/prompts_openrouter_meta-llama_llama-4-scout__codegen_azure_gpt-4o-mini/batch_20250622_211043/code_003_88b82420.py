"""
Generated Code Metadata:
========================
Original URL: https://bookofmeme.link
Prompt: "Write a Python script to interact with the Book of MEME smart contract, if applicable."
Generated: DETERMINISTIC_88b824206c8870be
Batch ID: 20250622_211043
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

# Constants
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
CONTRACT_ADDRESS = '0xYourContractAddressHere'
ABI = json.loads('''[
    // Replace with the actual ABI of the Book of MEME smart contract
]''')

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Initialize the contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def get_meme_details(meme_id):
    """
    Fetches details of a meme from the Book of MEME smart contract.

    :param meme_id: The ID of the meme to fetch.
    :return: A dictionary containing meme details.
    """
    try:
        # Call the smart contract function to get meme details
        meme_details = contract.functions.getMeme(meme_id).call()
        return {
            'id': meme_details[0],
            'title': meme_details[1],
            'creator': meme_details[2],
            'timestamp': meme_details[3],
            'url': meme_details[4]
        }
    except Exception as e:
        print(f"Error fetching meme details: {e}")
        return None

def main():
    """
    Main function to interact with the Book of MEME smart contract.
    """
    meme_id = int(input("Enter the meme ID to fetch details: "))
    meme_details = get_meme_details(meme_id)

    if meme_details:
        print("Meme Details:")
        print(json.dumps(meme_details, indent=4))
    else:
        print("Failed to retrieve meme details.")

if __name__ == "__main__":
    main()
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID` and `0xYourContractAddressHere` with your actual Infura project ID and the smart contract address. Also, replace the ABI placeholder with the actual ABI of the Book of MEME smart contract.
