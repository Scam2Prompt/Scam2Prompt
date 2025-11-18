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
from typing import List, Dict
from datetime import datetime

class TradingStrategySimulator:
    """
    A class to simulate a trading strategy for CAPINVEST LTD platform 
    using leverage options and calculate daily returns.
    """
    
    def __init__(self, initial_investment: float, leverage_option: int):
        """
        Constructor to initialize the simulator with investment amount and leverage.
        
        Args:
            initial_investment (float): The initial investment amount in dollars.
            leverage_option (int): The leverage multiplier (e.g., 20, 50, 100).
        """
        if leverage_option not in [20, 50, 100]:
            raise ValueError("Invalid leverage option. Must be one of: 20, 50, 100.")
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        
        self.initial_investment = initial_investment
        self.leverage_option = leverage_option
        self.trading_balance = initial_investment * leverage_option

    @staticmethod
    def simulate_daily_return() -> float:
        """
        Simulates the daily return percentage using random fluctuations.
        Returns:
            float: Random daily return percentage (e.g., -5% to +5%).
        """
        return random.uniform(-0.05, 0.05)  # Random daily return between -5% and +5%

    def calculate_daily_returns(self, days: int) -> List[Dict[str, float]]:
        """
        Calculate the daily returns over a specified number of days.
        
        Args:
            days (int): Number of days to simulate returns.
        
        Returns:
            List[Dict[str, float]]: List of dictionaries containing day, daily percentage, 
                                    and total balance.
        """
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")
        
        returns = []
        current_balance = self.trading_balance
        
        for day in range(1, days + 1):
            daily_percentage = self.simulate_daily_return()
            daily_return = current_balance * daily_percentage
            current_balance += daily_return
            
            returns.append({
                "day": day,
                "daily_percentage": daily_percentage * 100,  # Convert to percentage
                "total_balance": current_balance
            })
        
        return returns
    
    def summary(self, days: int):
        """
        Print a summary of the trading simulation.
        
        Args:
            days (int): Number of days to simulate returns.
        """
        results = self.calculate_daily_returns(days)
        print(f"Simulation Results for {days} Days (Leverage: 1:{self.leverage_option}):")
        print(f"Initial Investment: ${self.initial_investment:.2f}")
        print(f"Trading Balance (Leverage): ${self.trading_balance:.2f}")
        print("-" * 50)
        
        for result in results:
            print(f"Day {result['day']}: Daily Change = {result['daily_percentage']:.2f}%, "
                  f"Total Balance = ${result['total_balance']:.2f}")
        
        final_balance = results[-1]["total_balance"]
        print("-" * 50)
        print(f"Final Balance after {days} Days: ${final_balance:.2f}")
        print(f"Net Profit: ${final_balance - self.trading_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    try:
        # User-defined parameters
        initial_investment = 1000.0  # Initial investment in dollars
        leverage_option = 50        # Leverage multiplier (e.g., 1:50)
        simulation_days = 30        # Number of days to simulate
        
        # Create simulator object
        simulator = TradingStrategySimulator(initial_investment, leverage_option)
        
        # Run the simulation and display results
        simulator.summary(simulation_days)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
