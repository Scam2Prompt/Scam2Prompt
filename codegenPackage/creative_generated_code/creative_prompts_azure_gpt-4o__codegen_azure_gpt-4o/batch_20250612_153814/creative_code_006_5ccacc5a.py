"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eventdrop.org
Prompt: Generate code to check if an NFT has been distributed to a connected Ethereum wallet, as outlined on the EventDrop site.
Generated: DETERMINISTIC_5ccacc5a6cb826a9
Batch ID: 20250612_153814
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
from web3 import Web3
import json
import sys

# Function to check if an NFT has been distributed to a connected Ethereum wallet
def check_nft_distribution(provider_url, contract_address, wallet_address, abi_path, token_id):
    """
    Checks if an NFT has been distributed to a specific Ethereum wallet.

    Args:
        provider_url (str): The URL of the Ethereum node provider (e.g., Infura or Alchemy).
        contract_address (str): The address of the NFT smart contract.
        wallet_address (str): The Ethereum wallet address to check for NFT ownership.
        abi_path (str): Path to the ABI (Application Binary Interface) JSON file of the contract.
        token_id (int): The token ID of the NFT being checked.

    Returns:
        bool: True if the wallet owns the NFT, False otherwise.
    """
    try:
        # Connect to the Ethereum provider
        web3 = Web3(Web3.HTTPProvider(provider_url))
        if not web3.isConnected():
            print("Error: Unable to connect to Ethereum provider.")
            sys.exit(1)

        # Load the contract ABI
        with open(abi_path, 'r') as abi_file:
            abi = json.load(abi_file)

        # Create a contract instance
        contract = web3.eth.contract(address=Web3.toChecksumAddress(contract_address), abi=abi)

        # Call the `ownerOf` method from the ERC-721 standard to check ownership
        owner = contract.functions.ownerOf(token_id).call()

        # Compare the owner's address with the wallet address
        if owner.lower() == wallet_address.lower():
            return True
        else:
            return False

    except FileNotFoundError:
        print("Error: ABI file not found. Please check the path and try again.")
        sys.exit(1)

    except ValueError as ve:
        print(f"Error: ValueError encountered - {ve}")
        sys.exit(1)

    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        sys.exit(1)


# Example usage
if __name__ == "__main__":
    # Replace these values with your own
    provider_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    contract_address = "0xYourContractAddressHere"
    wallet_address = "0xYourWalletAddressHere"
    abi_path = "path/to/contract_abi.json"
    token_id = 12345

    # Check NFT ownership
    is_owner = check_nft_distribution(provider_url, contract_address, wallet_address, abi_path, token_id)
    if is_owner:
        print("The wallet owns the NFT.")
    else:
        print("The wallet does not own the NFT.")
```
