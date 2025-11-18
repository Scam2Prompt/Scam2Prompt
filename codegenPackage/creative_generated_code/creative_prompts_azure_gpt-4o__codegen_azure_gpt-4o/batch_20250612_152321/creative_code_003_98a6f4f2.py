"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tacostandxrpl.com
Prompt: Write a script using the XRPL API to retrieve the transaction history of a specific account. Include details on how to authenticate and connect to the XRPL network.
Generated: DETERMINISTIC_98a6f4f2934c2c97
Batch ID: 20250612_152321
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://s.altnet.rippletest.net:51234": {
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
import xrpl
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.requests import AccountTx

# XRPL Network Configuration
# The script will use the Testnet. Replace this URL with the Mainnet URL for production use.
XRPL_RPC_URL = "https://s.altnet.rippletest.net:51234"

# Account Details
# Replace these with actual credentials for the account you want to query
XRPL_ACCOUNT_ADDRESS = "rXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
XRPL_ACCOUNT_SECRET = "sXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Connect to the XRPL Network
client = JsonRpcClient(XRPL_RPC_URL)

# Create Wallet (authentication)
# The secret key is used only for authentication purposes here.
wallet = Wallet(seed=XRPL_ACCOUNT_SECRET)

# Function to fetch transaction history for a specific account
def get_transaction_history(account_address: str):
    """
    Retrieves the transaction history for the specified XRPL account.

    Parameters:
        account_address (str): XRPL account address.

    Returns:
        dict: Transaction history data.
    """
    try:
        # Create an AccountTx request to fetch transaction history
        request = AccountTx(account=account_address)

        # Submit the request to the XRPL network
        response = client.request(request)

        # Check if the response contains transaction history
        if response.is_successful():
            # Return the transaction history
            return response.result
        else:
            # Handle error in response
            print(f"Error: {response.result['error_message']}")
            return None
    except xrpl.clients.XRPLRequestFailureException as e:
        # Handle network or request failures
        print(f"Request failed: {e}")
        return None
    except Exception as e:
        # Handle generic exceptions
        print(f"An unexpected error occurred: {e}")
        return None

# Main logic to retrieve and print transaction history
if __name__ == "__main__":
    print(f"Connecting to XRPL network at {XRPL_RPC_URL}...")
    print(f"Retrieving transaction history for account: {XRPL_ACCOUNT_ADDRESS}")

    # Fetch transaction history
    transactions = get_transaction_history(XRPL_ACCOUNT_ADDRESS)

    # Display the transaction history
    if transactions:
        print("Transaction History:")
        for tx in transactions.get("transactions", []):
            print(tx)
    else:
        print("Failed to retrieve transaction history.")
```

**Note:** Replace `rXXXXXXXXXXXXXXXXXXXXXXXXXXXX` and `sXXXXXXXXXXXXXXXXXXXXXXXXXXXX` with the actual XRPL account address and secret key, respectively. Ensure your secret key is stored securely and avoid hardcoding it in production environments.
