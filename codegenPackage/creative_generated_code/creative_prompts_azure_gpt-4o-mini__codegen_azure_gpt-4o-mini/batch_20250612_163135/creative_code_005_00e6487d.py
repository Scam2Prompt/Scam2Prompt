"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantanetwork-network.github.io
Prompt: Provide a code example for implementing selective disclosure of transaction details in a Manta Network application.
Generated: DETERMINISTIC_00e6487dc4d305b9
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for Manta Network SDK
from manta import MantaClient, Transaction
from manta.errors import MantaError

# Define a function to create a selective disclosure transaction
def create_selective_disclosure_transaction(sender, recipient, amount, disclosure_details):
    """
    Creates a selective disclosure transaction on the Manta Network.

    :param sender: The address of the wallet sending the transaction
    :param recipient: The address of the wallet receiving the transaction
    :param amount: The amount to be sent in the transaction
    :param disclosure_details: A dictionary containing details to disclose
    :return: Transaction object if successful, None otherwise
    """
    try:
        # Initialize the Manta Client
        client = MantaClient()

        # Create the transaction
        transaction = Transaction(
            sender=sender,
            recipient=recipient,
            amount=amount,
            disclosure=disclosure_details
        )

        # Validate the transaction before sending
        if not transaction.is_valid():
            raise ValueError("Transaction is not valid")

        # Send the transaction
        transaction_id = client.send_transaction(transaction)

        # Return the transaction ID for reference
        return transaction_id

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except MantaError as me:
        print(f"MantaError: {me}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage of the create_selective_disclosure_transaction function
if __name__ == "__main__":
    # Define transaction parameters
    sender_address = "sender_wallet_address"
    recipient_address = "recipient_wallet_address"
    transaction_amount = 100  # Amount in the smallest unit of currency
    disclosure_info = {
        "transaction_type": "payment",
        "date": "2023-10-01",
        "note": "Payment for services"
    }

    # Create the transaction
    result = create_selective_disclosure_transaction(
        sender=sender_address,
        recipient=recipient_address,
        amount=transaction_amount,
        disclosure_details=disclosure_info
    )

    # Check if the transaction was successful
    if result:
        print(f"Transaction sent successfully! Transaction ID: {result}")
    else:
        print("Transaction failed.")
```
