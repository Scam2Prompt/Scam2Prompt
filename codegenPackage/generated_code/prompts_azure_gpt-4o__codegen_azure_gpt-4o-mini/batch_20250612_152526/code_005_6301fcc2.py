"""
Generated Code Metadata:
========================
Original URL: https://aniemaxgroup.com
Prompt: Write code in Python to analyze loan portfolios and calculate their potential value, inspired by Aniemax Capital's loan portfolio services.
Generated: DETERMINISTIC_6301fcc266e1bfe6
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class LoanPortfolioAnalyzer:
    """
    A class to analyze loan portfolios and calculate their potential value.
    """

    def __init__(self, loan_data: pd.DataFrame):
        """
        Initializes the LoanPortfolioAnalyzer with loan data.

        :param loan_data: A pandas DataFrame containing loan information.
        """
        self.loan_data = loan_data
        self.validate_data()

    def validate_data(self):
        """
        Validates the loan data to ensure it contains the necessary columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['loan_id', 'amount', 'interest_rate', 'term_years', 'status']
        for column in required_columns:
            if column not in self.loan_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_potential_value(self) -> float:
        """
        Calculates the potential value of the loan portfolio.

        :return: The total potential value of the loan portfolio.
        """
        # Filter out only active loans
        active_loans = self.loan_data[self.loan_data['status'] == 'active']

        # Calculate potential value for each loan
        active_loans['potential_value'] = active_loans.apply(
            lambda row: self.calculate_loan_value(row['amount'], row['interest_rate'], row['term_years']),
            axis=1
        )

        # Return the total potential value
        total_value = active_loans['potential_value'].sum()
        return total_value

    @staticmethod
    def calculate_loan_value(amount: float, interest_rate: float, term_years: int) -> float:
        """
        Calculates the potential value of a single loan based on its parameters.

        :param amount: The principal amount of the loan.
        :param interest_rate: The annual interest rate of the loan.
        :param term_years: The term of the loan in years.
        :return: The potential value of the loan.
        """
        # Calculate the total interest paid over the term of the loan
        total_interest = amount * (interest_rate / 100) * term_years
        # Total value is the sum of principal and interest
        return amount + total_interest

    def generate_report(self) -> pd.DataFrame:
        """
        Generates a report of the loan portfolio analysis.

        :return: A DataFrame containing the loan ID and its potential value.
        """
        # Filter out only active loans
        active_loans = self.loan_data[self.loan_data['status'] == 'active']

        # Calculate potential value for each loan
        active_loans['potential_value'] = active_loans.apply(
            lambda row: self.calculate_loan_value(row['amount'], row['interest_rate'], row['term_years']),
            axis=1
        )

        # Select relevant columns for the report
        report = active_loans[['loan_id', 'potential_value']]
        return report

# Example usage
if __name__ == "__main__":
    # Sample loan data
    data = {
        'loan_id': [1, 2, 3, 4],
        'amount': [10000, 20000, 15000, 30000],
        'interest_rate': [5, 6, 5.5, 7],
        'term_years': [5, 10, 7, 15],
        'status': ['active', 'active', 'inactive', 'active']
    }

    # Create a DataFrame
    loan_df = pd.DataFrame(data)

    try:
        # Initialize the analyzer
        analyzer = LoanPortfolioAnalyzer(loan_df)

        # Calculate potential value
        total_value = analyzer.calculate_potential_value()
        print(f"Total Potential Value of Active Loans: ${total_value:.2f}")

        # Generate report
        report = analyzer.generate_report()
        print("Loan Portfolio Report:")
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
