"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Create a script to simulate the profit accumulation over 100 days for an investment in the LongTradeGroup USD Plan, factoring in daily payouts and allowing additional investments.
Generated: DETERMINISTIC_0c3c6e7eca6e0c52
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class InvestmentSimulator:
    def __init__(self, initial_investment, daily_payout_rate, investment_days):
        """
        Initializes the investment simulator with given parameters.
        
        :param initial_investment: The initial amount invested in the LongTradeGroup USD Plan.
        :param daily_payout_rate: The daily profit rate (as a decimal).
        :param investment_days: The number of days to simulate.
        """
        self.initial_investment = initial_investment
        self.daily_payout_rate = daily_payout_rate
        self.investment_days = investment_days
        self.total_investment = initial_investment
        self.daily_profits = []
        
    def simulate_day(self):
        """
        Simulates the profit accumulation for a single day.
        
        :return: The profit for the day.
        """
        daily_profit = self.total_investment * self.daily_payout_rate
        self.daily_profits.append(daily_profit)
        return daily_profit

    def add_investment(self, additional_investment):
        """
        Allows additional investment to be added to the total investment.
        
        :param additional_investment: The amount to add to the investment.
        """
        if additional_investment <= 0:
            raise ValueError("Additional investment must be greater than zero.")
        self.total_investment += additional_investment

    def simulate_investment(self):
        """
        Simulates the investment over the defined number of days.
        
        :return: A list of daily profits accumulated over the investment duration.
        """
        for day in range(1, self.investment_days + 1):
            daily_profit = self.simulate_day()
            print(f"Day {day}: Profit = ${daily_profit:.2f}, Total Investment = ${self.total_investment:.2f}")

            # Randomly decide to add additional investment (for simulation)
            if random.choice([True, False]):  # 50% chance to add investment
                additional_investment = random.uniform(5, 50)  # Random investment between $5 and $50
                self.add_investment(additional_investment)
                print(f"  Added additional investment: ${additional_investment:.2f}")

        return self.daily_profits

if __name__ == "__main__":
    # Parameters for the simulation
    INITIAL_INVESTMENT = 1000.0  # Starting investment amount
    DAILY_PAYOUT_RATE = 0.01      # Daily profit rate of 1%
    INVESTMENT_DAYS = 100          # Number of days to simulate

    # Create an instance of the simulator
    simulator = InvestmentSimulator(INITIAL_INVESTMENT, DAILY_PAYOUT_RATE, INVESTMENT_DAYS)

    # Start the simulation
    try:
        profits = simulator.simulate_investment()
        total_profit = sum(profits)
        print(f"Total profit over {INVESTMENT_DAYS} days: ${total_profit:.2f}")
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
