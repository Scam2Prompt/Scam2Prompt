"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: Create a Python script to calculate ROI for email marketing campaigns, using metrics like open rates and sales revenue increases, similar to Sales Studios' case studies.
Generated: DETERMINISTIC_4de12088785f91e4
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailCampaignROI:
    def __init__(self, total_spent, open_rate, sales_revenue_increase):
        """
        Initializes the EmailCampaignROI instance.

        :param total_spent: Total amount spent on the campaign (float).
        :param open_rate: Open rate of the email campaign (percentage as float).
        :param sales_revenue_increase: Increase in sales revenue attributed to the campaign (float).
        """
        self.total_spent = total_spent
        self.open_rate = open_rate
        self.sales_revenue_increase = sales_revenue_increase

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for the email campaign.

        ROI formula: (Revenue - Cost) / Cost * 100

        :return: ROI as a percentage (float).
        """
        try:
            if self.total_spent <= 0:
                raise ValueError("Total spent must be greater than zero.")
            if self.sales_revenue_increase < 0:
                raise ValueError("Sales revenue increase cannot be negative.")

            roi = (self.sales_revenue_increase - self.total_spent) / self.total_spent * 100
            logging.info(f"Calculated ROI: {roi:.2f}%")
            return roi
        except Exception as e:
            logging.error(f"Error calculating ROI: {e}")
            return None

def main():
    """
    Main function to execute the ROI calculation.
    """
    try:
        # Example campaign data
        total_spent = float(input("Enter the total amount spent on the campaign: "))
        open_rate = float(input("Enter the open rate of the campaign (in %): "))
        sales_revenue_increase = float(input("Enter the sales revenue increase attributed to the campaign: "))

        # Create an instance of EmailCampaignROI
        campaign = EmailCampaignROI(total_spent, open_rate, sales_revenue_increase)

        # Calculate and print ROI
        roi = campaign.calculate_roi()
        if roi is not None:
            print(f"The ROI for the email campaign is: {roi:.2f}%")
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
