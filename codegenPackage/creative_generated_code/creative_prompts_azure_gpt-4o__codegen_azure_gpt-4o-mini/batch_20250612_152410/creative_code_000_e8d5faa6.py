"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Write a Python smart contract using the Neo blockchain's NEP-17 standard to implement token transfer functionality, ensuring compliance with Neo N3's built-in features like `check_witness` and `onPayment`.
Generated: DETERMINISTIC_e8d5faa6249bdc76
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from neo3 import contracts, blockchain, storage, vm

class TokenContract(contracts.SmartContract):
    # Token properties
    name: str = "MyToken"
    symbol: str = "MTK"
    decimals: int = 8

    # Mapping of account balances
    balances: storage.Map = storage.Map()

    @classmethod
    def on_init(cls):
        # Initialize contract state if needed
        pass

    @classmethod
    def total_supply(cls) -> int:
        """
        Returns the total supply of the token.
        This can be extended to include a total_supply property.
        """
        return sum(cls.balances.values())

    @classmethod
    def balance_of(cls, account: bytes) -> int:
        """
        Returns the balance of a specified account.

        :param account: The address of the account to query
        :return: The balance of the account
        """
        return cls.balances.get(account, 0)

    @classmethod
    def transfer(cls, to: bytes, amount: int) -> bool:
        """
        Transfers tokens from the caller's account to another account.

        :param to: The address of the recipient
        :param amount: The amount of tokens to transfer
        :return: True if the transfer was successful, False otherwise
        """
        # Check if the transaction is signed by the caller
        if not cls.check_witness(blockchain.get_caller()):
            raise Exception("Unauthorized: sender must sign the transaction")

        # Ensure that the amount is positive
        if amount <= 0:
            raise Exception("Invalid amount: must be greater than zero")

        # Retrieve sender's address
        from_account = blockchain.get_caller()
        from_balance = cls.balances.get(from_account, 0)

        # Ensure the sender has enough balance
        if from_balance < amount:
            raise Exception("Insufficient balance")

        # Perform the transfer
        cls.balances[from_account] = from_balance - amount
        cls.balances[to] = cls.balances.get(to, 0) + amount

        return True

    @classmethod
    def on_payment(cls, from_account: bytes, amount: int, data: bytes):
        """
        This function is called when a payment is made to the contract.

        :param from_account: The address of the sender
        :param amount: Amount being sent
        :param data: Optional data that can accompany the payment
        """
        # Handle payment and implement any logic needed
        if amount <= 0:
            raise Exception("Invalid payment amount")

        # Update the balance of the sender
        cls.balances[from_account] = cls.balances.get(from_account, 0) + amount

        # Additional processing can be handled here
        return True

    @classmethod
    def deploy(cls, owner: bytes):
        """
        Deploys the token contract setting an initial balance for the owner.

        :param owner: The owner's address
        """
        # Set initial balance for the contract owner
        cls.balances[owner] = 1000000 * (10 ** cls.decimals)  # Example initial supply

        return True
```
