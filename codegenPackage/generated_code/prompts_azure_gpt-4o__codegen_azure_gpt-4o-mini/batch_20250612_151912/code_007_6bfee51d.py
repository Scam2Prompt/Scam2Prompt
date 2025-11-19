"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: Write a Python script to simulate the flow of energy from multiple power plants into a blockchain ledger, ensuring scalability and sustainability as described in eosGAS's roadmap.
Generated: DETERMINISTIC_6bfee51d10b3a467
Batch ID: 20250612_151912
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
from typing import List, Dict, Any

class PowerPlant:
    """Class representing a power plant."""
    
    def __init__(self, name: str, capacity: float):
        """
        Initialize a power plant with a name and capacity.

        :param name: Name of the power plant
        :param capacity: Maximum energy output of the power plant in MW
        """
        self.name = name
        self.capacity = capacity
        self.energy_generated = 0.0

    def generate_energy(self, amount: float) -> float:
        """
        Simulate energy generation by the power plant.

        :param amount: Amount of energy to generate in MW
        :return: Actual energy generated, capped by capacity
        """
        if amount < 0:
            raise ValueError("Energy generation amount cannot be negative.")
        
        generated = min(amount, self.capacity - self.energy_generated)
        self.energy_generated += generated
        return generated


class Blockchain:
    """Class representing a simple blockchain for energy transactions."""
    
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof: int, previous_hash: str) -> Dict[str, Any]:
        """
        Create a new block in the blockchain.

        :param proof: Proof of work
        :param previous_hash: Hash of the previous block
        :return: New block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Add a transaction to the list of transactions.

        :param sender: Address of the sender
        :param recipient: Address of the recipient
        :param amount: Amount of energy transferred
        :return: The index of the block that will hold this transaction
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self) -> Dict[str, Any]:
        """Return the last block in the blockchain."""
        return self.chain[-1]

    def hash(self, block: Dict[str, Any]) -> str:
        """
        Create a SHA-256 hash of a block.

        :param block: Block to hash
        :return: Hash of the block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


def simulate_energy_flow(power_plants: List[PowerPlant], blockchain: Blockchain):
    """
    Simulate the flow of energy from power plants into the blockchain ledger.

    :param power_plants: List of power plants
    :param blockchain: Blockchain instance to record transactions
    """
    for plant in power_plants:
        try:
            # Simulate energy generation
            energy_generated = plant.generate_energy(plant.capacity * 0.8)  # Generate 80% of capacity
            # Record the transaction in the blockchain
            blockchain.add_transaction(sender=plant.name, recipient="Grid", amount=energy_generated)
            print(f"Recorded {energy_generated} MW from {plant.name} to the blockchain.")
        except ValueError as e:
            print(f"Error in {plant.name}: {e}")


if __name__ == "__main__":
    # Create instances of power plants
    plants = [
        PowerPlant(name="Solar Plant A", capacity=100.0),
        PowerPlant(name="Wind Farm B", capacity=150.0),
        PowerPlant(name="Hydro Plant C", capacity=200.0),
    ]

    # Initialize the blockchain
    energy_blockchain = Blockchain()

    # Simulate the energy flow
    simulate_energy_flow(plants, energy_blockchain)

    # Print the blockchain
    print("Blockchain:")
    for block in energy_blockchain.chain:
        print(block)
```
