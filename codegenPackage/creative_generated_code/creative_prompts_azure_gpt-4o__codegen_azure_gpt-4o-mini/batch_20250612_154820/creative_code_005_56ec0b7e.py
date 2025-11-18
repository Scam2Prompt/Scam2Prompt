"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bit200.site
Prompt: Develop a script to calculate and display betting profit times for cryptocurrency trading, referencing the features mentioned on the ALADIN TRADER website.
Generated: DETERMINISTIC_56ec0b7eff7f6c34
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoBettingProfitCalculator:
    def __init__(self, initial_investment, buy_price, sell_price, quantity):
        """
        Initializes the profit calculator with initial investment, buy price, sell price, and quantity.

        :param initial_investment: The amount of money initially invested in cryptocurrency.
        :param buy_price: The price at which the cryptocurrency was purchased.
        :param sell_price: The price at which the cryptocurrency is sold.
        :param quantity: The number of cryptocurrency units bought.
        """
        self.initial_investment = initial_investment
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity

    def calculate_profit(self):
        """
        Calculates the profit from the cryptocurrency trading.

        :return: The profit amount.
        :raises ValueError: If buy_price or sell_price is zero or negative.
        """
        if self.buy_price <= 0 or self.sell_price <= 0:
            logging.error("Buy price and sell price must be greater than zero.")
            raise ValueError("Buy price and sell price must be greater than zero.")

        # Calculate total cost and potential revenue
        total_cost = self.buy_price * self.quantity
        potential_revenue = self.sell_price * self.quantity

        # Calculate profit
        profit = potential_revenue - total_cost

        # Log the calculated values for debugging
        logging.info(f"Total Cost: {total_cost}, Potential Revenue: {potential_revenue}, Profit: {profit}")

        return profit

    def calculate_profit_percentage(self):
        """
        Calculates the profit percentage based on the initial investment.

        :return: Profit percentage.
        :raises ValueError: If initial investment is zero or negative.
        """
        if self.initial_investment <= 0:
            logging.error("Initial investment must be greater than zero.")
            raise ValueError("Initial investment must be greater than zero.")

        # Calculate profit
        profit = self.calculate_profit()

        # Calculate profit percentage
        profit_percentage = (profit / self.initial_investment) * 100

        logging.info(f"Profit Percentage: {profit_percentage}%")
        return profit_percentage

def main():
    # Example usage of the CryptoBettingProfitCalculator
    try:
        # User-defined values for the calculator
        initial_investment = 1000.0  # Initial investment in USD
        buy_price = 50.0              # Buy price per unit of cryptocurrency
        sell_price = 75.0             # Sell price per unit of cryptocurrency
        quantity = 10                  # Quantity of cryptocurrency bought

        # Create a profit calculator instance
        calculator = CryptoBettingProfitCalculator(initial_investment, buy_price, sell_price, quantity)

        # Calculate and display profit and profit percentage
        profit = calculator.calculate_profit()
        profit_percentage = calculator.calculate_profit_percentage()

        print(f"Calculated Profit: ${profit:.2f}")
        print(f"Profit Percentage: {profit_percentage:.2f}%")

    except ValueError as e:
        # Handle any value errors that arise from invalid inputs
        logging.error(f"ValueError: {e}")
    except Exception as e:
        # Handle any unforeseen exceptions
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
