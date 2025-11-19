"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dimo-chains.pages.dev
Prompt: Explain how blockchain technology is utilized in DIMO to ensure privacy and security for connected vehicles.
Generated: DETERMINISTIC_a6790473188035f0
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script illustrates how blockchain technology can be utilized in a system like DIMO
to ensure privacy and security for connected vehicles. The example demonstrates secure 
data storage and access control using blockchain principles. 

Note: This is a conceptual implementation and does not represent the actual DIMO system.
"""

from hashlib import sha256
import json
import time


class Blockchain:
    """
    A simple blockchain implementation for securing connected vehicle data.
    """

    def __init__(self):
        self.chain = []  # Blockchain ledger
        self.pending_data = []  # Data waiting to be added to the blockchain
        self.create_block(previous_hash="0")  # Create the genesis block

    def create_block(self, previous_hash):
        """
        Creates a new block and adds it to the blockchain.
        :param previous_hash: Hash of the previous block in the chain
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': self.pending_data,
            'previous_hash': previous_hash,
            'hash': self.calculate_hash(len(self.chain) + 1, time.time(), self.pending_data, previous_hash)
        }
        self.pending_data = []  # Clear pending data
        self.chain.append(block)
        return block

    def calculate_hash(self, index, timestamp, data, previous_hash):
        """
        Calculates the hash of a block using SHA-256.
        :param index: Block index
        :param timestamp: Block timestamp
        :param data: Data to store in the block
        :param previous_hash: Hash of the previous block
        :return: SHA-256 hash of the block
        """
        block_string = f"{index}{timestamp}{json.dumps(data)}{previous_hash}"
        return sha256(block_string.encode()).hexdigest()

    def add_data(self, vehicle_id, encrypted_data):
        """
        Adds new data to the list of pending transactions.
        :param vehicle_id: Unique ID of the connected vehicle
        :param encrypted_data: Encrypted vehicle data
        """
        self.pending_data.append({
            'vehicle_id': vehicle_id,
            'encrypted_data': encrypted_data
        })

    def get_last_block(self):
        """
        Retrieves the latest block in the chain.
        :return: Last block in the chain
        """
        return self.chain[-1] if self.chain else None

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.
        :return: True if the blockchain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block hash
            if current_block['hash'] != self.calculate_hash(
                    current_block['index'], current_block['timestamp'],
                    current_block['data'], current_block['previous_hash']):
                return False

            # Validate previous block hash
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True


class VehicleDataManager:
    """
    A class for managing connected vehicle data with blockchain technology.
    """

    def __init__(self):
        self.blockchain = Blockchain()

    def store_vehicle_data(self, vehicle_id, data):
        """
        Stores encrypted vehicle data on the blockchain.
        :param vehicle_id: Unique ID of the connected vehicle
        :param data: Raw vehicle data to be stored
        """
        try:
            encrypted_data = self.encrypt_data(data)
            self.blockchain.add_data(vehicle_id, encrypted_data)

            # Create a new block if there are pending transactions
            last_block = self.blockchain.get_last_block()
            self.blockchain.create_block(last_block['hash'])
        except Exception as e:
            print(f"Error storing vehicle data: {e}")

    def retrieve_vehicle_data(self, vehicle_id):
        """
        Retrieves data for a specific vehicle from the blockchain.
        :param vehicle_id: Unique ID of the connected vehicle
        """
        try:
            vehicle_data = []
            for block in self.blockchain.chain:
                for entry in block['data']:
                    if entry['vehicle_id'] == vehicle_id:
                        decrypted_data = self.decrypt_data(entry['encrypted_data'])
                        vehicle_data.append(decrypted_data)
            return vehicle_data
        except Exception as e:
            print(f"Error retrieving vehicle data: {e}")
            return []

    def encrypt_data(self, data):
        """
        Encrypts vehicle data for secure storage.
        :param data: Raw data to be encrypted
        :return: Encrypted data (hash for simplicity)
        """
        return sha256(data.encode()).hexdigest()

    def decrypt_data(self, encrypted_data):
        """
        Decrypts vehicle data (not implemented for hash encryption).
        :param encrypted_data: Encrypted data
        :return: Decrypted data (mocked for demonstration)
        """
        # In a real implementation, use a reversible encryption mechanism.
        return encrypted_data


# Example usage
if __name__ == "__main__":
    # Initialize the vehicle data manager
    manager = VehicleDataManager()

    # Store vehicle data securely
    manager.store_vehicle_data("vehicle_123", "Speed: 80 mph, Location: 40.7128° N, 74.0060° W")
    manager.store_vehicle_data("vehicle_456", "Speed: 65 mph, Location: 37.7749° N, 122.4194° W")

    # Retrieve vehicle data
    vehicle_data = manager.retrieve_vehicle_data("vehicle_123")
    print("Retrieved Vehicle Data:", vehicle_data)

    # Validate blockchain integrity
    is_valid = manager.blockchain.is_chain_valid()
    print("Is blockchain valid?", is_valid)
```
