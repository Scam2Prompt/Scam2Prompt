"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.se
Prompt: Explain how Trade GPT helps users understand different types of investments, including cryptocurrencies and mutual funds.
Generated: DETERMINISTIC_de56d1311b7f0bab
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investment:
    """A base class for various types of investments."""
    
    def __init__(self, name, investment_type):
        """
        Initializes the Investment class.

        Parameters:
        name (str): The name of the investment.
        investment_type (str): The type of investment (e.g., cryptocurrency, mutual fund).
        """
        self.name = name
        self.investment_type = investment_type

    def get_investment_info(self):
        """Returns basic information about the investment."""
        return f"{self.name} is a type of {self.investment_type}."


class Cryptocurrency(Investment):
    """A class to represent a cryptocurrency investment."""
    
    def __init__(self, name, market_cap):
        """
        Initializes the Cryptocurrency class.

        Parameters:
        name (str): The name of the cryptocurrency.
        market_cap (float): The market capitalization of the cryptocurrency.
        """
        super().__init__(name, "Cryptocurrency")
        self.market_cap = market_cap

    def get_investment_info(self):
        """Returns detailed information about the cryptocurrency investment."""
        return f"{self.name} is a cryptocurrency with a market cap of ${self.market_cap:,.2f}."


class MutualFund(Investment):
    """A class to represent a mutual fund investment."""
    
    def __init__(self, name, expense_ratio):
        """
        Initializes the MutualFund class.

        Parameters:
        name (str): The name of the mutual fund.
        expense_ratio (float): The expense ratio of the mutual fund.
        """
        super().__init__(name, "Mutual Fund")
        self.expense_ratio = expense_ratio

    def get_investment_info(self):
        """Returns detailed information about the mutual fund investment."""
        return f"{self.name} is a mutual fund with an expense ratio of {self.expense_ratio:.2%}."


def main():
    """Main function to demonstrate the Investment classes."""
    try:
        # Create instances of investments
        bitcoin = Cryptocurrency("Bitcoin", 780000000000)  # Market cap in dollars
        vanguard_500 = MutualFund("Vanguard 500 Index Fund", 0.03)  # Expense ratio in decimal

        # Get investment information
        print(bitcoin.get_investment_info())
        print(vanguard_500.get_investment_info())
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
