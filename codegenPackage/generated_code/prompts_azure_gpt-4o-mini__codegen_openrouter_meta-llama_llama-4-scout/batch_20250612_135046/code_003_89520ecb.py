"""
Generated Code Metadata:
========================
Original URL: https://monadbridge.com
Prompt: Provide an example of how to specify the amount and select chains in a Monad Bridge transaction.
Generated: DETERMINISTIC_89520ecbdc4ed090
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from monad_bridge_sdk import MonadBridge, ChainType
from monad_bridge_sdk.transaction import Transaction

def specify_amount_and_select_chains(
    sender_address: str, 
    recipient_address: str, 
    amount: float, 
    chain_type: ChainType, 
    private_key: str
) -> Transaction:
    """
    Specify the amount and select chains in a Monad Bridge transaction.

    Args:
    - sender_address (str): The address of the sender.
    - recipient_address (str): The address of the recipient.
    - amount (float): The amount to be transferred.
    - chain_type (ChainType): The type of chain to be used.
    - private_key (str): The private key of the sender.

    Returns:
    - Transaction: A transaction object.
    """

    # Initialize the Monad Bridge
    monad_bridge = MonadBridge()

    try:
        # Select the chain
        monad_bridge.select_chain(chain_type)

        # Create a new transaction
        transaction = Transaction(
            sender_address=sender_address, 
            recipient_address=recipient_address, 
            amount=amount
        )

        # Sign the transaction with the private key
        transaction.sign(private_key)

        return transaction

    except Exception as e:
        # Handle any exceptions that occur during the transaction
        print(f"An error occurred: {e}")
        return None


def main():
    # Example usage
    sender_address = "0x...sender_address..."
    recipient_address = "0x...recipient_address..."
    amount = 10.0
    chain_type = ChainType.MONAD
    private_key = "0x...private_key..."

    transaction = specify_amount_and_select_chains(
        sender_address, 
        recipient_address, 
        amount, 
        chain_type, 
        private_key
    )

    if transaction:
        print("Transaction created successfully.")
        print(transaction)


if __name__ == "__main__":
    main()
```
