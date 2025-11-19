"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Create a function that simulates the allocation of the $SOPH token supply for node operators, including the 3-month lock-up period for rewards.
Generated: DETERMINISTIC_658470538e7ace88
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import random

class SOPHTokenAllocator:
    def __init__(self, total_supply: float, lockup_period_months: int = 3):
        """
        Initialize the SOPH Token Allocator.

        :param total_supply: Total amount of SOPH tokens available for allocation.
        :param lockup_period_months: Duration (in months) for the lock-up period. Default is 3 months.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive value.")

        self.total_supply = total_supply
        self.lockup_period = timedelta(days=lockup_period_months * 30)  # Approximation of 30 days per month
        self.allocations = []

    def allocate_tokens(self, node_operators: dict):
        """
        Allocates SOPH tokens to node operators based on their performance.

        :param node_operators: A dictionary where keys are operator IDs and values are their performance metrics.
        :return: A list of allocated tokens for each node operator.
        """
        total_performance = sum(node_operators.values())
        
        if total_performance <= 0:
            raise ValueError("Total performance must be positive to allocate tokens.")

        for operator_id, performance in node_operators.items():
            # Calculate the allocation based on performance ratio
            allocation = (performance / total_performance) * self.total_supply
            
            # Apply lock-up period to allocations
            lockup_end_date = datetime.now() + self.lockup_period
            
            self.allocations.append({
                'operator_id': operator_id,
                'allocated_tokens': allocation,
                'lockup_end_date': lockup_end_date.strftime('%Y-%m-%d %H:%M:%S')
            })

        return self.allocations

    def display_allocations(self):
        """
        Display the allocation results in a readable format.
        """
        for allocation in self.allocations:
            print(f"Operator ID: {allocation['operator_id']}, "
                  f"Allocated Tokens: {allocation['allocated_tokens']:.2f}, "
                  f"Lock-up End Date: {allocation['lockup_end_date']}")

# Example usage:
if __name__ == "__main__":
    try:
        token_allocator = SOPHTokenAllocator(total_supply=1000000)
        node_operators = {
            'node1': random.uniform(1, 100),
            'node2': random.uniform(1, 100),
            'node3': random.uniform(1, 100)
        }
        allocations = token_allocator.allocate_tokens(node_operators)
        token_allocator.display_allocations()
    except ValueError as e:
        print(f"Error: {e}")
```
