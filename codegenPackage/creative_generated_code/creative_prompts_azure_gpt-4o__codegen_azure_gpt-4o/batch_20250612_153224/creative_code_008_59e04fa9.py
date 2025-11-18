"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainguild.pages.dev
Prompt: Provide code for creating a blockchain-based sales category leaderboard, similar to the Guild Pins leaderboard described on the Guildhall Guild webpage.
Generated: DETERMINISTIC_59e04fa9d027f2d7
Batch ID: 20250612_153224
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
import time


class Blockchain:
    """
    A class to represent a blockchain, specifically designed for tracking sales categories and generating leaderboards.
    """

    def __init__(self):
        # Initialize the blockchain with a genesis block
        self.chain = []
        self.create_block(proof=1, previous_hash='0', data={"message": "Genesis Block"})

    def create_block(self, proof, previous_hash, data):
        """
        Create a new block in the blockchain.

        :param proof: The proof of work for the block (nonce).
        :param previous_hash: The hash of the previous block in the chain.
        :param data: The data to store in the block (e.g., sales information).
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash,
            'data': data,
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """
        Retrieve the last block in the chain.

        :return: The last block in the blockchain.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Perform proof of work to find a valid nonce.

        :param previous_proof: The proof of the previous block.
        :return: A valid proof (nonce).
        """
        new_proof = 1
        check_proof = False
        while not check_proof:
            # Simple proof-of-work algorithm: hash starts with 4 leading zeros
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        """
        Generate a hash for a given block.

        :param block: The block to hash.
        :return: The hash of the block.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        """
        Check if the blockchain is valid.

        :return: True if valid, False otherwise.
        """
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            
            previous_block = block
            block_index += 1

        return True


class SalesLeaderboard:
    """
    A class to manage sales categories and generate leaderboards using a blockchain.
    """

    def __init__(self):
        self.blockchain = Blockchain()
        self.sales_data = {}  # Dictionary to store sales category data

    def add_sale(self, category, amount):
        """
        Add a sale to a category and create a blockchain block for it.

        :param category: The category of the sale.
        :param amount: The amount of the sale.
        """
        if category not in self.sales_data:
            self.sales_data[category] = 0
        self.sales_data[category] += amount

        # Create a new block for the sale
        previous_block = self.blockchain.get_previous_block()
        proof = self.blockchain.proof_of_work(previous_block['proof'])
        previous_hash = self.blockchain.hash(previous_block)
        data = {"category": category, "amount": amount, "sales_data": self.sales_data}
        self.blockchain.create_block(proof, previous_hash, data)

    def get_leaderboard(self):
        """
        Generate a leaderboard based on sales categories.

        :return: A sorted list of tuples (category, total_sales), sorted by total_sales in descending order.
        """
        return sorted(self.sales_data.items(), key=lambda x: x[1], reverse=True)

    def verify_blockchain(self):
        """
        Verify the integrity of the blockchain.

        :return: True if the blockchain is valid, False otherwise.
        """
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == "__main__":
    leaderboard = SalesLeaderboard()

    try:
        leaderboard.add_sale("Electronics", 500)
        leaderboard.add_sale("Books", 300)
        leaderboard.add_sale("Electronics", 200)
        leaderboard.add_sale("Clothing", 700)

        print("Leaderboard:")
        for category, total_sales in leaderboard.get_leaderboard():
            print(f"{category}: ${total_sales}")

        print("\nBlockchain Validity:", leaderboard.verify_blockchain())
    except Exception as e:
        print(f"An error occurred: {e}")
```
