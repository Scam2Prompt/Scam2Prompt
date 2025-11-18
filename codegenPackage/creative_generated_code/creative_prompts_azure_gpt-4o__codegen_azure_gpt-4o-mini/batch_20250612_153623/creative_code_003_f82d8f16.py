"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Develop a Python program that calculates and compares the total cost of different types of loans (personal, consignado, with collateral, and specific financing) based on user input for loan amount, interest rate, and repayment period.
Generated: DETERMINISTIC_f82d8f1693d6e87b
Batch ID: 20250612_153623
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
    A class to represent a loan and calculate the total cost based on type.
    """

    def __init__(self, amount: float, interest_rate: float, repayment_period: int):
        """
        Initialize the loan with amount, interest rate, and repayment period.

        :param amount: The principal loan amount
        :param interest_rate: Annual interest rate (as a percentage)
        :param repayment_period: Repayment period in months
        """
        self.amount = amount
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.repayment_period = repayment_period

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of the loan.

        :return: Total cost of the loan including interest
        """
        total_cost = self.amount * (1 + self.interest_rate * self.repayment_period / 12)
        return total_cost


def get_loan_type():
    """
    Prompt user to select a type of loan.
    
    :return: Selected loan type as string
    """
    print("Select loan type:")
    print("1. Personal Loan")
    print("2. Consignado Loan")
    print("3. Loan with Collateral")
    print("4. Specific Financing")

    while True:
        loan_type = input("Enter the loan type number (1-4): ")
        if loan_type in ['1', '2', '3', '4']:
            return loan_type
        print("Invalid selection. Please enter a number between 1 and 4.")


def main():
    """
    Main function to execute loan calculation based on user input.
    """
    try:
        # Get user input for loan details
        amount = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        repayment_period = int(input("Enter the repayment period in months: "))

        # Get the loan type from user input
        loan_type = get_loan_type()

        # Create a loan object
        loan = Loan(amount, interest_rate, repayment_period)

        # Calculate total cost
        total_cost = loan.calculate_total_cost()

        # Output results based on loan type
        loan_types = {
            '1': "Personal Loan",
            '2': "Consignado Loan",
            '3': "Loan with Collateral",
            '4': "Specific Financing"
        }
        print(f"\nTotal cost of {loan_types[loan_type]}: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error in input: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
