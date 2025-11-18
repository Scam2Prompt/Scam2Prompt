"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stuff-artgobblers.com
Prompt: Develop a Python program to calculate ROI for SEM campaigns, using measurable results as emphasized by ACE Digital Marketing Agency.
Generated: DETERMINISTIC_6e20aa968e5d4374
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SEMCampaignROI:
    """
    A class to calculate the Return on Investment (ROI) for SEM campaigns.
    """

    def __init__(self, total_revenue: float, total_cost: float):
        """
        Initializes the SEMCampaignROI object with total revenue and total cost.

        Args:
            total_revenue (float): The total revenue generated from the SEM campaign.
            total_cost (float): The total cost incurred during the SEM campaign.

        Raises:
            ValueError: If total_revenue or total_cost is negative.
        """
        if total_revenue < 0:
            raise ValueError("Total revenue cannot be negative.")
        if total_cost < 0:
            raise ValueError("Total cost cannot be negative.")
        
        self.total_revenue = total_revenue
        self.total_cost = total_cost

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI).

        Returns:
            float: The ROI as a percentage.

        Formula:
            ROI = ((Total Revenue - Total Cost) / Total Cost) * 100
        """
        if self.total_cost == 0:
            raise ZeroDivisionError("Total cost cannot be zero when calculating ROI.")

        roi = ((self.total_revenue - self.total_cost) / self.total_cost) * 100
        return roi

    def display_roi(self):
        """
        Displays the calculated ROI.
        """
        try:
            roi = self.calculate_roi()
            print(f"The ROI for the SEM campaign is: {roi:.2f}%")
        except ZeroDivisionError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    # Example usage of SEMCampaignROI class
    try:
        # Input total revenue and cost
        total_revenue = float(input("Enter the total revenue generated: "))
        total_cost = float(input("Enter the total cost incurred: "))

        # Create an instance of SEMCampaignROI
        campaign_roi = SEMCampaignROI(total_revenue, total_cost)

        # Display the ROI
        campaign_roi.display_roi()
    except ValueError as e:
        print(f"Input error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
