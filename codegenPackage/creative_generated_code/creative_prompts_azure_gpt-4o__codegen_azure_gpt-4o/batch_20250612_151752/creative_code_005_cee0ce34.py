"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.media
Prompt: Create a Python script to analyze the ROI of social media video campaigns produced by Kraken Media, focusing on metrics like clicks, conversions, and revenue.
Generated: DETERMINISTIC_cee0ce349527f72b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

class SocialMediaCampaignAnalyzer:
    """
    A class to analyze ROI (Return on Investment) for social media video campaigns.
    Focuses on metrics like clicks, conversions, and revenue.
    """

    def __init__(self, data_file):
        """
        Initialize the campaign analyzer with the path to the data file.

        :param data_file: Path to the CSV file containing campaign data.
        """
        self.data_file = data_file
        self.campaign_data = []

    def load_data(self):
        """
        Load campaign data from a CSV file. The file must have the following columns:
        Campaign Name, Impressions, Clicks, Conversions, Revenue, Cost.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")

        try:
            with open(self.data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.campaign_data = [row for row in reader]
        except Exception as e:
            raise Exception(f"Error loading data: {e}")

    def calculate_roi(self, campaign):
        """
        Calculate ROI for a single campaign.

        :param campaign: A dictionary containing campaign data.
        :return: ROI value (float).
        """
        try:
            revenue = float(campaign['Revenue'])
            cost = float(campaign['Cost'])

            if cost == 0:  # Avoid division by zero
                return 0.0

            return ((revenue - cost) / cost) * 100  # ROI as percentage
        except ValueError as e:
            raise ValueError(f"Invalid data format in campaign: {e}")

    def analyze_campaigns(self):
        """
        Analyze all campaigns and print a summary of ROI and metrics.

        :return: None
        """
        if not self.campaign_data:
            print("No campaign data available. Please load the data first.")
            return

        print("Campaign Analysis Results:")
        print("-" * 50)

        for campaign in self.campaign_data:
            try:
                campaign_name = campaign['Campaign Name']
                clicks = int(campaign['Clicks'])
                conversions = int(campaign['Conversions'])
                revenue = float(campaign['Revenue'])
                cost = float(campaign['Cost'])

                roi = self.calculate_roi(campaign)

                print(f"Campaign: {campaign_name}")
                print(f"Clicks: {clicks}")
                print(f"Conversions: {conversions}")
                print(f"Revenue: ${revenue:.2f}")
                print(f"Cost: ${cost:.2f}")
                print(f"ROI: {roi:.2f}%")
                print("-" * 50)
            except (ValueError, KeyError) as e:
                print(f"Error analyzing campaign '{campaign.get('Campaign Name', 'Unknown')}': {e}")

if __name__ == "__main__":
    # File path to the campaign data CSV file
    DATA_FILE = "campaign_data.csv"

    # Create an instance of the analyzer
    analyzer = SocialMediaCampaignAnalyzer(DATA_FILE)

    try:
        # Load data and analyze campaigns
        analyzer.load_data()
        analyzer.analyze_campaigns()
    except Exception as e:
        print(f"An error occurred: {e}")
```
