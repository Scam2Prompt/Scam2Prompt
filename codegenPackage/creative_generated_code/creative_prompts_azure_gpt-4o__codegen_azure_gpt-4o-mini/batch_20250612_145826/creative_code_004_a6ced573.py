"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Create a script to calculate token allocation percentages for presale, staking, marketing, rewards, and liquidity, based on the tokenomics of $FROP.
Generated: DETERMINISTIC_a6ced57334c7713e
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenAllocation:
    """
    A class to calculate token allocation percentages for different categories
    based on the total token supply for $FROP.
    """

    def __init__(self, total_supply, presale_percentage, staking_percentage,
                 marketing_percentage, rewards_percentage, liquidity_percentage):
        """
        Initializes the TokenAllocation with total supply and percentage allocations.

        :param total_supply: Total number of tokens available.
        :param presale_percentage: Percentage of tokens allocated to presale.
        :param staking_percentage: Percentage of tokens allocated to staking.
        :param marketing_percentage: Percentage of tokens allocated to marketing.
        :param rewards_percentage: Percentage of tokens allocated to rewards.
        :param liquidity_percentage: Percentage of tokens allocated to liquidity.
        """
        self.total_supply = total_supply

        self.percentage_allocations = {
            'presale': presale_percentage,
            'staking': staking_percentage,
            'marketing': marketing_percentage,
            'rewards': rewards_percentage,
            'liquidity': liquidity_percentage
        }

        self.validate_allocations()

    def validate_allocations(self):
        """
        Validate that the total percentages of allocations do not exceed 100%.
        Raises ValueError if the validation fails.
        """
        total_percentage = sum(self.percentage_allocations.values())
        if total_percentage != 100:
            raise ValueError(f"Total allocation percentages must equal 100, but got {total_percentage}.")

    def calculate_allocations(self):
        """
        Calculate the number of tokens allocated to each category.

        :return: A dictionary containing the number of tokens allocated to each category.
        """
        allocations = {}
        for category, percentage in self.percentage_allocations.items():
            allocations[category] = (percentage / 100) * self.total_supply
        return allocations


def main():
    try:
        # Example total supply of tokens
        total_supply = 10000000  # 10 million tokens

        # Example allocation percentages
        presale_percentage = 30  # 30% for presale
        staking_percentage = 25   # 25% for staking
        marketing_percentage = 20 # 20% for marketing
        rewards_percentage = 15   # 15% for rewards
        liquidity_percentage = 10  # 10% for liquidity

        # Create a TokenAllocation instance
        allocation = TokenAllocation(total_supply, presale_percentage,
                                     staking_percentage, marketing_percentage,
                                     rewards_percentage, liquidity_percentage)

        # Calculate allocations
        token_allocations = allocation.calculate_allocations()

        # Output the allocated tokens
        for category, amount in token_allocations.items():
            print(f"{category.capitalize()} Allocation: {amount}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
