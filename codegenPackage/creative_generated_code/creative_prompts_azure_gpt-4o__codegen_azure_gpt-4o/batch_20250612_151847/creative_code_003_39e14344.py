"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binotradefx.com
Prompt: Create a program that simulates the investment growth process described on BinoTrade Fx, including features like payouts every 60 minutes and package-specific ROI calculations.
Generated: DETERMINISTIC_39e1434431967daf
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta


class InvestmentPackage:
    """
    Class representing an investment package with specific ROI and payout frequency.
    """

    def __init__(self, name, roi_percent, duration_minutes):
        """
        Initializes the investment package.
        :param name: Name of the investment package
        :param roi_percent: ROI percentage per payout cycle (e.g., 5 for 5%)
        :param duration_minutes: Duration of each payout cycle in minutes
        """
        self.name = name
        self.roi_percent = roi_percent
        self.duration_minutes = duration_minutes


class InvestmentAccount:
    """
    Class representing a user's investment account.
    """

    def __init__(self, initial_balance, investment_package):
        """
        Initializes the investment account with the given balance and package.
        :param initial_balance: Initial investment balance in dollars
        :param investment_package: The chosen investment package (InvestmentPackage object)
        """
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.investment_package = investment_package
        self.start_time = datetime.now()
        self.last_payout_time = self.start_time

    def calculate_payout(self):
        """
        Calculates the payout based on the package's ROI percentage.
        :return: Payout amount in dollars
        """
        return self.current_balance * (self.investment_package.roi_percent / 100)

    def process_payout(self):
        """
        Processes a payout by adding the calculated payout to the current balance.
        """
        payout = self.calculate_payout()
        self.current_balance += payout
        self.last_payout_time = datetime.now()
        print(f"[{self.last_payout_time.strftime('%Y-%m-%d %H:%M:%S')}] Payout of ${payout:.2f} processed. "
              f"Current balance: ${self.current_balance:.2f}")

    def simulate_growth(self, duration_minutes):
        """
        Simulates investment growth over a specified number of minutes.
        :param duration_minutes: Total duration to simulate in minutes
        """
        end_time = self.start_time + timedelta(minutes=duration_minutes)
        while datetime.now() < end_time:
            time.sleep(self.investment_package.duration_minutes * 60)  # Wait for the payout interval
            self.process_payout()
        print(f"Simulation complete. Final balance: ${self.current_balance:.2f}")


def main():
    """
    Entry point for the investment growth simulation program.
    """
    print("Welcome to BinoTrade Fx Investment Simulator!")

    # Example packages
    basic_package = InvestmentPackage(name="Basic", roi_percent=1, duration_minutes=60)
    premium_package = InvestmentPackage(name="Premium", roi_percent=5, duration_minutes=60)

    # User selects a package
    print("Available Packages:")
    print(f"1. {basic_package.name} (ROI: {basic_package.roi_percent}% every {basic_package.duration_minutes} minutes)")
    print(f"2. {premium_package.name} (ROI: {premium_package.roi_percent}% every {premium_package.duration_minutes} minutes)")

    package_choice = input("Enter the number corresponding to your chosen package: ")
    if package_choice == "1":
        selected_package = basic_package
    elif package_choice == "2":
        selected_package = premium_package
    else:
        print("Invalid choice. Exiting simulation.")
        return

    # User enters initial balance
    try:
        initial_balance = float(input("Enter your initial investment amount (in $): "))
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than 0.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # User enters simulation duration
    try:
        simulation_duration = int(input("Enter simulation duration (in minutes): "))
        if simulation_duration <= 0:
            raise ValueError("Simulation duration must be greater than 0.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Create and run investment account
    account = InvestmentAccount(initial_balance, selected_package)
    account.simulate_growth(simulation_duration)


if __name__ == "__main__":
    main()
```
