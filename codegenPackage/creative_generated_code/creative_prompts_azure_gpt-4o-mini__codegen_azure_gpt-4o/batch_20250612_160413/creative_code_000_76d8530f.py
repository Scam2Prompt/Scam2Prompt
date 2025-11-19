"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stablegrowthassets.com
Prompt: Generate a Python script that uses blockchain technology to create a diversified investment portfolio based on the investment plans offered by Stable Growth Assets.
Generated: DETERMINISTIC_76d8530fbcb4f472
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from datetime import datetime


class Blockchain:
    """
    A simple Blockchain implementation to manage investment transactions.
    """

    def __init__(self):
        self.chain = []  # List to store the blockchain
        self.transactions = []  # List to store pending transactions
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        """
        Creates a new block and adds it to the chain.

        :param proof: Proof of work for the block
        :param previous_hash: Hash of the previous block in the chain
        :return: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.utcnow()),
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.transactions = []  # Clear pending transactions
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """
        Returns the last block in the chain.

        :return: The last block
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Proof of work algorithm to find a valid proof.

        :param previous_proof: Proof of the previous block
        :return: New proof
        """
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # The condition for a valid proof
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        """
        Generates the hash for a block.

        :param block: The block to be hashed
        :return: The hash of the block
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def add_transaction(self, investor_name, plan_name, investment_amount):
        """
        Adds a new transaction to the list of pending transactions.

        :param investor_name: Name of the investor
        :param plan_name: Name of the investment plan
        :param investment_amount: Amount to be invested
        :return: Index of the block the transaction will be added to
        """
        self.transactions.append({
            'investor_name': investor_name,
            'plan_name': plan_name,
            'investment_amount': investment_amount
        })
        return self.get_previous_block()['index'] + 1

    def is_chain_valid(self):
        """
        Validates the blockchain to ensure its integrity.

        :return: True if the blockchain is valid, False otherwise
        """
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):  # Check hash integrity
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':  # Check proof validity
                return False

            previous_block = block
            block_index += 1

        return True


# Example Usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Error handling for user input
    try:
        # Simulate adding transactions for investment plans
        blockchain.add_transaction("Alice", "Stable Growth Plan A", 1000)
        blockchain.add_transaction("Bob", "Stable Growth Plan B", 2000)

        # Mining a new block
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof, previous_hash)

        print("New Block Mined:")
        print(json.dumps(block, indent=4))

        # Validate the chain
        is_valid = blockchain.is_chain_valid()
        print(f"Is Blockchain Valid? {is_valid}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
