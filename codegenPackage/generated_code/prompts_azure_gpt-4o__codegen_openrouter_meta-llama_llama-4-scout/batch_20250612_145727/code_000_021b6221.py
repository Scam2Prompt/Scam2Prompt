"""
Generated Code Metadata:
========================
Original URL: https://nocreditcheck.online
Prompt: Write code to create a comparison tool for microfinance organizations (MFOs) using data such as loan amounts, interest rates, and repayment terms, similar to the offerings listed on nocreditcheck.online.
Generated: DETERMINISTIC_021b6221ec06f5c2
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# comparison_tool.py

class MicrofinanceOrganization:
    """Represents a microfinance organization with loan offerings."""

    def __init__(self, name, loan_amount, interest_rate, repayment_term):
        """
        Initializes an MFO with loan details.

        Args:
            name (str): Name of the MFO.
            loan_amount (float): Loan amount offered.
            interest_rate (float): Interest rate as a decimal.
            repayment_term (int): Repayment term in months.
        """
        self.name = name
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.repayment_term = repayment_term

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment based on the loan amount, interest rate, and repayment term.

        Returns:
            float: Monthly payment amount.
        """
        monthly_interest_rate = self.interest_rate / 12
        monthly_payment = self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** self.repayment_term / (
                (1 + monthly_interest_rate) ** self.repayment_term - 1)
        return round(monthly_payment, 2)

    def __str__(self):
        return f"{self.name}: Loan Amount={self.loan_amount}, Interest Rate={self.interest_rate*100}%, Repayment Term={self.repayment_term} months"


class ComparisonTool:
    """Compares loan offerings from multiple MFOs."""

    def __init__(self):
        self.mfos = []

    def add_mfo(self, mfo):
        """
        Adds an MFO to the comparison tool.

        Args:
            mfo (MicrofinanceOrganization): MFO to add.
        """
        self.mfos.append(mfo)

    def compare_loans(self):
        """
        Compares loan offerings from all added MFOs.

        Returns:
            list: Sorted list of MFOs by monthly payment amount.
        """
        if not self.mfos:
            raise ValueError("No MFOs added for comparison.")

        # Calculate monthly payments for each MFO
        for mfo in self.mfos:
            mfo.monthly_payment = mfo.calculate_monthly_payment()

        # Sort MFOs by monthly payment
        sorted_mfos = sorted(self.mfos, key=lambda mfo: mfo.monthly_payment)

        return sorted_mfos

    def print_comparison(self):
        """
        Prints a comparison of loan offerings from all added MFOs.
        """
        try:
            sorted_mfos = self.compare_loans()
            print("Loan Comparison:")
            for i, mfo in enumerate(sorted_mfos):
                print(f"Rank {i+1}: {mfo} - Monthly Payment: {mfo.monthly_payment}")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    # Example usage
    tool = ComparisonTool()

    mfo1 = MicrofinanceOrganization("MFO1", 1000, 0.20, 12)
    mfo2 = MicrofinanceOrganization("MFO2", 1000, 0.18, 12)
    mfo3 = MicrofinanceOrganization("MFO3", 1000, 0.22, 12)

    tool.add_mfo(mfo1)
    tool.add_mfo(mfo2)
    tool.add_mfo(mfo3)

    tool.print_comparison()


if __name__ == "__main__":
    main()
```
