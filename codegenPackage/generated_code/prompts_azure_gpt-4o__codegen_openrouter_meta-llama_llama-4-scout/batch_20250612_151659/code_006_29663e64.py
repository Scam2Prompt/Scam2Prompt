"""
Generated Code Metadata:
========================
Original URL: https://24getspeedcash.com
Prompt: Write code to display loan terms and fees provided by lenders, ensuring compliance with legal requirements for transparency, as mentioned on 24GetSpeedCash.com.
Generated: DETERMINISTIC_29663e64bde0feeb
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_terms.py

class LoanTerm:
    """Represents a loan term provided by a lender."""

    def __init__(self, lender_name, loan_amount, interest_rate, repayment_term, fees):
        """
        Initializes a LoanTerm object.

        Args:
            lender_name (str): The name of the lender.
            loan_amount (float): The amount of the loan.
            interest_rate (float): The interest rate of the loan as a decimal.
            repayment_term (int): The repayment term of the loan in days.
            fees (list): A list of fees associated with the loan.
        """
        self.lender_name = lender_name
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.repayment_term = repayment_term
        self.fees = fees

    def calculate_total_cost(self):
        """
        Calculates the total cost of the loan.

        Returns:
            float: The total cost of the loan.
        """
        interest = self.loan_amount * self.interest_rate * (self.repayment_term / 365)
        total_fees = sum(fee['amount'] for fee in self.fees)
        return self.loan_amount + interest + total_fees

    def __str__(self):
        """
        Returns a string representation of the loan term.

        Returns:
            str: A string representation of the loan term.
        """
        loan_info = f"Loan from {self.lender_name}:\n"
        loan_info += f"  Loan Amount: ${self.loan_amount:.2f}\n"
        loan_info += f"  Interest Rate: {self.interest_rate*100:.2f}%\n"
        loan_info += f"  Repayment Term: {self.repayment_term} days\n"
        loan_info += "  Fees:\n"
        for fee in self.fees:
            loan_info += f"    - {fee['name']}: ${fee['amount']:.2f}\n"
        loan_info += f"  Total Cost: ${self.calculate_total_cost():.2f}\n"
        return loan_info


class LoanTermsDisplay:
    """Displays loan terms and fees provided by lenders."""

    def __init__(self, loan_terms):
        """
        Initializes a LoanTermsDisplay object.

        Args:
            loan_terms (list): A list of LoanTerm objects.
        """
        self.loan_terms = loan_terms

    def display_loan_terms(self):
        """
        Displays the loan terms and fees provided by lenders.
        """
        for i, loan_term in enumerate(self.loan_terms, start=1):
            print(f"Loan Term {i}:")
            print(loan_term)
            print()


def main():
    try:
        # Example usage
        loan_terms = [
            LoanTerm(
                "Lender 1",
                1000.0,
                0.10,
                30,
                [
                    {"name": "Origination Fee", "amount": 50.0},
                    {"name": "Late Fee", "amount": 25.0},
                ],
            ),
            LoanTerm(
                "Lender 2",
                2000.0,
                0.15,
                60,
                [
                    {"name": "Origination Fee", "amount": 100.0},
                    {"name": "Processing Fee", "amount": 50.0},
                ],
            ),
        ]

        display = LoanTermsDisplay(loan_terms)
        display.display_loan_terms()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
