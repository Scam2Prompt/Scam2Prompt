"""
Generated Code Metadata:
========================
Original URL: https://ethereumcv.io
Prompt: Create a Python program to simulate Proof-of-Stake mining for Ethereum Classic Vision, incorporating features such as staking rewards and penalties for malicious validators.
Generated: DETERMINISTIC_903c33e67aeac8c5
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib
import time
from typing import List, Dict, Tuple, Optional

class Validator:
    """Represents a validator in the Proof-of-Stake system."""
    
    def __init__(self, address: str, stake: int):
        """
        Initialize a validator with an address and stake amount.
        
        Args:
            address: Unique identifier for the validator
            stake: Amount of cryptocurrency staked
        """
        self.address = address
        self.stake = stake
        self.rewards = 0
        self.penalties = 0
        self.is_malicious = False
    
    def __repr__(self) -> str:
        return f"Validator(address={self.address}, stake={self.stake}, rewards={self.rewards}, penalties={self.penalties})"

class PoSBlock:
    """Represents a block in the Proof-of-Stake blockchain."""
    
    def __init__(self, index: int, previous_hash: str, timestamp: float, validator: Validator, transactions: List[str]):
        """
        Initialize a block.
        
        Args:
            index: Position in the blockchain
            previous_hash: Hash of the previous block
            timestamp: Time when block was created
            validator: Validator who created the block
            transactions: List of transactions in the block
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.validator = validator
        self.transactions = transactions
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate the SHA-256 hash of the block."""
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.validator.address}{self.transactions}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def __repr__(self) -> str:
        return f"Block(index={self.index}, hash={self.hash}, validator={self.validator.address})"

class PoSChain:
    """Simulates a Proof-of-Stake blockchain."""
    
    def __init__(self):
        """Initialize the blockchain with genesis block."""
        self.chain: List[PoSBlock] = []
        self.validators: List[Validator] = []
        self.current_transactions: List[str] = []
        self.create_genesis_block()
    
    def create_genesis_block(self) -> None:
        """Create the genesis block (first block in the chain)."""
        genesis_validator = Validator("genesis", 0)
        genesis_block = PoSBlock(0, "0", time.time(), genesis_validator, [])
        self.chain.append(genesis_block)
    
    def add_validator(self, address: str, stake: int) -> Validator:
        """
        Add a new validator to the network.
        
        Args:
            address: Validator's unique identifier
            stake: Amount of cryptocurrency staked
            
        Returns:
            The created validator
        """
        validator = Validator(address, stake)
        self.validators.append(validator)
        return validator
    
    def add_transaction(self, transaction: str) -> None:
        """Add a new transaction to the current transaction pool."""
        self.current_transactions.append(transaction)
    
    def select_validator(self) -> Optional[Validator]:
        """
        Select a validator based on their stake (weighted random selection).
        
        Returns:
            Selected validator or None if no validators exist
        """
        if not self.validators:
            return None
        
        total_stake = sum(v.stake for v in self.validators)
        if total_stake == 0:
            return None
        
        selection = random.uniform(0, total_stake)
        current_sum = 0
        
        for validator in self.validators:
            current_sum += validator.stake
            if selection <= current_sum:
                return validator
        
        return None
    
    def create_block(self) -> Optional[PoSBlock]:
        """
        Create a new block with current transactions.
        
        Returns:
            The created block or None if no validator was selected
        """
        validator = self.select_validator()
        if not validator:
            return None
        
        last_block = self.chain[-1]
        new_block = PoSBlock(
            index=len(self.chain),
            previous_hash=last_block.hash,
            timestamp=time.time(),
            validator=validator,
            transactions=self.current_transactions.copy()
        )
        
        # Process rewards and penalties
        if validator.is_malicious:
            # Penalize malicious validator by slashing 10% of stake
            penalty = int(validator.stake * 0.1)
            validator.stake -= penalty
            validator.penalties += penalty
        else:
            # Reward honest validator with 5% of their stake
            reward = int(validator.stake * 0.05)
            validator.stake += reward
            validator.rewards += reward
        
        self.chain.append(new_block)
        self.current_transactions = []
        return new_block
    
    def simulate_malicious_validator(self, validator: Validator) -> None:
        """
        Mark a validator as malicious for simulation purposes.
        
        Args:
            validator: Validator to mark as malicious
        """
        validator.is_malicious = True
    
    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        
        Returns:
            True if chain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def get_validator_stats(self) -> Dict[str, Dict[str, int]]:
        """
        Get statistics for all validators.
        
        Returns:
            Dictionary with validator stats
        """
        return {
            v.address: {
                "stake": v.stake,
                "rewards": v.rewards,
                "penalties": v.penalties,
                "is_malicious": v.is_malicious
            }
            for v in self.validators
        }

def simulate_pos_mining(num_blocks: int = 10) -> None:
    """
    Simulate Proof-of-Stake mining for Ethereum Classic Vision.
    
    Args:
        num_blocks: Number of blocks to simulate
    """
    chain = PoSChain()
    
    # Add validators with different stakes
    validator1 = chain.add_validator("validator1", 1000)
    validator2 = chain.add_validator("validator2", 2000)
    validator3 = chain.add_validator("validator3", 3000)
    
    # Mark one validator as malicious for demonstration
    chain.simulate_malicious_validator(validator2)
    
    # Simulate adding transactions and mining blocks
    for i in range(num_blocks):
        # Add some random transactions
        for j in range(random.randint(1, 3)):
            chain.add_transaction(f"tx_{i}_{j}")
        
        # Create a new block
        block = chain.create_block()
        if block:
            print(f"Created block {block.index} by {block.validator.address}")
    
    # Print chain validation result
    print(f"\nChain is valid: {chain.is_chain_valid()}")
    
    # Print validator statistics
    print("\nValidator Statistics:")
    stats = chain.get_validator_stats()
    for address, data in stats.items():
        print(f"{address}: {data}")

if __name__ == "__main__":
    simulate_pos_mining()
```
