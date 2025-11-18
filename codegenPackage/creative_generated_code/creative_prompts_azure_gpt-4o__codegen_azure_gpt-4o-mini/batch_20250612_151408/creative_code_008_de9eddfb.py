"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffer.pages.dev
Prompt: Create a script to simulate the scalability of Puffer's stake pool with diverse Node Operators and a low capital requirement of 0.25 ETH.
Generated: DETERMINISTIC_de9eddfba11aa8e0
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class NodeOperator:
    """
    Represents a Node Operator in the stake pool.
    Each operator is initialized with a name, capital, and a performance metric.
    """

    def __init__(self, name: str, capital: float):
        if capital < 0:
            raise ValueError("Capital must be a non-negative value.")
        self.name = name
        self.capital = capital
        self.performance_metric = self.calculate_performance_metric()

    def calculate_performance_metric(self) -> float:
        """
        Simulates a performance metric based on the capital.
        Higher capital generally leads to better performance.
        """
        return self.capital * random.uniform(0.8, 1.2)  # Simulate performance variability

    def __repr__(self):
        return f"NodeOperator(name={self.name}, capital={self.capital}, performance={self.performance_metric})"


class StakePool:
    """
    Represents a Stake Pool consisting of multiple Node Operators.
    It manages the pool's total capital and calculates overall performance.
    """

    def __init__(self, capital_requirement: float):
        self.capital_requirement = capital_requirement
        self.operators: List[NodeOperator] = []

    def add_operator(self, operator: NodeOperator) -> None:
        """
        Adds a Node Operator to the stake pool if it meets the capital requirement.
        """
        if operator.capital < self.capital_requirement:
            raise ValueError(f"Operator {operator.name} does not meet the capital requirement of {self.capital_requirement} ETH.")
        self.operators.append(operator)

    def total_performance(self) -> float:
        """
        Calculates the total performance of all operators in the pool.
        """
        if not self.operators:
            return 0.0
        return sum(operator.performance_metric for operator in self.operators)

    def __repr__(self):
        return f"StakePool(total_operators={len(self.operators)}, total_performance={self.total_performance()})"


def simulate_stake_pool(num_operators: int, capital_requirement: float) -> StakePool:
    """
    Simulates the creation of a stake pool with a specified number of Node Operators.
    Each operator is assigned random capital between the requirement and double the requirement.
    """
    pool = StakePool(capital_requirement)

    for i in range(num_operators):
        # Randomly generate capital between requirement and double the requirement
        capital = random.uniform(capital_requirement, 2 * capital_requirement)
        operator = NodeOperator(name=f"Operator_{i + 1}", capital=capital)
        
        try:
            pool.add_operator(operator)
        except ValueError as e:
            print(f"Error adding operator: {e}")

    return pool


if __name__ == "__main__":
    NUM_OPERATORS = 10
    CAPITAL_REQUIREMENT = 0.25  # in ETH

    # Simulate the stake pool
    stake_pool = simulate_stake_pool(NUM_OPERATORS, CAPITAL_REQUIREMENT)

    # Display the results
    print(stake_pool)
    for operator in stake_pool.operators:
        print(operator)
```
