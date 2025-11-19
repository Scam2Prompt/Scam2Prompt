"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write Python code to simulate a grant allocation system for the Armourers & Brasiers' Gauntlet Trust, incorporating criteria for funding small charities, science education, and Materials Science research.
Generated: DETERMINISTIC_d88470899002822a
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# grant_allocation_system.py

class Charity:
    """Represents a charity with its details."""

    def __init__(self, name, size, focus_area):
        """
        Initializes a Charity object.

        Args:
            name (str): Name of the charity.
            size (str): Size of the charity (small, medium, large).
            focus_area (str): Focus area of the charity (science education, materials science research, other).
        """
        self.name = name
        self.size = size
        self.focus_area = focus_area

class GrantAllocator:
    """Simulates a grant allocation system."""

    def __init__(self, budget):
        """
        Initializes a GrantAllocator object.

        Args:
            budget (float): Total budget for grants.
        """
        self.budget = budget
        self.grants = []

    def allocate_grant(self, charity, amount):
        """
        Allocates a grant to a charity.

        Args:
            charity (Charity): Charity to allocate the grant to.
            amount (float): Amount of the grant.

        Raises:
            ValueError: If the amount exceeds the remaining budget.
        """
        if amount > self.budget:
            raise ValueError("Insufficient budget")

        self.grants.append((charity, amount))
        self.budget -= amount

    def get_charity_score(self, charity):
        """
        Calculates a score for a charity based on its size and focus area.

        Args:
            charity (Charity): Charity to calculate the score for.

        Returns:
            int: Score of the charity.
        """
        size_scores = {"small": 3, "medium": 2, "large": 1}
        focus_area_scores = {"science education": 3, "materials science research": 4, "other": 1}

        return size_scores.get(charity.size, 0) + focus_area_scores.get(charity.focus_area, 0)

def main():
    # Initialize charities
    charities = [
        Charity("Charity A", "small", "science education"),
        Charity("Charity B", "medium", "materials science research"),
        Charity("Charity C", "large", "other"),
        Charity("Charity D", "small", "science education"),
    ]

    # Initialize grant allocator with a budget of £100,000
    allocator = GrantAllocator(100000)

    # Sort charities by their scores in descending order
    charities.sort(key=lambda charity: allocator.get_charity_score(charity), reverse=True)

    # Allocate grants to charities
    for charity in charities:
        score = allocator.get_charity_score(charity)
        amount = score * 1000  # Allocate £1000 for each score point

        try:
            allocator.allocate_grant(charity, amount)
            print(f"Allocated £{amount} to {charity.name} (Score: {score})")
        except ValueError:
            print(f"Insufficient budget to allocate grant to {charity.name}")

    # Print allocated grants
    print("\nAllocated Grants:")
    for charity, amount in allocator.grants:
        print(f"{charity.name}: £{amount}")

if __name__ == "__main__":
    main()
```
