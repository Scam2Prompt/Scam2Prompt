"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com
Prompt: Generate a Python script that simulates daily profit calculations for an investment of R1,000.00 ZAR at Zadepositslot.
Generated: DETERMINISTIC_66d6b88807de0cec
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from datetime import datetime, timedelta

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentSimulator:
    def __init__(self, initial_investment, daily_return_range, simulation_days):
        """
        Initialize the investment simulator.

        :param initial_investment: Initial amount invested (in ZAR)
        :param daily_return_range: Tuple containing the minimum and maximum profit percentage for the day
        :param simulation_days: Number of days to simulate
        """
        self.initial_investment = initial_investment
        self.daily_return_range = daily_return_range
        self.simulation_days = simulation_days
        self.daily_profits = []

    def calculate_daily_profit(self):
        """
        Calculate the daily profit based on a random percentage within the defined range.
        
        :return: Daily profit amount (in ZAR)
        """
        min_return, max_return = self.daily_return_range
        daily_return_percentage = random.uniform(min_return, max_return)
        daily_profit = self.initial_investment * (daily_return_percentage / 100)
        return daily_profit

    def simulate(self):
        """
        Simulate the investment over the defined number of days.
        """
        logging.info("Starting investment simulation...")
        total_profit = 0
        for day in range(1, self.simulation_days + 1):
            daily_profit = self.calculate_daily_profit()
            total_profit += daily_profit
            self.daily_profits.append(daily_profit)
            logging.info(f"Day {day}: Daily Profit = R{daily_profit:.2f}")

        logging.info(f"Total profit over {self.simulation_days} days: R{total_profit:.2f}")
        self.initial_investment += total_profit
        logging.info(f"Total investment value after {self.simulation_days} days: R{self.initial_investment:.2f}")

if __name__ == "__main__":
    try:
        initial_investment = 1000.00  # Initial investment in ZAR
        daily_return_range = (1, 5)    # Daily return between 1% and 5%
        simulation_days = 30            # Simulate for 30 days

        # Create an instance of InvestmentSimulator
        simulator = InvestmentSimulator(initial_investment, daily_return_range, simulation_days)

        # Run the simulation
        simulator.simulate()
        
    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")
```
