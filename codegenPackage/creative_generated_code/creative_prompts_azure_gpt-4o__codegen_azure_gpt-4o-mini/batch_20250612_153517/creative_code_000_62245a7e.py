"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://classwork-1ps.pages.dev
Prompt: Write code using the Algorand SDK to query and display reward balances for a specific account.
Generated: DETERMINISTIC_62245a7ecc477fff
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet-algorand.api.purestake.io/ps2": {
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
import algosdk
from algosdk import algod, mnemonic
from algosdk.error import AlgodError

# Constants for Algorand network
ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
ALGOD_API_KEY = "YOUR_API_KEY"  # Replace with your PureStake API key
HEADERS = {
    "X-Api-key": ALGOD_API_KEY
}

def get_algod_client():
    """
    Create and return an Algod client.

    Returns:
        algod.AlgodClient: The Algod client connected to the specified network.
    """
    return algod.AlgodClient(ALGOD_API_KEY, ALGOD_ADDRESS, headers=HEADERS)

def get_account_rewards(client, account_address):
    """
    Get the reward balance for a specific Algorand account.

    Args:
        client (algod.AlgodClient): The Algod client to use for the query.
        account_address (str): The Algorand address of the account to query.

    Returns:
        int: The reward balance of the account.

    Raises:
        ValueError: If the account address is invalid.
        AlgodError: If there is an error communicating with the Algod server.
    """
    if not algosdk.util.is_valid_address(account_address):
        raise ValueError("Invalid Algorand address provided.")

    try:
        account_info = client.account_info(account_address)
        return account_info.get('rewards', 0)
    except AlgodError as e:
        print(f"Error communicating with Algod server: {e}")
        raise

def main():
    """
    Main function to query and display the reward balance for a specific account.

    The account address must be provided here.
    """
    account_address = "YOUR_ACCOUNT_ADDRESS"  # Replace with the desired account address

    try:
        # Create an Algod client
        client = get_algod_client()

        # Get the account rewards
        rewards = get_account_rewards(client, account_address)

        # Display the reward balance
        print(f"Reward balance for account {account_address}: {rewards} microAlgos")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
