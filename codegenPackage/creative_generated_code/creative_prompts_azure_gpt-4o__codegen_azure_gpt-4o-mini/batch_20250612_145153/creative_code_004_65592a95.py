"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Write a Python script to generate detailed performance reports for digital marketing campaigns, incorporating metrics similar to those used by IDEX Marketing for data-driven decision-making.
Generated: DETERMINISTIC_65592a95541af504
Batch ID: 20250612_145153
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingCampaignReport:
    def __init__(self, data_file):
        """
        Initializes the MarketingCampaignReport with data from a specified CSV file.

        :param data_file: Path to the CSV file containing marketing campaign data.
        """
        self.data_file = data_file
        self.df = self.load_data()

    def load_data(self):
        """
        Loads marketing campaign data from a CSV file.

        :return: Pandas DataFrame containing the campaign data.
        """
        try:
            df = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
            return df
        except Exception as e:
            logging.error(f"Failed to load data from {self.data_file}: {e}")
            raise

    def generate_report(self):
        """
        Generates a performance report including key metrics.
        """
        try:
            metrics = {
                'total_spent': self.df['Spent'].sum(),
                'total_clicks': self.df['Clicks'].sum(),
                'total_impressions': self.df['Impressions'].sum(),
                'avg_ctr': (self.df['Clicks'].sum() / self.df['Impressions'].sum()) * 100,
                'avg_cpc': self.df['Spent'].sum() / self.df['Clicks'].sum(),
            }

            report = pd.DataFrame(metrics, index=[0])
            logging.info("Performance report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"Failed to generate report: {e}")
            raise

    def visualize_data(self):
        """
        Visualizes campaign performance data using matplotlib.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(self.df['Campaign'], self.df['Spent'], color='blue', label='Spent')
            plt.ylabel('Amount Spent')
            plt.title('Marketing Campaign Spend')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.savefig('campaign_spend_report.png')
            logging.info("Visualization saved as campaign_spend_report.png.")
        except Exception as e:
            logging.error(f"Failed to visualize data: {e}")
            raise

def main():
    """
    Main function to execute the MarketingCampaignReport.
    """
    try:
        # The CSV file path should be updated to the actual location of the data file.
        report_generator = MarketingCampaignReport(data_file='campaign_data.csv')
        report = report_generator.generate_report()
        print(report)
        report_generator.visualize_data()
    except Exception as e:
        logging.error(f"An error occurred during report generation: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the CSV file `campaign_data.csv` exists in the specified path with appropriate columns such as `Spent`, `Clicks`, `Impressions`, and `Campaign` for this script to run successfully.
