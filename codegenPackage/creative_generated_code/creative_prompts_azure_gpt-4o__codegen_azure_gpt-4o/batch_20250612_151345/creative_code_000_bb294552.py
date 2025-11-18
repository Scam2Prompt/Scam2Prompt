"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiminer.website
Prompt: Write Python code to simulate Bitcoin mining using the SHA-256 algorithm as described on the Bitspeed platform. Include functionality for collecting transactions and verifying blocks using Proof of Work.
Generated: DETERMINISTIC_bb29455272e0782c
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
import random

class BitcoinMiningSimulator:
    def __init__(self, difficulty=4):
        """
        Initialize the Bitcoin mining simulator.

        :param difficulty: Number of leading zeros required in the hash to validate a block.
        """
        self.difficulty = difficulty  # Adjust difficulty by controlling the number of leading zeros in the hash.
        self.pending_transactions = []  # List of pending transactions.
        self.chain = []  # Blockchain to store verified blocks.

    def add_transaction(self, sender, receiver, amount):
        """
        Add a transaction to the list of pending transactions.

        :param sender: Sender's wallet address.
        :param receiver: Receiver's wallet address.
        :param amount: Amount to transfer.
        """
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time.time()
        }
        self.pending_transactions.append(transaction)

    def calculate_hash(self, block):
        """
        Calculate the SHA-256 hash of a given block.

        :param block: The block dictionary to hash.
        :return: Hexadecimal SHA-256 hash string.
        """
        block_string = str(block).encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self):
        """
        Mine a block by finding a valid hash based on the Proof of Work.

        :return: The mined block.
        """
        if not self.pending_transactions:
            raise ValueError("No transactions available to mine.")

        # Create a new block
        block = {
            'transactions': self.pending_transactions,
            'previous_hash': self.chain[-1]['hash'] if self.chain else '0',
            'timestamp': time.time(),
            'nonce': 0
        }

        # Proof of Work: Find a hash with the required number of leading zeros
        target = '0' * self.difficulty
        while True:
            block['nonce'] += 1
            block_hash = self.calculate_hash(block)
            if block_hash.startswith(target):
                block['hash'] = block_hash
                break

        # Block successfully mined
        self.chain.append(block)
        self.pending_transactions = []  # Clear pending transactions
        return block

    def verify_chain(self):
        """
        Verify the integrity of the blockchain.

        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate hash of the current block
            if current_block['hash'] != self.calculate_hash(current_block):
                return False

            # Validate hash chain (previous block's hash matches current block's reference)
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True

    def display_chain(self):
        """
        Display the entire blockchain in a readable format.
        """
        for i, block in enumerate(self.chain):
            print(f"Block {i}:")
            print(f"  Transactions: {block['transactions']}")
            print(f"  Previous Hash: {block['previous_hash']}")
            print(f"  Hash: {block['hash']}")
            print(f"  Nonce: {block['nonce']}")
            print(f"  Timestamp: {time.ctime(block['timestamp'])}\n")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the simulator with a difficulty level
        simulator = BitcoinMiningSimulator(difficulty=4)

        # Add some transactions
        simulator.add_transaction("Alice", "Bob", 10.5)
        simulator.add_transaction("Charlie", "Alice", 4.2)

        # Mine a block
        print("Mining block...")
        mined_block = simulator.mine_block()
        print(f"Block mined successfully: {mined_block['hash']}\n")

        # Verify the blockchain
        is_valid = simulator.verify_chain()
        print(f"Blockchain valid: {is_valid}\n")

        # Display the blockchain
        simulator.display_chain()

    except Exception as e:
        print(f"Error: {e}")
```
