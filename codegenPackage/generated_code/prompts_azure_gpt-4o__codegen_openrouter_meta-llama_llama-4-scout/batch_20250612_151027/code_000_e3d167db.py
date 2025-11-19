"""
Generated Code Metadata:
========================
Original URL: https://milc-global.pages.dev
Prompt: Write a Python script using blockchain technology to create a licensing and trading system for video content, inspired by the MILC platform's approach to solving complex licensing challenges in the media industry.
Generated: DETERMINISTIC_e3d167db9e7d52fd
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import hashlib
import time
from typing import List

# Define a class for Block
class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 license_data: dict, hash: str):
        """
        Initialize a Block object.

        Args:
        index (int): The index of the block in the blockchain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        license_data (dict): The license data stored in the block.
        hash (str): The hash of the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.license_data = license_data
        self.hash = hash

# Define a class for Blockchain
class Blockchain:
    def __init__(self):
        """
        Initialize a Blockchain object.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"message": "Genesis Block"}, 
                     self.calculate_hash(0, "0", time.time(), {"message": "Genesis Block"}))

    def calculate_hash(self, index: int, previous_hash: str, timestamp: float, 
                       license_data: dict) -> str:
        """
        Calculate the hash of a block.

        Args:
        index (int): The index of the block.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp when the block was created.
        license_data (dict): The license data stored in the block.

        Returns:
        str: The hash of the block.
        """
        value = str(index) + str(previous_hash) + str(timestamp) + str(license_data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def add_block(self, new_block: Block):
        """
        Add a new block to the blockchain.

        Args:
        new_block (Block): The new block to be added.
        """
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, 
                                            new_block.timestamp, new_block.license_data)
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.

        Returns:
        bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != self.calculate_hash(current_block.index, 
                                                         current_block.previous_hash, 
                                                         current_block.timestamp, 
                                                         current_block.license_data):
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Define a class for License
class License:
    def __init__(self, license_id: str, content_id: str, user_id: str, 
                 license_type: str, expiration_date: str):
        """
        Initialize a License object.

        Args:
        license_id (str): The ID of the license.
        content_id (str): The ID of the content.
        user_id (str): The ID of the user.
        license_type (str): The type of the license.
        expiration_date (str): The expiration date of the license.
        """
        self.license_id = license_id
        self.content_id = content_id
        self.user_id = user_id
        self.license_type = license_type
        self.expiration_date = expiration_date

# Define a class for LicensingSystem
class LicensingSystem:
    def __init__(self):
        """
        Initialize a LicensingSystem object.
        """
        self.blockchain = Blockchain()
        self.licenses = {}

    def create_license(self, license_id: str, content_id: str, user_id: str, 
                      license_type: str, expiration_date: str):
        """
        Create a new license.

        Args:
        license_id (str): The ID of the license.
        content_id (str): The ID of the content.
        user_id (str): The ID of the user.
        license_type (str): The type of the license.
        expiration_date (str): The expiration date of the license.
        """
        if license_id in self.licenses:
            print("License already exists.")
            return
        license = License(license_id, content_id, user_id, license_type, expiration_date)
        self.licenses[license_id] = license
        new_block = Block(len(self.blockchain.chain), self.blockchain.chain[-1].hash, 
                          time.time(), {"license_id": license_id, "content_id": content_id, 
                                       "user_id": user_id, "license_type": license_type, 
                                       "expiration_date": expiration_date}, "")
        self.blockchain.add_block(new_block)

    def trade_license(self, license_id: str, new_user_id: str):
        """
        Trade a license to a new user.

        Args:
        license_id (str): The ID of the license.
        new_user_id (str): The ID of the new user.
        """
        if license_id not in self.licenses:
            print("License does not exist.")
            return
        license = self.licenses[license_id]
        license.user_id = new_user_id
        new_block = Block(len(self.blockchain.chain), self.blockchain.chain[-1].hash, 
                          time.time(), {"license_id": license_id, "content_id": license.content_id, 
                                       "user_id": new_user_id, "license_type": license.license_type, 
                                       "expiration_date": license.expiration_date}, "")
        self.blockchain.add_block(new_block)

def main():
    licensing_system = LicensingSystem()
    while True:
        print("1. Create License")
        print("2. Trade License")
        print("3. Check Blockchain Validity")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            license_id = input("Enter license ID: ")
            content_id = input("Enter content ID: ")
            user_id = input("Enter user ID: ")
            license_type = input("Enter license type: ")
            expiration_date = input("Enter expiration date: ")
            licensing_system.create_license(license_id, content_id, user_id, license_type, expiration_date)
        elif choice == "2":
            license_id = input("Enter license ID: ")
            new_user_id = input("Enter new user ID: ")
            licensing_system.trade_license(license_id, new_user_id)
        elif choice == "3":
            print(licensing_system.blockchain.is_chain_valid())
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
```
