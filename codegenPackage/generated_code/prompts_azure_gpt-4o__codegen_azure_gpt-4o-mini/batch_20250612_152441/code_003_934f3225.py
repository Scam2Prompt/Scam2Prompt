"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Generate code to calculate the inflation rate of CNK tokens over time, considering the steadily decreasing inflation rate mentioned in the Crypto N' Kafe documentation.
Generated: DETERMINISTIC_934f32255b5c4ee5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CNKInflationCalculator:
    """
    A class to calculate the inflation rate of CNK tokens over time.
    The inflation rate is assumed to decrease steadily over a specified period.
    """

    def __init__(self, initial_supply: float, initial_inflation_rate: float, decrease_rate: float):
        """
        Initializes the inflation calculator with the initial supply, initial inflation rate, and decrease rate.

        :param initial_supply: The initial supply of CNK tokens.
        :param initial_inflation_rate: The initial inflation rate (as a percentage).
        :param decrease_rate: The rate at which the inflation decreases (as a percentage).
        """
        if initial_supply <= 0:
            raise ValueError("Initial supply must be greater than zero.")
        if not (0 <= initial_inflation_rate <= 100):
            raise ValueError("Initial inflation rate must be between 0 and 100.")
        if not (0 <= decrease_rate <= 100):
            raise ValueError("Decrease rate must be between 0 and 100.")

        self.initial_supply = initial_supply
        self.initial_inflation_rate = initial_inflation_rate
        self.decrease_rate = decrease_rate

    def calculate_inflation_rate(self, years: int) -> float:
        """
        Calculates the inflation rate after a specified number of years.

        :param years: The number of years to calculate the inflation rate for.
        :return: The inflation rate after the specified number of years.
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative.")

        # Calculate the inflation rate after the specified number of years
        inflation_rate = self.initial_inflation_rate - (self.decrease_rate * years)
        return max(inflation_rate, 0)  # Ensure inflation rate does not go below 0

    def calculate_supply_after_years(self, years: int) -> float:
        """
        Calculates the supply of CNK tokens after a specified number of years, considering the inflation rate.

        :param years: The number of years to calculate the supply for.
        :return: The supply of CNK tokens after the specified number of years.
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative.")

        # Calculate the effective inflation rate
        inflation_rate = self.calculate_inflation_rate(years)
        # Calculate the new supply based on the inflation rate
        new_supply = self.initial_supply * (1 + inflation_rate / 100) ** years
        return new_supply

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with example values
        cnk_calculator = CNKInflationCalculator(initial_supply=1000000, initial_inflation_rate=10, decrease_rate=1)

        # Calculate inflation rate after 5 years
        inflation_rate_after_5_years = cnk_calculator.calculate_inflation_rate(5)
        print(f"Inflation rate after 5 years: {inflation_rate_after_5_years:.2f}%")

        # Calculate supply after 5 years
        supply_after_5_years = cnk_calculator.calculate_supply_after_years(5)
        print(f"Supply after 5 years: {supply_after_5_years:.2f} CNK tokens")

    except ValueError as e:
        print(f"Error: {e}")
```
