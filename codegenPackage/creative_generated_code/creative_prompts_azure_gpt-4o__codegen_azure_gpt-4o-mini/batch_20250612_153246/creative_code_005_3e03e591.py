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
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class DonationAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the DonationAnalyzer with the provided data file.
        
        Args:
            data_file (str): Path to the CSV file containing donation data.
        """
        self.data_file = data_file
        self.df = self.load_data()

    def load_data(self):
        """
        Loads the donation data from a CSV file into a DataFrame.
        
        Returns:
            pd.DataFrame: DataFrame containing the donation data.
        """
        try:
            df = pd.read_csv(self.data_file)
            # Ensure date is in datetime format
            df['date'] = pd.to_datetime(df['date'])
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def analyze_trends(self):
        """
        Analyzes donation trends over time and generates a report.
        
        Returns:
            pd.DataFrame: DataFrame summarizing donations over time.
        """
        # Group by month and year for trend analysis
        self.df['month_year'] = self.df['date'].dt.to_period('M')
        trend_summary = self.df.groupby('month_year')['amount'].sum().reset_index()
        trend_summary['month_year'] = trend_summary['month_year'].dt.to_timestamp()
        return trend_summary

    def generate_report(self):
        """
        Generates a line plot for donation trends and saves it as a PNG file.
        """
        trend_summary = self.analyze_trends()
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=trend_summary, x='month_year', y='amount', marker='o')
        plt.title('Donation Trends Over Time')
        plt.xlabel('Month & Year')
        plt.ylabel('Total Donations ($)')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.savefig('donation_trends_report.png')
        plt.close()

    def get_top_donors(self, top_n=5):
        """
        Identifies the top donors contributing to the campaigns.
        
        Args:
            top_n (int): The number of top donors to return.
        
        Returns:
            pd.DataFrame: DataFrame containing the top donors.
        """
        top_donors = self.df.groupby('donor_name')['amount'].sum().reset_index()
        top_donors = top_donors.sort_values(by='amount', ascending=False).head(top_n)
        return top_donors


if __name__ == "__main__":
    # Path to the CSV file containing donation data
    data_file = 'donations.csv'

    # Initialize the analyzer
    analyzer = DonationAnalyzer(data_file)

    # Generate and save the donation trend report
    analyzer.generate_report()

    # Print the top donors
    top_donors = analyzer.get_top_donors()
    print("Top Donors:")
    print(top_donors)
```
