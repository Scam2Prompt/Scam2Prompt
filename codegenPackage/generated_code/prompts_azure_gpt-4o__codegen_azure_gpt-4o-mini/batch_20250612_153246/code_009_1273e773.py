"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: Write a Python program to calculate ROI for digital marketing campaigns, using Rankraze's proven performance record as a benchmark.
Generated: DETERMINISTIC_1273e77321c9a02d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingCampaign:
    """
    A class to represent a digital marketing campaign and calculate its Return on Investment (ROI).
    """

    def __init__(self, campaign_name, total_investment, total_revenue):
        """
        Initializes the MarketingCampaign with the campaign name, total investment, and total revenue.

        :param campaign_name: str - The name of the marketing campaign
        :param total_investment: float - The total amount invested in the campaign
        :param total_revenue: float - The total revenue generated from the campaign
        """
        self.campaign_name = campaign_name
        self.total_investment = total_investment
        self.total_revenue = total_revenue

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for the marketing campaign.

        :return: float - The ROI percentage
        :raises ValueError: If total_investment is zero or negative
        """
        if self.total_investment <= 0:
            logging.error("Total investment must be greater than zero.")
            raise ValueError("Total investment must be greater than zero.")

        roi = ((self.total_revenue - self.total_investment) / self.total_investment) * 100
        logging.info(f"Calculated ROI for {self.campaign_name}: {roi:.2f}%")
        return roi

def main():
    """
    Main function to execute the ROI calculation for a digital marketing campaign.
    """
    try:
        # Example campaign data
        campaign_name = "Spring Sale Campaign"
        total_investment = 5000.00  # Total investment in dollars
        total_revenue = 15000.00     # Total revenue generated in dollars

        # Create a MarketingCampaign instance
        campaign = MarketingCampaign(campaign_name, total_investment, total_revenue)

        # Calculate and print the ROI
        roi = campaign.calculate_roi()
        print(f"The ROI for the campaign '{campaign.campaign_name}' is {roi:.2f}%")

    except ValueError as e:
        logging.error(f"Error calculating ROI: {e}")

if __name__ == "__main__":
    main()
```
