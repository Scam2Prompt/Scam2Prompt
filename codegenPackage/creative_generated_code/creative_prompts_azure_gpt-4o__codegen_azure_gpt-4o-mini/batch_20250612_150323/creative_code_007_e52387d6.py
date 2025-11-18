"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensee.io
Prompt: Write Python code to perform multi-dimensional analytics on credit portfolio exposures, including misbooking tracking, using Opensee's real-time data aggregation tools.
Generated: DETERMINISTIC_e52387d680d67d76
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class CreditPortfolioAnalytics:
    """
    A class to perform multi-dimensional analytics on credit portfolio exposures.
    """

    def __init__(self, data_source):
        """
        Initializes the CreditPortfolioAnalytics with a data source.

        :param data_source: A Pandas DataFrame containing credit exposure data.
        """
        self.data_source = data_source

    def validate_data(self):
        """
        Validates the data for required columns and correct data types.

        Raises:
            ValueError: If required columns are missing or data types are incorrect.
        """
        required_columns = ['exposure', 'risk_rating', 'counterparty', 'misbooking']
        for column in required_columns:
            if column not in self.data_source.columns:
                raise ValueError(f"Missing required column: {column}")

        if not pd.api.types.is_numeric_dtype(self.data_source['exposure']):
            raise ValueError("Column 'exposure' must be numeric.")

    def calculate_total_exposure(self):
        """
        Calculates the total exposure in the credit portfolio.

        :return: Total exposure as a float.
        """
        total_exposure = self.data_source['exposure'].sum()
        return total_exposure

    def track_misbookings(self):
        """
        Tracks the number and amount of misbooked entries in the portfolio.

        :return: DataFrame summarizing misbooked entries.
        """
        misbooked_entries = self.data_source[self.data_source['misbooking'] == True]
        misbooking_summary = misbooked_entries.groupby('counterparty')['exposure'].agg(['count', 'sum']).reset_index()
        misbooking_summary.columns = ['Counterparty', 'Misbooking Count', 'Total Misbooking Exposure']
        return misbooking_summary

    def aggregate_by_risk_rating(self):
        """
        Aggregates exposures by risk rating.

        :return: DataFrame containing aggregated exposures by risk rating.
        """
        risk_aggregation = self.data_source.groupby('risk_rating')['exposure'].sum().reset_index()
        risk_aggregation.columns = ['Risk Rating', 'Total Exposure']
        return risk_aggregation

    def run_analytics(self):
        """
        Runs the complete analytics process: validation, total exposure, misbooking tracking, and risk aggregation.

        :return: A dictionary containing all analytics results.
        """
        results = {}
        try:
            self.validate_data()
            results['Total Exposure'] = self.calculate_total_exposure()
            results['Misbooking Summary'] = self.track_misbookings()
            results['Risk Aggregation'] = self.aggregate_by_risk_rating()
        except ValueError as e:
            return {"Error": str(e)}
        except Exception as e:
            return {"Error": "An unexpected error occurred: " + str(e)}

        return results


# Example usage
if __name__ == "__main__":
    # Simulated data source
    data = {
        'exposure': [100000, 200000, 300000, 150000, 250000, 50000],
        'risk_rating': ['A', 'B', 'A', 'C', 'B', 'A'],
        'counterparty': ['Client1', 'Client2', 'Client1', 'Client3', 'Client2', 'Client4'],
        'misbooking': [False, True, False, True, False, False]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Initialize the analytics class with the DataFrame
    analytics = CreditPortfolioAnalytics(df)

    # Run analytics and print the results
    analytics_results = analytics.run_analytics()
    print(analytics_results)
```
