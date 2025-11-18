"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Create a Python script to calculate ROI (Return on Investment) for marketing campaigns, using input data such as campaign costs, revenue generated, and customer acquisition metrics.
Generated: DETERMINISTIC_a0c447816aa30a1d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to output to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingCampaign:
    """
    A class to represent a marketing campaign and calculate its ROI.
    
    Attributes
    ----------
    cost : float
        The cost of the marketing campaign.
    revenue : float
        The revenue generated from the campaign.
    customers_acquired : int
        The number of customers acquired through the campaign.
    """
    
    def __init__(self, cost, revenue, customers_acquired):
        """
        Initializes the MarketingCampaign with cost, revenue, and customers_acquired.
        
        Parameters
        ----------
        cost : float
            The cost of the marketing campaign.
        revenue : float
            The revenue generated from the campaign.
        customers_acquired : int
            The number of customers acquired through the campaign.
        """
        self.cost = cost
        self.revenue = revenue
        self.customers_acquired = customers_acquired

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for the marketing campaign.
        
        Returns
        -------
        float
            The ROI as a percentage.
        """
        try:
            if self.cost <= 0:
                raise ValueError("Cost must be greater than zero.")

            roi = ((self.revenue - self.cost) / self.cost) * 100
            logging.info(f"Calculated ROI: {roi:.2f}%")
            return roi

        except Exception as e:
            logging.error(f"Error calculating ROI: {e}")
            return None

    def summary(self):
        """
        Provides a summary of the marketing campaign metrics.
        
        Returns
        -------
        str
            A summary string containing the campaign metrics.
        """
        roi = self.calculate_roi()
        summary_str = (
            f"Marketing Campaign Summary:\n"
            f"Cost: ${self.cost:.2f}\n"
            f"Revenue: ${self.revenue:.2f}\n"
            f"Customers Acquired: {self.customers_acquired}\n"
            f"ROI: {roi:.2f}%" if roi is not None else "ROI: Calculation Error"
        )
        logging.info(summary_str)
        return summary_str

def main():
    """
    Main function to execute the ROI calculation for a marketing campaign.
    Modify the campaign parameters below as needed.
    """
    # Example campaign data
    campaign_cost = 5000  # Campaign cost
    revenue_generated = 15000  # Revenue generated from the campaign
    customers_acquired = 200  # Customers acquired through the campaign
    
    # Create an instance of MarketingCampaign
    campaign = MarketingCampaign(campaign_cost, revenue_generated, customers_acquired)
    
    # Print the campaign summary
    print(campaign.summary())

if __name__ == "__main__":
    main()
```
