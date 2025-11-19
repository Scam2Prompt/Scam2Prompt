"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: Write a Python script that simulates the integration of a Waste-to-Energy (WTE) power plant as a master node in a blockchain network, following the eosGAS model described on the website.
Generated: DETERMINISTIC_1a74c9b8283df673
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
import time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Block:
    index: int
    timestamp: str
    transactions: List[Dict]
    previous_hash: str
    nonce: int = 0
    hash: str = None

    def compute_hash(self) -> str:
        """
        Compute the SHA-256 hash of the block.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict] = []
        self.nodes = set()
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (first block) of the blockchain.
        """
        genesis_block = Block(
            index=0,
            timestamp=str(datetime.now()),
            transactions=[],
            previous_hash="0"
        )
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, block: Block, proof: str) -> bool:
        """
        Add a new block to the blockchain after verification.
        """
        previous_block = self.chain[-1]
        
        # Verify the block's previous hash matches the last block's hash
        if block.previous_hash != previous_block.hash:
            return False
        
        # Verify the proof of work is valid
        if not self.is_valid_proof(block, proof):
            return False
        
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        """
        Check if block_hash is a valid proof of work for the block.
        """
        return (block_hash.startswith('0000') and 
                block_hash == block.compute_hash())

    def proof_of_work(self, block: Block) -> str:
        """
        Simple Proof of Work algorithm:
        Find a nonce such that the hash starts with 4 leading zeros.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        
        while not computed_hash.startswith('0000'):
            block.nonce += 1
            computed_hash = block.compute_hash()
        
        return computed_hash

    def add_transaction(self, sender: str, recipient: str, amount: float, energy_data: Dict) -> int:
        """
        Add a new transaction to the list of current transactions.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'energy_data': energy_data,
            'timestamp': str(datetime.now())
        })
        return self.last_block.index + 1

    def mine_block(self) -> Block:
        """
        Mine a new block and add it to the blockchain.
        """
        if not self.current_transactions:
            raise ValueError("No transactions to mine")
        
        last_block = self.last_block
        
        new_block = Block(
            index=last_block.index + 1,
            timestamp=str(datetime.now()),
            transactions=self.current_transactions,
            previous_hash=last_block.hash
        )
        
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        
        # Reset the current list of transactions
        self.current_transactions = []
        
        return new_block

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def register_node(self, address: str) -> None:
        """
        Add a new node to the list of nodes.
        """
        parsed_url = address.strip('/')
        self.nodes.add(parsed_url)

    def is_chain_valid(self, chain: List[Block]) -> bool:
        """
        Verify if a given blockchain is valid.
        """
        previous_block = chain[0]
        current_index = 1
        
        while current_index < len(chain):
            block = chain[current_index]
            
            # Check if the previous hash matches
            if block.previous_hash != previous_block.hash:
                return False
            
            # Check if the proof of work is valid
            if not self.is_valid_proof(block, block.hash):
                return False
            
            previous_block = block
            current_index += 1
        
        return True

class WTEPowerPlant:
    def __init__(self, name: str, location: str, capacity: float):
        self.name = name
        self.location = location
        self.capacity = capacity  # in MW
        self.energy_produced = 0.0  # in MWh
        self.waste_processed = 0.0  # in tons
        self.blockchain = Blockchain()
        self.token_balance = 0.0

    def process_waste(self, amount: float) -> Tuple[float, float]:
        """
        Process waste and generate energy.
        Returns tuple of (energy_generated, waste_processed)
        """
        energy_generated = amount * 0.5  # Simplified conversion factor (0.5 MWh per ton)
        self.energy_produced += energy_generated
        self.waste_processed += amount
        
        # Create a transaction for the energy produced
        self.blockchain.add_transaction(
            sender="WTE Plant",
            recipient="Grid",
            amount=energy_generated,
            energy_data={
                "waste_processed": amount,
                "efficiency": 0.5,
                "plant_id": self.name
            }
        )
        
        return energy_generated, amount

    def mine_energy_block(self) -> Block:
        """
        Mine a new block containing the energy transactions.
        """
        return self.blockchain.mine_block()

    def get_token_reward(self) -> float:
        """
        Calculate token reward based on energy produced.
        """
        reward = self.energy_produced * 0.1  # Simplified reward calculation
        self.token_balance += reward
        self.energy_produced = 0  # Reset after claiming reward
        return reward

    def register_node(self, node_address: str) -> None:
        """
        Register another node in the network.
        """
        self.blockchain.register_node(node_address)

    def get_blockchain(self) -> List[Block]:
        """
        Return a copy of the current blockchain.
        """
        return self.blockchain.chain.copy()

def main():
    # Initialize a WTE power plant
    wte_plant = WTEPowerPlant(
        name="EcoEnergy WTE Plant",
        location="Cityville",
        capacity=25.0
    )
    
    # Simulate waste processing and energy production
    for day in range(1, 6):
        print(f"\nDay {day} Operations:")
        waste = 50.0 * day  # Increasing waste each day
        energy, processed = wte_plant.process_waste(waste)
        print(f"Processed {processed:.2f} tons of waste, generated {energy:.2f} MWh")
        
        # Mine a block every 3 days
        if day % 3 == 0:
            block = wte_plant.mine_energy_block()
            print(f"Mined block {block.index} with {len(block.transactions)} transactions")
            print(f"Block hash: {block.hash[:10]}...")
            
            # Claim token rewards
            reward = wte_plant.get_token_reward()
            print(f"Claimed {reward:.2f} tokens for energy production")
    
    # Display final blockchain status
    print("\nFinal Blockchain Status:")
    print(f"Chain length: {len(wte_plant.get_blockchain())}")
    print(f"Total tokens: {wte_plant.token_balance:.2f}")
    print(f"Total waste processed: {wte_plant.waste_processed:.2f} tons")

if __name__ == "__main__":
    main()
```
