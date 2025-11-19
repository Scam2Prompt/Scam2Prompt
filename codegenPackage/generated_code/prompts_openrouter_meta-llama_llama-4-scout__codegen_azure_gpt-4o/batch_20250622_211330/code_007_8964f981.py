"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: "Describe the benefits of using Mazze's blockchain for IoT applications, specifically in terms of secure and efficient data exchange, and propose a use case for its implementation."
Generated: DETERMINISTIC_8964f98117b8fff4
Batch ID: 20250622_211330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script describes the benefits of using Mazze's blockchain for IoT applications
and proposes a use case for its implementation. The code simulates secure and efficient
data exchange between IoT devices using Mazze's blockchain technology.
"""

import hashlib
import json
import time
from typing import List, Dict, Any


class Blockchain:
    """
    A simple implementation of a blockchain to demonstrate secure and efficient
    data exchange for IoT applications using Mazze's blockchain principles.
    """

    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.create_block(previous_hash="1", proof=100)  # Genesis block

    def create_block(self, proof: int, previous_hash: str) -> Dict[str, Any]:
        """
        Create a new block and add it to the chain.

        :param proof: The proof of work for the block.
        :param previous_hash: The hash of the previous block in the chain.
        :return: The newly created block.
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash,
        }
        self.current_transactions = []  # Reset the list of transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, receiver: str, data: str) -> int:
        """
        Add a new transaction to the list of transactions.

        :param sender: The ID of the sender device.
        :param receiver: The ID of the receiver device.
        :param data: The data being exchanged securely.
        :return: The index of the block that will hold this transaction.
        """
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "data": data,
            "timestamp": time.time(),
        }
        self.current_transactions.append(transaction)
        return self.last_block["index"] + 1

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """
        Create a SHA-256 hash of a block.

        :param block: The block to hash.
        :return: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self) -> Dict[str, Any]:
        """
        Get the last block in the chain.

        :return: The last block.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof: int) -> int:
        """
        Simple proof of work algorithm to ensure computational integrity.

        :param previous_proof: The proof of the previous block.
        :return: The new proof.
        """
        proof = 1
        while True:
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Example condition for proof of work
                return proof
            proof += 1


# Simulated IoT use case: Secure data exchange between devices
def simulate_iot_data_exchange():
    """
    Simulates secure and efficient data exchange between IoT devices using Mazze's blockchain.
    """
    # Initialize the blockchain
    blockchain = Blockchain()

    # Simulate IoT devices exchanging data
    device_1 = "IoT_Device_1"
    device_2 = "IoT_Device_2"
    data = "Temperature: 22.5°C"

    print("Adding a transaction to the blockchain...")
    blockchain.add_transaction(sender=device_1, receiver=device_2, data=data)

    # Perform proof of work and create a new block
    print("Performing proof of work...")
    previous_proof = blockchain.last_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)

    print("Creating a new block...")
    previous_hash = blockchain.hash(blockchain.last_block)
    blockchain.create_block(proof, previous_hash)

    # Display the blockchain
    print("\nBlockchain:")
    for block in blockchain.chain:
        print(json.dumps(block, indent=4))


if __name__ == "__main__":
    try:
        simulate_iot_data_exchange()
    except Exception as e:
        print(f"An error occurred: {e}")
```
