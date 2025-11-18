"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tortoken.io
Prompt: Generate code to calculate the distribution percentages of TOR tokens based on the allocation plan provided (e.g., 25% for Airdrop, 10% for Pre-sale, etc.) using Python.
Generated: DETERMINISTIC_73fca29ebd7f8c15
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenDistribution:
    """
    A class to calculate the distribution percentages of TOR tokens based on a given allocation plan.
    """

    def __init__(self, total_tokens: float):
        """
        Initializes the TokenDistribution class with the total number of tokens.

        Args:
            total_tokens (float): The total number of TOR tokens available for distribution.

        Raises:
            ValueError: If total_tokens is less than or equal to zero.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        self.total_tokens = total_tokens
        self.allocations = {}

    def add_allocation(self, name: str, percentage: float):
        """
        Adds an allocation plan for the TOR tokens.

        Args:
            name (str): The name of the allocation (e.g., 'Airdrop').
            percentage (float): The percentage of total tokens for this allocation.

        Raises:
            ValueError: If percentage is negative or if it causes total allocations to exceed 100%.
        """
        if percentage < 0:
            raise ValueError("Percentage cannot be negative.")
        current_total_percentage = sum(self.allocations.values())
        if current_total_percentage + percentage > 100:
            raise ValueError("Total allocation cannot exceed 100%.")
        
        self.allocations[name] = percentage

    def calculate_distribution(self):
        """
        Calculates the distribution of tokens based on the allocation percentages.

        Returns:
            dict: A dictionary with allocation names as keys and the number of tokens allocated as values.
        """
        distribution = {}
        for name, percentage in self.allocations.items():
            allocated_tokens = (percentage / 100) * self.total_tokens
            distribution[name] = allocated_tokens
        return distribution

    def display_distribution(self):
        """
        Displays the distribution of TOR tokens in a readable format.
        """
        distribution = self.calculate_distribution()
        print("TOR Token Distribution:")
        for name, allocated_tokens in distribution.items():
            print(f"{name}: {allocated_tokens:.2f} TOR tokens")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the TokenDistribution with total tokens
        total_tokens = 1000000  # Example total tokens
        token_distribution = TokenDistribution(total_tokens)

        # Add allocation plans
        token_distribution.add_allocation('Airdrop', 25)
        token_distribution.add_allocation('Pre-sale', 10)
        token_distribution.add_allocation('Team', 15)
        token_distribution.add_allocation('Reserve', 20)
        token_distribution.add_allocation('Development', 30)  # This should be fine

        # Display the distribution
        token_distribution.display_distribution()

    except ValueError as e:
        print(f"Error: {e}")
```
