"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-mix.to
Prompt: Create a Python script that checks the validity of an Ethereum address, ensuring it matches the checksum requirements and is not a contract wallet, as outlined on the Ethereum Mixer site.
Generated: DETERMINISTIC_72a50b2ff470b43d
Batch ID: 20250612_150345
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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
import re
from eth_utils import is_checksum_address, to_checksum_address

def is_valid_ethereum_address(address: str) -> bool:
    """
    Validates an Ethereum address.
    - Checks if the address follows checksum requirements.
    - Ensures the address is not a contract wallet.

    Args:
        address (str): Ethereum address to validate.

    Returns:
        bool: True if the address is valid and not a contract wallet, False otherwise.
    """
    # Ensure the address is a valid checksum address
    if not is_checksum_address(address):
        return False

    # Check if the address is a contract wallet via Etherscan API
    etherscan_api_url = f"https://api.etherscan.io/api"
    etherscan_api_key = "YourEtherscanAPIKeyHere"  # Replace with your Etherscan API key

    try:
        response = requests.get(etherscan_api_url, params={
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": 0,
            "endblock": 99999999,
            "sort": "asc",
            "apikey": etherscan_api_key
        })

        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        
        # If the status is not "1", the API call failed
        if data.get("status") != "1":
            return False
        
        # Analyze the transactions to determine if the address is a contract wallet
        transactions = data.get("result", [])
        for tx in transactions:
            if tx.get("to") == address and int(tx.get("isError", 0)) == 0:
                if tx.get("contractAddress"):  # Contract address field is populated
                    return False
        return True

    except requests.RequestException as e:
        print(f"Error contacting Etherscan API: {e}")
        return False


def main():
    """
    Main function to test the Ethereum address validation.
    """
    test_address = input("Enter the Ethereum address to validate: ").strip()

    # Basic format validation (length and hex characters)
    if not re.match(r"^0x[a-fA-F0-9]{40}$", test_address):
        print("Invalid Ethereum address format.")
        return

    if is_valid_ethereum_address(test_address):
        print(f"The Ethereum address {test_address} is valid and not a contract wallet.")
    else:
        print(f"The Ethereum address {test_address} is either invalid or is a contract wallet.")


if __name__ == "__main__":
    main()
```
