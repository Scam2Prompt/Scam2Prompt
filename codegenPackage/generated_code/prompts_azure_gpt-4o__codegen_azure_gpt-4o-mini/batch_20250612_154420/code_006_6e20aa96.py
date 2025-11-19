"""
Generated Code Metadata:
========================
Original URL: https://stuff-artgobblers.com
Prompt: Develop a Python program to calculate ROI for SEM campaigns, using measurable results as emphasized by ACE Digital Marketing Agency.
Generated: DETERMINISTIC_6e20aa968e5d4374
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SEMCampaignROI:
    """
    A class to calculate the Return on Investment (ROI) for Search Engine Marketing (SEM) campaigns.
    """

    def __init__(self, total_revenue: float, total_cost: float):
        """
        Initializes the SEMCampaignROI with total revenue and total cost.

        :param total_revenue: Total revenue generated from the SEM campaign.
        :param total_cost: Total cost incurred for the SEM campaign.
        """
        if total_cost < 0:
            raise ValueError("Total cost cannot be negative.")
        if total_revenue < 0:
            raise ValueError("Total revenue cannot be negative.")

        self.total_revenue = total_revenue
        self.total_cost = total_cost

    def calculate_roi(self) -> float:
        """
        Calculates the ROI for the SEM campaign.

        :return: The ROI as a percentage.
        """
        if self.total_cost == 0:
            raise ZeroDivisionError("Total cost cannot be zero when calculating ROI.")

        roi = (self.total_revenue - self.total_cost) / self.total_cost * 100
        return roi

    def display_roi(self) -> None:
        """
        Displays the ROI in a formatted manner.
        """
        try:
            roi = self.calculate_roi()
            print(f"The ROI for the SEM campaign is: {roi:.2f}%")
        except (ZeroDivisionError, ValueError) as e:
            print(f"Error calculating ROI: {e}")


def main():
    """
    Main function to execute the ROI calculation for SEM campaigns.
    """
    try:
        # Example values for total revenue and total cost
        total_revenue = float(input("Enter the total revenue generated from the SEM campaign: "))
        total_cost = float(input("Enter the total cost incurred for the SEM campaign: "))

        # Create an instance of SEMCampaignROI
        campaign_roi = SEMCampaignROI(total_revenue, total_cost)

        # Display the calculated ROI
        campaign_roi.display_roi()

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
