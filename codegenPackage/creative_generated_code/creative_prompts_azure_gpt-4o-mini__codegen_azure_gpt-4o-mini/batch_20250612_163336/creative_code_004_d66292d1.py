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
import seaborn as sns
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CampaignAnalyzer:
    def __init__(self, data_file):
        """
        Initialize the CampaignAnalyzer with the provided data file.
        
        Args:
            data_file (str): Path to the CSV file containing campaign data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """Load the campaign data from a CSV file into a DataFrame."""
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("The file is empty.")
            raise
        except pd.errors.ParserError:
            logging.error("Error parsing the CSV file.")
            raise

    def preprocess_data(self):
        """Preprocess the data for analysis."""
        if self.data is None:
            logging.error("Data is not loaded. Please load data first.")
            raise ValueError("Data not loaded.")

        # Convert date column to datetime
        self.data['campaign_date'] = pd.to_datetime(self.data['campaign_date'], errors='coerce')
        self.data.dropna(subset=['campaign_date'], inplace=True)

        logging.info("Data preprocessing completed.")

    def generate_report(self):
        """Generate performance reports based on the loaded data."""
        if self.data is None:
            logging.error("Data is not loaded. Please load data first.")
            raise ValueError("Data not loaded.")

        # Calculate metrics
        total_spend = self.data['spend'].sum()
        total_reach = self.data['reach'].sum()
        total_clicks = self.data['clicks'].sum()
        ctr = (total_clicks / total_reach) * 100 if total_reach > 0 else 0

        report = {
            'Total Spend': total_spend,
            'Total Reach': total_reach,
            'Total Clicks': total_clicks,
            'Click-Through Rate (%)': ctr
        }

        logging.info("Report generated successfully.")
        return report

    def visualize_data(self):
        """Visualize key metrics for the campaign."""
        if self.data is None:
            logging.error("Data is not loaded. Please load data first.")
            raise ValueError("Data not loaded.")

        # Set style for the plots
        sns.set(style="whitegrid")

        # Create a bar plot for spend vs reach
        plt.figure(figsize=(10, 6))
        sns.barplot(x='campaign_name', y='spend', data=self.data, color='blue', label='Spend')
        sns.barplot(x='campaign_name', y='reach', data=self.data, color='orange', label='Reach')
        plt.title('Campaign Spend vs Reach')
        plt.xlabel('Campaign Name')
        plt.ylabel('Amount')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
        logging.info("Data visualization completed.")

def main():
    """Main function to run the campaign analysis."""
    analyzer = CampaignAnalyzer('campaign_data.csv')
    
    try:
        analyzer.load_data()
        analyzer.preprocess_data()
        report = analyzer.generate_report()
        print("Performance Report:")
        for key, value in report.items():
            print(f"{key}: {value}")
        analyzer.visualize_data()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
