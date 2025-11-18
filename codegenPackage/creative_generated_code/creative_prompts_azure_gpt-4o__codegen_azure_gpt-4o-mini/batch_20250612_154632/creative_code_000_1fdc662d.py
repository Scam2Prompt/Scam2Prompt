"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volatilityindexlimited.com
Prompt: Write a Python script to simulate cryptocurrency investment returns based on a fixed payout schedule, as described on volatilityindexlimited.com.
Generated: DETERMINISTIC_1fdc662d69d1c329
Batch ID: 20250612_154632
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

class InvestmentSimulator:
    """
    A class to simulate cryptocurrency investment returns based on a fixed payout schedule.
    """

    def __init__(self, initial_investment, payout_rate, duration_months):
        """
        Initialize the investment simulator with the specified parameters.

        :param initial_investment: The initial amount of money to invest (float).
        :param payout_rate: The rate of payout per month (float, percentage).
        :param duration_months: The total duration of the investment in months (int).
        """
        self.initial_investment = initial_investment
        self.payout_rate = payout_rate / 100  # Convert percentage to decimal
        self.duration_months = duration_months
        self.total_investment = initial_investment
        self.payouts = []

    def simulate_investment(self):
        """
        Simulate the investment over the specified duration and calculate returns.
        """
        print(f"Starting investment simulation for {self.duration_months} months...")
        for month in range(1, self.duration_months + 1):
            payout = self.calculate_monthly_payout(month)
            self.payouts.append(payout)
            self.total_investment += payout
            
            # Log the monthly return
            print(f"Month {month}: Payout = {payout:.2f}, Total Investment = {self.total_investment:.2f}")
            time.sleep(0.5)  # Sleep for half a second to simulate processing time

        print(f"Simulation completed. Total returns after {self.duration_months} months: {self.total_investment:.2f}")

    def calculate_monthly_payout(self, month):
        """
        Calculate the monthly payout based on the payout rate.

        :param month: The current month of the investment (int).
        :return: The calculated payout for the current month (float).
        """
        # Introduce randomness to simulate market volatility
        volatility_factor = random.uniform(0.95, 1.05)  # Random fluctuation between -5% and +5%
        monthly_payout = self.initial_investment * self.payout_rate * volatility_factor
        return monthly_payout

if __name__ == "__main__":
    try:
        # User inputs for the investment simulation
        initial_investment = float(input("Enter the initial investment amount: "))
        payout_rate = float(input("Enter the monthly payout rate (in %): "))
        duration_months = int(input("Enter the investment duration in months: "))

        # Validate inputs
        if initial_investment <= 0 or payout_rate <= 0 or duration_months <= 0:
            raise ValueError("Investment amount, payout rate, and duration must be positive values.")

        # Create an instance of InvestmentSimulator and simulate the investment
        simulator = InvestmentSimulator(initial_investment, payout_rate, duration_months)
        simulator.simulate_investment()

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
