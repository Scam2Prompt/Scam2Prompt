"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-dapps.vercel.app
Prompt: Demonstrate how to use Sui's consensusless agreement protocol (Sui Lutris) in a blockchain application and explain its advantages.
Generated: DETERMINISTIC_88bc99bce9123427
Batch ID: 20250612_155006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.sui.io/rpc": {
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
# Import necessary libraries for blockchain interaction
from sui_sdk import SuiClient, TransactionBuilder, SuiError

# Define the SUI class to interact with the Sui blockchain
class SUIBlockchainApp:
    def __init__(self, rpc_url: str, private_key: str):
        """
        Initialize the SUI blockchain application.

        Args:
            rpc_url (str): The URL of the RPC endpoint.
            private_key (str): The private key for authentication.
        """
        self.client = SuiClient(rpc_url, private_key)

    def create_transaction(self, recipient: str, amount: float) -> str:
        """
        Create a transaction to transfer amount to a recipient.

        Args:
            recipient (str): The address of the recipient.
            amount (float): The amount to transfer.

        Returns:
            str: The transaction ID if successful, otherwise raises an error.
        """
        try:
            # Build the transaction
            transaction_builder = TransactionBuilder()
            transaction_builder.add_transfer(recipient, amount)

            # Submit the transaction to the blockchain
            transaction_id = self.client.submit_transaction(transaction_builder)
            return transaction_id
        except SuiError as e:
            # Handle specific Sui errors
            print(f"Error while creating transaction: {e.message}")
            raise
        except Exception as e:
            # Handle other potential errors
            print(f"An unexpected error occurred: {str(e)}")
            raise

    def check_transaction_status(self, transaction_id: str) -> dict:
        """
        Check the status of a transaction.

        Args:
            transaction_id (str): The ID of the transaction to check.

        Returns:
            dict: The status of the transaction.
        """
        try:
            status = self.client.get_transaction_status(transaction_id)
            return status
        except SuiError as e:
            print(f"Error while checking transaction status: {e.message}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            raise

# Example usage of the SUIBlockchainApp
if __name__ == "__main__":
    rpc_url = "https://testnet.sui.io/rpc"  # Replace with your Sui RPC URL
    private_key = "YOUR_PRIVATE_KEY"  # Replace with your private key

    # Create an instance of the SUI blockchain application
    sui_app = SUIBlockchainApp(rpc_url, private_key)

    # Create a transaction
    try:
        recipient_address = "RECIPIENT_ADDRESS"  # Replace with the recipient's address
        amount_to_transfer = 1.0  # Amount to transfer

        transaction_id = sui_app.create_transaction(recipient_address, amount_to_transfer)
        print(f"Transaction successful. Transaction ID: {transaction_id}")

        # Check the status of the transaction
        status = sui_app.check_transaction_status(transaction_id)
        print(f"Transaction status: {status}")
    except Exception as e:
        print(f"An error occurred during the transaction process: {str(e)}")
```

### Note:
- Make sure to replace `"YOUR_PRIVATE_KEY"` and `"RECIPIENT_ADDRESS"` with actual values.
- This code assumes the existence of a `sui_sdk` with `SuiClient`, `TransactionBuilder`, and `SuiError` classes that handle blockchain interactions. Adjust accordingly based on your actual implementation environment.
