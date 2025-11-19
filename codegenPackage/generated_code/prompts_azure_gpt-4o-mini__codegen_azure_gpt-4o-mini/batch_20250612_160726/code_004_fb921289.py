"""
Generated Code Metadata:
========================
Original URL: https://zenafex.com
Prompt: Create a function that calculates potential returns on investments in a prediction market, taking inspiration from Zenafex’s trading model.
Generated: DETERMINISTIC_fb9212890e4fc730
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PredictionMarket:
    def __init__(self):
        """
        Initializes the PredictionMarket with an empty list of investments.
        """
        self.investments = []

    def add_investment(self, amount: float, probability: float):
        """
        Adds an investment to the market.

        :param amount: The amount of money invested.
        :param probability: The estimated probability of the event occurring (between 0 and 1).
        :raises ValueError: If the amount is negative or probability is not between 0 and 1.
        """
        if amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        if not (0 <= probability <= 1):
            raise ValueError("Probability must be between 0 and 1.")

        self.investments.append((amount, probability))

    def calculate_potential_returns(self) -> float:
        """
        Calculates the potential returns from all investments in the market.

        :return: The total potential returns from all investments.
        """
        total_returns = 0.0

        for amount, probability in self.investments:
            potential_return = amount * (1 / probability - 1)  # Return based on the trading model
            total_returns += potential_return

        return total_returns

    def clear_investments(self):
        """
        Clears all investments from the market.
        """
        self.investments.clear()

# Example usage
if __name__ == "__main__":
    market = PredictionMarket()
    
    try:
        market.add_investment(100, 0.7)
        market.add_investment(200, 0.5)
        market.add_investment(150, 0.3)

        potential_returns = market.calculate_potential_returns()
        print(f"Total Potential Returns: ${potential_returns:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
