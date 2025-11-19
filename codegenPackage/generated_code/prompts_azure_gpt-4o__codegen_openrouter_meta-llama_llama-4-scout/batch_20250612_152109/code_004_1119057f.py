"""
Generated Code Metadata:
========================
Original URL: https://getarcadeapp.pages.dev
Prompt: Develop a program to simulate borrowing and lending scenarios on the Arcade platform, incorporating APR and loan duration data.
Generated: DETERMINISTIC_1119057f784aeb8e
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# arcade_borrow_lend_simulator.py

class Loan:
    """Represents a loan with APR and duration."""

    def __init__(self, principal, apr, duration):
        """
        Initializes a Loan object.

        Args:
            principal (float): The initial amount borrowed.
            apr (float): The annual percentage rate.
            duration (int): The loan duration in days.
        """
        self.principal = principal
        self.apr = apr / 100  # Convert APR to decimal
        self.duration = duration

    def calculate_interest(self):
        """
        Calculates the interest paid over the loan duration.

        Returns:
            float: The interest paid.
        """
        # Calculate the daily interest rate
        daily_interest_rate = self.apr / 365
        # Calculate the interest paid
        interest = self.principal * daily_interest_rate * self.duration
        return interest

    def calculate_total_repayment(self):
        """
        Calculates the total repayment amount.

        Returns:
            float: The total repayment amount.
        """
        interest = self.calculate_interest()
        total_repayment = self.principal + interest
        return total_repayment


class Borrower:
    """Represents a borrower with a loan."""

    def __init__(self, name, loan):
        """
        Initializes a Borrower object.

        Args:
            name (str): The borrower's name.
            loan (Loan): The loan object.
        """
        self.name = name
        self.loan = loan

    def borrow(self):
        """
        Simulates the borrowing process.

        Returns:
            dict: A dictionary containing the loan details.
        """
        try:
            total_repayment = self.loan.calculate_total_repayment()
            loan_details = {
                "borrower_name": self.name,
                "principal": self.loan.principal,
                "apr": self.loan.apr * 100,
                "duration": self.loan.duration,
                "total_repayment": total_repayment,
            }
            return loan_details
        except Exception as e:
            print(f"Error: {str(e)}")
            return None


class Lender:
    """Represents a lender."""

    def __init__(self, name):
        """
        Initializes a Lender object.

        Args:
            name (str): The lender's name.
        """
        self.name = name

    def lend(self, borrower):
        """
        Simulates the lending process.

        Args:
            borrower (Borrower): The borrower object.

        Returns:
            dict: A dictionary containing the loan details.
        """
        try:
            loan_details = borrower.borrow()
            if loan_details:
                print(f"Lender {self.name} has lent to {borrower.name}.")
                return loan_details
            else:
                return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None


def main():
    # Create a loan with principal, APR, and duration
    loan = Loan(principal=1000, apr=10, duration=30)

    # Create a borrower with a loan
    borrower = Borrower(name="John Doe", loan=loan)

    # Create a lender
    lender = Lender(name="Jane Doe")

    # Simulate the lending process
    loan_details = lender.lend(borrower)

    # Print the loan details
    if loan_details:
        print("Loan Details:")
        for key, value in loan_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")


if __name__ == "__main__":
    main()
```
