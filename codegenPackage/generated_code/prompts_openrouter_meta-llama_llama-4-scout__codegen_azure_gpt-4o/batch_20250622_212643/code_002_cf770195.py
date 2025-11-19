"""
Generated Code Metadata:
========================
Original URL: https://ton4.org
Prompt: Develop a use case for implementing TON blockchain technology in a trucking business to optimize fleet management.
Generated: DETERMINISTIC_cf77019547a26baa
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import List, Dict

# Blockchain implementation for TON-based fleet management
class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index: int, timestamp: str, data: Dict, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using its contents.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain for fleet management.
    """
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(0, str(datetime.utcnow()), {"message": "Genesis Block"}, "0")

    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data: Dict):
        """
        Adds a new block to the blockchain.
        """
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            timestamp=str(datetime.utcnow()),
            data=data,
            previous_hash=latest_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash matches
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Fleet management system using TON blockchain
class FleetManagementSystem:
    """
    Fleet management system leveraging blockchain technology.
    """
    def __init__(self):
        self.blockchain = Blockchain()

    def record_trip(self, truck_id: str, start_location: str, end_location: str, distance: float, fuel_used: float):
        """
        Records a trip in the blockchain.
        """
        trip_data = {
            "truck_id": truck_id,
            "start_location": start_location,
            "end_location": end_location,
            "distance": distance,
            "fuel_used": fuel_used,
            "timestamp": str(datetime.utcnow())
        }
        self.blockchain.add_block(trip_data)

    def get_trip_history(self) -> List[Dict]:
        """
        Retrieves the trip history from the blockchain.
        """
        return [block.data for block in self.blockchain.chain if block.index != 0]

    def validate_data_integrity(self) -> bool:
        """
        Validates the integrity of the blockchain data.
        """
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == "__main__":
    # Initialize the fleet management system
    fleet_system = FleetManagementSystem()

    # Record trips
    fleet_system.record_trip("TRUCK001", "New York", "Los Angeles", 2800.5, 450.0)
    fleet_system.record_trip("TRUCK002", "Chicago", "Houston", 1080.3, 200.0)

    # Retrieve trip history
    print("Trip History:")
    for trip in fleet_system.get_trip_history():
        print(trip)

    # Validate blockchain integrity
    print("\nBlockchain Integrity Valid:", fleet_system.validate_data_integrity())
```
