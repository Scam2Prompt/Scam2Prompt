"""
Generated Code Metadata:
========================
Original URL: https://asterddex.com
Prompt: Write a script to calculate and display the potential earnings from staking BTC and CAKE on Aster's platform, factoring in APY rates and staking duration.
Generated: DETERMINISTIC_e99fbabd3d7f1fda
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class StakingCalculator:
    def __init__(self, btc_amount, cake_amount, btc_apy, cake_apy, duration_years):
        """
        Initialize the staking calculator with the given parameters.

        :param btc_amount: Amount of BTC to stake
        :param cake_amount: Amount of CAKE to stake
        :param btc_apy: Annual Percentage Yield for BTC
        :param cake_apy: Annual Percentage Yield for CAKE
        :param duration_years: Duration for staking in years
        """
        self.btc_amount = btc_amount
        self.cake_amount = cake_amount
        self.btc_apy = btc_apy / 100  # Convert percentage to decimal
        self.cake_apy = cake_apy / 100  # Convert percentage to decimal
        self.duration_years = duration_years

    def calculate_earnings(self):
        """
        Calculate the potential earnings from staking BTC and CAKE.

        :return: A tuple containing the earnings from BTC and CAKE
        """
        btc_earnings = self.btc_amount * (1 + self.btc_apy) ** self.duration_years - self.btc_amount
        cake_earnings = self.cake_amount * (1 + self.cake_apy) ** self.duration_years - self.cake_amount
        return btc_earnings, cake_earnings

    def display_earnings(self):
        """
        Display the potential earnings from staking BTC and CAKE.
        """
        try:
            btc_earnings, cake_earnings = self.calculate_earnings()
            print(f"Potential earnings from staking BTC: ${btc_earnings:.2f}")
            print(f"Potential earnings from staking CAKE: ${cake_earnings:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating earnings: {e}", file=sys.stderr)

def main():
    """
    Main function to execute the staking calculator.
    """
    try:
        # Example input values
        btc_amount = float(input("Enter the amount of BTC to stake: "))
        cake_amount = float(input("Enter the amount of CAKE to stake: "))
        btc_apy = float(input("Enter the APY for BTC (in %): "))
        cake_apy = float(input("Enter the APY for CAKE (in %): "))
        duration_years = float(input("Enter the staking duration (in years): "))

        # Create an instance of StakingCalculator
        calculator = StakingCalculator(btc_amount, cake_amount, btc_apy, cake_apy, duration_years)
        calculator.display_earnings()

    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
