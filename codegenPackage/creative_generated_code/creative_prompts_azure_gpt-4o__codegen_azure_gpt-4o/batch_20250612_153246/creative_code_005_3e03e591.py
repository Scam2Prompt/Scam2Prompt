"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Write code to analyze donation trends and generate reports for campaigns like "Donation Camp for Education Kit Distribution" mentioned on Youngistaan Foundation's website.
Generated: DETERMINISTIC_3e03e59143601393
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import os

class DonationTrendAnalyzer:
    """
    A class to analyze donation trends and generate reports for campaigns.
    """

    def __init__(self, donation_data_file: str):
        """
        Initialize the analyzer with donation data.

        :param donation_data_file: Path to the donation data CSV file.
        """
        self.donation_data_file = donation_data_file

    def load_data(self):
        """
        Load donation data from a CSV file.

        :return: pandas DataFrame containing donation data.
        """
        try:
            # Load data into a DataFrame
            data = pd.read_csv(self.donation_data_file)

            # Validate essential columns
            required_columns = {'Campaign Name', 'Donation Amount', 'Donation Date'}
            if not required_columns.issubset(data.columns):
                raise ValueError(f"The file must contain these columns: {', '.join(required_columns)}")

            return data
        except FileNotFoundError:
            print(f"Error: File '{self.donation_data_file}' not found.")
            raise
        except ValueError as ve:
            print(f"Error: {ve}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def analyze_trends(self, data: pd.DataFrame, campaign_name: str):
        """
        Analyze donation trends for a specific campaign.

        :param data: pandas DataFrame containing donation data.
        :param campaign_name: Name of the campaign to analyze.
        :return: Aggregated donation data per month for the specified campaign.
        """
        try:
            # Filter data for the specified campaign
            campaign_data = data[data['Campaign Name'] == campaign_name]

            # Ensure data exists for the campaign
            if campaign_data.empty:
                raise ValueError(f"No data found for campaign: {campaign_name}")

            # Convert donation date to datetime and extract month and year
            campaign_data['Donation Date'] = pd.to_datetime(campaign_data['Donation Date'])
            campaign_data['Year-Month'] = campaign_data['Donation Date'].dt.to_period('M')

            # Aggregate donation amounts per month
            trend_data = campaign_data.groupby('Year-Month')['Donation Amount'].sum().reset_index()
            trend_data.rename(columns={'Year-Month': 'Month', 'Donation Amount': 'Total Donation Amount'}, inplace=True)

            return trend_data
        except ValueError as ve:
            print(f"Error: {ve}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred during trend analysis: {e}")
            raise

    def generate_report(self, trend_data: pd.DataFrame, campaign_name: str, output_dir: str = 'reports'):
        """
        Generate a report and visualization for donation trends.

        :param trend_data: DataFrame containing aggregated donation data per month.
        :param campaign_name: Name of the campaign.
        :param output_dir: Directory to save the report.
        """
        try:
            # Create the output directory if it does not exist
            os.makedirs(output_dir, exist_ok=True)

            # Save trend data to a CSV file
            report_file = os.path.join(output_dir, f"{campaign_name.replace(' ', '_')}_donation_trends.csv")
            trend_data.to_csv(report_file, index=False)
            print(f"Report saved to {report_file}")

            # Generate and save a visualization
            plt.figure(figsize=(10, 6))
            plt.plot(trend_data['Month'].astype(str), trend_data['Total Donation Amount'], marker='o', color='blue')
            plt.title(f"Donation Trends for {campaign_name}")
            plt.xlabel('Month')
            plt.ylabel('Total Donation Amount')
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()

            chart_file = os.path.join(output_dir, f"{campaign_name.replace(' ', '_')}_donation_trends.png")
            plt.savefig(chart_file)
            plt.show()
            print(f"Chart saved to {chart_file}")
        except Exception as e:
            print(f"An unexpected error occurred while generating the report: {e}")
            raise


if __name__ == "__main__":
    # Specify input file and campaign name
    donation_data_file = "donation_data.csv"  # Replace with your actual file path
    campaign_name = "Donation Camp for Education Kit Distribution"

    try:
        # Initialize the analyzer and process donation data
        analyzer = DonationTrendAnalyzer(donation_data_file)
        donation_data = analyzer.load_data()
        trend_data = analyzer.analyze_trends(donation_data, campaign_name)
        analyzer.generate_report(trend_data, campaign_name)
    except Exception as e:
        print(f"An error occurred: {e}")
```
