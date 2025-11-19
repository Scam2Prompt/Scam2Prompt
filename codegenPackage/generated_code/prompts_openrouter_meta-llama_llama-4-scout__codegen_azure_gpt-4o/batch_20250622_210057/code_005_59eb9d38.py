"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogs.pages.dev
Prompt: Design a tokenomics system for a new cryptocurrency project, inspired by the 900 million token supply and 90% token availability described for the Bitcoin Dogs project.
Generated: DETERMINISTIC_59eb9d388d4b5e37
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import decimal

class TokenomicsSystem:
    """
    A class to represent the tokenomics system for a cryptocurrency project.
    Inspired by the Bitcoin Dogs project with a 900 million token supply and 90% token availability.
    """

    def __init__(self, total_supply: int, available_percentage: float):
        """
        Initialize the tokenomics system.

        :param total_supply: Total token supply (e.g., 900 million).
        :param available_percentage: Percentage of tokens available for circulation (e.g., 90%).
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= available_percentage <= 100):
            raise ValueError("Available percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.available_percentage = available_percentage
        self.available_supply = self.calculate_available_supply()
        self.reserved_supply = self.calculate_reserved_supply()

    def calculate_available_supply(self) -> int:
        """
        Calculate the number of tokens available for circulation.

        :return: Available token supply.
        """
        return int(self.total_supply * (self.available_percentage / 100))

    def calculate_reserved_supply(self) -> int:
        """
        Calculate the number of tokens reserved (not available for circulation).

        :return: Reserved token supply.
        """
        return self.total_supply - self.available_supply

    def distribute_tokens(self, allocation: dict) -> dict:
        """
        Distribute available tokens based on allocation percentages.

        :param allocation: A dictionary where keys are entity names and values are allocation percentages.
        :return: A dictionary with entity names and their allocated token amounts.
        """
        if not allocation:
            raise ValueError("Allocation dictionary cannot be empty.")
        if sum(allocation.values()) != 100:
            raise ValueError("Allocation percentages must sum to 100.")

        distribution = {}
        for entity, percentage in allocation.items():
            distribution[entity] = int(self.available_supply * (percentage / 100))
        return distribution

    def __str__(self):
        """
        Return a string representation of the tokenomics system.

        :return: String representation of the tokenomics system.
        """
        return (f"Total Supply: {self.total_supply}\n"
                f"Available Supply: {self.available_supply}\n"
                f"Reserved Supply: {self.reserved_supply}\n"
                f"Available Percentage: {self.available_percentage}%")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics system
        tokenomics = TokenomicsSystem(total_supply=900_000_000, available_percentage=90)

        # Print tokenomics details
        print(tokenomics)

        # Define allocation percentages
        allocation = {
            "Team": 20,
            "Marketing": 30,
            "Community Rewards": 50
        }

        # Distribute tokens based on allocation
        distribution = tokenomics.distribute_tokens(allocation)
        print("\nToken Distribution:")
        for entity, tokens in distribution.items():
            print(f"{entity}: {tokens} tokens")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
