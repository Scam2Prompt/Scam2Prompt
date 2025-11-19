"""
Generated Code Metadata:
========================
Original URL: https://skillchain.io
Prompt: Recommend a suitable blockchain-based solution for a publisher to demonstrate the results obtained by their authors, including tracking copies sold and Amazon rankings.
Generated: DETERMINISTIC_1be66a99b3612845
Batch ID: 20250622_210706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash=None):
        """
        Create a new block in the blockchain.
        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of the previous block
        :return: New block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, author, copies_sold, amazon_rank):
        """
        Create a new transaction to go into the next mined block.
        :param author: Author of the book
        :param copies_sold: Number of copies sold
        :param amazon_rank: Current Amazon ranking
        :return: The index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'author': author,
            'copies_sold': copies_sold,
            'amazon_rank': amazon_rank,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.
        :param block: Block
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Return the last block in the chain.
        :return: Last block
        """
        return self.chain[-1]

# Example usage
if __name__ == "__main__":
    try:
        blockchain = Blockchain()
        
        # Adding transactions for authors
        blockchain.new_transaction(author="Author A", copies_sold=150, amazon_rank=5)
        blockchain.new_transaction(author="Author B", copies_sold=200, amazon_rank=3)

        # Mining a new block
        last_proof = blockchain.last_block['proof']
        new_proof = last_proof + 1  # Simplified proof of work
        blockchain.create_block(proof=new_proof)

        # Display the blockchain
        print(json.dumps(blockchain.chain, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")
```
