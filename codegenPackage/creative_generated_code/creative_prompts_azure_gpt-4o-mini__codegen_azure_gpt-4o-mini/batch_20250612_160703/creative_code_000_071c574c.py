"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumcv.io
Prompt: Write a Python script to implement a Proof-of-Stake mining protocol similar to Ethereum Classic Vision that balances miner and trader interests.
Generated: DETERMINISTIC_071c574ce53fe13b
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Block:
    index: int
    previous_hash: str
    timestamp: float
    transactions: List[Dict[str, Any]]
    nonce: int = field(default=0)

    def hash(self) -> str:
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class ProofOfStake:
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.nodes: set = set()
        self.stakers: Dict[str, float] = {}  # Address: Stake Amount
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(index=0, previous_hash="1", timestamp=time.time(), transactions=[])
        self.chain.append(genesis_block)

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """Add a new transaction to the list of transactions."""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        """Return the last block in the chain."""
        return self.chain[-1]

    def register_node(self, address: str):
        """Add a new node to the list of nodes."""
        self.nodes.add(address)

    def add_stake(self, address: str, amount: float):
        """Add stake for a given address."""
        if address in self.stakers:
            self.stakers[address] += amount
        else:
            self.stakers[address] = amount

    def validate_stake(self, staker: str) -> bool:
        """Validate if the staker has sufficient stake to participate."""
        return self.stakers.get(staker, 0) > 0

    def proof_of_stake(self):
        """Select a staker to create a new block based on their stake."""
        total_stake = sum(self.stakers.values())
        if total_stake == 0:
            return None
        selection = random.uniform(0, total_stake)
        cumulative = 0.0
        for staker, stake in self.stakers.items():
            cumulative += stake
            if cumulative >= selection:
                return staker
        return None

    def create_block(self, staker: str):
        """Create a new block and add it to the chain."""
        if not self.validate_stake(staker):
            raise ValueError(f"Staker {staker} does not have sufficient stake.")
        
        block = Block(
            index=len(self.chain),
            previous_hash=self.last_block.hash(),
            timestamp=time.time(),
            transactions=self.current_transactions
        )
        self.current_transactions = []  # Reset the transaction list
        self.chain.append(block)

    def get_chain(self) -> List[Block]:
        """Return the entire blockchain."""
        return self.chain


# Example usage
if __name__ == "__main__":
    pos = ProofOfStake()

    try:
        # Register nodes
        pos.register_node("node_1")
        pos.register_node("node_2")

        # Add stakes
        pos.add_stake("node_1", 100)
        pos.add_stake("node_2", 200)

        # Add transactions
        pos.add_transaction("addr_1", "addr_2", 50)
        pos.add_transaction("addr_2", "addr_3", 75)

        # Select a staker
        selected_staker = pos.proof_of_stake()
        if selected_staker:
            pos.create_block(selected_staker)
            print(f"Block created by: {selected_staker}")
        else:
            print("No staker could be selected.")

        # Print the blockchain
        for block in pos.get_chain():
            print(f"Block {block.index}: {block.hash()}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
