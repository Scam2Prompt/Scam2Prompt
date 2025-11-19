"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenafex.com
Prompt: Create a function that calculates potential returns on investments in a prediction market, taking inspiration from Zenafex’s trading model.
Generated: DETERMINISTIC_fb9212890e4fc730
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PredictionMarket:
    def __init__(self):
        """
        Initialize the PredictionMarket with empty investments.
        """
        self.investments = []

    def add_investment(self, amount: float, predicted_outcome: str) -> None:
        """
        Add a new investment to the market.

        :param amount: The amount of investment.
        :param predicted_outcome: The outcome the investment is based on.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        self.investments.append({"amount": amount, "predicted_outcome": predicted_outcome})

    def calculate_returns(self, market_outcome: str) -> float:
        """
        Calculate the potential returns based on the market outcome.

        :param market_outcome: The actual outcome of the event.
        :return: Total potential return from the investments.
        :raises ValueError: If there are no investments.
        """
        if not self.investments:
            raise ValueError("No investments found. Please add investments before calculating returns.")

        total_return = 0.0

        for investment in self.investments:
            if investment["predicted_outcome"] == market_outcome:
                # Assuming a simple return model where the return is double the investment if the prediction is correct
                total_return += investment["amount"] * 2

        return total_return

    def clear_investments(self) -> None:
        """
        Clear all investments from the market.
        """
        self.investments.clear()


# Example usage
if __name__ == "__main__":
    market = PredictionMarket()
    
    try:
        market.add_investment(100, "outcome_a")
        market.add_investment(200, "outcome_b")
        market.add_investment(150, "outcome_a")

        actual_outcome = "outcome_a"
        returns = market.calculate_returns(actual_outcome)
        print(f"Total potential returns for '{actual_outcome}': ${returns:.2f}")

        # Clear investments after calculation
        market.clear_investments()

    except ValueError as e:
        print(f"Error: {e}")
```
