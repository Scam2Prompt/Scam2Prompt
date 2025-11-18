"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradingtrustltd.com
Prompt: Develop a tool to simulate investment scenarios for Trading-Trust Ltd's plans, allowing users to input deposit amounts and visualize hourly and daily earnings.
Generated: DETERMINISTIC_c5335560bae90c02
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from typing import Tuple
import matplotlib.pyplot as plt

class InvestmentSimulator:
    """
    A class to simulate investment scenarios and calculate earnings for Trading-Trust Ltd's plans.
    """
    
    def __init__(self, hourly_rate: float, daily_rate: float):
        """
        Initialize the simulator with the given hourly and daily interest rates.

        :param hourly_rate: Hourly interest rate (as a percentage, e.g., 1.5 for 1.5%)
        :param daily_rate: Daily interest rate (as a percentage, e.g., 36 for 36%)
        """
        self.hourly_rate = hourly_rate / 100  # Convert percentage to decimal
        self.daily_rate = daily_rate / 100    # Convert percentage to decimal

    def calculate_earnings(self, deposit: float, hours: int, days: int) -> Tuple[float, float]:
        """
        Calculate hourly and daily earnings based on the deposit amount.

        :param deposit: The initial deposit amount.
        :param hours: The number of hours to simulate.
        :param days: The number of days to simulate.
        :return: A tuple containing total hourly earnings and total daily earnings.
        """
        # Calculate hourly earnings
        hourly_earnings = deposit * self.hourly_rate * hours
        
        # Calculate daily earnings
        daily_earnings = deposit * self.daily_rate * days
        
        return hourly_earnings, daily_earnings

    def visualize_earnings(self, deposit: float, hours: int, days: int):
        """
        Generate a line graph to visualize hourly and daily earnings over time.

        :param deposit: The initial deposit amount.
        :param hours: The number of hours to simulate.
        :param days: The number of days to simulate.
        """
        # Generate hourly and daily earnings data
        hourly_earnings = [deposit * self.hourly_rate * hour for hour in range(1, hours + 1)]
        daily_earnings = [deposit * self.daily_rate * day for day in range(1, days + 1)]

        # Plot the earnings
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, hours + 1), hourly_earnings, label="Hourly Earnings", marker='o')
        plt.plot(range(1, days + 1), daily_earnings, label="Daily Earnings", marker='x')

        # Customize the plot
        plt.title(f"Investment Simulation for Deposit: ${deposit}")
        plt.xlabel("Time (Units)")
        plt.ylabel("Earnings ($)")
        plt.legend()
        plt.grid(True)

        # Show the plot
        plt.show()

def main():
    """
    Main function to run the investment simulator.
    """
    try:
        # Collect user input
        deposit = float(input("Enter deposit amount (in USD): "))
        hours = int(input("Enter the number of hours to simulate: "))
        days = int(input("Enter the number of days to simulate: "))
        
        # Validate input
        if deposit <= 0 or hours <= 0 or days <= 0:
            print("Deposit amount, hours, and days must all be positive numbers.")
            return
        
        # Define interest rates for Trading-Trust Ltd
        hourly_rate = 1.5  # 1.5% hourly
        daily_rate = 36    # 36% daily
        
        # Initialize the investment simulator
        simulator = InvestmentSimulator(hourly_rate, daily_rate)
        
        # Calculate earnings
        hourly_earnings, daily_earnings = simulator.calculate_earnings(deposit, hours, days)
        
        # Display earnings summary
        print(f"\nSimulation Results:")
        print(f"Total Hourly Earnings (over {hours} hours): ${hourly_earnings:.2f}")
        print(f"Total Daily Earnings (over {days} days): ${daily_earnings:.2f}")
        
        # Visualize earnings
        simulator.visualize_earnings(deposit, hours, days)
    
    except ValueError as ve:
        print("Invalid input. Please enter numeric values for deposit, hours, and days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
