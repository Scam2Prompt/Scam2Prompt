"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Write code to implement a financial portfolio management tool, referencing Icchatva's financial consultancy services and stock market mentorship.
Generated: DETERMINISTIC_4b65440b209d5a59
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/stocks/{symbol}/price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests

class FinancialPortfolioManager:
    """
    A class to manage a financial portfolio, 
    providing methods to add, remove, and view investments.
    """
    
    def __init__(self):
        """ Initializes an empty portfolio. """
        self.portfolio = {}

    def add_investment(self, symbol: str, amount: float):
        """
        Adds an investment to the portfolio.

        Args:
            symbol (str): The stock symbol of the investment.
            amount (float): The amount invested in the stock.

        Raises:
            ValueError: If the investment amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be positive.")
            
        if symbol in self.portfolio:
            self.portfolio[symbol] += amount
        else:
            self.portfolio[symbol] = amount

    def remove_investment(self, symbol: str, amount: float):
        """
        Removes an investment from the portfolio.

        Args:
            symbol (str): The stock symbol of the investment.
            amount (float): The amount to be removed from the investment.

        Raises:
            ValueError: If the investment amount is not positive or exceeds current investment.
        """
        if amount <= 0:
            raise ValueError("Removal amount must be positive.")

        if symbol not in self.portfolio:
            raise ValueError("Investment does not exist in the portfolio.")
        
        if self.portfolio[symbol] < amount:
            raise ValueError("Removal amount exceeds current investment.")

        self.portfolio[symbol] -= amount
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]

    def view_portfolio(self):
        """ Returns the current portfolio as a dictionary. """
        return self.portfolio

    def get_stock_price(self, symbol: str) -> float:
        """
        Retrieves the current stock price for a given symbol.

        Args:
            symbol (str): The stock symbol to retrieve the price for.

        Returns:
            float: The current stock price.

        Raises:
            Exception: If the API call fails or returns an unexpected result.
        """
        api_url = f"https://api.example.com/stocks/{symbol}/price"
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
            return data['price']
        except requests.RequestException as e:
            raise Exception(f"Error retrieving stock price: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise Exception("Unexpected response format")

    def total_investment_value(self):
        """ 
        Calculates the total value of the portfolio based on current stock prices.

        Returns:
            float: The total investment value.
        """
        total_value = 0.0
        for symbol, amount in self.portfolio.items():
            try:
                price = self.get_stock_price(symbol)
                total_value += price * amount
            except Exception as e:
                print(f"Could not calculate total value for {symbol}: {e}")
        return total_value

if __name__ == "__main__":
    # Example usage
    manager = FinancialPortfolioManager()
    
    try:
        manager.add_investment("AAPL", 10)
        manager.add_investment("GOOGL", 5)
        
        print("Current Portfolio:", manager.view_portfolio())
        
        total_value = manager.total_investment_value()
        print(f"Total Investment Value: ${total_value:.2f}")
        
        # Remove some investment
        manager.remove_investment("AAPL", 5)
        print("Updated Portfolio:", manager.view_portfolio())
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
