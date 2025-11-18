"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-jessecoinorg.pages.dev
Prompt: Generate code to calculate token distribution for a cryptocurrency with a total supply of 100,000,000 tokens, ensuring the presale adheres to the specified BASE-to-JESSE exchange rates.
Generated: DETERMINISTIC_ac2bcdc04d5d3ac0
Batch ID: 20250612_153400
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
    A class to calculate the token distribution for a cryptocurrency presale.
    
    Attributes:
        total_supply (int): Total supply of the tokens.
        base_to_jesse_rate (float): The exchange rate from BASE to JESSE.
        presale_percentage (float): The percentage of total supply allocated for presale.
    """

    def __init__(self, total_supply: int, base_to_jesse_rate: float, presale_percentage: float):
        """
        Initializes the TokenDistribution with total supply, exchange rate, and presale percentage.

        Args:
            total_supply (int): The total number of tokens available.
            base_to_jesse_rate (float): The BASE to JESSE exchange rate.
            presale_percentage (float): Percentage of tokens allocated for presale.

        Raises:
            ValueError: If any parameter is out of expected range.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        if base_to_jesse_rate <= 0:
            raise ValueError("Base to Jesse exchange rate must be a positive float.")
        if not (0 < presale_percentage <= 100):
            raise ValueError("Presale percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.base_to_jesse_rate = base_to_jesse_rate
        self.presale_percentage = presale_percentage

    def calculate_presale_tokens(self) -> int:
        """
        Calculates the number of tokens allocated for presale.

        Returns:
            int: Number of tokens allocated for presale.
        """
        return int(self.total_supply * (self.presale_percentage / 100))

    def calculate_exchange_value(self) -> float:
        """
        Calculates the total value of presale tokens in JESSE based on the BASE to JESSE exchange rate.

        Returns:
            float: Total value of presale tokens in JESSE.
        """
        presale_tokens = self.calculate_presale_tokens()
        return presale_tokens * self.base_to_jesse_rate

    def display_distribution(self):
        """
        Displays the token distribution information.
        """
        try:
            presale_tokens = self.calculate_presale_tokens()
            exchange_value = self.calculate_exchange_value()
            print(f"Total Supply: {self.total_supply} tokens")
            print(f"Presale Allocation: {presale_tokens} tokens")
            print(f"Value of Presale Tokens in JESSE: {exchange_value:.2f} JESSE")
        except Exception as e:
            print(f"An error occurred while calculating distribution: {str(e)}")


# Example usage:
if __name__ == "__main__":
    try:
        total_supply = 100_000_000
        base_to_jesse_rate = 1.5  # Example exchange rate
        presale_percentage = 20  # Example presale percentage

        token_distribution = TokenDistribution(total_supply, base_to_jesse_rate, presale_percentage)
        token_distribution.display_distribution()
    except ValueError as ve:
        print(f"Input error: {ve}")
```

This code initializes a `TokenDistribution` class that calculates the presale token allocation and its value in JESSE based on given parameters. It includes error handling to ensure all inputs are valid and provides a method to display the distribution details.
