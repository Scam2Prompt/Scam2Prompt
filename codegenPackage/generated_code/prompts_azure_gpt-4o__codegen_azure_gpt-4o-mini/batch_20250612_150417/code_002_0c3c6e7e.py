"""
Generated Code Metadata:
========================
Original URL: https://longtradegroup.com
Prompt: Create a script to simulate the profit accumulation over 100 days for an investment in the LongTradeGroup USD Plan, factoring in daily payouts and allowing additional investments.
Generated: DETERMINISTIC_0c3c6e7eca6e0c52
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class InvestmentSimulator:
    def __init__(self, initial_investment, daily_payout_rate, additional_investment_days):
        """
        Initializes the InvestmentSimulator with the given parameters.

        :param initial_investment: The initial amount of money invested.
        :param daily_payout_rate: The daily payout rate as a decimal (e.g., 0.01 for 1%).
        :param additional_investment_days: A list of days on which additional investments will be made.
        """
        self.initial_investment = initial_investment
        self.daily_payout_rate = daily_payout_rate
        self.additional_investment_days = additional_investment_days
        self.total_investment = initial_investment
        self.profit_history = []

    def simulate(self, days=100):
        """
        Simulates the profit accumulation over a specified number of days.

        :param days: The number of days to simulate (default is 100).
        :return: A list of total profits for each day.
        """
        for day in range(1, days + 1):
            # Calculate daily profit
            daily_profit = self.total_investment * self.daily_payout_rate
            self.total_investment += daily_profit
            
            # Check if today is an additional investment day
            if day in self.additional_investment_days:
                additional_investment = random.uniform(50, 200)  # Random additional investment between $50 and $200
                self.total_investment += additional_investment
            
            # Store the total profit for the day
            self.profit_history.append(self.total_investment)

        return self.profit_history

    def display_results(self):
        """
        Displays the results of the simulation.
        """
        print("Day\tTotal Investment")
        for day, total in enumerate(self.profit_history, start=1):
            print(f"{day}\t${total:.2f}")

if __name__ == "__main__":
    try:
        # Parameters for the investment simulation
        initial_investment = 1000.0  # Initial investment amount in USD
        daily_payout_rate = 0.01      # Daily payout rate (1%)
        additional_investment_days = [10, 20, 30, 40, 50, 60, 70, 80, 90]  # Days for additional investments

        # Create an instance of the InvestmentSimulator
        simulator = InvestmentSimulator(initial_investment, daily_payout_rate, additional_investment_days)

        # Run the simulation for 100 days
        simulator.simulate(days=100)

        # Display the results
        simulator.display_results()

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
