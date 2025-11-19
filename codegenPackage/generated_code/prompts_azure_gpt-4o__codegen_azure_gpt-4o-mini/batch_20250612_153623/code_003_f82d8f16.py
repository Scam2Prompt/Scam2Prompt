"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Develop a Python program that calculates and compares the total cost of different types of loans (personal, consignado, with collateral, and specific financing) based on user input for loan amount, interest rate, and repayment period.
Generated: DETERMINISTIC_f82d8f1693d6e87b
Batch ID: 20250612_153623
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
    A class to represent a loan and calculate its total cost.
    """

    def __init__(self, amount: float, interest_rate: float, years: int):
        """
        Initializes the Loan instance.

        :param amount: The principal amount of the loan.
        :param interest_rate: The annual interest rate (as a percentage).
        :param years: The repayment period in years.
        """
        self.amount = amount
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the loan including interest.

        :return: The total cost of the loan.
        """
        total_cost = self.amount * (1 + self.interest_rate * self.years)
        return total_cost


def get_loan_details(loan_type: str) -> tuple:
    """
    Prompts the user for loan details based on the loan type.

    :param loan_type: The type of loan for which details are being collected.
    :return: A tuple containing the loan amount, interest rate, and repayment period.
    """
    try:
        amount = float(input(f"Enter the loan amount for {loan_type}: "))
        interest_rate = float(input(f"Enter the annual interest rate (in %): "))
        years = int(input(f"Enter the repayment period in years: "))
        return amount, interest_rate, years
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_loan_details(loan_type)


def main():
    """
    Main function to execute the loan comparison program.
    """
    loan_types = ["Personal Loan", "Consigned Loan", "Collateral Loan", "Specific Financing"]
    loans = {}

    # Collect loan details for each type
    for loan_type in loan_types:
        loans[loan_type] = get_loan_details(loan_type)

    # Calculate and display total costs for each loan type
    print("\nTotal Loan Costs:")
    for loan_type, details in loans.items():
        loan = Loan(*details)
        total_cost = loan.calculate_total_cost()
        print(f"{loan_type}: Total Cost = ${total_cost:.2f}")


if __name__ == "__main__":
    main()
```
