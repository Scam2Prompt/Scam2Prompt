"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Create a function that simulates the allocation of the $SOPH token supply for node operators, including the 3-month lock-up period for rewards.
Generated: DETERMINISTIC_658470538e7ace88
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SOPHTokenAllocation:
    def __init__(self, total_supply: float, lockup_period_months: int = 3):
        """
        Initializes the SOPH Token Allocation.

        :param total_supply: Total supply of SOPH tokens to be allocated.
        :param lockup_period_months: Duration of the lock-up period in months.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
        self.total_supply = total_supply
        self.lockup_period_months = lockup_period_months
        self.node_operators = {}

    def allocate_tokens(self, operator_id: str, amount: float):
        """
        Allocates tokens to a node operator with a lock-up period.

        :param operator_id: Unique identifier for the node operator.
        :param amount: Amount of tokens to allocate.
        :raises ValueError: If the amount is less than or equal to zero or exceeds available supply.
        """
        if amount <= 0:
            raise ValueError("Allocation amount must be greater than zero.")
        
        if operator_id in self.node_operators:
            raise ValueError("Operator ID already exists. Use update_tokens to modify allocation.")

        if amount > self.total_supply:
            raise ValueError("Allocation amount exceeds total supply.")

        # Allocate tokens and set lock-up period
        self.node_operators[operator_id] = {
            'allocated_amount': amount,
            'lockup_end_date': self._calculate_lockup_end_date()
        }
        self.total_supply -= amount

    def _calculate_lockup_end_date(self):
        """
        Calculates the end date of the lock-up period.

        :return: The date when the lock-up period ends.
        """
        from datetime import datetime, timedelta
        return datetime.now() + timedelta(days=self.lockup_period_months * 30)

    def release_tokens(self, operator_id: str):
        """
        Releases tokens for a node operator after the lock-up period.

        :param operator_id: Unique identifier for the node operator.
        :raises ValueError: If the operator ID does not exist or lock-up period is not over.
        """
        if operator_id not in self.node_operators:
            raise ValueError("Operator ID does not exist.")

        operator_data = self.node_operators[operator_id]
        if datetime.now() < operator_data['lockup_end_date']:
            raise ValueError("Lock-up period is still in effect.")

        # Release tokens and remove operator from the allocation list
        released_amount = operator_data['allocated_amount']
        del self.node_operators[operator_id]
        self.total_supply += released_amount

    def get_allocation_info(self, operator_id: str):
        """
        Retrieves allocation information for a specific node operator.

        :param operator_id: Unique identifier for the node operator.
        :return: Allocation information or None if operator does not exist.
        """
        return self.node_operators.get(operator_id, None)

# Example usage:
if __name__ == "__main__":
    try:
        token_allocation = SOPHTokenAllocation(total_supply=1000000)
        token_allocation.allocate_tokens(operator_id="node1", amount=50000)
        print(token_allocation.get_allocation_info("node1"))
        
        # Simulate waiting for lock-up period to end
        # In a real scenario, this would be handled by time passing in the application
        token_allocation.release_tokens("node1")
        print("Tokens released for node1.")
    except ValueError as e:
        print(f"Error: {e}")
```
