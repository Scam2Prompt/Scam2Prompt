"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Write a Python script to analyze marketing campaign data and generate performance reports, similar to the analytics services offered by IDEX Marketing.
Generated: DETERMINISTIC_d66292d1b8083315
Batch ID: 20250612_163336
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
import logging
import sys

# Configure logging for the script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("marketing_analysis.log", mode="w")
    ]
)

class CampaignDataAnalyzer:
    """
    Class to analyze marketing campaign data and generate performance reports.
    """
    def __init__(self, data_file):
        """
        Initialize the CampaignDataAnalyzer with the input data file.

        :param data_file: Path to the CSV file containing campaign data
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Load marketing campaign data from the CSV file into a Pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info(f"Data successfully loaded from {self.data_file}")
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("The file is empty")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred while loading data: {e}")
            raise

    def validate_data(self):
        """
        Validate the loaded data to ensure required columns are present.

        :raises ValueError: If required columns are missing
        """
        required_columns = ['CampaignName', 'Clicks', 'Impressions', 'Conversions', 'Cost']
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            error_message = f"Missing required columns: {', '.join(missing_columns)}"
            logging.error(error_message)
            raise ValueError(error_message)
        logging.info("Data validation successful")

    def compute_metrics(self):
        """
        Compute performance metrics for each campaign.

        Adds columns for Click-Through Rate (CTR), Conversion Rate (CVR), and Cost per Conversion (CPC).
        """
        try:
            self.data['CTR'] = (self.data['Clicks'] / self.data['Impressions']) * 100
            self.data['CVR'] = (self.data['Conversions'] / self.data['Clicks']) * 100
            self.data['CPC'] = self.data['Cost'] / self.data['Conversions']
            logging.info("Metrics computed successfully")
        except ZeroDivisionError:
            logging.warning("Division by zero encountered during metric computation")
        except Exception as e:
            logging.error(f"An unexpected error occurred while computing metrics: {e}")
            raise

    def generate_summary_report(self):
        """
        Generate a summary report for the campaign data.

        Prints the summary statistics and saves a bar plot of campaign performance.
        """
        try:
            summary = self.data[['CampaignName', 'CTR', 'CVR', 'CPC']].describe()
            logging.info("Summary statistics generated successfully")
            print("Summary Statistics:")
            print(summary)

            # Generate a bar plot for CTR and CVR
            self.data.set_index('CampaignName')[['CTR', 'CVR']].plot(kind='bar', figsize=(10, 6))
            plt.title('Campaign Performance (CTR & CVR)')
            plt.xlabel('Campaign Name')
            plt.ylabel('Percentage')
            plt.tight_layout()
            plt.savefig('campaign_performance.png')
            logging.info("Performance plot saved as 'campaign_performance.png'")
        except Exception as e:
            logging.error(f"An unexpected error occurred while generating the report: {e}")
            raise

def main():
    """
    Main function to run the CampaignDataAnalyzer.
    """
    # Path to the CSV file containing marketing data
    data_file = "marketing_campaign_data.csv"

    # Initialize the analyzer
    analyzer = CampaignDataAnalyzer(data_file)

    try:
        # Load and validate data
        analyzer.load_data()
        analyzer.validate_data()

        # Compute metrics and generate report
        analyzer.compute_metrics()
        analyzer.generate_summary_report()
    except Exception as e:
        logging.error(f"An unexpected error occurred in the main flow: {e}")

if __name__ == "__main__":
    main()
```
