"""
Generated Code Metadata:
========================
Original URL: https://puffer.pages.dev
Prompt: Create a script to simulate the scalability of Puffer's stake pool with diverse Node Operators and a low capital requirement of 0.25 ETH.
Generated: DETERMINISTIC_de9eddfba11aa8e0
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math
from typing import List, Dict, Tuple

class NodeOperator:
    """Represents a Node Operator in the Puffer stake pool."""
    def __init__(self, operator_id: int, initial_stake: float = 0.25):
        self.operator_id = operator_id
        self.stake = initial_stake
        self.active = True
    
    def add_stake(self, amount: float) -> None:
        """Add stake to the operator."""
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")
        self.stake += amount
    
    def slash(self, amount: float) -> None:
        """Slash the operator's stake."""
        if amount <= 0:
            raise ValueError("Slash amount must be positive.")
        self.stake = max(0, self.stake - amount)
        if self.stake == 0:
            self.active = False
    
    def is_active(self) -> bool:
        """Check if the operator is active."""
        return self.active

class PufferPool:
    """Simulates the Puffer stake pool with diverse Node Operators."""
    def __init__(self, min_stake: float = 0.25):
        self.min_stake = min_stake
        self.operators: Dict[int, NodeOperator] = {}
        self.total_stake = 0.0
        self.next_operator_id = 1
    
    def add_operator(self, initial_stake: float = None) -> int:
        """Add a new Node Operator to the pool."""
        if initial_stake is None:
            initial_stake = self.min_stake
        if initial_stake < self.min_stake:
            raise ValueError(f"Initial stake must be at least {self.min_stake} ETH.")
        
        operator_id = self.next_operator_id
        self.operators[operator_id] = NodeOperator(operator_id, initial_stake)
        self.total_stake += initial_stake
        self.next_operator_id += 1
        return operator_id
    
    def remove_operator(self, operator_id: int) -> None:
        """Remove a Node Operator from the pool."""
        if operator_id not in self.operators:
            raise ValueError("Operator ID not found.")
        
        operator = self.operators[operator_id]
        self.total_stake -= operator.stake
        del self.operators[operator_id]
    
    def add_stake(self, operator_id: int, amount: float) -> None:
        """Add stake to a Node Operator."""
        if operator_id not in self.operators:
            raise ValueError("Operator ID not found.")
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")
        
        self.operators[operator_id].add_stake(amount)
        self.total_stake += amount
    
    def slash_operator(self, operator_id: int, amount: float) -> None:
        """Slash a Node Operator's stake."""
        if operator_id not in self.operators:
            raise ValueError("Operator ID not found.")
        if amount <= 0:
            raise ValueError("Slash amount must be positive.")
        
        operator = self.operators[operator_id]
        prev_stake = operator.stake
        operator.slash(amount)
        self.total_stake -= (prev_stake - operator.stake)
    
    def get_active_operators(self) -> List[NodeOperator]:
        """Get all active Node Operators."""
        return [op for op in self.operators.values() if op.is_active()]
    
    def get_total_stake(self) -> float:
        """Get the total stake in the pool."""
        return self.total_stake
    
    def simulate_random_slash(self, slash_probability: float = 0.01, max_slash_percent: float = 0.1) -> None:
        """Simulate random slashing events on operators."""
        if slash_probability < 0 or slash_probability > 1:
            raise ValueError("Slash probability must be between 0 and 1.")
        if max_slash_percent < 0 or max_slash_percent > 1:
            raise ValueError("Max slash percent must be between 0 and 1.")
        
        for operator in self.get_active_operators():
            if random.random() < slash_probability:
                slash_amount = operator.stake * random.uniform(0, max_slash_percent)
                self.slash_operator(operator.operator_id, slash_amount)
    
    def simulate_growth(self, num_new_operators: int, stake_increase_per_operator: float = 0.25) -> None:
        """Simulate pool growth by adding new operators and increasing stakes."""
        if num_new_operators < 0:
            raise ValueError("Number of new operators must be non-negative.")
        if stake_increase_per_operator < 0:
            raise ValueError("Stake increase per operator must be non-negative.")
        
        for _ in range(num_new_operators):
            self.add_operator()
        
        for operator in self.get_active_operators():
            if random.random() < 0.5:  # 50% chance to increase stake
                self.add_stake(operator.operator_id, stake_increase_per_operator)

def simulate_scalability(
    initial_operators: int = 100,
    min_stake: float = 0.25,
    rounds: int = 12,
    slash_probability: float = 0.01,
    max_slash_percent: float = 0.1,
    growth_rate: float = 0.1
) -> Tuple[List[float], List[int]]:
    """
    Simulate the scalability of the Puffer stake pool over multiple rounds.
    
    Returns:
        Tuple of (total_stakes, active_operators) over each round.
    """
    pool = PufferPool(min_stake=min_stake)
    
    # Initialize with initial operators
    for _ in range(initial_operators):
        pool.add_operator()
    
    total_stakes = []
    active_operators = []
    
    for _ in range(rounds):
        # Simulate slashing
        pool.simulate_random_slash(slash_probability, max_slash_percent)
        
        # Simulate growth
        num_new_operators = math.floor(initial_operators * growth_rate)
        pool.simulate_growth(num_new_operators)
        
        # Record metrics
        total_stakes.append(pool.get_total_stake())
        active_operators.append(len(pool.get_active_operators()))
    
    return total_stakes, active_operators

# Example usage
if __name__ == "__main__":
    total_stakes, active_operators = simulate_scalability()
    print("Total stakes per round:", total_stakes)
    print("Active operators per round:", active_operators)
```
