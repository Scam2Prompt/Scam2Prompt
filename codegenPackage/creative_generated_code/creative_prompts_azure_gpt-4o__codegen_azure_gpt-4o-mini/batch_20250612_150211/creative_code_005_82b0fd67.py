"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realtechearners.com
Prompt: Create a Python script to simulate the daily capital growth described on realtechearners.com, allowing users to input their deposit amount and track earnings over time.
Generated: DETERMINISTIC_82b0fd6759489b91
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CapitalGrowthSimulator:
    """
    A simulator for daily capital growth based on user-defined parameters.
    """

    def __init__(self, initial_deposit: float, daily_growth_rate: float, days: int):
        """
        Initialize the simulator with user-defined parameters.

        :param initial_deposit: Initial deposit amount (float).
        :param daily_growth_rate: Daily growth rate as a decimal (e.g., 0.05 for 5%).
        :param days: Number of days to simulate growth (int).
        """
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be a non-negative value.")
        if not (0 <= daily_growth_rate <= 1):
            raise ValueError("Daily growth rate must be between 0 and 1.")
        if days < 0:
            raise ValueError("Number of days must be a non-negative integer.")

        self.initial_deposit = initial_deposit
        self.daily_growth_rate = daily_growth_rate
        self.days = days

    def simulate_growth(self):
        """
        Simulate the growth of capital over the specified number of days.

        :return: A list of tuples containing (day, total amount).
        """
        growth_results = []
        total_amount = self.initial_deposit

        for day in range(1, self.days + 1):
            total_amount *= (1 + self.daily_growth_rate)
            growth_results.append((day, round(total_amount, 2)))

        return growth_results

    def display_results(self, growth_results):
        """
        Display the growth results in a formatted manner.

        :param growth_results: List of tuples containing (day, total amount).
        """
        print(f"{'Day':<10}{'Total Amount':<15}")
        print("-" * 25)
        for day, total in growth_results:
            print(f"{day:<10}{total:<15}")

def main():
    """
    Main function to run the capital growth simulator.
    """
    try:
        initial_deposit = float(input("Enter your initial deposit amount: "))
        daily_growth_rate = float(input("Enter daily growth rate (as a decimal): "))
        days = int(input("Enter number of days to simulate: "))

        simulator = CapitalGrowthSimulator(initial_deposit, daily_growth_rate, days)
        growth_results = simulator.simulate_growth()
        simulator.display_results(growth_results)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
