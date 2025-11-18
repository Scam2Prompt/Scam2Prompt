"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Create a script to analyze partner profitability based on Vertiv's margin-rich IT infrastructure portfolio and incentive rewards program.
Generated: DETERMINISTIC_b5a690cb984fce97
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class PartnerProfitabilityAnalyzer:
    """
    A class to analyze partner profitability based on Vertiv's margin-rich IT infrastructure portfolio
    and incentive rewards program.
    """

    def __init__(self, sales_data: pd.DataFrame, incentive_data: pd.DataFrame):
        """
        Initializes the PartnerProfitabilityAnalyzer with sales and incentive data.

        Parameters:
        sales_data (pd.DataFrame): DataFrame containing sales data with partner details and revenue.
        incentive_data (pd.DataFrame): DataFrame containing incentive data related to partners.
        """
        self.sales_data = sales_data
        self.incentive_data = incentive_data

    def validate_data(self):
        """
        Validates the input data for required columns.
        Raises ValueError if required columns are missing.
        """
        required_sales_columns = {'partner_id', 'revenue', 'cost'}
        required_incentive_columns = {'partner_id', 'incentive'}

        if not required_sales_columns.issubset(self.sales_data.columns):
            raise ValueError(f"Sales data must contain the following columns: {required_sales_columns}")

        if not required_incentive_columns.issubset(self.incentive_data.columns):
            raise ValueError(f"Incentive data must contain the following columns: {required_incentive_columns}")

    def calculate_profitability(self) -> pd.DataFrame:
        """
        Calculates profitability for each partner.

        Returns:
        pd.DataFrame: A DataFrame containing partner profitability details.
        """
        self.validate_data()

        # Calculate profit and total earnings (profit + incentives)
        self.sales_data['profit'] = self.sales_data['revenue'] - self.sales_data['cost']
        self.sales_data['total_earnings'] = self.sales_data['profit'] + self.sales_data['partner_id'].map(
            self.incentive_data.set_index('partner_id')['incentive'].fillna(0)
        )

        # Group by partner_id and aggregate results
        profitability_summary = self.sales_data.groupby('partner_id').agg(
            total_revenue=('revenue', 'sum'),
            total_cost=('cost', 'sum'),
            total_profit=('profit', 'sum'),
            total_incentives=('partner_id', lambda x: self.incentive_data[self.incentive_data['partner_id'].isin(x)]['incentive'].sum()),
            total_earnings=('total_earnings', 'sum')
        ).reset_index()

        return profitability_summary

    def save_results(self, results: pd.DataFrame, file_path: str):
        """
        Saves the profitability results to a CSV file.

        Parameters:
        results (pd.DataFrame): DataFrame containing the profitability results.
        file_path (str): The file path where the results will be saved.
        """
        try:
            results.to_csv(file_path, index=False)
            print(f"Results successfully saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving results: {e}")

def main():
    # Sample data for demonstration
    sales_data = pd.DataFrame({
        'partner_id': [1, 2, 1, 2, 3],
        'revenue': [1000, 2000, 1500, 2500, 3000],
        'cost': [600, 1200, 800, 1400, 2000]
    })

    incentive_data = pd.DataFrame({
        'partner_id': [1, 2, 3],
        'incentive': [100, 200, 300]
    })

    analyzer = PartnerProfitabilityAnalyzer(sales_data, incentive_data)
    profitability_results = analyzer.calculate_profitability()
    analyzer.save_results(profitability_results, 'partner_profitability.csv')

if __name__ == "__main__":
    main()
```
