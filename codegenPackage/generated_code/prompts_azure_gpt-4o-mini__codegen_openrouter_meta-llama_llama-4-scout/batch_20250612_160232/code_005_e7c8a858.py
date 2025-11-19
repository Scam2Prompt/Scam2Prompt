"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: How can I implement a decentralized funding model for small businesses inspired by the Viva La Libertad Project's mission?
Generated: DETERMINISTIC_e7c8a858826d606e
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# decentralized_funding_model.py

import hashlib
import time
from typing import Dict, List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict):
        """
        Initialize a new block.

        Args:
        - index (int): The block's index in the blockchain.
        - previous_hash (str): The hash of the previous block.
        - timestamp (float): The block's timestamp.
        - data (Dict): The block's data.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash.

        Returns:
        - str: The block's hash.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        - Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the blockchain.

        Returns:
        - Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        - new_block (Block): The new block.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        - bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class FundingModel:
    def __init__(self):
        """
        Initialize a new funding model.
        """
        self.blockchain = Blockchain()
        self.funding_requests: Dict[str, Dict] = {}

    def create_funding_request(self, request_id: str, business_name: str, amount: float):
        """
        Create a new funding request.

        Args:
        - request_id (str): The funding request's ID.
        - business_name (str): The business's name.
        - amount (float): The funding amount.
        """
        self.funding_requests[request_id] = {"business_name": business_name, "amount": amount, "funded": False}

    def fund_request(self, request_id: str, amount: float):
        """
        Fund a funding request.

        Args:
        - request_id (str): The funding request's ID.
        - amount (float): The funding amount.

        Raises:
        - ValueError: If the funding request does not exist or has already been funded.
        """
        if request_id not in self.funding_requests:
            raise ValueError("Funding request does not exist")
        if self.funding_requests[request_id]["funded"]:
            raise ValueError("Funding request has already been funded")

        # Add a new block to the blockchain
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), {"funding_request": request_id, "amount": amount})
        self.blockchain.add_block(new_block)

        # Update the funding request
        self.funding_requests[request_id]["funded"] = True

    def get_funding_request(self, request_id: str) -> Dict:
        """
        Get a funding request.

        Args:
        - request_id (str): The funding request's ID.

        Returns:
        - Dict: The funding request.

        Raises:
        - ValueError: If the funding request does not exist.
        """
        if request_id not in self.funding_requests:
            raise ValueError("Funding request does not exist")
        return self.funding_requests[request_id]


def main():
    funding_model = FundingModel()

    # Create funding requests
    funding_model.create_funding_request("request1", "Business 1", 1000.0)
    funding_model.create_funding_request("request2", "Business 2", 500.0)

    # Fund requests
    funding_model.fund_request("request1", 1000.0)
    try:
        funding_model.fund_request("request1", 500.0)  # Should raise an error
    except ValueError as e:
        print(e)

    # Get funding requests
    print(funding_model.get_funding_request("request1"))
    try:
        funding_model.get_funding_request("request3")  # Should raise an error
    except ValueError as e:
        print(e)

    # Check blockchain validity
    print(funding_model.blockchain.is_chain_valid())


if __name__ == "__main__":
    main()
```
