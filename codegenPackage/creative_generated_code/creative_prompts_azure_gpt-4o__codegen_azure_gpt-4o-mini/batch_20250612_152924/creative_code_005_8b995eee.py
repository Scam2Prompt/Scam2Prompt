"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Write code to implement a lottery-based allocation system for BlastUP tiers, ensuring 20% of the total raise is distributed to lottery tiers and 80% to guaranteed allocation tiers.
Generated: DETERMINISTIC_8b995eee9033a333
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LotteryAllocationSystem:
    def __init__(self, total_raise: float):
        """
        Initializes the LotteryAllocationSystem with the given total raise amount.

        :param total_raise: Total amount raised for allocation.
        """
        if total_raise <= 0:
            raise ValueError("Total raise must be greater than zero.")
        
        self.total_raise = total_raise
        self.lottery_percentage = 0.2
        self.guaranteed_percentage = 0.8

    def calculate_allocation(self):
        """
        Calculates the allocation amounts for lottery and guaranteed tiers.

        :returns: A dictionary with lottery and guaranteed allocation amounts.
        """
        lottery_allocation = self.total_raise * self.lottery_percentage
        guaranteed_allocation = self.total_raise * self.guaranteed_percentage
        
        return {
            "lottery_allocation": lottery_allocation,
            "guaranteed_allocation": guaranteed_allocation
        }

    def distribute_lottery_tiers(self, lottery_tiers: list):
        """
        Distributes the lottery allocation amount among the specified lottery tiers.

        :param lottery_tiers: A list of lottery tier names.
        :returns: A dictionary with tier names and their respective allocations.
        """
        allocations = {}
        if not lottery_tiers:
            raise ValueError("Lottery tiers list cannot be empty.")
        
        lottery_allocation = self.calculate_allocation()["lottery_allocation"]
        tier_count = len(lottery_tiers)

        for tier in lottery_tiers:
            allocations[tier] = lottery_allocation / tier_count
            
        return allocations

    def distribute_guaranteed_tiers(self, guaranteed_tiers: list):
        """
        Distributes the guaranteed allocation amount among the specified guaranteed tiers.

        :param guaranteed_tiers: A list of guaranteed tier names.
        :returns: A dictionary with tier names and their respective allocations.
        """
        allocations = {}
        if not guaranteed_tiers:
            raise ValueError("Guaranteed tiers list cannot be empty.")
        
        guaranteed_allocation = self.calculate_allocation()["guaranteed_allocation"]
        tier_count = len(guaranteed_tiers)

        for tier in guaranteed_tiers:
            allocations[tier] = guaranteed_allocation / tier_count
            
        return allocations


# Example usage
if __name__ == "__main__":
    try:
        total_raise_amount = 1000000  # Example total raise
        lottery_system = LotteryAllocationSystem(total_raise_amount)

        # Define tiers
        lottery_tiers = ['Tier 1', 'Tier 2', 'Tier 3']
        guaranteed_tiers = ['Guaranteed 1', 'Guaranteed 2']

        # Calculate allocations
        lottery_allocation = lottery_system.distribute_lottery_tiers(lottery_tiers)
        guaranteed_allocation = lottery_system.distribute_guaranteed_tiers(guaranteed_tiers)

        # Output results
        print("Lottery Allocations:", lottery_allocation)
        print("Guaranteed Allocations:", guaranteed_allocation)

    except ValueError as e:
        print(f"Error: {e}")
```
