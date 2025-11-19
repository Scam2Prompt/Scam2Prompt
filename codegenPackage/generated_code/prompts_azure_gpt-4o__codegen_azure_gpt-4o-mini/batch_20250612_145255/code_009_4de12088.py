"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Create a Python script to calculate ROI for email marketing campaigns, using metrics like open rates and sales revenue increases, similar to Sales Studios' case studies.
Generated: DETERMINISTIC_4de12088785f91e4
Batch ID: 20250612_145255
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

class EmailMarketingROI:
    def __init__(self, total_revenue: float, total_cost: float, open_rate: float, sales_increase: float):
        """
        Initialize the EmailMarketingROI class with the necessary metrics.

        :param total_revenue: Total revenue generated from the campaign
        :param total_cost: Total cost of the email marketing campaign
        :param open_rate: Open rate of the email campaign (as a percentage)
        :param sales_increase: Increase in sales attributed to the campaign
        """
        self.total_revenue = total_revenue
        self.total_cost = total_cost
        self.open_rate = open_rate / 100  # Convert percentage to decimal
        self.sales_increase = sales_increase

    def calculate_roi(self) -> float:
        """
        Calculate the Return on Investment (ROI) for the email marketing campaign.

        :return: ROI as a percentage
        """
        if self.total_cost == 0:
            logging.error("Total cost cannot be zero when calculating ROI.")
            raise ValueError("Total cost cannot be zero.")

        roi = ((self.total_revenue - self.total_cost) / self.total_cost) * 100
        logging.info(f"Calculated ROI: {roi:.2f}%")
        return roi

    def calculate_effective_open_rate(self) -> float:
        """
        Calculate the effective open rate based on sales increase.

        :return: Effective open rate as a percentage
        """
        if self.sales_increase < 0:
            logging.error("Sales increase cannot be negative.")
            raise ValueError("Sales increase cannot be negative.")

        effective_open_rate = self.open_rate * (self.sales_increase / self.total_revenue) * 100
        logging.info(f"Calculated effective open rate: {effective_open_rate:.2f}%")
        return effective_open_rate

def main():
    try:
        # Example metrics for the email marketing campaign
        total_revenue = 15000.0  # Total revenue generated
        total_cost = 3000.0      # Total cost of the campaign
        open_rate = 25.0          # Open rate in percentage
        sales_increase = 5000.0   # Increase in sales attributed to the campaign

        # Create an instance of EmailMarketingROI
        roi_calculator = EmailMarketingROI(total_revenue, total_cost, open_rate, sales_increase)

        # Calculate ROI
        roi = roi_calculator.calculate_roi()
        print(f"Return on Investment (ROI): {roi:.2f}%")

        # Calculate effective open rate
        effective_open_rate = roi_calculator.calculate_effective_open_rate()
        print(f"Effective Open Rate: {effective_open_rate:.2f}%")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
