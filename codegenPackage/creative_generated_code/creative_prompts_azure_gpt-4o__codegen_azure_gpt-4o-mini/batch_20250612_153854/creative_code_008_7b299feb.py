"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Write a function to calculate returns on private equity investments, incorporating strategic planning and prudent investment management principles as highlighted by Alghanim Capital.
Generated: DETERMINISTIC_7b299feb2e27fa59
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrivateEquityInvestment:
    """
    A class to represent a private equity investment and calculate its returns.
    """

    def __init__(self, initial_investment, annual_rate_of_return, duration_years):
        """
        Initializes the private equity investment parameters.

        :param initial_investment: The initial amount invested (float).
        :param annual_rate_of_return: The expected annual rate of return in percentage (float).
        :param duration_years: The duration of the investment in years (int).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if annual_rate_of_return < 0:
            raise ValueError("Annual rate of return cannot be negative.")
        if duration_years <= 0:
            raise ValueError("Duration years must be greater than zero.")
        
        self.initial_investment = initial_investment
        self.annual_rate_of_return = annual_rate_of_return / 100  # Convert percentage to decimal
        self.duration_years = duration_years

    def calculate_returns(self):
        """
        Calculates the future value of the investment after the specified duration 
        using the formula for compound interest.

        :return: The future value of the investment (float).
        """
        future_value = self.initial_investment * (1 + self.annual_rate_of_return) ** self.duration_years
        return future_value

    def display_investment_summary(self):
        """
        Displays a summary of the investment details and calculated returns.

        :return: None
        """
        try:
            future_value = self.calculate_returns()
            print(f"Initial Investment: ${self.initial_investment:,.2f}")
            print(f"Annual Rate of Return: {self.annual_rate_of_return * 100:.2f}%")
            print(f"Investment Duration: {self.duration_years} years")
            print(f"Future Value of Investment: ${future_value:,.2f}")
        except Exception as e:
            print(f"Error while calculating returns: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        investment = PrivateEquityInvestment(initial_investment=100000, annual_rate_of_return=8, duration_years=5)
        investment.display_investment_summary()
    except ValueError as ve:
        print(f"Input error: {ve}")
```
