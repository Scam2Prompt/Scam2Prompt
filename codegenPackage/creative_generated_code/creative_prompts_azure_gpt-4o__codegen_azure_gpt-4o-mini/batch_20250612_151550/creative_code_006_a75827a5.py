"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premiertradeoptions.com
Prompt: Develop a function to automate the calculation and application of Copy Stop Loss (CSL) ratios between 5% and 95%, as explained on Premier Trade Options.
Generated: DETERMINISTIC_a75827a575c5f0ab
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPortfolio:
    """
    A class to represent an investment portfolio and calculate Copy Stop Loss (CSL) ratios.
    """

    def __init__(self, initial_investment):
        """
        Initialize the portfolio with an initial investment amount.
        
        :param initial_investment: The initial amount invested.
        :raises ValueError: If the initial investment is not a positive number.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be a positive number.")
        self.initial_investment = initial_investment

    def calculate_csl(self, target_value, csl_percentage):
        """
        Calculate the Copy Stop Loss (CSL) value based on the target value and CSL percentage.

        :param target_value: The current value of the investment.
        :param csl_percentage: The percentage for the Copy Stop Loss (must be between 5 and 95).
        :return: The CSL value.
        :raises ValueError: If the CSL percentage is not in the range of 5 to 95.
        """
        if not (5 <= csl_percentage <= 95):
            raise ValueError("CSL percentage must be between 5 and 95.")

        # Calculate the CSL value
        csl_value = target_value * (1 - csl_percentage / 100)
        return csl_value

    def apply_csl(self, current_value, csl_percentage):
        """
        Apply the calculated Copy Stop Loss to determine if an action needs to be taken.

        :param current_value: The current market value of the investment.
        :param csl_percentage: The percentage for the Copy Stop Loss.
        :return: A message indicating whether to sell or hold the investment.
        """
        try:
            # Calculate the Copy Stop Loss value
            csl_value = self.calculate_csl(current_value, csl_percentage)

            # Determine action based on current value and CSL value
            if current_value < csl_value:
                return "Sell the investment to limit losses."
            else:
                return "Hold the investment."

        except ValueError as e:
            return str(e)

# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of InvestmentPortfolio with an initial investment
        portfolio = InvestmentPortfolio(initial_investment=10000)

        # Determine current value and CSL percentage
        current_value = 9200
        csl_percentage = 10

        # Apply Copy Stop Loss and print action
        action = portfolio.apply_csl(current_value, csl_percentage)
        print(action)

    except Exception as e:
        print(f"An error occurred: {e}")
```
