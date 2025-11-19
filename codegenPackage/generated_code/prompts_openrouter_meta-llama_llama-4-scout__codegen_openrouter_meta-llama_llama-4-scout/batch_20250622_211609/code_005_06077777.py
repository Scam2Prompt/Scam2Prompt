"""
Generated Code Metadata:
========================
Original URL: https://exytrade.com
Prompt: "Develop a simple portfolio management tool for tracking investments in stock market and equity trading, similar to Exytrade's services."
Generated: DETERMINISTIC_06077777cd69a21a
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_management_tool.py

import datetime
import json

class Investment:
    """Represents an investment in the stock market."""

    def __init__(self, symbol, name, purchase_price, quantity):
        """
        Initializes an Investment object.

        Args:
            symbol (str): Stock symbol (e.g., AAPL).
            name (str): Stock name (e.g., Apple Inc.).
            purchase_price (float): Purchase price per share.
            quantity (int): Number of shares purchased.
        """
        self.symbol = symbol
        self.name = name
        self.purchase_price = purchase_price
        self.quantity = quantity

    def calculate_value(self, current_price):
        """
        Calculates the current value of the investment.

        Args:
            current_price (float): Current market price per share.

        Returns:
            float: Current value of the investment.
        """
        return current_price * self.quantity

    def calculate_gain_loss(self, current_price):
        """
        Calculates the gain or loss of the investment.

        Args:
            current_price (float): Current market price per share.

        Returns:
            float: Gain or loss of the investment.
        """
        current_value = self.calculate_value(current_price)
        purchase_value = self.purchase_price * self.quantity
        return current_value - purchase_value


class Portfolio:
    """Represents a portfolio of investments."""

    def __init__(self):
        """Initializes an empty portfolio."""
        self.investments = {}

    def add_investment(self, investment):
        """
        Adds an investment to the portfolio.

        Args:
            investment (Investment): Investment to add.
        """
        self.investments[investment.symbol] = investment

    def remove_investment(self, symbol):
        """
        Removes an investment from the portfolio.

        Args:
            symbol (str): Symbol of the investment to remove.

        Raises:
            KeyError: If the investment is not in the portfolio.
        """
        if symbol not in self.investments:
            raise KeyError(f"Investment '{symbol}' not found in portfolio.")
        del self.investments[symbol]

    def get_investment(self, symbol):
        """
        Gets an investment from the portfolio.

        Args:
            symbol (str): Symbol of the investment to get.

        Returns:
            Investment: Investment with the given symbol.

        Raises:
            KeyError: If the investment is not in the portfolio.
        """
        if symbol not in self.investments:
            raise KeyError(f"Investment '{symbol}' not found in portfolio.")
        return self.investments[symbol]

    def calculate_total_value(self, current_prices):
        """
        Calculates the total value of the portfolio.

        Args:
            current_prices (dict): Current market prices per share.

        Returns:
            float: Total value of the portfolio.
        """
        total_value = 0
        for investment in self.investments.values():
            total_value += investment.calculate_value(current_prices[investment.symbol])
        return total_value

    def calculate_total_gain_loss(self, current_prices):
        """
        Calculates the total gain or loss of the portfolio.

        Args:
            current_prices (dict): Current market prices per share.

        Returns:
            float: Total gain or loss of the portfolio.
        """
        total_gain_loss = 0
        for investment in self.investments.values():
            total_gain_loss += investment.calculate_gain_loss(current_prices[investment.symbol])
        return total_gain_loss


def load_portfolio(filename):
    """
    Loads a portfolio from a JSON file.

    Args:
        filename (str): Name of the file to load.

    Returns:
        Portfolio: Loaded portfolio.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            portfolio = Portfolio()
            for investment_data in data['investments']:
                investment = Investment(
                    investment_data['symbol'],
                    investment_data['name'],
                    investment_data['purchase_price'],
                    investment_data['quantity']
                )
                portfolio.add_investment(investment)
            return portfolio
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file '{filename}': {e}")


def save_portfolio(portfolio, filename):
    """
    Saves a portfolio to a JSON file.

    Args:
        portfolio (Portfolio): Portfolio to save.
        filename (str): Name of the file to save.

    Raises:
        Exception: If an error occurs while saving the file.
    """
    try:
        data = {
            'investments': [
                {
                    'symbol': investment.symbol,
                    'name': investment.name,
                    'purchase_price': investment.purchase_price,
                    'quantity': investment.quantity
                }
                for investment in portfolio.investments.values()
            ]
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise Exception(f"Error saving file '{filename}': {e}")


def main():
    # Create a portfolio
    portfolio = Portfolio()

    # Add investments
    investment1 = Investment('AAPL', 'Apple Inc.', 100.0, 10)
    investment2 = Investment('GOOGL', 'Alphabet Inc.', 500.0, 5)
    portfolio.add_investment(investment1)
    portfolio.add_investment(investment2)

    # Save portfolio to file
    save_portfolio(portfolio, 'portfolio.json')

    # Load portfolio from file
    loaded_portfolio = load_portfolio('portfolio.json')

    # Calculate total value and gain/loss
    current_prices = {'AAPL': 120.0, 'GOOGL': 600.0}
    total_value = loaded_portfolio.calculate_total_value(current_prices)
    total_gain_loss = loaded_portfolio.calculate_total_gain_loss(current_prices)

    # Print results
    print(f"Total Value: ${total_value:.2f}")
    print(f"Total Gain/Loss: ${total_gain_loss:.2f}")


if __name__ == '__main__':
    main()
```
