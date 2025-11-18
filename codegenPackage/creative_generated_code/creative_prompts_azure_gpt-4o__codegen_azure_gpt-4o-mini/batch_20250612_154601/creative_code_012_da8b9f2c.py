"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Generate Python code to track and analyze Pay Per Click (PPC) marketing campaigns, incorporating the strategies outlined in Solutech System's Google Ads services.
Generated: DETERMINISTIC_da8b9f2cace07e6e
Batch ID: 20250612_154601
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
import matplotlib.pyplot as plt

class PPCampaignTracker:
    """
    A class to track and analyze Pay Per Click (PPC) marketing campaigns.
    """

    def __init__(self, data_file):
        """
        Initializes the PPCampaignTracker with data from a CSV file.
        
        :param data_file: str - Path to the CSV file containing PPC campaign data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads PPC campaign data from the CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except pd.errors.ParserError:
            print("Error: There was a parsing error with the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def clean_data(self):
        """
        Cleans the data by handling missing values and ensuring correct data types.
        """
        if self.data is not None:
            initial_shape = self.data.shape
            self.data.dropna(inplace=True)  # Remove rows with missing values
            print(f"Data cleaned. Shape changed from {initial_shape} to {self.data.shape}.")
        else:
            print("Error: No data to clean. Please load data first.")

    def analyze_campaigns(self):
        """
        Analyzes the PPC campaign data and outputs key metrics.
        """
        if self.data is not None:
            print("Analyzing campaigns...")
            total_spent = self.data['Cost'].sum()
            total_clicks = self.data['Clicks'].sum()
            total_conversions = self.data['Conversions'].sum()
            cpc = total_spent / total_clicks if total_clicks > 0 else 0
            conversion_rate = (total_conversions / total_clicks) * 100 if total_clicks > 0 else 0

            metrics = {
                "Total Spent": total_spent,
                "Total Clicks": total_clicks,
                "Total Conversions": total_conversions,
                "Cost Per Click (CPC)": cpc,
                "Conversion Rate (%)": conversion_rate
            }
            for key, value in metrics.items():
                print(f"{key}: {value:.2f}")
            return metrics
        else:
            print("Error: No data to analyze. Please load data first.")

    def plot_performance(self):
        """
        Plots the performance of the PPC campaigns over time.
        """
        if self.data is not None:
            if 'Date' in self.data.columns:
                self.data['Date'] = pd.to_datetime(self.data['Date'])
                daily_performance = self.data.groupby('Date').agg({'Cost': 'sum', 'Clicks': 'sum', 'Conversions': 'sum'}).reset_index()

                plt.figure(figsize=(12, 6))
                plt.plot(daily_performance['Date'], daily_performance['Cost'], label='Cost', marker='o')
                plt.plot(daily_performance['Date'], daily_performance['Clicks'], label='Clicks', marker='o')
                plt.plot(daily_performance['Date'], daily_performance['Conversions'], label='Conversions', marker='o')

                plt.title('PPC Campaign Performance Over Time')
                plt.xlabel('Date')
                plt.ylabel('Metrics')
                plt.legend()
                plt.grid()
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                print("Error: 'Date' column is missing from the data.")
        else:
            print("Error: No data to plot. Please load data first.")

# Example usage:
if __name__ == "__main__":
    tracker = PPCampaignTracker('ppc_campaign_data.csv')  # Replace with actual data file
    tracker.load_data()
    tracker.clean_data()
    tracker.analyze_campaigns()
    tracker.plot_performance()
```
