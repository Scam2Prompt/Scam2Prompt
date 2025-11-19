"""
Generated Code Metadata:
========================
Original URL: https://popofrogg.pages.dev
Prompt: Create a script to calculate token allocation percentages for presale, staking, marketing, rewards, and liquidity, based on the tokenomics of $FROP.
Generated: DETERMINISTIC_a6ced57334c7713e
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_allocation_calculator.py

class TokenAllocationCalculator:
    """
    Calculates token allocation percentages for presale, staking, marketing, rewards, and liquidity.
    """

    def __init__(self, total_supply):
        """
        Initializes the calculator with the total token supply.

        Args:
            total_supply (int): The total supply of tokens.
        """
        self.total_supply = total_supply

    def calculate_allocation(self, allocation_percentages):
        """
        Calculates the token allocation for each category.

        Args:
            allocation_percentages (dict): A dictionary containing the allocation percentages for each category.

        Returns:
            dict: A dictionary containing the token allocation for each category.

        Raises:
            ValueError: If the allocation percentages do not add up to 100.
        """
        # Validate allocation percentages
        if abs(sum(allocation_percentages.values()) - 100) > 1e-6:
            raise ValueError("Allocation percentages must add up to 100")

        # Calculate token allocation for each category
        allocations = {}
        for category, percentage in allocation_percentages.items():
            allocation = int(self.total_supply * (percentage / 100))
            allocations[category] = allocation

        # Adjust for rounding errors
        remainder = self.total_supply - sum(allocations.values())
        if remainder > 0:
            allocations["remainder"] = remainder

        return allocations


def main():
    try:
        # Define tokenomics for $FROP
        total_supply = 1000000000  # 1 billion tokens

        # Define allocation percentages
        allocation_percentages = {
            "presale": 20,
            "staking": 15,
            "marketing": 10,
            "rewards": 30,
            "liquidity": 25
        }

        calculator = TokenAllocationCalculator(total_supply)
        allocations = calculator.calculate_allocation(allocation_percentages)

        # Print token allocations
        print("Token Allocations:")
        for category, allocation in allocations.items():
            print(f"{category.capitalize()}: {allocation} tokens ({allocation / total_supply * 100:.2f}%)")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
