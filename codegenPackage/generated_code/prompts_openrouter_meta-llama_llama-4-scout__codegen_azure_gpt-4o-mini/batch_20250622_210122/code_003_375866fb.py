"""
Generated Code Metadata:
========================
Original URL: https://bitcoindog.pages.dev
Prompt: Design a tokenomics system for a new cryptocurrency project, using the 900 million token supply and 90% token availability described in the Bitcoin Dogs tokenomics section.
Generated: DETERMINISTIC_375866fb3ab459a2
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    def __init__(self, total_supply: int, available_supply_percentage: float):
        """
        Initializes the Tokenomics system with total supply and available supply percentage.

        :param total_supply: Total number of tokens available for the project.
        :param available_supply_percentage: Percentage of tokens that are available for distribution.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        if not (0 <= available_supply_percentage <= 100):
            raise ValueError("Available supply percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.available_supply_percentage = available_supply_percentage
        self.available_supply = self.calculate_available_supply()

    def calculate_available_supply(self) -> int:
        """
        Calculates the available supply based on the total supply and available supply percentage.

        :return: The number of tokens available for distribution.
        """
        return int(self.total_supply * (self.available_supply_percentage / 100))

    def distribute_tokens(self, amount: int) -> str:
        """
        Distributes tokens to users.

        :param amount: The number of tokens to distribute.
        :return: A message indicating the result of the distribution.
        """
        if amount <= 0:
            return "Amount must be a positive integer."
        if amount > self.available_supply:
            return "Insufficient available supply for distribution."

        self.available_supply -= amount
        return f"Successfully distributed {amount} tokens. Remaining available supply: {self.available_supply}"

    def get_tokenomics_summary(self) -> dict:
        """
        Provides a summary of the tokenomics.

        :return: A dictionary containing total supply, available supply, and available supply percentage.
        """
        return {
            "total_supply": self.total_supply,
            "available_supply": self.available_supply,
            "available_supply_percentage": self.available_supply_percentage
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Tokenomics system with 900 million total supply and 90% availability
        tokenomics = Tokenomics(total_supply=900_000_000, available_supply_percentage=90)

        # Print the tokenomics summary
        print(tokenomics.get_tokenomics_summary())

        # Distribute some tokens
        print(tokenomics.distribute_tokens(10_000_000))  # Distributing 10 million tokens
        print(tokenomics.get_tokenomics_summary())  # Print updated summary

    except ValueError as e:
        print(f"Error: {e}")
```
