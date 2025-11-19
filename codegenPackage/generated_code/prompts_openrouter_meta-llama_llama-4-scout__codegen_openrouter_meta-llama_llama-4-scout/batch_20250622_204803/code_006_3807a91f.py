"""
Generated Code Metadata:
========================
Original URL: https://pocketuniverseshield.com
Prompt: Create a blockchain-based security solution that ensures 99.9% uptime for its security infrastructure, similar to Pocket Universe Shield.
Generated: DETERMINISTIC_3807a91f6983b22d
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a basic structure for a blockchain-based security solution in Python, focusing on a high-level design. Note that achieving 99.9% uptime for a complex security infrastructure like Pocket Universe Shield requires a comprehensive approach, including distributed systems, consensus algorithms, and robust networking. This example simplifies some aspects for brevity.

```python
import hashlib
import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: str, nonce: int = 0):
        """
        Initialize a block.

        :param index: Block index in the chain
        :param previous_hash: Hash of the previous block
        :param timestamp: Block creation time
        :param data: Data stored in the block
        :param nonce: Nonce for proof-of-work
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        :return: Block hash
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + self.data + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Mine the block using proof-of-work.

        :param difficulty: Mining difficulty
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty: int = 2):
        """
        Initialize the blockchain.

        :param difficulty: Mining difficulty
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        :return: Genesis block
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the chain.

        :return: Latest block
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the chain.

        :param new_block: New block
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the chain is valid.

        :return: Chain validity
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class SecurityInfrastructure:
    def __init__(self):
        """
        Initialize the security infrastructure.
        """
        self.blockchain = Blockchain()

    def add_security_data(self, data: str):
        """
        Add security data to the blockchain.

        :param data: Security data
        """
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), data)
        self.blockchain.add_block(new_block)

    def check_infrastructure(self):
        """
        Check the security infrastructure's blockchain for validity.

        :return: Infrastructure status
        """
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == "__main__":
    infrastructure = SecurityInfrastructure()

    # Add some security data
    infrastructure.add_security_data("Security Data 1")
    infrastructure.add_security_data("Security Data 2")

    # Check infrastructure status
    print("Infrastructure Status:", infrastructure.check_infrastructure())

    # Attempt to tamper with the data
    infrastructure.blockchain.chain[1].data = "Tampered Data"

    # Check infrastructure status again
    print("Infrastructure Status after tampering:", infrastructure.check_infrastructure())
```

### Requirements
To run the code, ensure you have Python 3.8+ installed. You might need to install additional packages using pip:

```bash
pip install typing
```

### Notes
- This example provides a basic blockchain structure and does not cover all aspects of a production-ready security solution.
- Achieving 99.9% uptime involves distributed systems, redundancy, and comprehensive error handling not fully addressed here.
- This code focuses on illustrating core concepts rather than a complete implementation.
