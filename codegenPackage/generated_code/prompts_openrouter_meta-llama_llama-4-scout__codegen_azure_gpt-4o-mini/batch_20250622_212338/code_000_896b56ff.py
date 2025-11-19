"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Write a Python code snippet for calculating Return on Investment (ROI) for digital marketing campaigns, considering the context of business crisis and urgent restructuring.
Generated: DETERMINISTIC_896b56ff4aa7ea1f
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MarketingCampaign:
    """
    A class to represent a marketing campaign and calculate its Return on Investment (ROI).
    """

    def __init__(self, investment: float, revenue: float):
        """
        Initializes the MarketingCampaign with investment and revenue.

        :param investment: Total amount invested in the marketing campaign.
        :param revenue: Total revenue generated from the campaign.
        """
        if investment < 0:
            raise ValueError("Investment cannot be negative.")
        if revenue < 0:
            raise ValueError("Revenue cannot be negative.")

        self.investment = investment
        self.revenue = revenue

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI).

        ROI is calculated using the formula:
        ROI = (Revenue - Investment) / Investment * 100

        :return: ROI as a percentage.
        """
        if self.investment == 0:
            raise ZeroDivisionError("Investment cannot be zero when calculating ROI.")

        roi = (self.revenue - self.investment) / self.investment * 100
        return roi

def main():
    """
    Main function to execute the ROI calculation for a marketing campaign.
    """
    try:
        # Example values for investment and revenue
        investment = float(input("Enter the total investment in the campaign: "))
        revenue = float(input("Enter the total revenue generated from the campaign: "))

        # Create a MarketingCampaign instance
        campaign = MarketingCampaign(investment, revenue)

        # Calculate and display the ROI
        roi = campaign.calculate_roi()
        print(f"The Return on Investment (ROI) for the campaign is: {roi:.2f}%")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Calculation error: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
