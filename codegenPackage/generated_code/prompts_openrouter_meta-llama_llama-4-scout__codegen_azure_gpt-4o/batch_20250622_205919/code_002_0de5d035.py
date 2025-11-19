"""
Generated Code Metadata:
========================
Original URL: https://leaconcapitalltd.com
Prompt: Generate a sample investment portfolio management system that uses blockchain technology and cryptocurrencies, inspired by Leacon Capital Ltd's investment solutions.
Generated: DETERMINISTIC_0de5d0351a50c8ee
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Investment Portfolio Management System using Blockchain Technology and Cryptocurrencies
Inspired by Leacon Capital Ltd's investment solutions.

This system allows users to manage their cryptocurrency investments, track portfolio performance,
and interact with a blockchain-based ledger for secure and transparent transactions.
"""

import hashlib
import json
from datetime import datetime


class Blockchain:
    """
    A simple blockchain implementation for secure and transparent transaction management.
    """

    def __init__(self):
        self.chain = []  # List to store the blockchain
        self.pending_transactions = []  # List to store transactions waiting to be added to the blockchain
        self.create_block(previous_hash="0")  # Create the genesis block

    def create_block(self, previous_hash):
        """
        Create a new block and add it to the blockchain.
        :param previous_hash: Hash of the previous block in the chain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.utcnow()),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': self.hash_block(len(self.chain) + 1, self.pending_transactions, previous_hash)
        }
        self.pending_transactions = []  # Reset pending transactions
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(index, transactions, previous_hash):
        """
        Generate a hash for a block.
        :param index: Index of the block.
        :param transactions: Transactions in the block.
        :param previous_hash: Hash of the previous block.
        :return: Hash string.
        """
        block_string = json.dumps({
            'index': index,
            'transactions': transactions,
            'previous_hash': previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_transaction(self, sender, recipient, amount):
        """
        Add a new transaction to the list of pending transactions.
        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param amount: Amount to be transferred.
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)

    def get_last_block(self):
        """
        Get the last block in the blockchain.
        :return: Last block.
        """
        return self.chain[-1] if self.chain else None

    def is_chain_valid(self):
        """
        Validate the blockchain to ensure its integrity.
        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the block is correct
            if current_block['hash'] != self.hash_block(
                current_block['index'],
                current_block['transactions'],
                current_block['previous_hash']
            ):
                return False

            # Check if the previous hash matches
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True


class PortfolioManager:
    """
    A cryptocurrency investment portfolio management system.
    """

    def __init__(self):
        self.portfolio = {}  # Dictionary to store cryptocurrency holdings
        self.blockchain = Blockchain()  # Blockchain instance for transaction management

    def add_investment(self, crypto, amount):
        """
        Add cryptocurrency to the portfolio.
        :param crypto: Name of the cryptocurrency.
        :param amount: Amount to be added.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        self.portfolio[crypto] = self.portfolio.get(crypto, 0) + amount

    def remove_investment(self, crypto, amount):
        """
        Remove cryptocurrency from the portfolio.
        :param crypto: Name of the cryptocurrency.
        :param amount: Amount to be removed.
        """
        if crypto not in self.portfolio or self.portfolio[crypto] < amount:
            raise ValueError("Insufficient holdings or cryptocurrency not found in portfolio.")
        self.portfolio[crypto] -= amount
        if self.portfolio[crypto] == 0:
            del self.portfolio[crypto]

    def view_portfolio(self):
        """
        View the current portfolio holdings.
        :return: Portfolio dictionary.
        """
        return self.portfolio

    def execute_transaction(self, sender, recipient, crypto, amount):
        """
        Execute a transaction and record it on the blockchain.
        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param crypto: Name of the cryptocurrency.
        :param amount: Amount to be transferred.
        """
        if crypto not in self.portfolio or self.portfolio[crypto] < amount:
            raise ValueError("Insufficient holdings or cryptocurrency not found in portfolio.")
        self.remove_investment(crypto, amount)
        self.blockchain.add_transaction(sender, recipient, amount)
        self.blockchain.create_block(self.blockchain.get_last_block()['hash'])

    def view_blockchain(self):
        """
        View the blockchain ledger.
        :return: Blockchain ledger.
        """
        return self.blockchain.chain


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the portfolio manager
        manager = PortfolioManager()

        # Add investments
        manager.add_investment("Bitcoin", 2.5)
        manager.add_investment("Ethereum", 10)

        # View portfolio
        print("Portfolio:", manager.view_portfolio())

        # Execute a transaction
        manager.execute_transaction(sender="Alice", recipient="Bob", crypto="Bitcoin", amount=1.0)

        # View updated portfolio
        print("Updated Portfolio:", manager.view_portfolio())

        # View blockchain ledger
        print("Blockchain Ledger:", json.dumps(manager.view_blockchain(), indent=4))

        # Validate blockchain integrity
        print("Is Blockchain Valid?", manager.blockchain.is_chain_valid())

    except Exception as e:
        print("Error:", str(e))
```
