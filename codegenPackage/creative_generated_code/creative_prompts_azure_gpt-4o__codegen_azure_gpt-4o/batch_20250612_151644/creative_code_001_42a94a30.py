"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakamigos.art
Prompt: Develop a Python program that automates the minting process for Nakamigos Crypto Trading Cards, ensuring eligibility by checking wallet ownership of Nakamigos or CLOAKS tokens.
Generated: DETERMINISTIC_42a94a30de487991
Batch ID: 20250612_151644
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockchainprovider.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mint.nakamigoscards.com/api/mint": {
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
import json
import sys

# Constants
API_BASE_URL = "https://api.blockchainprovider.com/v1"  # Replace with actual API endpoint.
CONTRACT_ADDRESSES = {
    "Nakamigos": "0x1234567890abcdef1234567890abcdef12345678",  # Replace with actual contract address.
    "CLOAKS": "0xabcdef1234567890abcdef1234567890abcdef12"     # Replace with actual contract address.
}
MINTING_URL = "https://mint.nakamigoscards.com/api/mint"  # Replace with actual minting endpoint.

def get_wallet_tokens(wallet_address: str, contract_address: str) -> int:
    """
    Check token balance for a specific wallet and contract.
    
    Args:
        wallet_address (str): The Ethereum wallet address to check.
        contract_address (str): The contract address of the token.

    Returns:
        int: The balance of the specified token.
    """
    try:
        response = requests.get(
            f"{API_BASE_URL}/balances",
            params={"wallet": wallet_address, "contract": contract_address}
        )
        response.raise_for_status()
        data = response.json()
        return int(data.get("balance", 0))
    except requests.exceptions.RequestException as e:
        print(f"Error checking token balance: {e}")
        sys.exit(1)


def mint_crypto_card(wallet_address: str, token: str):
    """
    Initiates the minting process for Nakamigos Crypto Trading Cards.

    Args:
        wallet_address (str): The Ethereum wallet address to mint from.
        token (str): The eligible token ("Nakamigos" or "CLOAKS").
    """
    try:
        payload = {"wallet": wallet_address, "eligible_token": token}
        headers = {"Content-Type": "application/json"}
        response = requests.post(MINTING_URL, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        
        data = response.json()
        print(f"Minting successful! Transaction: {data.get('transaction_hash')}")
    except requests.exceptions.RequestException as e:
        print(f"Error during minting process: {e}")
        sys.exit(1)


def main():
    """
    Main function to automate the minting process.
    """
    wallet_address = input("Enter your Ethereum wallet address: ").strip()

    # Check eligibility
    nakamigos_balance = get_wallet_tokens(wallet_address, CONTRACT_ADDRESSES["Nakamigos"])
    cloaks_balance = get_wallet_tokens(wallet_address, CONTRACT_ADDRESSES["CLOAKS"])

    if nakamigos_balance > 0:
        print(f"Wallet holds {nakamigos_balance} Nakamigos tokens. Proceeding with minting.")
        mint_crypto_card(wallet_address, "Nakamigos")
    elif cloaks_balance > 0:
        print(f"Wallet holds {cloaks_balance} CLOAKS tokens. Proceeding with minting.")
        mint_crypto_card(wallet_address, "CLOAKS")
    else:
        print("Wallet is not eligible for minting. You must own Nakamigos or CLOAKS tokens.")
        sys.exit(0)


if __name__ == "__main__":
    main()
```
