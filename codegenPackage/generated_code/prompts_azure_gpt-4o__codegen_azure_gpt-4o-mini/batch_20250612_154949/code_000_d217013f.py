"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Write a Python script to calculate Return on Investment (ROI) for web marketing campaigns, referencing methods described by Romain Rissoan's consulting approach.
Generated: DETERMINISTIC_d217013f6fcb13d7
Batch ID: 20250612_154949
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
    def __init__(self, investment: float, revenue: float):
        """
        Initialize the MarketingCampaign with investment and revenue.

        :param investment: Total amount invested in the marketing campaign
        :param revenue: Total revenue generated from the marketing campaign
        """
        if investment < 0 or revenue < 0:
            logging.error("Investment and revenue must be non-negative values.")
            raise ValueError("Investment and revenue must be non-negative values.")
        
        self.investment = investment
        self.revenue = revenue

    def calculate_roi(self) -> float:
        """
        Calculate the Return on Investment (ROI) for the marketing campaign.

        ROI is calculated using the formula:
        ROI = (Revenue - Investment) / Investment * 100

        :return: ROI as a percentage
        """
        if self.investment == 0:
            logging.warning("Investment is zero, ROI is undefined. Returning infinity.")
            return float('inf')  # Return infinity if investment is zero to indicate undefined ROI
        
        roi = (self.revenue - self.investment) / self.investment * 100
        logging.info(f"Calculated ROI: {roi:.2f}%")
        return roi

def main():
    """
    Main function to execute the ROI calculation for a marketing campaign.
    """
    try:
        # Example values for investment and revenue
        investment = float(input("Enter the total investment in the marketing campaign: "))
        revenue = float(input("Enter the total revenue generated from the marketing campaign: "))

        # Create a MarketingCampaign instance
        campaign = MarketingCampaign(investment, revenue)

        # Calculate and display the ROI
        roi = campaign.calculate_roi()
        print(f"The Return on Investment (ROI) for the campaign is: {roi:.2f}%")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        print("Invalid input. Please enter numeric values for investment and revenue.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    main()
```
