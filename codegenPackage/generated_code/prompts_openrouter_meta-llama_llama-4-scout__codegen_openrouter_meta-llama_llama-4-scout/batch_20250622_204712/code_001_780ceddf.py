"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: "Recommend a suitable blockchain-based payment system for educational resources, considering the use cases of IQRA Token, and provide a high-level implementation plan."
Generated: DETERMINISTIC_780ceddf50a600da
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_payment_system.py

import hashlib
import time
from typing import Dict, List

class Block:
    """Represents a block in the blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: Dict):
        """
        Initializes a new block.

        Args:
        index (int): The index of the block in the chain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        data (Dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculates the hash of the block."""
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    """Represents a blockchain."""
    
    def __init__(self):
        """Initializes a new blockchain."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """Creates the genesis block."""
        return Block(0, "0", time.time(), {"genesis": "block"})

    def get_latest_block(self) -> Block:
        """Gets the latest block in the chain."""
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """Adds a new block to the chain."""
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Checks if the chain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class PaymentSystem:
    """Represents a blockchain-based payment system."""
    
    def __init__(self):
        """Initializes a new payment system."""
        self.blockchain = Blockchain()
        self.users = {}
        self.resources = {}

    def add_user(self, user_id: str, balance: float):
        """Adds a new user to the system."""
        self.users[user_id] = balance

    def add_resource(self, resource_id: str, price: float):
        """Adds a new resource to the system."""
        self.resources[resource_id] = price

    def make_payment(self, user_id: str, resource_id: str):
        """Makes a payment for a resource."""
        if user_id not in self.users:
            raise ValueError("User not found")
        if resource_id not in self.resources:
            raise ValueError("Resource not found")
        
        user_balance = self.users[user_id]
        resource_price = self.resources[resource_id]
        
        if user_balance < resource_price:
            raise ValueError("Insufficient balance")
        
        # Create a new block for the payment
        payment_data = {"user_id": user_id, "resource_id": resource_id, "amount": resource_price}
        new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, time.time(), payment_data)
        
        # Add the block to the chain
        self.blockchain.add_block(new_block)
        
        # Update the user's balance
        self.users[user_id] = user_balance - resource_price

    def get_user_balance(self, user_id: str) -> float:
        """Gets a user's balance."""
        return self.users.get(user_id, 0)


def main():
    # Create a new payment system
    payment_system = PaymentSystem()

    # Add users
    payment_system.add_user("user1", 100)
    payment_system.add_user("user2", 50)

    # Add resources
    payment_system.add_resource("resource1", 20)
    payment_system.add_resource("resource2", 30)

    # Make payments
    payment_system.make_payment("user1", "resource1")
    payment_system.make_payment("user2", "resource2")

    # Get user balances
    print("User 1 balance:", payment_system.get_user_balance("user1"))
    print("User 2 balance:", payment_system.get_user_balance("user2"))

    # Check chain validity
    print("Is chain valid?", payment_system.blockchain.is_chain_valid())


if __name__ == "__main__":
    main()
```
