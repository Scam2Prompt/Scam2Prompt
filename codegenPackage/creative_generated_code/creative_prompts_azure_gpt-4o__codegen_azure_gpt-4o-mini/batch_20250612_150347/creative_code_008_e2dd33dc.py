"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Write code to generate annual tax reports for businesses, incorporating optimization techniques described by Arbitum Consulting.
Generated: DETERMINISTIC_e2dd33dc18f929dd
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict

class TaxReportGenerator:
    """
    A class to generate annual tax reports for businesses.

    Attributes:
        business_data (pd.DataFrame): DataFrame containing business transactions.
    """

    def __init__(self, business_data: pd.DataFrame):
        """
        Initializes the TaxReportGenerator with business data.

        Args:
            business_data (pd.DataFrame): A DataFrame containing business transaction data.
        """
        self.business_data = business_data

    def validate_data(self) -> None:
        """
        Validates the business data for necessary columns.

        Raises:
            ValueError: If required columns are missing.
        """
        required_columns = ['date', 'amount', 'category']
        for column in required_columns:
            if column not in self.business_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def filter_transactions(self, year: int) -> pd.DataFrame:
        """
        Filters transactions for the given year.

        Args:
            year (int): The year for which to filter transactions.

        Returns:
            pd.DataFrame: Filtered DataFrame containing transactions for the specified year.
        """
        return self.business_data[self.business_data['date'].dt.year == year]

    def calculate_taxable_income(self, transactions: pd.DataFrame) -> float:
        """
        Calculates the total taxable income from filtered transactions.

        Args:
            transactions (pd.DataFrame): DataFrame containing filtered transactions.

        Returns:
            float: Total taxable income.
        """
        # Assume income is represented by 'amount' with a positive value
        return transactions[transactions['amount'] > 0]['amount'].sum()

    def generate_report(self, year: int) -> Dict[str, float]:
        """
        Generates the tax report for the given year.

        Args:
            year (int): The year for which to generate the report.

        Returns:
            dict: A dictionary containing the financial summary for the year.
        """
        self.validate_data()
        transactions = self.filter_transactions(year)

        if transactions.empty:
            return {"message": "No transactions found for this year."}

        taxable_income = self.calculate_taxable_income(transactions)

        report = {
            "year": year,
            "total_transactions": transactions.shape[0],
            "taxable_income": taxable_income,
        }

        return report

def main():
    # Sample data creation for demonstration
    data = {
        'date': pd.date_range(start='2022-01-01', periods=365, freq='D'),
        'amount': [100 + (i % 10) * 10 for i in range(365)],
        'category': ['income'] * 365
    }
    
    # Create a DataFrame
    business_data = pd.DataFrame(data)
    
    # Convert string dates to datetime
    business_data['date'] = pd.to_datetime(business_data['date'])

    # Initialize the report generator
    report_generator = TaxReportGenerator(business_data)

    # Generate report for a specific year
    try:
        report = report_generator.generate_report(year=2022)
        print(report)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
