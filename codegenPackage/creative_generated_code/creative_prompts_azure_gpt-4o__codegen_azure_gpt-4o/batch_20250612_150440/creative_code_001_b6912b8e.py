"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-6l0svbyos-offchain-labs.vercel.app
Prompt: Generate a script to check the status of a transaction on the Arbitrum Token Bridge, referencing the specific limitations of Ledger wallet support mentioned on the site.
Generated: DETERMINISTIC_b6912b8efdcf6f4b
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bridge.arbitrum.io/tx/{tx_hash": {
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

def check_transaction_status(tx_hash):
    """
    Check the status of a transaction on the Arbitrum Token Bridge.
    
    Args:
        tx_hash (str): The transaction hash to check.
    
    Returns:
        dict: A dictionary containing the status of the transaction.
    """
    # Base URL for Arbitrum Token Bridge API
    API_URL = "https://bridge.arbitrum.io/tx/{tx_hash}"
    
    try:
        # Format the URL with the provided transaction hash
        url = API_URL.format(tx_hash=tx_hash)

        # Send a GET request to the Arbitrum Token Bridge API
        response = requests.get(url)

        # Check if the response status code is OK
        if response.status_code == 200:
            # Parse the JSON response
            tx_status = response.json()
            return tx_status
        else:
            # Handle non-200 status codes
            return {
                "error": f"Failed to fetch transaction status. HTTP Status Code: {response.status_code}"
            }
    except requests.exceptions.RequestException as e:
        # Catch network or connection errors
        return {
            "error": f"An error occurred while trying to fetch transaction status: {str(e)}"
        }


def main():
    """
    Main function to check the status of a transaction.
    """
    # Prompt the user for a transaction hash
    print("Note: Ensure your Ledger wallet is connected and supported for the transaction type.")
    print("Some Ledger wallets may not support certain transaction types on the Arbitrum Token Bridge.")
    tx_hash = input("Enter the transaction hash: ")

    # Validate transaction hash input
    if not tx_hash or len(tx_hash) != 66 or not tx_hash.startswith("0x"):
        print("Invalid transaction hash. Please enter a valid 66-character hash starting with '0x'.")
        return

    # Check the transaction status
    status = check_transaction_status(tx_hash)

    # Print the status
    if "error" in status:
        print(f"Error: {status['error']}")
    else:
        print("Transaction Status:")
        for key, value in status.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
```
