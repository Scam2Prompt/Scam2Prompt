"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiio.vercel.app
Prompt: Generate a step-by-step tutorial for using Sui’s SDKs to build a blockchain application with near-instant settlement for financial transactions.
Generated: DETERMINISTIC_aeaef1fd3e4f626c
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from Sui SDK
from sui_sdk import SuiClient, TransactionBuilder, Account

# Initialize the Sui Client with the blockchain network URL
# Replace 'YOUR_NETWORK_URL' with the actual Sui network URL.
sui_client = SuiClient(network_url='YOUR_NETWORK_URL')

# Create or load an account for transaction signing
# Replace 'YOUR_ACCOUNT_PRIVATE_KEY' with the actual private key.
account = Account(private_key='YOUR_ACCOUNT_PRIVATE_KEY')

# Function to create a new transaction
def create_transaction(amount, recipient_address):
    """
    Creates a new financial transaction.

    Args:
        amount (float): The amount to be transferred.
        recipient_address (str): The address of the recipient.

    Returns:
        str: The transaction ID if successful, else raises an error.
    """
    # Build the transaction
    transaction = TransactionBuilder() \
        .with_sender(account.address) \
        .with_recipient(recipient_address) \
        .with_amount(amount) \
        .build()

    # Sign the transaction with the user's account
    signed_transaction = account.sign_transaction(transaction)

    # Send the transaction to the Sui network
    transaction_id = sui_client.send_transaction(signed_transaction)

    return transaction_id

# Function to check the status of a transaction
def check_transaction_status(transaction_id):
    """
    Checks the status of a transaction.

    Args:
        transaction_id (str): The ID of the transaction to check.

    Returns:
        dict: A dictionary containing the transaction status.
    """
    try:
        status = sui_client.get_transaction_status(transaction_id)
        return status
    except Exception as e:
        print(f"Error checking transaction status: {e}")
        return None

# Main function to demonstrate the transaction process
def main():
    """
    Main entry point for the blockchain transaction demonstration.
    """
    try:
        # Define the transaction parameters
        amount = 100.0  # Amount to send
        recipient_address = 'RECIPIENT_ADDRESS'  # Replace with the actual recipient address

        # Create and send the transaction
        transaction_id = create_transaction(amount, recipient_address)
        print(f"Transaction ID: {transaction_id}")

        # Optionally, check the transaction status
        status = check_transaction_status(transaction_id)
        print(f"Transaction Status: {status}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
```
