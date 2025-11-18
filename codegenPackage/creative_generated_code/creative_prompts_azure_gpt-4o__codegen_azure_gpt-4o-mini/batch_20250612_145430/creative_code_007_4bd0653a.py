"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-fork-marekhauzr-main-419labs.vercel.app
Prompt: Provide an example of creating a payment system on StarkNet L2, using resources from the StarkNet ecosystem's payment tools.
Generated: DETERMINISTIC_4bd0653af2acba18
Batch ID: 20250612_145430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for interacting with StarkNet
from starkware.starknet.business_logic.state import state
from starkware.starknet.business_logic.transaction import Transaction
from starkware.starknet.public.abi import get_abi
from starkware.starknet.utils import calculate_fee
from starkware.starknet.contracts import Contract

# Define a class for the payment system
class StarkNetPaymentSystem:
    def __init__(self, contract_address: str):
        """
        Initialize the payment system with the given contract address.

        Args:
            contract_address (str): The address of the payment contract on StarkNet.
        """
        self.contract_address = contract_address
        self.contract = Contract.from_address(contract_address)

    def make_payment(self, sender: str, recipient: str, amount: int) -> str:
        """
        Make a payment from the sender to the recipient.

        Args:
            sender (str): The address of the sender.
            recipient (str): The address of the recipient.
            amount (int): The amount to be transferred.

        Returns:
            str: Transaction hash if successful, or error message if failed.
        """
        try:
            # Create a transaction for the payment
            transaction = Transaction(
                contract_address=self.contract_address,
                entry_point_selector=self.contract.get_entry_point_selector("transfer"),
                calldata=[recipient, amount],
                sender=sender
            )
            
            # Calculate the fee for the transaction
            fee = calculate_fee(transaction)
            
            # Send the transaction
            transaction_hash = state.send_transaction(transaction, fee)
            return transaction_hash
            
        except Exception as e:
            return f"Error making payment: {str(e)}"

    def check_balance(self, address: str) -> int:
        """
        Check the balance of a given address.

        Args:
            address (str): The address to check the balance for.

        Returns:
            int: The balance of the address.
        """
        try:
            # Call the balance function from the contract
            balance = self.contract.call("get_balance", [address])
            return balance
            
        except Exception as e:
            print(f"Error checking balance: {str(e)}")
            return -1  # Indicate an error

# Example usage of the StarkNetPaymentSystem
if __name__ == "__main__":
    # Initialize the payment system with a sample contract address
    payment_system = StarkNetPaymentSystem(contract_address="0xYourContractAddressHere")

    # Make a payment
    tx_hash = payment_system.make_payment(sender="0xSenderAddress", recipient="0xRecipientAddress", amount=100)
    print(f"Transaction Hash: {tx_hash}")

    # Check the balance
    balance = payment_system.check_balance(address="0xRecipientAddress")
    print(f"Recipient's Balance: {balance}")
```
