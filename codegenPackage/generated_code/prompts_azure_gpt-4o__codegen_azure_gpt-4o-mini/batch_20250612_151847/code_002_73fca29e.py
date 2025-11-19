"""
Generated Code Metadata:
========================
Original URL: https://tortoken.io
Prompt: Generate code to calculate the distribution percentages of TOR tokens based on the allocation plan provided (e.g., 25% for Airdrop, 10% for Pre-sale, etc.) using Python.
Generated: DETERMINISTIC_73fca29ebd7f8c15
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenDistribution:
    def __init__(self, total_tokens):
        """
        Initializes the TokenDistribution class with the total number of tokens.

        :param total_tokens: Total number of TOR tokens to distribute.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be a positive integer.")
        self.total_tokens = total_tokens
        self.allocations = {}

    def add_allocation(self, name, percentage):
        """
        Adds an allocation to the distribution plan.

        :param name: Name of the allocation (e.g., 'Airdrop', 'Pre-sale').
        :param percentage: Percentage of total tokens for this allocation.
        :raises ValueError: If the percentage is not between 0 and 100.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.allocations[name] = percentage

    def calculate_distribution(self):
        """
        Calculates the distribution of tokens based on the allocation plan.

        :return: A dictionary with allocation names and their corresponding token amounts.
        :raises ValueError: If the total allocation exceeds 100%.
        """
        total_percentage = sum(self.allocations.values())
        if total_percentage > 100:
            raise ValueError("Total allocation percentages exceed 100%.")

        distribution = {}
        for name, percentage in self.allocations.items():
            distribution[name] = (percentage / 100) * self.total_tokens

        return distribution

    def display_distribution(self):
        """
        Displays the distribution of tokens in a readable format.
        """
        try:
            distribution = self.calculate_distribution()
            print("Token Distribution:")
            for name, amount in distribution.items():
                print(f"{name}: {amount:.2f} TOR tokens")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    try:
        total_tokens = 1000000  # Total TOR tokens
        distribution_plan = TokenDistribution(total_tokens)

        # Adding allocations
        distribution_plan.add_allocation("Airdrop", 25)
        distribution_plan.add_allocation("Pre-sale", 10)
        distribution_plan.add_allocation("Staking Rewards", 15)
        distribution_plan.add_allocation("Team", 20)
        distribution_plan.add_allocation("Development", 30)  # This will cause an error

        # Display the distribution
        distribution_plan.display_distribution()
    except Exception as e:
        print(f"An error occurred: {e}")
```
