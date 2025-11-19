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
import uuid


class SOPHTokenAllocationError(Exception):
    """Custom exception for SOPH token allocation errors."""
    pass


class TokenAllocation:
    def __init__(self, total_supply):
        """
        Initializes the TokenAllocation class.

        :param total_supply: Total supply of SOPH tokens available for allocation.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than 0.")
        self.total_supply = total_supply
        self.node_operator_allocations = {}

    def allocate_tokens(self, node_operator_id, allocation_amount):
        """
        Allocates tokens to a specific node operator.

        :param node_operator_id: Unique identifier for the node operator.
        :param allocation_amount: Number of tokens to allocate to the node operator.
        :raises SOPHTokenAllocationError: If there are insufficient tokens or invalid inputs.
        """
        if allocation_amount <= 0:
            raise SOPHTokenAllocationError("Allocation amount must be greater than 0.")
        if allocation_amount > self.total_supply:
            raise SOPHTokenAllocationError("Insufficient tokens for allocation.")

        # Reduce the available supply
        self.total_supply -= allocation_amount

        # Set up allocation with a lock-up period
        lock_up_period_end = datetime.now() + timedelta(days=90)
        self.node_operator_allocations[node_operator_id] = {
            "allocation_amount": allocation_amount,
            "allocation_date": datetime.now(),
            "lock_up_period_end": lock_up_period_end,
        }

    def check_rewards_status(self, node_operator_id):
        """
        Checks if the lock-up period for a node operator's rewards has ended.

        :param node_operator_id: Unique identifier for the node operator.
        :return: A tuple containing the status (True/False) and remaining lock-up days.
        :raises KeyError: If the node operator ID is not found.
        """
        if node_operator_id not in self.node_operator_allocations:
            raise KeyError("Node operator ID not found.")

        allocation = self.node_operator_allocations[node_operator_id]
        now = datetime.now()
        remaining_days = (allocation["lock_up_period_end"] - now).days

        if now >= allocation["lock_up_period_end"]:
            return True, 0  # Lock-up period ended
        return False, max(remaining_days, 0)  # Lock-up period ongoing

    def get_allocation_details(self):
        """
        Retrieves a summary of all token allocations.

        :return: A dictionary containing all allocations.
        """
        return self.node_operator_allocations


# Example Usage (Uncomment to test)
if __name__ == "__main__":
    try:
        # Create an instance of TokenAllocation with a given supply
        total_supply = 1000000  # Example: 1,000,000 SOPH tokens
        allocation_system = TokenAllocation(total_supply)

        # Allocate tokens to node operators
        node_operator_1 = str(uuid.uuid4())
        allocation_system.allocate_tokens(node_operator_1, 50000)

        node_operator_2 = str(uuid.uuid4())
        allocation_system.allocate_tokens(node_operator_2, 75000)

        # Check lock-up status for a node operator
        status, days_left = allocation_system.check_rewards_status(node_operator_1)
        print(f"Node Operator 1 Rewards Status: {'Unlocked' if status else 'Locked'}, Days Left: {days_left}")

        # Print summary of allocations
        print("Allocations:", allocation_system.get_allocation_details())

    except Exception as e:
        print(f"Error: {str(e)}")
```
