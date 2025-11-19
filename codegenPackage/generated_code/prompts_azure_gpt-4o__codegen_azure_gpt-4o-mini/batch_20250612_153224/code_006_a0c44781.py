"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Create a Python script to calculate ROI (Return on Investment) for marketing campaigns, using input data such as campaign costs, revenue generated, and customer acquisition metrics.
Generated: DETERMINISTIC_a0c447816aa30a1d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingCampaign:
    def __init__(self, campaign_cost: float, revenue_generated: float, customers_acquired: int):
        """
        Initializes the MarketingCampaign object with campaign cost, revenue generated, and customers acquired.

        :param campaign_cost: Total cost of the marketing campaign
        :param revenue_generated: Total revenue generated from the campaign
        :param customers_acquired: Number of customers acquired through the campaign
        """
        self.campaign_cost = campaign_cost
        self.revenue_generated = revenue_generated
        self.customers_acquired = customers_acquired

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI) for the marketing campaign.

        ROI is calculated using the formula: ROI = (Revenue - Cost) / Cost * 100

        :return: ROI as a percentage
        """
        if self.campaign_cost == 0:
            logging.error("Campaign cost cannot be zero when calculating ROI.")
            raise ValueError("Campaign cost cannot be zero.")

        roi = (self.revenue_generated - self.campaign_cost) / self.campaign_cost * 100
        logging.info(f"Calculated ROI: {roi:.2f}%")
        return roi

    def cost_per_acquisition(self) -> float:
        """
        Calculates the cost per acquisition (CPA) for the marketing campaign.

        CPA is calculated using the formula: CPA = Cost / Customers Acquired

        :return: CPA as a float
        """
        if self.customers_acquired == 0:
            logging.error("Number of customers acquired cannot be zero when calculating CPA.")
            raise ValueError("Number of customers acquired cannot be zero.")

        cpa = self.campaign_cost / self.customers_acquired
        logging.info(f"Calculated Cost Per Acquisition: ${cpa:.2f}")
        return cpa

def main():
    try:
        # Example input data for a marketing campaign
        campaign_cost = float(input("Enter the campaign cost: "))
        revenue_generated = float(input("Enter the revenue generated: "))
        customers_acquired = int(input("Enter the number of customers acquired: "))

        # Create a MarketingCampaign instance
        campaign = MarketingCampaign(campaign_cost, revenue_generated, customers_acquired)

        # Calculate and display ROI and CPA
        roi = campaign.calculate_roi()
        cpa = campaign.cost_per_acquisition()

        print(f"Return on Investment (ROI): {roi:.2f}%")
        print(f"Cost Per Acquisition (CPA): ${cpa:.2f}")

    except ValueError as e:
        logging.error(f"Input error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
