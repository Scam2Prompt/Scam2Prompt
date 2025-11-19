"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Create a program that estimates loan eligibility based on income, similar to the Loan Eligibility Estimator tool mentioned on the IFSC Finder website.
Generated: DETERMINISTIC_9971b119ac284c41
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_eligibility_estimator.py

class LoanEligibilityEstimator:
    """
    Estimates loan eligibility based on income.

    Attributes:
        income (float): The user's income.
        loan_term (int): The loan term in years.
        interest_rate (float): The interest rate as a decimal.
        debt_to_income_ratio (float): The maximum debt-to-income ratio.
        max_loan_amount (float): The maximum loan amount.
    """

    def __init__(self, income, loan_term, interest_rate, debt_to_income_ratio=0.36, max_loan_amount=500000):
        """
        Initializes the LoanEligibilityEstimator.

        Args:
            income (float): The user's income.
            loan_term (int): The loan term in years.
            interest_rate (float): The interest rate as a decimal.
            debt_to_income_ratio (float, optional): The maximum debt-to-income ratio. Defaults to 0.36.
            max_loan_amount (float, optional): The maximum loan amount. Defaults to 500000.
        """
        self.income = income
        self.loan_term = loan_term
        self.interest_rate = interest_rate
        self.debt_to_income_ratio = debt_to_income_ratio
        self.max_loan_amount = max_loan_amount

    def calculate_monthly_payment(self, loan_amount):
        """
        Calculates the monthly payment for a given loan amount.

        Args:
            loan_amount (float): The loan amount.

        Returns:
            float: The monthly payment.
        """
        monthly_interest_rate = self.interest_rate / 12
        number_of_payments = self.loan_term * 12
        monthly_payment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / (
                (1 + monthly_interest_rate) ** number_of_payments - 1)
        return monthly_payment

    def estimate_loan_eligibility(self):
        """
        Estimates the loan eligibility based on income.

        Returns:
            dict: A dictionary containing the estimated loan amount and monthly payment.
        """
        try:
            # Calculate the maximum monthly payment based on the debt-to-income ratio
            max_monthly_payment = self.income * self.debt_to_income_ratio / 12

            # Calculate the maximum loan amount based on the maximum monthly payment
            max_loan_amount_based_on_income = max_monthly_payment / (self.interest_rate / 12) * (
                    1 - (1 + self.interest_rate / 12) ** (-self.loan_term * 12))

            # Limit the maximum loan amount to the specified maximum loan amount
            estimated_loan_amount = min(max_loan_amount_based_on_income, self.max_loan_amount)

            # Ensure the estimated loan amount is not negative
            if estimated_loan_amount < 0:
                estimated_loan_amount = 0

            # Calculate the estimated monthly payment
            estimated_monthly_payment = self.calculate_monthly_payment(estimated_loan_amount)

            return {
                "estimated_loan_amount": estimated_loan_amount,
                "estimated_monthly_payment": estimated_monthly_payment
            }

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    income = float(input("Enter your income: "))
    loan_term = int(input("Enter the loan term in years: "))
    interest_rate = float(input("Enter the interest rate as a percentage (e.g., 8 for 8%): ")) / 100

    estimator = LoanEligibilityEstimator(income, loan_term, interest_rate)
    eligibility = estimator.estimate_loan_eligibility()

    if eligibility:
        print(f"Estimated loan amount: ${eligibility['estimated_loan_amount']:.2f}")
        print(f"Estimated monthly payment: ${eligibility['estimated_monthly_payment']:.2f}")


if __name__ == "__main__":
    main()
```
