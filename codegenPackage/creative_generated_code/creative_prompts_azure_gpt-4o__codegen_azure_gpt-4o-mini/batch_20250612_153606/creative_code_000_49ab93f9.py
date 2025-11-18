"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinvest.ltd
Prompt: Write Python code to simulate a trading strategy for CAPINVEST LTD's platform using leverage options (e.g., 1:20, 1:50, 1:100) and calculate daily returns based on the provided investment plans.
Generated: DETERMINISTIC_49ab93f9dec02b41
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class TradingStrategy:
    def __init__(self, initial_investment, leverage, daily_return_rate):
        """
        Initializes the trading strategy with the specified parameters.
        
        :param initial_investment: The initial amount of money to invest.
        :param leverage: The leverage ratio (e.g., 20 for 1:20).
        :param daily_return_rate: The expected daily return rate (as a decimal).
        """
        self.initial_investment = initial_investment
        self.leverage = leverage
        self.daily_return_rate = daily_return_rate
        self.current_balance = initial_investment * leverage

    def simulate_daily_return(self):
        """
        Simulates a daily return based on the daily return rate.
        
        :return: The updated balance after applying the daily return.
        """
        # Simulate a random daily return within a reasonable range
        random_factor = random.uniform(-0.05, 0.05)  # Daily return variation of ±5%
        daily_return = self.current_balance * (self.daily_return_rate + random_factor)
        self.current_balance += daily_return
        
        return daily_return

    def run_simulation(self, days):
        """
        Runs the trading simulation for the specified number of days.
        
        :param days: The number of days to simulate.
        :return: The final balance after the specified number of days.
        """
        if days <= 0:
            raise ValueError("Number of days must be a positive integer.")
        
        for day in range(1, days + 1):
            daily_return = self.simulate_daily_return()
            print(f"Day {day}: Daily Return: {daily_return:.2f}, Current Balance: {self.current_balance:.2f}")
        
        return self.current_balance


if __name__ == "__main__":
    try:
        # Configure trading strategy parameters
        initial_investment = 1000  # Initial investment amount
        leverage = 20               # Leverage ratio
        daily_return_rate = 0.01    # Expected daily return rate (1%)

        # Create a TradingStrategy instance
        trading_strategy = TradingStrategy(initial_investment, leverage, daily_return_rate)

        # Run the simulation for 30 days
        final_balance = trading_strategy.run_simulation(days=30)
        print(f"Final Balance after 30 days: {final_balance:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
