"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globaltradexplus.com
Prompt: Create a sample investment plan using the Globaltradexplus structure, detailing how to allocate funds across forex, stocks, and cryptocurrencies.
Generated: DETERMINISTIC_65652a1a89b5ec92
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan using a structured allocation across
    forex, stocks, and cryptocurrencies.

    Attributes
    ----------
    forex_allocation : float
        Percentage of total investment allocated to forex.
    stocks_allocation : float
        Percentage of total investment allocated to stocks.
    crypto_allocation : float
        Percentage of total investment allocated to cryptocurrencies.
    total_investment : float
        Total amount of money to be invested.

    Methods
    -------
    calculate_allocations():
        Calculates the allocated amounts for each investment type.
    display_allocations():
        Displays the allocated amounts in a readable format.
    """

    def __init__(self, total_investment, forex_percentage, stocks_percentage, crypto_percentage):
        """
        Constructs all the necessary attributes for the InvestmentPlan object.

        Parameters
        ----------
        total_investment : float
            Total amount of money to be invested.
        forex_percentage : float
            Allocation percentage for forex.
        stocks_percentage : float
            Allocation percentage for stocks.
        crypto_percentage : float
            Allocation percentage for cryptocurrencies.
        """
        if not (0 <= forex_percentage <= 100) or not (0 <= stocks_percentage <= 100) or not (0 <= crypto_percentage <= 100):
            raise ValueError("Allocation percentages must be between 0 and 100.")

        if forex_percentage + stocks_percentage + crypto_percentage != 100:
            raise ValueError("Allocation percentages must sum up to 100.")

        self.total_investment = total_investment
        self.forex_allocation = forex_percentage
        self.stocks_allocation = stocks_percentage
        self.crypto_allocation = crypto_percentage

    def calculate_allocations(self):
        """
        Calculates the allocated amounts for forex, stocks, and cryptocurrencies.

        Returns
        -------
        dict
            A dictionary with the allocated amounts for each investment type.
        """
        allocations = {
            "Forex": (self.forex_allocation / 100) * self.total_investment,
            "Stocks": (self.stocks_allocation / 100) * self.total_investment,
            "Cryptocurrencies": (self.crypto_allocation / 100) * self.total_investment,
        }
        return allocations

    def display_allocations(self):
        """
        Displays the allocated amounts in a readable format.
        """
        allocations = self.calculate_allocations()
        print("Investment Allocations:")
        for investment_type, amount in allocations.items():
            print(f"{investment_type}: ${amount:,.2f}")


if __name__ == "__main__":
    try:
        # Create an instance of InvestmentPlan with a total investment of $10,000
        investment_plan = InvestmentPlan(total_investment=10000, forex_percentage=40, stocks_percentage=40, crypto_percentage=20)
        
        # Display the investment allocations
        investment_plan.display_allocations()
    except ValueError as e:
        print(f"Error: {e}")
```
