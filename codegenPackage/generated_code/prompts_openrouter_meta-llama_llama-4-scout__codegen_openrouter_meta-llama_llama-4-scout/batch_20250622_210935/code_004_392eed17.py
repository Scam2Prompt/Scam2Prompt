"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Write a code snippet to compare the total cost of different loan options, considering the CET (Custo Efetivo Total) and interest rates, to help an individual choose the best loan for their needs.
Generated: DETERMINISTIC_392eed1749510b76
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_comparator.py

class Loan:
    """Represents a loan option with its characteristics."""

    def __init__(self, name, principal, interest_rate, cet, loan_term):
        """
        Initializes a Loan object.

        Args:
            name (str): Name of the loan.
            principal (float): The initial amount borrowed.
            interest_rate (float): The annual interest rate as a decimal.
            cet (float): The Custo Efetivo Total (CET) as a decimal.
            loan_term (int): The loan term in years.
        """
        self.name = name
        self.principal = principal
        self.interest_rate = interest_rate
        self.cet = cet
        self.loan_term = loan_term

    def calculate_total_cost(self):
        """
        Calculates the total cost of the loan.

        Returns:
            float: The total cost of the loan.
        """
        # Calculate the total interest paid over the loan term
        total_interest = self.principal * self.interest_rate * self.loan_term
        # Add the CET to the total interest
        total_cost = self.principal + total_interest + (self.principal * self.cet)
        return total_cost


def compare_loan_options(loans):
    """
    Compares the total cost of different loan options.

    Args:
        loans (list[Loan]): A list of Loan objects.

    Returns:
        dict: A dictionary with loan names as keys and their total costs as values.
    """
    try:
        # Initialize an empty dictionary to store the results
        results = {}
        # Iterate over each loan option
        for loan in loans:
            # Calculate the total cost of the loan
            total_cost = loan.calculate_total_cost()
            # Store the result in the dictionary
            results[loan.name] = total_cost
        return results
    except Exception as e:
        # Handle any exceptions that occur during the calculation
        print(f"An error occurred: {e}")
        return None


def main():
    # Define loan options
    loan1 = Loan("Loan A", 10000, 0.08, 0.02, 5)
    loan2 = Loan("Loan B", 10000, 0.07, 0.03, 5)
    loan3 = Loan("Loan C", 10000, 0.09, 0.01, 5)

    # Compare loan options
    loans = [loan1, loan2, loan3]
    results = compare_loan_options(loans)

    # Print the results
    if results:
        print("Loan Comparison Results:")
        for loan, total_cost in results.items():
            print(f"{loan}: ${total_cost:.2f}")
        # Find the best loan option (the one with the lowest total cost)
        best_loan = min(results, key=results.get)
        print(f"\nThe best loan option is: {best_loan}")


if __name__ == "__main__":
    main()
```
