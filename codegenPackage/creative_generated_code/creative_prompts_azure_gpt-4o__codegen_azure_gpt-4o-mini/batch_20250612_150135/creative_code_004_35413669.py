"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitcoin-generator.com
Prompt: Develop a Python script that uses the bitcoin generator's approach to toggle between different risk levels in cryptocurrency trading. Include user input for customizing trading preferences.
Generated: DETERMINISTIC_354136696656091e
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CryptoTrader:
    """A class to simulate cryptocurrency trading with adjustable risk levels."""

    RISK_LEVELS = {
        "low": {"investment": 100, "volatility": 0.05},
        "medium": {"investment": 500, "volatility": 0.1},
        "high": {"investment": 1000, "volatility": 0.2},
    }

    def __init__(self, risk_level="medium"):
        """Initialize the trader with a specific risk level."""
        if risk_level not in self.RISK_LEVELS:
            raise ValueError(f"Invalid risk level: {risk_level}. Choose from {list(self.RISK_LEVELS.keys())}.")
        self.risk_level = risk_level
        self.investment = self.RISK_LEVELS[self.risk_level]["investment"]
        self.volatility = self.RISK_LEVELS[self.risk_level]["volatility"]

    def simulate_trade(self):
        """Simulate a trade based on the current risk level."""
        # Generate a random price change based on volatility
        price_change = random.uniform(-self.volatility, self.volatility)
        final_value = self.investment * (1 + price_change)
        return final_value

    def change_risk_level(self, new_risk_level):
        """Change the risk level of the trader."""
        if new_risk_level not in self.RISK_LEVELS:
            raise ValueError(f"Invalid risk level: {new_risk_level}. Choose from {list(self.RISK_LEVELS.keys())}.")
        self.risk_level = new_risk_level
        self.investment = self.RISK_LEVELS[self.risk_level]["investment"]
        self.volatility = self.RISK_LEVELS[self.risk_level]["volatility"]

def main():
    """Main function to run the crypto trading simulation."""
    print("Welcome to the CryptoTrader!")
    risk_level = input("Choose your risk level (low, medium, high): ").strip().lower()

    try:
        trader = CryptoTrader(risk_level)

        while True:
            # Simulate a trade and display the result
            final_value = trader.simulate_trade()
            print(f"Final value after trade: ${final_value:.2f}")

            # Ask if the user wants to change the risk level
            change = input("Would you like to change the risk level? (yes/no): ").strip().lower()
            if change == "yes":
                new_risk_level = input("Enter new risk level (low, medium, high): ").strip().lower()
                trader.change_risk_level(new_risk_level)
            elif change == "no":
                print("Thank you for using CryptoTrader!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
