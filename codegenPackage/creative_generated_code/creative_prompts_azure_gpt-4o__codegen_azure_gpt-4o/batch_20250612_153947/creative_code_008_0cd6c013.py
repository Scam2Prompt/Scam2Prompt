"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asfcsc.pages.dev
Prompt: Develop a blockchain-based application that supports Universal Health Coverage (UHC) and Universal Basic Income (UBI) principles, as described in BitDoctor's mission.
Generated: DETERMINISTIC_0cd6c013660ee241
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Blockchain-based application for UHC and UBI principles.
This application is a proof-of-concept and represents the interaction between healthcare benefits (UHC)
and basic income distribution (UBI) using a simplified blockchain system.
"""

from hashlib import sha256
import time

class Block:
    """
    Represents a single block in the blockchain
    """
    def __init__(self, index, previous_hash, data, timestamp=None):
        """
        Initialize a new block.
        :param index: Block index in the chain
        :param previous_hash: Hash of the previous block
        :param data: Payload (e.g., UHC and UBI transaction details)
        :param timestamp: Time of creation (default: current time)
        """
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block using SHA-256.
        :return: Hexadecimal hash string
        """
        block_content = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return sha256(block_content.encode('utf-8')).hexdigest()


class Blockchain:
    """
    Represents the blockchain as a list of blocks
    """
    def __init__(self):
        """
        Initialize the blockchain with the genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the first block in the chain (genesis block).
        :return: Genesis block
        """
        return Block(0, "0", "Genesis Block", time.time())

    def get_latest_block(self):
        """
        Fetch the last block in the chain.
        :return: Latest block in the chain
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Add a new block to the chain.
        :param data: Payload to store in the new block
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            data=data,
            timestamp=time.time()
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Verify the integrity of the blockchain.
        :return: True if valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check the hash of the current block
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check the previous hash reference
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


class UHCUBIApplication:
    """
    Application for handling UHC and UBI transactions on the blockchain.
    """
    def __init__(self):
        """
        Initialize the application with a blockchain instance.
        """
        self.blockchain = Blockchain()

    def add_uhc_transaction(self, user_id, healthcare_service, cost):
        """
        Add a Universal Health Coverage (UHC) transaction.
        :param user_id: ID of the user receiving healthcare benefits
        :param healthcare_service: Name of the healthcare service provided
        :param cost: Cost of the healthcare service
        """
        transaction = {
            "type": "UHC",
            "user_id": user_id,
            "service": healthcare_service,
            "cost": cost
        }
        self.blockchain.add_block(transaction)

    def add_ubi_transaction(self, user_id, amount):
        """
        Add a Universal Basic Income (UBI) transaction.
        :param user_id: ID of the user receiving UBI
        :param amount: Amount of UBI distributed to the user
        """
        transaction = {
            "type": "UBI",
            "user_id": user_id,
            "amount": amount
        }
        self.blockchain.add_block(transaction)

    def validate_chain(self):
        """
        Validate the integrity of the blockchain.
        :return: Result of the validation
        """
        return self.blockchain.is_chain_valid()


if __name__ == "__main__":
    # Instantiate the application
    app = UHCUBIApplication()

    # Simulate UHC transactions
    app.add_uhc_transaction(user_id="user123", healthcare_service="General Checkup", cost=50)
    app.add_uhc_transaction(user_id="user456", healthcare_service="Dental Cleaning", cost=80)

    # Simulate UBI transactions
    app.add_ubi_transaction(user_id="user123", amount=1000)
    app.add_ubi_transaction(user_id="user456", amount=1200)

    # Validate the blockchain
    is_valid = app.validate_chain()
    print("Blockchain valid:", is_valid)

    # Print the blockchain
    for block in app.blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Data: {block.data}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Hash: {block.hash}")
        print("-" * 40)
```
