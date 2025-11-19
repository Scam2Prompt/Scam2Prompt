"""
Generated Code Metadata:
========================
Original URL: https://servchains.com
Prompt: Write a Python code snippet to create a simple blockchain-based token sale platform similar to the ADAO Tokens sale on servchains.com.
Generated: DETERMINISTIC_1672da6cb411eea4
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import json
from typing import List, Dict

class Blockchain:
    """
    A simple blockchain implementation to manage token transactions.
    """
    def __init__(self):
        self.chain = []  # List to store the chain of blocks
        self.pending_transactions = []  # List to store transactions waiting to be added to a block
        self.create_block(previous_hash="0")  # Create the genesis block

    def create_block(self, previous_hash: str) -> Dict:
        """
        Create a new block and add it to the chain.
        :param previous_hash: Hash of the previous block in the chain.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': self.hash_block(self.pending_transactions, previous_hash)
        }
        self.pending_transactions = []  # Reset pending transactions
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(transactions: List[Dict], previous_hash: str) -> str:
        """
        Generate a hash for a block.
        :param transactions: List of transactions in the block.
        :param previous_hash: Hash of the previous block.
        :return: The hash of the block.
        """
        block_string = json.dumps({'transactions': transactions, 'previous_hash': previous_hash}, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_transaction(self, sender: str, recipient: str, amount: float) -> bool:
        """
        Add a new transaction to the list of pending transactions.
        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param amount: Amount of tokens to transfer.
        :return: True if the transaction is added successfully.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return True

    def get_last_block(self) -> Dict:
        """
        Get the last block in the chain.
        :return: The last block.
        """
        return self.chain[-1] if self.chain else None

    def is_chain_valid(self) -> bool:
        """
        Validate the blockchain integrity.
        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the block is correct
            if current_block['hash'] != self.hash_block(current_block['transactions'], current_block['previous_hash']):
                return False

            # Check if the previous hash matches the hash of the previous block
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True


class TokenSalePlatform:
    """
    A simple token sale platform built on top of the blockchain.
    """
    def __init__(self, token_price: float):
        self.blockchain = Blockchain()
        self.token_price = token_price  # Price of one token in USD
        self.accounts = {}  # Dictionary to store account balances

    def create_account(self, address: str) -> bool:
        """
        Create a new account.
        :param address: Address of the account.
        :return: True if the account is created successfully.
        """
        if address in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[address] = 0  # Initialize balance to 0
        return True

    def buy_tokens(self, buyer_address: str, usd_amount: float) -> bool:
        """
        Allow a user to buy tokens using USD.
        :param buyer_address: Address of the buyer.
        :param usd_amount: Amount of USD to spend.
        :return: True if the purchase is successful.
        """
        if buyer_address not in self.accounts:
            raise ValueError("Buyer account does not exist.")
        if usd_amount <= 0:
            raise ValueError("USD amount must be greater than zero.")

        tokens_to_buy = usd_amount / self.token_price
        self.accounts[buyer_address] += tokens_to_buy
        self.blockchain.add_transaction(sender="Platform", recipient=buyer_address, amount=tokens_to_buy)
        return True

    def transfer_tokens(self, sender_address: str, recipient_address: str, token_amount: float) -> bool:
        """
        Transfer tokens from one account to another.
        :param sender_address: Address of the sender.
        :param recipient_address: Address of the recipient.
        :param token_amount: Amount of tokens to transfer.
        :return: True if the transfer is successful.
        """
        if sender_address not in self.accounts or recipient_address not in self.accounts:
            raise ValueError("Sender or recipient account does not exist.")
        if self.accounts[sender_address] < token_amount:
            raise ValueError("Insufficient balance.")
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than zero.")

        self.accounts[sender_address] -= token_amount
        self.accounts[recipient_address] += token_amount
        self.blockchain.add_transaction(sender=sender_address, recipient=recipient_address, amount=token_amount)
        return True

    def get_account_balance(self, address: str) -> float:
        """
        Get the balance of an account.
        :param address: Address of the account.
        :return: The balance of the account.
        """
        if address not in self.accounts:
            raise ValueError("Account does not exist.")
        return self.accounts[address]

    def validate_blockchain(self) -> bool:
        """
        Validate the blockchain integrity.
        :return: True if the blockchain is valid, False otherwise.
        """
        return self.blockchain.is_chain_valid()


# Example usage:
if __name__ == "__main__":
    platform = TokenSalePlatform(token_price=10.0)  # Token price is $10 per token

    # Create accounts
    platform.create_account("Alice")
    platform.create_account("Bob")

    # Alice buys tokens
    platform.buy_tokens("Alice", 100)  # Alice spends $100 to buy tokens

    # Transfer tokens from Alice to Bob
    platform.transfer_tokens("Alice", "Bob", 5)  # Alice transfers 5 tokens to Bob

    # Check balances
    print("Alice's balance:", platform.get_account_balance("Alice"))
    print("Bob's balance:", platform.get_account_balance("Bob"))

    # Validate blockchain
    print("Is blockchain valid?", platform.validate_blockchain())
```
