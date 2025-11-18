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
import random
import time
from datetime import datetime, timedelta


class CryptoCapitalGrowthSimulator:
    """
    A class to simulate the hourly or daily growth of capital in a cryptocurrency account.
    """

    def __init__(self, initial_capital, growth_rate_range, frequency="hourly"):
        """
        Initialize the simulator.

        Args:
            initial_capital (float): The starting capital.
            growth_rate_range (tuple): The minimum and maximum growth rates as percentages (e.g., (0.1, 0.5)).
            frequency (str): The frequency of growth. Can be "hourly" or "daily".
        """
        self.current_capital = initial_capital
        self.growth_rate_range = growth_rate_range
        self.frequency = frequency
        self.last_updated = datetime.now()

    def simulate_growth(self):
        """
        Simulate the growth of capital based on the frequency.
        """
        # Calculate the time elapsed since the last update
        now = datetime.now()
        time_elapsed = now - self.last_updated

        # Determine the growth interval based on frequency
        if self.frequency == "hourly":
            interval = timedelta(hours=1)
        elif self.frequency == "daily":
            interval = timedelta(days=1)
        else:
            raise ValueError("Frequency must be either 'hourly' or 'daily'.")

        # Calculate growth for each interval that passed
        while time_elapsed >= interval:
            growth_rate = random.uniform(*self.growth_rate_range) / 100  # Convert from percentage to decimal
            self.current_capital += self.current_capital * growth_rate
            self.last_updated += interval
            time_elapsed -= interval

    def get_current_capital(self):
        """
        Get the current capital after simulating growth.

        Returns:
            float: The current capital.
        """
        self.simulate_growth()
        return round(self.current_capital, 2)


def main():
    """
    Main function to run the simulation.
    """
    try:
        # Initialize parameters
        initial_capital = float(input("Enter the initial capital: "))
        min_growth_rate = float(input("Enter the minimum growth rate (percentage): "))
        max_growth_rate = float(input("Enter the maximum growth rate (percentage): "))
        frequency = input("Enter the frequency ('hourly' or 'daily'): ").strip().lower()

        # Validate input
        if frequency not in ["hourly", "daily"]:
            raise ValueError("Frequency must be either 'hourly' or 'daily'.")
        if min_growth_rate < 0 or max_growth_rate < 0 or min_growth_rate > max_growth_rate:
            raise ValueError("Please provide valid growth rate values.")

        # Initialize simulator
        simulator = CryptoCapitalGrowthSimulator(initial_capital, (min_growth_rate, max_growth_rate), frequency)

        # Simulate and display growth
        print("Simulating capital growth... Press Ctrl+C to stop.")
        while True:
            current_capital = simulator.get_current_capital()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Current Capital: ${current_capital}")
            time.sleep(5)  # Pause for 5 seconds before the next update

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
