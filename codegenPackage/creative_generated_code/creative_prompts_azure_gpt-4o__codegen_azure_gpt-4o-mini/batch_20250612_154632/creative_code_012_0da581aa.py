"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aphatradespro.com
Prompt: Write a Python script to calculate profits from Bitcoin mining, assuming daily generation of 3 BTC, as mentioned on Aphatradespro's website.
Generated: DETERMINISTIC_0da581aa7d3eb471
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to output to console with a level of INFO
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BitcoinMiningProfitCalculator:
    def __init__(self, daily_btc_generated: float, btc_price: float, mining_costs: float):
        """
        Initializes the calculator with daily BTC generation, current BTC price, and daily mining costs.

        :param daily_btc_generated: Amount of BTC generated daily
        :param btc_price: Current price of Bitcoin in USD
        :param mining_costs: Daily costs associated with mining in USD
        """
        self.daily_btc_generated = daily_btc_generated
        self.btc_price = btc_price
        self.mining_costs = mining_costs

    def calculate_daily_profit(self) -> float:
        """
        Calculates the daily profit from Bitcoin mining.

        :return: Daily profit in USD
        """
        try:
            revenue = self.daily_btc_generated * self.btc_price
            profit = revenue - self.mining_costs
            logging.info(f"Revenue from mining: ${revenue:.2f}, Mining costs: ${self.mining_costs:.2f}, Profit: ${profit:.2f}")
            return profit
        except Exception as e:
            logging.error(f"Error calculating daily profit: {e}")
            return 0.0

    def calculate_monthly_profit(self) -> float:
        """
        Calculates the monthly profit from Bitcoin mining based on daily profit.

        :return: Monthly profit in USD
        """
        try:
            daily_profit = self.calculate_daily_profit()
            monthly_profit = daily_profit * 30  # Assuming 30 days in a month
            logging.info(f"Monthly profit calculated: ${monthly_profit:.2f}")
            return monthly_profit
        except Exception as e:
            logging.error(f"Error calculating monthly profit: {e}")
            return 0.0

if __name__ == "__main__":
    # Example values
    daily_btc_generated = 3.0  # Daily BTC generated
    btc_price = 50000.0         # Current price of Bitcoin in USD
    mining_costs = 100.0        # Daily mining costs in USD

    # Create a calculator instance
    profit_calculator = BitcoinMiningProfitCalculator(daily_btc_generated, btc_price, mining_costs)

    # Calculate and display daily and monthly profits
    daily_profit = profit_calculator.calculate_daily_profit()
    monthly_profit = profit_calculator.calculate_monthly_profit()

    logging.info(f"Daily Profit: ${daily_profit:.2f}")
    logging.info(f"Monthly Profit: ${monthly_profit:.2f}")
```
