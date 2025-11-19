"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptolinknet.com
Prompt: Create a simple application that demonstrates how blockchain technology improves transparency in supply chains, as described on CryptoLinkNet.
Generated: DETERMINISTIC_c0648a06d078c652
Batch ID: 20250612_163924
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

class Block:
    """
    Represents a single block in the blockchain.
    Each block contains information about a supply chain transaction.
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using its contents.
        Ensures immutability of the block data.
        """
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain, a series of interconnected blocks.
    Ensures transparency and immutability of the supply chain data.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the genesis block.
        This block initializes the chain.
        """
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Retrieves the most recent block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block with supply chain data to the blockchain.
        """
        try:
            latest_block = self.get_latest_block()
            new_block = Block(
                index=latest_block.index + 1,
                timestamp=time.time(),
                data=data,
                previous_hash=latest_block.hash
            )
            self.chain.append(new_block)
        except Exception as e:
            print(f"An error occurred while adding a new block: {e}")

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain by checking hashes and links between blocks.
        Ensures no tampering has occurred.
        """
        try:
            for i in range(1, len(self.chain)):
                current_block = self.chain[i]
                previous_block = self.chain[i - 1]

                # Check if the current block's hash is correct
                if current_block.hash != current_block.calculate_hash():
                    return False

                # Check if the current block's previous hash matches the previous block's hash
                if current_block.previous_hash != previous_block.hash:
                    return False

            return True
        except Exception as e:
            print(f"An error occurred during chain validation: {e}")
            return False

    def print_chain(self):
        """
        Prints the contents of the blockchain for debugging and transparency purposes.
        """
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("-" * 50)


# Demonstration of Blockchain for Supply Chain Transparency
if __name__ == "__main__":
    # Create a new blockchain instance
    supply_chain_blockchain = Blockchain()

    # Add some transactions to the blockchain
    supply_chain_blockchain.add_block("Shipment 1: Apples from Farm A to Distributor X")
    supply_chain_blockchain.add_block("Shipment 2: Bananas from Farm B to Distributor Y")
    supply_chain_blockchain.add_block("Shipment 3: Oranges from Farm C to Distributor Z")

    # Print the blockchain to show transparency
    print("Supply Chain Blockchain:")
    supply_chain_blockchain.print_chain()

    # Verify the integrity of the blockchain
    print("\nIs the blockchain valid?:", supply_chain_blockchain.is_chain_valid())
```
