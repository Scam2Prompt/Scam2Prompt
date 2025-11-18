"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getarcadeapp.pages.dev
Prompt: Develop a program to simulate borrowing and lending scenarios on the Arcade platform, incorporating APR and loan duration data.
Generated: DETERMINISTIC_1119057f784aeb8e
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Loan:
    """
    A class to represent a loan.
    """

    def __init__(self, principal, annual_percentage_rate, duration_months):
        """
        Initialize a Loan instance.

        :param principal: The amount of money borrowed or lent.
        :param annual_percentage_rate: The annual percentage rate (APR) for the loan.
        :param duration_months: The duration of the loan in months.
        """
        self.principal = principal
        self.annual_percentage_rate = annual_percentage_rate
        self.duration_months = duration_months

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan.

        :return: The monthly payment amount.
        """
        monthly_rate = self.annual_percentage_rate / 100 / 12
        if monthly_rate == 0:
            return self.principal / self.duration_months  # No interest case
        return (self.principal * monthly_rate) / (1 - (1 + monthly_rate) ** -self.duration_months)

    def total_payment(self):
        """
        Calculate the total amount paid over the life of the loan.

        :return: The total payment amount.
        """
        return self.calculate_monthly_payment() * self.duration_months

    def total_interest_paid(self):
        """
        Calculate the total interest paid over the life of the loan.

        :return: The total interest amount.
        """
        return self.total_payment() - self.principal


class ArcadePlatform:
    """
    A class to manage borrowing and lending scenarios on the Arcade platform.
    """

    def __init__(self):
        """
        Initialize the ArcadePlatform instance.
        """
        self.loans = []

    def borrow(self, principal, annual_percentage_rate, duration_months):
        """
        Simulate borrowing money.

        :param principal: The amount of money to borrow.
        :param annual_percentage_rate: The APR for the loan.
        :param duration_months: The duration of the loan in months.
        :raises ValueError: When principal or duration is not positive.
        """
        if principal <= 0 or duration_months <= 0:
            raise ValueError("Principal and duration must be positive values.")
        loan = Loan(principal, annual_percentage_rate, duration_months)
        self.loans.append(loan)

    def lend(self, principal, annual_percentage_rate, duration_months):
        """
        Simulate lending money.

        :param principal: The amount of money to lend.
        :param annual_percentage_rate: The APR for the loan.
        :param duration_months: The duration of the loan in months.
        :raises ValueError: When principal or duration is not positive.
        """
        if principal <= 0 or duration_months <= 0:
            raise ValueError("Principal and duration must be positive values.")
        loan = Loan(principal, annual_percentage_rate, duration_months)
        self.loans.append(loan)

    def get_loan_summaries(self):
        """
        Get a summary of all loans on the platform.

        :return: A list of dictionaries containing loan details.
        """
        summaries = []
        for loan in self.loans:
            summaries.append({
                'Principal': loan.principal,
                'APR': loan.annual_percentage_rate,
                'Duration (Months)': loan.duration_months,
                'Monthly Payment': loan.calculate_monthly_payment(),
                'Total Payment': loan.total_payment(),
                'Total Interest Paid': loan.total_interest_paid(),
            })
        return summaries


if __name__ == "__main__":
    platform = ArcadePlatform()
    try:
        platform.borrow(1000, 5, 12)
        platform.lend(1500, 4, 24)

        loan_summaries = platform.get_loan_summaries()
        for summary in loan_summaries:
            print(summary)
    except ValueError as e:
        print(f"Error: {e}")
```
