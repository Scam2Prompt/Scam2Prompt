"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camp-dmb.pages.dev
Prompt: Write a Python script to simulate the profit distribution for the "Achievers Plan," which offers a 15% return after 8 days, based on the deposit amount.
Generated: DETERMINISTIC_ef89c12d24ab2dac
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class AchieversPlan:
    def __init__(self, deposit_amount):
        """
        Initializes the AchieversPlan with the given deposit amount.

        :param deposit_amount: float - The initial deposit amount for the investment
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.deposit_amount = deposit_amount
        self.return_rate = 0.15  # 15% return
        self.duration_days = 8    # Investment duration in days

    def calculate_profit(self):
        """
        Calculates the profit based on the deposit amount and return rate.

        :return: float - The profit earned after the investment duration
        """
        profit = self.deposit_amount * self.return_rate
        return profit

    def simulate_investment(self):
        """
        Simulates the investment over the specified duration and returns the final amount.

        :return: float - The total amount after the investment duration
        """
        print(f"Investing ${self.deposit_amount:.2f} for {self.duration_days} days...")
        time.sleep(2)  # Simulate waiting for the investment period
        profit = self.calculate_profit()
        total_amount = self.deposit_amount + profit
        return total_amount

def main():
    """
    Main function to run the investment simulation.
    """
    try:
        # User input for deposit amount
        deposit_amount = float(input("Enter the deposit amount: "))
        
        # Create an instance of AchieversPlan
        achievers_plan = AchieversPlan(deposit_amount)
        
        # Simulate the investment and get the total amount
        total_amount = achievers_plan.simulate_investment()
        
        # Display the results
        print(f"Total amount after {achievers_plan.duration_days} days: ${total_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
