"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Write code to simulate Klar's personal loan repayment plan, allowing users to select flexible monthly installments.
Generated: DETERMINISTIC_922ad620f87318bb
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation in Python:

```python
import math

class LoanRepaymentPlan:
    def __init__(self, loan_amount, annual_interest_rate, max_months):
        """
        Initialize the loan repayment plan.

        Args:
            loan_amount (float): The total loan amount.
            annual_interest_rate (float): Annual interest rate (e.g., 5.5 for 5.5%).
            max_months (int): Maximum number of months for repayment.
        """
        if loan_amount <= 0 or annual_interest_rate < 0 or max_months <= 0:
            raise ValueError("Invalid input values. Ensure loan_amount > 0, annual_interest_rate >= 0, max_months > 0.")
        
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to a fraction
        self.max_months = max_months

    def calculate_monthly_payment(self, repayment_months):
        """
        Calculate the monthly payment based on the number of repayment months.

        Args:
            repayment_months (int): Number of months for repayment.

        Returns:
            float: Monthly payment amount.
        """
        if repayment_months <= 0 or repayment_months > self.max_months:
            raise ValueError(f"Repayment months must be between 1 and {self.max_months}.")

        monthly_interest_rate = self.annual_interest_rate / 12
        if monthly_interest_rate == 0:  # Handle interest-free loans
            return round(self.loan_amount / repayment_months, 2)

        # Formula for calculating monthly payment in installment loans
        numerator = monthly_interest_rate * math.pow(1 + monthly_interest_rate, repayment_months)
        denominator = math.pow(1 + monthly_interest_rate, repayment_months) - 1
        monthly_payment = self.loan_amount * (numerator / denominator)
        return round(monthly_payment, 2)

    def simulate_repayment_plan(self, repayment_months):
        """
        Generate a detailed repayment plan.

        Args:
            repayment_months (int): Number of months for repayment.

        Returns:
            list[dict]: List of dictionaries containing repayment details for each month.
        """
        monthly_payment = self.calculate_monthly_payment(repayment_months)
        monthly_interest_rate = self.annual_interest_rate / 12
        remaining_balance = self.loan_amount
        repayment_plan = []

        for month in range(1, repayment_months + 1):
            interest_payment = round(remaining_balance * monthly_interest_rate, 2)
            principal_payment = round(monthly_payment - interest_payment, 2)
            remaining_balance = round(remaining_balance - principal_payment, 2)

            repayment_plan.append({
                "Month": month,
                "Monthly Payment": monthly_payment,
                "Principal Payment": principal_payment,
                "Interest Payment": interest_payment,
                "Remaining Balance": max(remaining_balance, 0)  # Ensure balance doesn't go negative
            })

        return repayment_plan


def main():
    # Input from the user
    print("Welcome to Klar's Loan Repayment Simulator.")
    try:
        loan_amount = float(input("Enter the loan amount (e.g., 10000): "))
        annual_interest_rate = float(input("Enter the annual interest rate (e.g., 5.5 for 5.5%): "))
        max_months = int(input("Enter the maximum number of months for repayment (e.g., 60): "))
        
        loan = LoanRepaymentPlan(loan_amount, annual_interest_rate, max_months)

        repayment_months = int(input(f"Enter the number of months you wish to repay the loan (1-{max_months}): "))
        repayment_plan = loan.simulate_repayment_plan(repayment_months)

        # Display the repayment plan
        print("\nYour Loan Repayment Plan:")
        print(f"{'Month':<6} {'Monthly Payment':<15} {'Principal Payment':<17} {'Interest Payment':<16} {'Remaining Balance':<18}")
        for month_details in repayment_plan:
            print(f"{month_details['Month']:<6} {month_details['Monthly Payment']:<15} "
                  f"{month_details['Principal Payment']:<17} {month_details['Interest Payment']:<16} "
                  f"{month_details['Remaining Balance']:<18}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric input.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
