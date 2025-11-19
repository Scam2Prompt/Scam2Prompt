"""
Generated Code Metadata:
========================
Original URL: https://origineth.us
Prompt: What are the benefits and requirements for obtaining a Crédit Agricole loan for a small business, and how does it differ from a personal loan?
Generated: DETERMINISTIC_de6f15a789140f12
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Loan:
    """
    A class to represent a loan.

    Attributes:
    ----------
    loan_type : str
        Type of the loan (e.g., 'business', 'personal')
    amount : float
        Amount of the loan
    interest_rate : float
        Interest rate of the loan
    term_years : int
        Term of the loan in years
    """

    def __init__(self, loan_type, amount, interest_rate, term_years):
        """
        Initializes the Loan class with the given parameters.

        Parameters:
        ----------
        loan_type : str
            Type of the loan
        amount : float
            Amount of the loan
        interest_rate : float
            Interest rate of the loan
        term_years : int
            Term of the loan in years
        """
        self.loan_type = loan_type
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_years = term_years

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan.

        Returns:
        -------
        float
            The monthly payment amount
        """
        try:
            monthly_rate = self.interest_rate / 100 / 12
            number_of_payments = self.term_years * 12
            monthly_payment = (self.amount * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Interest rate cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the monthly payment: {e}")

    def get_loan_info(self):
        """
        Get a summary of the loan information.

        Returns:
        -------
        dict
            A dictionary containing loan details
        """
        return {
            "Loan Type": self.loan_type,
            "Amount": self.amount,
            "Interest Rate": self.interest_rate,
            "Term (Years)": self.term_years,
            "Monthly Payment": self.calculate_monthly_payment()
        }


def main():
    """
    Main function to demonstrate the Loan class functionality.
    """
    try:
        # Example of a business loan
        business_loan = Loan(loan_type='business', amount=50000, interest_rate=5.0, term_years=10)
        print("Business Loan Info:")
        print(business_loan.get_loan_info())

        # Example of a personal loan
        personal_loan = Loan(loan_type='personal', amount=20000, interest_rate=4.5, term_years=5)
        print("\nPersonal Loan Info:")
        print(personal_loan.get_loan_info())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
