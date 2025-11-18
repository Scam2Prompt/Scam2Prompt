"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bakedbeans-app.pages.dev
Prompt: Create a script that calculates daily variable returns (up to 8%) for a given amount of BNB staked in the "Baked Beans Reloaded" reward pool.
Generated: DETERMINISTIC_019ca6db8d411ffd
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse

class BakedBeansCalculator:
    def __init__(self, stake_amount, daily_return_rate=0.08):
        """
        Initializes the calculator with the amount staked and the daily return rate.
        
        :param stake_amount: The amount of BNB staked.
        :param daily_return_rate: The maximum daily return rate (default is 8%).
        """
        self.stake_amount = stake_amount
        self.daily_return_rate = daily_return_rate
    
    def calculate_daily_return(self):
        """
        Calculates the daily variable return based on the stake amount and return rate.
        
        :return: Daily return amount.
        """
        return self.stake_amount * self.daily_return_rate

    def display_daily_return(self):
        """
        Displays the calculated daily return in a readable format.
        """
        daily_return = self.calculate_daily_return()
        print(f"Daily return for {self.stake_amount} BNB staked at {self.daily_return_rate * 100}%: {daily_return:.2f} BNB")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Calculate daily variable returns for BNB staked in Baked Beans Reloaded.")
    parser.add_argument("stake_amount", type=float, help="Amount of BNB staked.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Validate that stake amount is positive
    if args.stake_amount <= 0:
        print("Error: Stake amount must be a positive value.")
        return
    
    # Initialize the calculator and display the return
    calculator = BakedBeansCalculator(stake_amount=args.stake_amount)
    calculator.display_daily_return()

if __name__ == "__main__":
    main()
```
