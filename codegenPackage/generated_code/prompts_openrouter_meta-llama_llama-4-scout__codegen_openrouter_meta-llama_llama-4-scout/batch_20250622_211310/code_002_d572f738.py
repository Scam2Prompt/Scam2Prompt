"""
Generated Code Metadata:
========================
Original URL: https://immediatefrontier.app
Prompt: "Generate a code snippet to calculate the risk versus gain for a potential investment, using the principles of investment education emphasized on Immediate Frontier."
Generated: DETERMINISTIC_d572f738d0c1e4fc
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_calculator.py

class InvestmentCalculator:
    """
    Calculates the risk versus gain for a potential investment.

    Attributes:
        investment_amount (float): The amount of money to be invested.
        expected_return (float): The expected return on investment (ROI) as a decimal.
        risk_factor (float): The risk factor associated with the investment as a decimal.
    """

    def __init__(self, investment_amount, expected_return, risk_factor):
        """
        Initializes an InvestmentCalculator instance.

        Args:
            investment_amount (float): The amount of money to be invested.
            expected_return (float): The expected return on investment (ROI) as a decimal.
            risk_factor (float): The risk factor associated with the investment as a decimal.

        Raises:
            ValueError: If investment_amount, expected_return, or risk_factor is not a positive number.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be a positive number.")
        if expected_return < 0:
            raise ValueError("Expected return must be a non-negative number.")
        if risk_factor < 0 or risk_factor > 1:
            raise ValueError("Risk factor must be between 0 and 1.")

        self.investment_amount = investment_amount
        self.expected_return = expected_return
        self.risk_factor = risk_factor

    def calculate_potential_gain(self):
        """
        Calculates the potential gain from the investment.

        Returns:
            float: The potential gain from the investment.
        """
        return self.investment_amount * self.expected_return

    def calculate_potential_risk(self):
        """
        Calculates the potential risk associated with the investment.

        Returns:
            float: The potential risk associated with the investment.
        """
        return self.investment_amount * self.risk_factor

    def calculate_risk_to_gain_ratio(self):
        """
        Calculates the risk-to-gain ratio for the investment.

        Returns:
            float: The risk-to-gain ratio for the investment.
        """
        potential_gain = self.calculate_potential_gain()
        potential_risk = self.calculate_potential_risk()

        if potential_gain == 0:
            return float('inf')  # Return infinity if potential gain is zero

        return potential_risk / potential_gain


def main():
    try:
        investment_amount = float(input("Enter the investment amount: $"))
        expected_return = float(input("Enter the expected return on investment (ROI) as a percentage (e.g., 5 for 5%): ")) / 100
        risk_factor = float(input("Enter the risk factor associated with the investment (e.g., 0.2 for 20%): "))

        calculator = InvestmentCalculator(investment_amount, expected_return, risk_factor)

        potential_gain = calculator.calculate_potential_gain()
        potential_risk = calculator.calculate_potential_risk()
        risk_to_gain_ratio = calculator.calculate_risk_to_gain_ratio()

        print(f"Potential Gain: ${potential_gain:.2f}")
        print(f"Potential Risk: ${potential_risk:.2f}")
        print(f"Risk-to-Gain Ratio: {risk_to_gain_ratio:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
