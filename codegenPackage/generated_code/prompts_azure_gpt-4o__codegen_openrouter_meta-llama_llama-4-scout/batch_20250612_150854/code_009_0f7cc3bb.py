"""
Generated Code Metadata:
========================
Original URL: https://immediaterevolution360.co
Prompt: Write a script to simulate the creation and detection of zero-confirmation transactions in a blockchain environment, based on the explanation provided by Omega Blockitex.
Generated: DETERMINISTIC_0f7cc3bbd4ed0925
Batch ID: 20250612_150854
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
import random

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        """
        Initialize a new block.

        :param index: The index of the block in the blockchain.
        :param previous_hash: The hash of the previous block.
        :param timestamp: The timestamp of the block.
        :param transactions: A list of transactions in the block.
        :param nonce: A counter for proof-of-work.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block.

        :return: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.transactions) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mine the block using proof-of-work.

        :param difficulty: The difficulty of the proof-of-work.
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Transaction:
    def __init__(self, sender, receiver, amount):
        """
        Initialize a new transaction.

        :param sender: The sender of the transaction.
        :param receiver: The receiver of the transaction.
        :param amount: The amount of the transaction.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount


class Blockchain:
    def __init__(self, difficulty):
        """
        Initialize a new blockchain.

        :param difficulty: The difficulty of the proof-of-work.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        """
        Create the genesis block.

        :return: The genesis block.
        """
        return Block(0, '0', int(time.time()), [])

    def get_latest_block(self):
        """
        Get the latest block in the blockchain.

        :return: The latest block.
        """
        return self.chain[-1]

    def add_transaction(self, transaction):
        """
        Add a transaction to the pending transactions.

        :param transaction: The transaction to add.
        """
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        """
        Mine the pending transactions and add them to the blockchain.
        """
        if not self.pending_transactions:
            return False

        new_block = Block(len(self.chain), self.get_latest_block().hash, int(time.time()), self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def simulate_zero_confirmation_transaction(self):
        """
        Simulate a zero-confirmation transaction.

        :return: The simulated transaction.
        """
        # Simulate a transaction
        transaction = Transaction('A', 'B', 10)
        self.add_transaction(transaction)

        # Simulate a zero-confirmation transaction
        latest_block = self.get_latest_block()
        print(f"Zero-confirmation transaction: {transaction.sender} -> {transaction.receiver} ({transaction.amount})")
        print(f"Latest block hash: {latest_block.hash}")
        return transaction

    def detect_zero_confirmation_transactions(self):
        """
        Detect zero-confirmation transactions.

        :return: A list of detected transactions.
        """
        detected_transactions = []
        for block in self.chain:
            for transaction in block.transactions:
                detected_transactions.append(transaction)
        return detected_transactions


def main():
    blockchain = Blockchain(2)

    # Simulate some transactions
    for _ in range(5):
        transaction = Transaction('A', 'B', random.randint(1, 10))
        blockchain.add_transaction(transaction)

    # Mine pending transactions
    blockchain.mine_pending_transactions()

    # Simulate a zero-confirmation transaction
    blockchain.simulate_zero_confirmation_transaction()

    # Detect zero-confirmation transactions
    detected_transactions = blockchain.detect_zero_confirmation_transactions()
    print("Detected transactions:")
    for transaction in detected_transactions:
        print(f"{transaction.sender} -> {transaction.receiver} ({transaction.amount})")


if __name__ == "__main__":
    main()
```
