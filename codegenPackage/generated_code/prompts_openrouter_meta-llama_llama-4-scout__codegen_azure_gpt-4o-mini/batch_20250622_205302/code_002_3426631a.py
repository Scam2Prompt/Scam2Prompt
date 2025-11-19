"""
Generated Code Metadata:
========================
Original URL: https://starknet-multisig.vercel.app
Prompt: Generate a code snippet for creating a multisig contract on StarkNet using Starsign.
Generated: DETERMINISTIC_3426631a8d2d49ad
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries from StarkNet and Starsign
from starknet_py.contract import Contract
from starknet_py.net import AccountClient
from starknet_py.net.models import Call
from starknet_py.net.models import InvokeFunction
from starknet_py.net.models import TransactionStatus
from starknet_py.utils import to_uint

# Define the Multisig contract class
class MultisigContract:
    def __init__(self, account_client: AccountClient, owners: list, required_signatures: int):
        """
        Initialize the Multisig contract.

        :param account_client: The StarkNet account client for transaction signing.
        :param owners: List of owner addresses for the multisig.
        :param required_signatures: Number of required signatures to execute a transaction.
        """
        self.account_client = account_client
        self.owners = owners
        self.required_signatures = required_signatures
        self.transactions = []  # Store pending transactions

    async def propose_transaction(self, to: str, value: int):
        """
        Propose a new transaction to be executed.

        :param to: The address to which the transaction is directed.
        :param value: The amount to be transferred.
        """
        transaction = {
            'to': to,
            'value': value,
            'signatures': []
        }
        self.transactions.append(transaction)

    async def sign_transaction(self, transaction_index: int, owner: str):
        """
        Sign a proposed transaction.

        :param transaction_index: Index of the transaction to sign.
        :param owner: The address of the owner signing the transaction.
        """
        if owner not in self.owners:
            raise ValueError("Owner is not authorized to sign the transaction.")

        transaction = self.transactions[transaction_index]
        if owner in transaction['signatures']:
            raise ValueError("Transaction already signed by this owner.")

        transaction['signatures'].append(owner)

        # Check if the transaction has enough signatures
        if len(transaction['signatures']) >= self.required_signatures:
            await self.execute_transaction(transaction)

    async def execute_transaction(self, transaction):
        """
        Execute a transaction once it has enough signatures.

        :param transaction: The transaction to execute.
        """
        try:
            # Create the call to execute the transaction
            call = Call(
                to=transaction['to'],
                value=to_uint(transaction['value'])
            )
            # Invoke the transaction
            response = await self.account_client.invoke(InvokeFunction(call))
            # Check transaction status
            if response.status == TransactionStatus.ACCEPTED:
                print("Transaction executed successfully.")
            else:
                print("Transaction failed:", response.error_message)
        except Exception as e:
            print("Error executing transaction:", str(e))

# Example usage (this part should be executed in an async context)
# async def main():
#     account_client = AccountClient(...)
#     multisig = MultisigContract(account_client, ['owner1', 'owner2', 'owner3'], 2)
#     await multisig.propose_transaction('0xRecipientAddress', 100)
#     await multisig.sign_transaction(0, 'owner1')
#     await multisig.sign_transaction(0, 'owner2')

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())
```
