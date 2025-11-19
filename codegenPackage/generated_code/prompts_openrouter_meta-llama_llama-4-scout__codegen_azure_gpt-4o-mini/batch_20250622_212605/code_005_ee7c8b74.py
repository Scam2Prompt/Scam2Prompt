"""
Generated Code Metadata:
========================
Original URL: https://lifonex.com
Prompt: Create a function to convert Lifonex market probabilities into potential profit/loss calculations, taking into account the 4.05% APY on cash and positions.
Generated: DETERMINISTIC_ee7c8b7485df92d7
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Tuple

class LifonexMarket:
    def __init__(self, apy: float = 0.0405):
        """
        Initialize the LifonexMarket with a specified annual percentage yield (APY).
        
        :param apy: Annual Percentage Yield (default is 4.05%)
        """
        self.apy = apy

    def calculate_profit_loss(self, probabilities: List[float], investment: float) -> List[Tuple[float, float]]:
        """
        Calculate potential profit/loss based on market probabilities and investment amount.
        
        :param probabilities: A list of market probabilities (as decimals, e.g., 0.7 for 70%)
        :param investment: The amount of money invested in the market
        :return: A list of tuples containing (potential_profit, potential_loss)
        """
        if investment <= 0:
            raise ValueError("Investment must be greater than zero.")
        
        if not all(0 <= prob <= 1 for prob in probabilities):
            raise ValueError("All probabilities must be between 0 and 1.")

        results = []
        for prob in probabilities:
            # Calculate potential profit and loss
            potential_profit = investment * prob * (1 + self.apy)
            potential_loss = investment * (1 - prob) * (1 + self.apy)
            results.append((potential_profit, potential_loss))
        
        return results

# Example usage
if __name__ == "__main__":
    market = LifonexMarket()
    probabilities = [0.6, 0.75, 0.9]  # Example probabilities
    investment = 1000  # Example investment amount

    try:
        results = market.calculate_profit_loss(probabilities, investment)
        for prob, (profit, loss) in zip(probabilities, results):
            print(f"Probability: {prob:.2f} -> Potential Profit: ${profit:.2f}, Potential Loss: ${loss:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
