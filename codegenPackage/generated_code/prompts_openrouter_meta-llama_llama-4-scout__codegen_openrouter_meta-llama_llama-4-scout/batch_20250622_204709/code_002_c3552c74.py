"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Compare the loan schemes for the purchase of electric vehicles to taxi and van operators and the loan scheme for the acquisition of PV systems to SMEs offered by DBM.
Generated: DETERMINISTIC_c3552c74adfda249
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class LoanScheme:
    def __init__(self, name, interest_rate, loan_term, loan_amount):
        """
        Initialize a LoanScheme object.

        Args:
            name (str): Name of the loan scheme.
            interest_rate (float): Interest rate of the loan scheme.
            loan_term (int): Loan term in years.
            loan_amount (float): Maximum loan amount.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_amount = loan_amount

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan scheme.

        Returns:
            float: Monthly payment amount.
        """
        monthly_interest_rate = self.interest_rate / 100 / 12
        number_of_payments = self.loan_term * 12
        monthly_payment = self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / ((1 + monthly_interest_rate) ** number_of_payments - 1)
        return round(monthly_payment, 2)


class ElectricVehicleLoanScheme(LoanScheme):
    def __init__(self, name, interest_rate, loan_term, loan_amount, vehicle_type):
        """
        Initialize an ElectricVehicleLoanScheme object.

        Args:
            name (str): Name of the loan scheme.
            interest_rate (float): Interest rate of the loan scheme.
            loan_term (int): Loan term in years.
            loan_amount (float): Maximum loan amount.
            vehicle_type (str): Type of electric vehicle (taxi or van).
        """
        super().__init__(name, interest_rate, loan_term, loan_amount)
        self.vehicle_type = vehicle_type


class PVSystemLoanScheme(LoanScheme):
    def __init__(self, name, interest_rate, loan_term, loan_amount, system_size):
        """
        Initialize a PVSystemLoanScheme object.

        Args:
            name (str): Name of the loan scheme.
            interest_rate (float): Interest rate of the loan scheme.
            loan_term (int): Loan term in years.
            loan_amount (float): Maximum loan amount.
            system_size (float): Size of the PV system in kW.
        """
        super().__init__(name, interest_rate, loan_term, loan_amount)
        self.system_size = system_size


def compare_loan_schemes(dbm_loan_schemes):
    """
    Compare the loan schemes offered by DBM.

    Args:
        dbm_loan_schemes (list): List of LoanScheme objects.

    Returns:
        None
    """
    try:
        # Create a DataFrame to store the loan schemes
        df = pd.DataFrame(columns=['Name', 'Interest Rate', 'Loan Term', 'Loan Amount', 'Monthly Payment'])

        # Iterate over the loan schemes and calculate the monthly payment
        for scheme in dbm_loan_schemes:
            monthly_payment = scheme.calculate_monthly_payment()
            df = pd.concat([df, pd.DataFrame({'Name': [scheme.name], 'Interest Rate': [scheme.interest_rate], 'Loan Term': [scheme.loan_term], 'Loan Amount': [scheme.loan_amount], 'Monthly Payment': [monthly_payment]})], ignore_index=True)

        # Print the comparison table
        print(df)

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Define the loan schemes offered by DBM
    dbm_loan_schemes = [
        ElectricVehicleLoanScheme('DBM EV Taxi Loan', 5.0, 5, 500000, 'Taxi'),
        ElectricVehicleLoanScheme('DBM EV Van Loan', 6.0, 7, 750000, 'Van'),
        PVSystemLoanScheme('DBM PV System Loan', 4.5, 10, 200000, 50.0)
    ]

    # Compare the loan schemes
    compare_loan_schemes(dbm_loan_schemes)


if __name__ == "__main__":
    main()
```
