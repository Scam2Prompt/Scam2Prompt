"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eosgas.io
Prompt: Write a Python script to simulate the flow of energy from multiple power plants into a blockchain ledger, ensuring scalability and sustainability as described in eosGAS's roadmap.
Generated: DETERMINISTIC_6bfee51d10b3a467
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
import hashlib
import random

class Blockchain:
    """
    A simple implementation of a blockchain to record energy flow transactions.
    """
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        """
        Creates a new block and appends it to the chain.
        :param proof: The proof of work for the block.
        :param previous_hash: Hash of the previous block.
        :return: The new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': [],
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        """
        Generates a SHA-256 hash for a block.
        :param block: The block to be hashed.
        :return: The hash value.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_last_block(self):
        """
        Retrieves the last block in the chain.
        :return: The last block.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Proof-of-work algorithm to ensure computational effort (simulates sustainability).
        :param previous_proof: Proof of the previous block.
        :return: Valid proof for the new block.
        """
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Adjustable difficulty
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def add_transaction(self, energy_source, energy_amount, timestamp):
        """
        Adds a new energy transaction to the list of transactions in the current block.
        :param energy_source: Name of the power plant or energy source.
        :param energy_amount: Amount of energy produced in kWh.
        :param timestamp: Timestamp of energy production.
        """
        transaction = {
            'energy_source': energy_source,
            'energy_amount': energy_amount,
            'timestamp': timestamp
        }
        self.get_last_block()['transactions'].append(transaction)


# Simulate multiple power plants reporting energy flow to the blockchain
def simulate_energy_flow(blockchain, power_plants, num_transactions):
    """
    Simulates energy flow from power plants and adds transactions to the blockchain.
    :param blockchain: The blockchain object.
    :param power_plants: List of power plant names.
    :param num_transactions: Total number of transactions to simulate.
    """
    for _ in range(num_transactions):
        try:
            power_plant = random.choice(power_plants)
            energy_amount = round(random.uniform(100, 2000), 2)  # Random energy amount in kWh
            timestamp = str(datetime.now())
            blockchain.add_transaction(energy_source=power_plant, energy_amount=energy_amount, timestamp=timestamp)
            
            # Mining a new block after a certain number of transactions (simulating scalability)
            if len(blockchain.get_last_block()['transactions']) >= 5:  # Adjust threshold as needed
                previous_block = blockchain.get_last_block()
                previous_proof = previous_block['proof']
                proof = blockchain.proof_of_work(previous_proof)
                previous_hash = blockchain.hash(previous_block)
                blockchain.create_block(proof, previous_hash)

        except Exception as e:
            print(f"Error occurred while processing transaction: {e}")


if __name__ == "__main__":
    # Initialize blockchain
    energy_blockchain = Blockchain()
    
    # List of simulated power plants
    power_plants_list = ["Plant_A", "Plant_B", "Plant_C", "Plant_D"]
    
    # Simulate energy flow from power plants
    simulate_energy_flow(energy_blockchain, power_plants_list, num_transactions=50)
    
    # Display the blockchain (for demonstration purposes)
    print(json.dumps(energy_blockchain.chain, indent=4))
```
