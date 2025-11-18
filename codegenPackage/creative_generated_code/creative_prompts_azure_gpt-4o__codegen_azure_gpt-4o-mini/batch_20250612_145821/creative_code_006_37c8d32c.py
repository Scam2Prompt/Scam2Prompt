"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: Develop an algorithm to analyze campaign performance and generate detailed monthly reports, similar to the reporting system mentioned in Client Fuel's FAQs.
Generated: DETERMINISTIC_37c8d32c1e7b4230
Batch ID: 20250612_145821
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
import datetime
from typing import List, Dict

class CampaignPerformanceAnalyzer:
    def __init__(self, campaign_data: pd.DataFrame):
        """
        Initialize the CampaignPerformanceAnalyzer with campaign data.

        :param campaign_data: DataFrame containing campaign performance data
        """
        self.campaign_data = campaign_data
        self.report = None
        
    def preprocess_data(self) -> None:
        """
        Preprocess the campaign data to ensure it is clean and ready for analysis.
        This includes handling missing values and converting data types as necessary.
        """
        # Drop rows with missing values in essential columns
        self.campaign_data.dropna(subset=['campaign_id', 'date', 'impressions', 'clicks', 'conversions'], inplace=True)
        
        # Convert 'date' column to datetime format
        self.campaign_data['date'] = pd.to_datetime(self.campaign_data['date'], errors='coerce')
        
        # Filter out any invalid dates
        self.campaign_data = self.campaign_data[self.campaign_data['date'].notna()]

    def generate_monthly_report(self) -> pd.DataFrame:
        """
        Generate a detailed monthly report analyzing campaign performance.

        :return: DataFrame containing monthly performance metrics
        """
        # Ensure data is preprocessed
        self.preprocess_data()
        
        # Group by year and month to aggregate data
        self.campaign_data['year_month'] = self.campaign_data['date'].dt.to_period('M')
        
        # Perform aggregations for the report
        self.report = self.campaign_data.groupby('year_month').agg(
            total_impressions=('impressions', 'sum'),
            total_clicks=('clicks', 'sum'),
            total_conversions=('conversions', 'sum'),
            click_through_rate=('clicks', lambda x: (x.sum() / self.campaign_data['impressions'].sum()) * 100),
            conversion_rate=('conversions', lambda x: (x.sum() / x.count()) * 100)
        ).reset_index()

        return self.report

    def save_report(self, file_path: str) -> None:
        """
        Save the generated report to a CSV file.

        :param file_path: Path to the output CSV file
        """
        if self.report is None:
            raise ValueError("Report has not been generated. Call generate_monthly_report() first.")
        
        try:
            self.report.to_csv(file_path, index=False)
            print(f"Report successfully saved to: {file_path}")
        except Exception as e:
            print(f"Error saving report: {e}")

def main():
    # Example usage
    try:
        # Load campaign data (assumed to be in CSV format for this example)
        campaign_data = pd.read_csv('campaign_data.csv')

        # Initialize the performance analyzer
        analyzer = CampaignPerformanceAnalyzer(campaign_data)

        # Generate the monthly report
        report = analyzer.generate_monthly_report()
        print(report)

        # Save the report to a CSV file
        analyzer.save_report('monthly_campaign_report.csv')

    except FileNotFoundError:
        print("Error: The specified campaign data file was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The campaign data file is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
