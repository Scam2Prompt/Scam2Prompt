"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aniemaxgroup.com
Prompt: Write code in Python to analyze loan portfolios and calculate their potential value, inspired by Aniemax Capital's loan portfolio services.
Generated: DETERMINISTIC_6301fcc266e1bfe6
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class LoanPortfolioAnalyzer:
    """
    A class to analyze loan portfolios and calculate their potential value.
    """

    def __init__(self, data_frame: pd.DataFrame):
        """
        Initializes the LoanPortfolioAnalyzer with a DataFrame containing loan data.

        :param data_frame: A DataFrame with at least 'loan_amount', 'interest_rate', 
                           'term_years', and 'default_probability' columns.
        """
        self.data_frame = data_frame

    def validate_data(self):
        """
        Validates the DataFrame to ensure required columns are present and contain valid data.

        :raises ValueError: If any required column is missing or contains invalid data.
        """
        required_columns = ['loan_amount', 'interest_rate', 'term_years', 'default_probability']
        for column in required_columns:
            if column not in self.data_frame.columns:
                raise ValueError(f"Missing required column: {column}")

            if not pd.api.types.is_numeric_dtype(self.data_frame[column]):
                raise ValueError(f"Column '{column}' must be numeric.")

    def calculate_present_value(self, loan_amount: float, interest_rate: float, term_years: int) -> float:
        """
        Calculates the present value of a loan using the formula for the present value of an annuity.

        :param loan_amount: The amount of the loan.
        :param interest_rate: The annual interest rate (as a decimal).
        :param term_years: The term of the loan in years.

        :return: The present value of the loan.
        """
        if interest_rate == 0:
            return loan_amount / (1 + 0.01) ** term_years  # Avoid division by zero

        return loan_amount * ((1 - (1 + interest_rate) ** -term_years) / interest_rate)

    def analyze_portfolio(self) -> pd.DataFrame:
        """
        Analyzes the loan portfolio and calculates the potential value of each loan.

        :return: A DataFrame with loan details and their calculated present values.
        """
        self.validate_data()
        
        # Calculate potential value for each loan
        self.data_frame['potential_value'] = self.data_frame.apply(
            lambda row: self.calculate_present_value(
                loan_amount=row['loan_amount'],
                interest_rate=row['interest_rate'] / 100,  # Convert percentage to decimal
                term_years=row['term_years']
            ),
            axis=1
        )

        return self.data_frame[['loan_amount', 'interest_rate', 'term_years', 'default_probability', 'potential_value']]

# Example usage:
if __name__ == "__main__":
    # Sample loan data for analysis
    loan_data = {
        'loan_amount': [10000, 25000, 50000],
        'interest_rate': [5, 7.5, 6],
        'term_years': [5, 10, 15],
        'default_probability': [0.02, 0.05, 0.01]
    }

    # Create a DataFrame
    loans_df = pd.DataFrame(loan_data)

    # Initialize the LoanPortfolioAnalyzer
    analyzer = LoanPortfolioAnalyzer(loans_df)

    # Analyze the portfolio and get the results
    try:
        results = analyzer.analyze_portfolio()
        print(results)
    except ValueError as e:
        print(f"Error: {e}")
```
