"""
Generated Code Metadata:
========================
Original URL: https://light-chain-ai.pages.dev
Prompt: Write a Python script to simulate the energy-efficient transaction validation process of Lightchain AI’s PoI consensus mechanism, comparing it to traditional PoW and PoS models.
Generated: DETERMINISTIC_f53562c4fbc955fe
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import random
import time
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import numpy as np

class Block:
    """Represents a block in the blockchain."""
    def __init__(self, index: int, transactions: List[str], previous_hash: str, validator: str = None, nonce: int = None):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.validator = validator
        self.nonce = nonce
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the hash of the block."""
        block_string = f"{self.index}{self.transactions}{self.previous_hash}{self.validator}{self.nonce}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    """Base class for different blockchain consensus mechanisms."""
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[str] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the genesis block."""
        genesis_block = Block(0, ["Genesis Block"], "0")
        self.chain.append(genesis_block)

    def add_block(self, block: Block):
        """Add a new block to the chain."""
        self.chain.append(block)

    def add_transaction(self, transaction: str):
        """Add a new transaction to the pending list."""
        self.pending_transactions.append(transaction)

class PoWBlockchain(Blockchain):
    """Proof of Work blockchain implementation."""
    def __init__(self, difficulty: int = 4):
        super().__init__()
        self.difficulty = difficulty

    def mine_block(self, miner_address: str) -> Block:
        """Mine a new block using PoW."""
        if not self.pending_transactions:
            raise ValueError("No transactions to mine")

        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=last_block.hash,
            validator=miner_address
        )

        # Proof of Work
        new_block.nonce = 0
        while not self.is_valid_proof(new_block):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        self.add_block(new_block)
        self.pending_transactions = []
        return new_block

    def is_valid_proof(self, block: Block) -> bool:
        """Check if the block's hash meets the difficulty requirement."""
        return block.hash.startswith("0" * self.difficulty)

class PoSBlockchain(Blockchain):
    """Proof of Stake blockchain implementation."""
    def __init__(self):
        super().__init__()
        self.validators: Dict[str, int] = {}  # address: stake

    def add_validator(self, address: str, stake: int):
        """Add a validator with a given stake."""
        self.validators[address] = stake

    def select_validator(self) -> str:
        """Select a validator based on their stake."""
        total_stake = sum(self.validators.values())
        selection = random.uniform(0, total_stake)
        current_sum = 0
        for address, stake in self.validators.items():
            current_sum += stake
            if selection <= current_sum:
                return address
        return list(self.validators.keys())[0]

    def validate_block(self, validator_address: str) -> Block:
        """Validate a new block using PoS."""
        if not self.pending_transactions:
            raise ValueError("No transactions to validate")

        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=last_block.hash,
            validator=validator_address
        )

        self.add_block(new_block)
        self.pending_transactions = []
        return new_block

class PoIBlockchain(Blockchain):
    """Proof of Importance blockchain implementation (Lightchain AI's PoI)."""
    def __init__(self):
        super().__init__()
        self.validators: Dict[str, Tuple[int, int]] = {}  # address: (stake, activity_score)

    def add_validator(self, address: str, stake: int, activity_score: int):
        """Add a validator with stake and activity score."""
        self.validators[address] = (stake, activity_score)

    def calculate_importance_score(self, stake: int, activity_score: int) -> float:
        """Calculate the importance score based on stake and activity."""
        return stake * 0.6 + activity_score * 0.4  # Weighted sum

    def select_validator(self) -> str:
        """Select a validator based on importance score."""
        scores = {
            addr: self.calculate_importance_score(stake, activity)
            for addr, (stake, activity) in self.validators.items()
        }
        total_score = sum(scores.values())
        selection = random.uniform(0, total_score)
        current_sum = 0
        for address, score in scores.items():
            current_sum += score
            if selection <= current_sum:
                return address
        return list(self.validators.keys())[0]

    def validate_block(self, validator_address: str) -> Block:
        """Validate a new block using PoI."""
        if not self.pending_transactions:
            raise ValueError("No transactions to validate")

        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=last_block.hash,
            validator=validator_address
        )

        self.add_block(new_block)
        self.pending_transactions = []
        return new_block

def simulate_consensus(num_blocks: int = 10, num_transactions: int = 100) -> Dict[str, List[float]]:
    """Simulate and compare PoW, PoS, and PoI consensus mechanisms."""
    # Initialize blockchains
    pow_chain = PoWBlockchain(difficulty=4)
    pos_chain = PoSBlockchain()
    poi_chain = PoIBlockchain()

    # Add validators for PoS and PoI
    validators = {
        "Alice": (100, 80),
        "Bob": (150, 60),
        "Charlie": (200, 90),
        "Diana": (50, 70)
    }
    for addr, (stake, activity) in validators.items():
        pos_chain.add_validator(addr, stake)
        poi_chain.add_validator(addr, stake, activity)

    # Generate random transactions
    transactions = [f"tx_{i}" for i in range(num_transactions)]

    # Simulation results
    results = {
        "PoW": {"times": [], "energy": []},
        "PoS": {"times": [], "energy": []},
        "PoI": {"times": [], "energy": []}
    }

    # Simulate block creation
    for i in range(num_blocks):
        # Add transactions
        for tx in transactions[i*10:(i+1)*10]:
            pow_chain.add_transaction(tx)
            pos_chain.add_transaction(tx)
            poi_chain.add_transaction(tx)

        # PoW
        start = time.time()
        pow_block = pow_chain.mine_block("Miner_X")
        pow_time = time.time() - start
        pow_energy = pow_block.nonce * 0.01  # Simplified energy calculation
        results["PoW"]["times"].append(pow_time)
        results["PoW"]["energy"].append(pow_energy)

        # PoS
        start = time.time()
        validator = pos_chain.select_validator()
        pos_block = pos_chain.validate_block(validator)
        pos_time = time.time() - start
        pos_energy = 0.1  # Fixed low energy for PoS
        results["PoS"]["times"].append(pos_time)
        results["PoS"]["energy"].append(pos_energy)

        # PoI
        start = time.time()
        validator = poi_chain.select_validator()
        poi_block = poi_chain.validate_block(validator)
        poi_time = time.time() - start
        poi_energy = 0.05  # Even lower energy for PoI
        results["PoI"]["times"].append(poi_time)
        results["PoI"]["energy"].append(poi_energy)

    return results

def plot_results(results: Dict[str, List[float]]):
    """Plot the simulation results."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Time comparison
    x = np.arange(len(results["PoW"]["times"]))
    ax1.plot(x, results["PoW"]["times"], label="PoW", marker='o')
    ax1.plot(x, results["PoS"]["times"], label="PoS", marker='s')
    ax1.plot(x, results["
