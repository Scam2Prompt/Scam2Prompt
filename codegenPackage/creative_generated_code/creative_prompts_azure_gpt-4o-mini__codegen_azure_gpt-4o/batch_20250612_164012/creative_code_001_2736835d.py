"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.evercoreglobal.com
Prompt: Write a code snippet that simulates the process of securing optimal financing solutions as described by Evercore Global.
Generated: DETERMINISTIC_2736835d66ef3139
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class FinancingOption:
    """
    Class to represent a financing option.
    """
    def __init__(self, lender_name, interest_rate, loan_amount, duration_years):
        self.lender_name = lender_name
        self.interest_rate = interest_rate  # Annual interest rate as a percentage
        self.loan_amount = loan_amount     # Total loan amount
        self.duration_years = duration_years  # Loan duration in years

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment using the formula for fixed-rate loans.
        Formula: M = P[r(1+r)^n] / [(1+r)^n - 1]
        Where:
        M = monthly payment
        P = loan amount
        r = monthly interest rate (annual rate divided by 12)
        n = total number of payments (months)
        """
        try:
            monthly_rate = self.interest_rate / 100 / 12
            total_payments = self.duration_years * 12
            if monthly_rate == 0:  # If interest rate is zero
                return self.loan_amount / total_payments
            
            monthly_payment = (
                self.loan_amount
                * monthly_rate
                * math.pow(1 + monthly_rate, total_payments)
                / (math.pow(1 + monthly_rate, total_payments) - 1)
            )
            return monthly_payment
        except Exception as e:
            raise ValueError(f"Error calculating monthly payment: {e}")

    def __str__(self):
        return f"Lender: {self.lender_name}, Interest Rate: {self.interest_rate}%, Loan Amount: ${self.loan_amount}, Duration: {self.duration_years} years"


class FinancingAdvisor:
    """
    Class to simulate the process of securing optimal financing solutions.
    """
    def __init__(self):
        self.options = []

    def add_option(self, option):
        """
        Add a financing option to the list.
        """
        if not isinstance(option, FinancingOption):
            raise TypeError("Option must be an instance of FinancingOption.")
        self.options.append(option)

    def find_best_option(self):
        """
        Find the optimal financing option based on the lowest monthly payment.
        """
        if not self.options:
            raise ValueError("No financing options available.")
        
        best_option = min(
            self.options,
            key=lambda option: option.calculate_monthly_payment()
        )
        return best_option

    def display_options(self):
        """
        Display all financing options.
        """
        if not self.options:
            print("No financing options added.")
        else:
            for option in self.options:
                print(option)


# Simulation
if __name__ == "__main__":
    try:
        advisor = FinancingAdvisor()

        # Adding financing options
        advisor.add_option(FinancingOption("Lender A", 3.5, 50000, 5))
        advisor.add_option(FinancingOption("Lender B", 4.0, 50000, 5))
        advisor.add_option(FinancingOption("Lender C", 2.8, 50000, 5))

        print("Available Financing Options:")
        advisor.display_options()

        # Finding and displaying the best option
        best_option = advisor.find_best_option()
        print("\nOptimal Financing Solution:")
        print(best_option)
        print(f"Monthly Payment: ${best_option.calculate_monthly_payment():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
