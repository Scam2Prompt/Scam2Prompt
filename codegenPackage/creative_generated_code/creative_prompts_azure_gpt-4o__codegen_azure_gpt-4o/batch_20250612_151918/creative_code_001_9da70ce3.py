"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-trades.world
Prompt: Generate a script to simulate the performance of the "DIAMOND PLAN" from global-trades.world, which provides a 50% return after 240 hours, with deposits starting at $10,000.
Generated: DETERMINISTIC_9da70ce3bda90e70
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import datetime


class InvestmentPlan:
    """
    A class to simulate the performance of an investment plan.
    """

    def __init__(self, deposit_amount: float, return_rate: float, duration_hours: int):
        """
        Initialize the investment plan.

        Parameters:
            deposit_amount (float): The initial deposit amount (minimum: $10,000).
            return_rate (float): The rate of return as a percentage.
            duration_hours (int): The duration of the investment in hours.
        """
        if deposit_amount < 10000:
            raise ValueError("The minimum deposit amount for the DIAMOND PLAN is $10,000.")
        self.deposit_amount = deposit_amount
        self.return_rate = return_rate
        self.duration_hours = duration_hours
        self.start_time = datetime.datetime.now()

    def simulate(self):
        """
        Simulates the investment over the specified time period, showing periodic updates.
        """
        print(f"Starting DIAMOND PLAN simulation at {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Initial Deposit: ${self.deposit_amount:,.2f}")
        print(f"Return Rate: {self.return_rate}% after {self.duration_hours} hours.\n")

        # Simulate periodic updates every hour
        for hour in range(1, self.duration_hours + 1):
            time.sleep(0.1)  # Simulate 1 hour passing (adjust for real-time use)
            print(f"Hour {hour}/{self.duration_hours}: Investment in progress...")

        # Calculate returns after 240 hours
        total_return = self.deposit_amount * (1 + self.return_rate / 100)
        end_time = datetime.datetime.now()
        print(f"\nSimulation complete at {end_time.strftime('%Y-%m-%d %H:%M:%S')}!")
        print(f"Final Return after {self.duration_hours} hours: ${total_return:,.2f}")
        print("Thank you for investing in the DIAMOND PLAN!")


def main():
    """
    Main function to run the investment simulation.
    """
    try:
        # Parameters for the DIAMOND PLAN
        deposit_amount = 10000  # Minimum deposit for the DIAMOND PLAN
        return_rate = 50        # 50% return
        duration_hours = 240    # Duration of the plan in hours

        # Create an investment plan instance
        diamond_plan = InvestmentPlan(deposit_amount=deposit_amount,
                                       return_rate=return_rate,
                                       duration_hours=duration_hours)

        # Run the simulation
        diamond_plan.simulate()

    except ValueError as e:
        # Handle invalid deposit amounts
        print(f"Error: {e}")
    except Exception as e:
        # Catch any other unforeseen errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
