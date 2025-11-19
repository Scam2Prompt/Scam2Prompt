"""
Generated Code Metadata:
========================
Original URL: https://vivadainfotech.com
Prompt: "Develop a code snippet to track and analyze the success rate of digital marketing campaigns for hospitals, using metrics like OPD visits and occupancy rates, inspired by Vivada Infotech's case studies."
Generated: DETERMINISTIC_b20330ddca58c215
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CampaignAnalyzer:
    """
    A class to track and analyze the success rate of digital marketing campaigns
    for hospitals using metrics like OPD visits and occupancy rates.
    """

    def __init__(self, campaign_data):
        """
        Initialize the CampaignAnalyzer with campaign data.

        :param campaign_data: A pandas DataFrame containing campaign metrics.
                              Expected columns: ['Campaign', 'OPD_Visits', 'Occupancy_Rate', 'Budget']
        """
        self.campaign_data = campaign_data

    def validate_data(self):
        """
        Validate the input data to ensure it contains the required columns.
        """
        required_columns = ['Campaign', 'OPD_Visits', 'Occupancy_Rate', 'Budget']
        missing_columns = [col for col in required_columns if col not in self.campaign_data.columns]

        if missing_columns:
            logging.error(f"Missing required columns: {missing_columns}")
            raise ValueError(f"Input data is missing required columns: {missing_columns}")

    def calculate_success_rate(self):
        """
        Calculate the success rate for each campaign based on OPD visits and occupancy rates.

        :return: A pandas DataFrame with success rate added as a new column.
        """
        try:
            # Success rate formula: (OPD_Visits * Occupancy_Rate) / Budget
            self.campaign_data['Success_Rate'] = (
                self.campaign_data['OPD_Visits'] * self.campaign_data['Occupancy_Rate']
            ) / self.campaign_data['Budget']

            logging.info("Successfully calculated success rates for campaigns.")
            return self.campaign_data

        except ZeroDivisionError:
            logging.error("Division by zero encountered in budget column.")
            raise ValueError("Budget column contains zero values, which is not allowed.")

        except Exception as e:
            logging.error(f"An error occurred while calculating success rates: {e}")
            raise

    def get_top_campaigns(self, top_n=3):
        """
        Retrieve the top N campaigns based on success rate.

        :param top_n: Number of top campaigns to retrieve (default is 3).
        :return: A pandas DataFrame containing the top N campaigns.
        """
        try:
            sorted_data = self.campaign_data.sort_values(by='Success_Rate', ascending=False)
            top_campaigns = sorted_data.head(top_n)

            logging.info(f"Retrieved top {top_n} campaigns based on success rate.")
            return top_campaigns

        except Exception as e:
            logging.error(f"An error occurred while retrieving top campaigns: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Sample campaign data
    data = {
        'Campaign': ['Campaign A', 'Campaign B', 'Campaign C', 'Campaign D'],
        'OPD_Visits': [120, 200, 150, 180],
        'Occupancy_Rate': [0.75, 0.85, 0.65, 0.90],
        'Budget': [1000, 1500, 1200, 1800]
    }

    # Create a DataFrame
    campaign_df = pd.DataFrame(data)

    try:
        # Initialize the analyzer
        analyzer = CampaignAnalyzer(campaign_df)

        # Validate the data
        analyzer.validate_data()

        # Calculate success rates
        updated_data = analyzer.calculate_success_rate()
        print("Updated Campaign Data with Success Rates:")
        print(updated_data)

        # Get top campaigns
        top_campaigns = analyzer.get_top_campaigns(top_n=2)
        print("\nTop Campaigns:")
        print(top_campaigns)

    except Exception as e:
        logging.error(f"An error occurred in the main program: {e}")
```
