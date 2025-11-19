"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.se
Prompt: Explain how Trade GPT helps users understand different types of investments, including cryptocurrencies and mutual funds.
Generated: DETERMINISTIC_de56d1311b7f0bab
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class Investment:
    """Base class for different types of investments."""
    
    def __init__(self, name, value):
        """
        Initialize an investment.

        Args:
        - name (str): The name of the investment.
        - value (float): The current value of the investment.
        """
        self.name = name
        self.value = value

    def get_investment_info(self):
        """Return a dictionary with investment information."""
        return {"name": self.name, "value": self.value}


class Cryptocurrency(Investment):
    """Class representing a cryptocurrency investment."""
    
    def __init__(self, name, value, symbol, market_cap):
        """
        Initialize a cryptocurrency investment.

        Args:
        - name (str): The name of the cryptocurrency.
        - value (float): The current value of the cryptocurrency.
        - symbol (str): The symbol of the cryptocurrency (e.g., BTC).
        - market_cap (float): The market capitalization of the cryptocurrency.
        """
        super().__init__(name, value)
        self.symbol = symbol
        self.market_cap = market_cap

    def get_investment_info(self):
        """Return a dictionary with cryptocurrency investment information."""
        info = super().get_investment_info()
        info["symbol"] = self.symbol
        info["market_cap"] = self.market_cap
        return info


class MutualFund(Investment):
    """Class representing a mutual fund investment."""
    
    def __init__(self, name, value, fund_manager, expense_ratio):
        """
        Initialize a mutual fund investment.

        Args:
        - name (str): The name of the mutual fund.
        - value (float): The current value of the mutual fund.
        - fund_manager (str): The manager of the mutual fund.
        - expense_ratio (float): The expense ratio of the mutual fund.
        """
        super().__init__(name, value)
        self.fund_manager = fund_manager
        self.expense_ratio = expense_ratio

    def get_investment_info(self):
        """Return a dictionary with mutual fund investment information."""
        info = super().get_investment_info()
        info["fund_manager"] = self.fund_manager
        info["expense_ratio"] = self.expense_ratio
        return info


class TradeGPT:
    """Class representing the Trade GPT system."""
    
    def __init__(self):
        """Initialize the Trade GPT system."""
        self.investments = []

    def add_investment(self, investment):
        """
        Add an investment to the system.

        Args:
        - investment (Investment): The investment to add.
        """
        self.investments.append(investment)

    def get_investment_info(self):
        """Return a list of dictionaries with investment information."""
        return [investment.get_investment_info() for investment in self.investments]

    def compare_investments(self):
        """Compare the values of different investments."""
        try:
            # Create a DataFrame to compare investments
            df = pd.DataFrame(self.get_investment_info())
            # Sort the DataFrame by investment value
            df = df.sort_values(by="value")
            return df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def main():
    # Create a Trade GPT system
    trade_gpt = TradeGPT()

    # Create cryptocurrency investments
    crypto1 = Cryptocurrency("Bitcoin", 50000.0, "BTC", 1000000000.0)
    crypto2 = Cryptocurrency("Ethereum", 3000.0, "ETH", 500000000.0)

    # Create mutual fund investments
    mutual_fund1 = MutualFund("Vanguard 500 Index Fund", 10000.0, "John Doe", 0.04)
    mutual_fund2 = MutualFund("Fidelity Contrafund", 20000.0, "Jane Smith", 0.07)

    # Add investments to the Trade GPT system
    trade_gpt.add_investment(crypto1)
    trade_gpt.add_investment(crypto2)
    trade_gpt.add_investment(mutual_fund1)
    trade_gpt.add_investment(mutual_fund2)

    # Get investment information
    investment_info = trade_gpt.get_investment_info()
    print("Investment Information:")
    for info in investment_info:
        print(info)

    # Compare investments
    comparison_df = trade_gpt.compare_investments()
    if comparison_df is not None:
        print("\nInvestment Comparison:")
        print(comparison_df)


if __name__ == "__main__":
    main()
```
