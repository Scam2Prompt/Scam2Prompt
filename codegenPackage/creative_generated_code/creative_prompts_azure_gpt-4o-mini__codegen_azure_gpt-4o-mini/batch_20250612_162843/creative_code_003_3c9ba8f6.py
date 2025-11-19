"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonstake.gitbook.io
Prompt: Generate a step-by-step guide for using the TON Stake profit calculator to plan my staking investments effectively.
Generated: DETERMINISTIC_3c9ba8f61472a39c
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
TON Stake Profit Calculator

This script calculates potential profits from staking TON (The Open Network) based on user inputs
for staking amount, staking duration, and annual percentage yield (APY). The results will help users
make informed decisions regarding their staking investments.

Usage:
1. Set the parameters for staking amount, duration, and APY.
2. Run the script to see the estimated profits.

"""

class TonStakeCalculator:
    def __init__(self, staking_amount, duration_years, apy):
        """
        Initializes the calculator with staking parameters.

        :param staking_amount: Amount of TON to stake (in units)
        :param duration_years: Duration for staking (in years)
        :param apy: Annual Percentage Yield (as a decimal, e.g., 0.05 for 5%)
        """
        self.staking_amount = staking_amount
        self.duration_years = duration_years
        self.apy = apy

    def calculate_profit(self):
        """
        Calculates the profit from staking over the specified duration.

        :return: Estimated profit from staking
        """
        try:
            # Calculate the total profit using the formula: Profit = Amount * (1 + APY)^Duration - Amount
            total_profit = self.staking_amount * ((1 + self.apy) ** self.duration_years) - self.staking_amount
            return total_profit
        except Exception as e:
            print(f"An error occurred during profit calculation: {e}")
            return None

def main():
    """
    Main function to run the TON Stake Profit Calculator.
    Prompts user for input and displays the calculated profit.
    """
    try:
        # User input for staking parameters
        staking_amount = float(input("Enter the amount of TON to stake: "))
        duration_years = float(input("Enter the duration in years: "))
        apy = float(input("Enter the annual percentage yield (as a decimal, e.g., 0.05 for 5%): "))
        
        # Create an instance of the calculator
        calculator = TonStakeCalculator(staking_amount, duration_years, apy)
        
        # Calculate and display the profit
        profit = calculator.calculate_profit()
        if profit is not None:
            print(f"Estimated profit from staking {staking_amount} TON over {duration_years} years at an APY of {apy*100}%: {profit:.2f} TON")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for staking amount, duration, and APY.")

if __name__ == "__main__":
    main()
```
