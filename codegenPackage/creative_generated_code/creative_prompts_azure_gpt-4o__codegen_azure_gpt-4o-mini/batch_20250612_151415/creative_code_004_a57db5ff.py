"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Generate a script to calculate fixed deposit maturity and interest, referencing the Fixed Deposit Calculator tool on the IFSC Finder webpage.
Generated: DETERMINISTIC_a57db5ff568bd0c3
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class FixedDepositCalculator:
    """
    A class to calculate the maturity amount and interest earned on a fixed deposit.
    """

    def __init__(self, principal, rate_of_interest, tenure_years):
        """
        Initializes the FixedDepositCalculator with principal amount, rate of interest, and tenure.

        :param principal: The initial amount of money deposited (float).
        :param rate_of_interest: The annual interest rate (as a percentage, float).
        :param tenure_years: The duration of the deposit in years (int).
        """
        self.principal = principal
        self.rate_of_interest = rate_of_interest / 100  # Convert percentage to decimal
        self.tenure_years = tenure_years

    def calculate_interest(self):
        """
        Calculates the interest earned on the fixed deposit.

        :return: The total interest earned (float).
        """
        try:
            interest = self.principal * self.rate_of_interest * self.tenure_years
            return interest
        except Exception as e:
            raise ValueError(f"Error calculating interest: {e}")

    def calculate_maturity_amount(self):
        """
        Calculates the total maturity amount at the end of the fixed deposit tenure.

        :return: The maturity amount (float).
        """
        try:
            interest = self.calculate_interest()
            maturity_amount = self.principal + interest
            return maturity_amount
        except Exception as e:
            raise ValueError(f"Error calculating maturity amount: {e}")

    def display_results(self):
        """
        Displays the calculated results for maturity amount and interest.
        """
        try:
            interest = self.calculate_interest()
            maturity_amount = self.calculate_maturity_amount()
            print(f"Principal Amount: {self.principal:.2f}")
            print(f"Rate of Interest: {self.rate_of_interest * 100:.2f}%")
            print(f"Tenure: {self.tenure_years} years")
            print(f"Interest Earned: {interest:.2f}")
            print(f"Maturity Amount: {maturity_amount:.2f}")
        except Exception as e:
            print(f"Error displaying results: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        principal = float(input("Enter the principal amount: "))
        rate_of_interest = float(input("Enter the annual interest rate (in %): "))
        tenure_years = int(input("Enter the tenure in years: "))
        
        fd_calculator = FixedDepositCalculator(principal, rate_of_interest, tenure_years)
        fd_calculator.display_results()
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
