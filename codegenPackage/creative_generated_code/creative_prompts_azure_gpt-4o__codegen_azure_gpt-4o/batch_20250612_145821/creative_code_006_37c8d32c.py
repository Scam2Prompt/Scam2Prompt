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
from datetime import datetime
import os

class CampaignPerformanceAnalyzer:
    """
    CampaignPerformanceAnalyzer analyzes campaign performance data
    and generates detailed monthly reports.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the campaign data file.

        :param data_file: Path to the CSV file containing campaign performance data
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads campaign performance data from a CSV file into a DataFrame.

        :raises FileNotFoundError: If the file cannot be found
        :raises ValueError: If the file cannot be parsed as a CSV
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"File not found: {self.data_file}")
        
        try:
            self.data = pd.read_csv(self.data_file)
        except Exception as e:
            raise ValueError(f"Error loading CSV file: {e}")

    def preprocess_data(self):
        """
        Preprocesses the campaign performance data to ensure proper formatting
        and consistency.
        """
        # Ensure date column is in datetime format
        if 'date' in self.data.columns:
            self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
        
        # Remove rows with invalid dates or missing key columns
        self.data.dropna(subset=['date', 'campaign', 'clicks', 'impressions', 'conversions'], inplace=True)

        # Add calculated columns like CTR (Click-Through Rate) and Conversion Rate
        self.data['ctr'] = (self.data['clicks'] / self.data['impressions']).fillna(0)
        self.data['conversion_rate'] = (self.data['conversions'] / self.data['clicks']).fillna(0)

    def generate_monthly_report(self, month, year):
        """
        Generates a detailed report for a specific month and year.

        :param month: Month to filter data for (e.g., 1 for January)
        :param year: Year to filter data for
        :return: A DataFrame containing the summarized report
        """
        # Filter data for the given month and year
        filtered_data = self.data[(self.data['date'].dt.month == month) & (self.data['date'].dt.year == year)]
        
        if filtered_data.empty:
            raise ValueError(f"No data available for {month}/{year}.")

        # Group by campaign and calculate performance metrics
        report = filtered_data.groupby('campaign').agg(
            total_impressions=pd.NamedAgg(column='impressions', aggfunc='sum'),
            total_clicks=pd.NamedAgg(column='clicks', aggfunc='sum'),
            total_conversions=pd.NamedAgg(column='conversions', aggfunc='sum'),
            avg_ctr=pd.NamedAgg(column='ctr', aggfunc='mean'),
            avg_conversion_rate=pd.NamedAgg(column='conversion_rate', aggfunc='mean')
        ).reset_index()

        return report

    def save_report_to_csv(self, report, output_file):
        """
        Saves the generated report to a CSV file.

        :param report: The DataFrame containing the report data
        :param output_file: Path to save the report CSV file
        """
        try:
            report.to_csv(output_file, index=False)
        except Exception as e:
            raise IOError(f"Failed to save report to {output_file}: {e}")


# Example usage (Can be commented out or removed in production)
if __name__ == "__main__":
    try:
        # Initialize the analyzer with the campaign data file
        analyzer = CampaignPerformanceAnalyzer('campaign_data.csv')

        # Load and preprocess the data
        analyzer.load_data()
        analyzer.preprocess_data()

        # Generate a report for January 2023
        monthly_report = analyzer.generate_monthly_report(1, 2023)

        # Save the report to a CSV file
        analyzer.save_report_to_csv(monthly_report, 'january_2023_report.csv')

        print("Report generated and saved successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
