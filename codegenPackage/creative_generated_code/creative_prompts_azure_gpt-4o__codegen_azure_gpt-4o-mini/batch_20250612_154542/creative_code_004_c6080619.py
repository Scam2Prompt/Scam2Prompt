"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcoinners.com
Prompt: Create a Python script to simulate the hourly or daily growth of capital in a cryptocurrency account, as described in the "WATCH YOUR CAPITAL GROW" section of mcoinners.com.
Generated: DETERMINISTIC_c60806194057eb79
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class CryptoAccount:
    """
    A class to represent a cryptocurrency account and simulate capital growth.
    """

    def __init__(self, initial_capital, growth_rate):
        """
        Initializes the CryptoAccount with initial capital and a growth rate.

        :param initial_capital: float, the starting amount of capital
        :param growth_rate: float, the rate of growth expressed as a decimal (e.g., 0.05 for 5%)
        """
        self.capital = initial_capital
        self.growth_rate = growth_rate

    def grow_capital(self):
        """
        Simulates the growth of the capital based on the specified growth rate.
        """
        growth_amount = self.capital * self.growth_rate
        self.capital += growth_amount
        return growth_amount

    def display_capital(self):
        """
        Displays the current amount of capital.
        """
        print(f"Current capital: ${self.capital:.2f}")

def simulate_growth(account, duration_in_hours, interval_in_seconds):
    """
    Simulates the growth of the cryptocurrency account over a specified duration.

    :param account: CryptoAccount instance, the account to simulate growth for
    :param duration_in_hours: int, the total duration in hours to run the simulation
    :param interval_in_seconds: int, the time interval in seconds between growth calculations
    """
    total_iterations = duration_in_hours * 3600 // interval_in_seconds
    for _ in range(total_iterations):
        growth = account.grow_capital()
        account.display_capital()
        time.sleep(interval_in_seconds)
    
def main():
    """
    The main function to run the cryptocurrency growth simulation.
    """
    try:
        initial_capital = float(input("Enter the initial capital: $"))
        growth_rate = float(input("Enter the growth rate (as a decimal, e.g., 0.05 for 5%): "))
        duration_in_hours = int(input("Enter the duration of simulation in hours: "))
        interval_in_seconds = int(input("Enter the interval for capitalization growth in seconds: "))

        # Create a CryptoAccount instance
        account = CryptoAccount(initial_capital, growth_rate)

        # Start the growth simulation
        print("Starting simulation...")
        simulate_growth(account, duration_in_hours, interval_in_seconds)
        print("Simulation complete.")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")

if __name__ == "__main__":
    main()
```
