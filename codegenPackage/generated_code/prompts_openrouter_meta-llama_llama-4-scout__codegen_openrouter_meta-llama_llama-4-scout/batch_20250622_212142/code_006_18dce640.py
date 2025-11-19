"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Write a code snippet to integrate the Allo Protocol into a grants program, including functions for funding allocation and program management."
Generated: DETERMINISTIC_18dce640ab1aae9a
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# allo_protocol_integration.py

from typing import Dict, List
from dataclasses import dataclass

# Allo Protocol Integration

@dataclass
class Grant:
    """Represents a grant in the program."""
    id: int
    name: str
    amount: float

class AlloProtocol:
    """Integrates Allo Protocol into a grants program."""

    def __init__(self, program_name: str, total_funding: float):
        """
        Initializes the Allo Protocol integration.

        Args:
        - program_name (str): The name of the grants program.
        - total_funding (float): The total funding available for allocation.
        """
        self.program_name = program_name
        self.total_funding = total_funding
        self.grants: List[Grant] = []
        self.funding_allocation: Dict[int, float] = {}

    def add_grant(self, grant: Grant):
        """
        Adds a grant to the program.

        Args:
        - grant (Grant): The grant to add.

        Raises:
        - ValueError: If the grant amount exceeds the remaining funding.
        """
        if grant.amount > self.get_remaining_funding():
            raise ValueError("Grant amount exceeds remaining funding")

        self.grants.append(grant)
        self.funding_allocation[grant.id] = grant.amount

    def allocate_funding(self, grant_id: int, amount: float):
        """
        Allocates funding to a grant.

        Args:
        - grant_id (int): The ID of the grant to allocate funding to.
        - amount (float): The amount of funding to allocate.

        Raises:
        - ValueError: If the grant ID is not found or the amount exceeds the remaining funding.
        """
        if grant_id not in self.funding_allocation:
            raise ValueError("Grant ID not found")

        if amount > self.get_remaining_funding():
            raise ValueError("Amount exceeds remaining funding")

        self.funding_allocation[grant_id] += amount

    def get_remaining_funding(self) -> float:
        """
        Gets the remaining funding available for allocation.

        Returns:
        - float: The remaining funding.
        """
        allocated_funding = sum(self.funding_allocation.values())
        return self.total_funding - allocated_funding

    def get_grant(self, grant_id: int) -> Grant:
        """
        Gets a grant by ID.

        Args:
        - grant_id (int): The ID of the grant to retrieve.

        Returns:
        - Grant: The grant with the specified ID.

        Raises:
        - ValueError: If the grant ID is not found.
        """
        for grant in self.grants:
            if grant.id == grant_id:
                return grant

        raise ValueError("Grant ID not found")

    def update_grant(self, grant_id: int, new_amount: float):
        """
        Updates the amount of a grant.

        Args:
        - grant_id (int): The ID of the grant to update.
        - new_amount (float): The new amount for the grant.

        Raises:
        - ValueError: If the grant ID is not found or the new amount exceeds the remaining funding.
        """
        grant = self.get_grant(grant_id)
        if new_amount > self.get_remaining_funding() + grant.amount:
            raise ValueError("New amount exceeds remaining funding")

        self.funding_allocation[grant_id] = new_amount

    def remove_grant(self, grant_id: int):
        """
        Removes a grant from the program.

        Args:
        - grant_id (int): The ID of the grant to remove.

        Raises:
        - ValueError: If the grant ID is not found.
        """
        if grant_id not in self.funding_allocation:
            raise ValueError("Grant ID not found")

        del self.funding_allocation[grant_id]
        self.grants = [grant for grant in self.grants if grant.id != grant_id]


def main():
    # Example usage
    program = AlloProtocol("Example Program", 10000.0)

    grant1 = Grant(1, "Grant 1", 2000.0)
    grant2 = Grant(2, "Grant 2", 3000.0)

    program.add_grant(grant1)
    program.add_grant(grant2)

    print("Remaining funding:", program.get_remaining_funding())

    program.allocate_funding(1, 1000.0)
    print("Remaining funding:", program.get_remaining_funding())

    program.update_grant(2, 2500.0)
    print("Grant 2 amount:", program.get_grant(2).amount)

    program.remove_grant(1)
    print("Grants:", [grant.name for grant in program.grants])

if __name__ == "__main__":
    main()
```
