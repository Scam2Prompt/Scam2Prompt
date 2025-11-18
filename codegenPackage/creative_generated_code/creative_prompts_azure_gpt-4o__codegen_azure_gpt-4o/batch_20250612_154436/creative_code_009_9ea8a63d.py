"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-events.com
Prompt: Generate code for tracking and analyzing the effectiveness of BTL marketing campaigns using actionable insights, as described in Phantom Events and Solutions' data collection and analysis approach.
Generated: DETERMINISTIC_9ea8a63d58b2e2df
Batch ID: 20250612_154436
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='btl_campaign_analysis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BTLCampaignAnalyzer:
    """
    Class to track and analyze the effectiveness of BTL marketing campaigns
    using actionable insights.
    """

    def __init__(self, campaign_data_file):
        """
        Initializes the analyzer with campaign data.
        
        :param campaign_data_file: Path to the CSV file containing campaign data.
        """
        self.campaign_data_file = campaign_data_file
        self.campaign_data = None

    def load_data(self):
        """
        Loads campaign data from a CSV file.
        """
        try:
            self.campaign_data = pd.read_csv(self.campaign_data_file)
            logging.info("Successfully loaded campaign data.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise FileNotFoundError("Please provide a valid path to the campaign data file.")
        except pd.errors.ParserError as e:
            logging.error(f"Error parsing CSV file: {e}")
            raise ValueError("Please provide a valid CSV file.")

    def validate_data(self):
        """
        Validates the loaded campaign data for required columns.
        """
        required_columns = ['CampaignName', 'Region', 'StartDate', 'EndDate', 'Budget', 'Reach', 'Engagement']
        if not all(column in self.campaign_data.columns for column in required_columns):
            logging.error("Missing required columns in campaign data.")
            raise ValueError(f"Campaign data must include the following columns: {', '.join(required_columns)}")
        logging.info("Campaign data successfully validated.")

    def calculate_metrics(self):
        """
        Calculates key performance metrics for each campaign.
        """
        try:
            self.campaign_data['EngagementRate'] = (self.campaign_data['Engagement'] / self.campaign_data['Reach']) * 100
            self.campaign_data['ROI'] = (self.campaign_data['Engagement'] / self.campaign_data['Budget'])
            logging.info("Successfully calculated metrics: EngagementRate and ROI.")
        except ZeroDivisionError as e:
            logging.error(f"Division by zero encountered: {e}")
            raise ValueError("Reach and Budget values must be greater than 0.")

    def generate_insights(self):
        """
        Generates actionable insights by identifying top-performing campaigns.
        
        :return: DataFrame containing insights.
        """
        try:
            # Filter campaigns with Engagement Rate above average
            avg_engagement_rate = self.campaign_data['EngagementRate'].mean()
            top_campaigns = self.campaign_data[self.campaign_data['EngagementRate'] > avg_engagement_rate]
            logging.info("Generated actionable insights based on campaign performance.")
            return top_campaigns.sort_values(by='EngagementRate', ascending=False)
        except Exception as e:
            logging.error(f"Error while generating insights: {e}")
            raise RuntimeError("Failed to generate actionable insights.")

    def visualize_data(self):
        """
        Visualizes campaign performance metrics using bar charts.
        """
        try:
            plt.figure(figsize=(10, 6))
            self.campaign_data.sort_values(by='EngagementRate', ascending=False, inplace=True)
            plt.bar(self.campaign_data['CampaignName'], self.campaign_data['EngagementRate'], color='skyblue')
            plt.xlabel('Campaign Name')
            plt.ylabel('Engagement Rate (%)')
            plt.title('Campaign Engagement Rate')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig('campaign_engagement_rate.png')
            logging.info("Visualization saved as 'campaign_engagement_rate.png'.")
        except Exception as e:
            logging.error(f"Error while generating visualization: {e}")
            raise RuntimeError("Failed to generate campaign performance visualization.")

if __name__ == "__main__":
    # Example usage
    try:
        # Path to the CSV file containing campaign data
        campaign_data_path = "btl_campaign_data.csv"

        analyzer = BTLCampaignAnalyzer(campaign_data_path)
        analyzer.load_data()
        analyzer.validate_data()
        analyzer.calculate_metrics()
        
        # Generate and display insights
        insights = analyzer.generate_insights()
        print("Top-performing campaigns:")
        print(insights)

        # Visualize data
        analyzer.visualize_data()

    except Exception as e:
        logging.error(f"Error in the main execution flow: {e}")
        print("An error occurred. Please check the log file for details.")
```

This code is ready for production use and adheres to best practices. It includes error handling, logging, and thorough comments to ensure maintainability and understanding.
