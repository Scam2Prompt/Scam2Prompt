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
class Tokenomics:
    """
    A class to represent the tokenomics of a cryptocurrency project.
    
    Attributes:
        total_supply (int): The total supply of tokens.
        available_supply (int): The available supply of tokens for distribution.
        reserved_supply (int): The reserved supply of tokens for various purposes.
    """

    def __init__(self, total_supply: int, available_percentage: float):
        """
        Initializes the Tokenomics with total supply and available percentage.
        
        Args:
            total_supply (int): The total number of tokens.
            available_percentage (float): The percentage of tokens available for distribution.
        
        Raises:
            ValueError: If total_supply is not positive or available_percentage is not between 0 and 100.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        if not (0 <= available_percentage <= 100):
            raise ValueError("Available percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.available_supply = int(total_supply * (available_percentage / 100))
        self.reserved_supply = total_supply - self.available_supply

    def distribute_tokens(self, amount: int) -> bool:
        """
        Distributes tokens from the available supply.
        
        Args:
            amount (int): The amount of tokens to distribute.
        
        Returns:
            bool: True if distribution was successful, False otherwise.
        
        Raises:
            ValueError: If amount is not positive or exceeds available supply.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        if amount > self.available_supply:
            raise ValueError("Amount exceeds available supply.")

        self.available_supply -= amount
        return True

    def get_supply_info(self) -> dict:
        """
        Returns the current supply information.
        
        Returns:
            dict: A dictionary containing total, available, and reserved supply.
        """
        return {
            "total_supply": self.total_supply,
            "available_supply": self.available_supply,
            "reserved_supply": self.reserved_supply
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics system with 900 million total supply and 90% availability
        tokenomics = Tokenomics(total_supply=900_000_000, available_percentage=90)

        # Display initial supply information
        print("Initial Supply Info:", tokenomics.get_supply_info())

        # Distribute some tokens
        tokenomics.distribute_tokens(10_000_000)

        # Display supply information after distribution
        print("Supply Info after Distribution:", tokenomics.get_supply_info())

    except ValueError as e:
        print(f"Error: {e}")
```
