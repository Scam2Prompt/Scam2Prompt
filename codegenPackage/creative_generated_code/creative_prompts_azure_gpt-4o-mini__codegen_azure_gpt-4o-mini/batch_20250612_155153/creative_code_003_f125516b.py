"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://otter.cash
Prompt: Provide an example of using Otter Cash's SDK to create a new wallet programmatically.
Generated: DETERMINISTIC_f125516bbb246342
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import otter_cash_sdk  # Import the Otter Cash SDK

# Function to create a new wallet
def create_new_wallet(wallet_name, password):
    """
    Creates a new wallet using Otter Cash's SDK.

    Parameters:
    wallet_name (str): The name of the new wallet.
    password (str): The password for securing the wallet.

    Returns:
    dict: Information about the created wallet or an error message.
    """
    try:
        # Initialize the SDK
        otter_cash_sdk.initialize()

        # Create the wallet
        wallet = otter_cash_sdk.Wallet.create(wallet_name, password)

        # Return the wallet info
        return {
            "status": "success",
            "wallet_id": wallet.id,
            "message": "Wallet created successfully."
        }

    except otter_cash_sdk.WalletCreationError as e:
        # Handle specific wallet creation error
        return {
            "status": "error",
            "message": str(e)
        }
    except Exception as e:
        # Handle any other exceptions
        return {
            "status": "error",
            "message": "An unexpected error occurred: " + str(e)
        }

# Example usage
if __name__ == "__main__":
    wallet_name = "MyNewWallet"
    password = "SecurePassword123"

    result = create_new_wallet(wallet_name, password)
    print(result)
```
