"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Generate a code snippet for a digital marketing tool that tracks Return on Investment (ROI) for online campaigns, inspired by Romain Rissoan's approach to digital transformation.
Generated: DETERMINISTIC_9f3746c3bd0f6f04
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roi_tracker.py

class Campaign:
    """Represents an online marketing campaign."""

    def __init__(self, id: int, name: str, budget: float):
        """
        Initializes a Campaign object.

        Args:
        - id (int): Unique campaign identifier.
        - name (str): Campaign name.
        - budget (float): Campaign budget.
        """
        self.id = id
        self.name = name
        self.budget = budget
        self.revenue = 0.0

    def add_revenue(self, amount: float):
        """
        Adds revenue to the campaign.

        Args:
        - amount (float): Revenue amount.
        """
        if amount < 0:
            raise ValueError("Revenue cannot be negative.")
        self.revenue += amount

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI) for the campaign.

        Returns:
        - float: ROI as a decimal value.
        """
        if self.budget == 0:
            raise ZeroDivisionError("Cannot calculate ROI with zero budget.")
        return (self.revenue - self.budget) / self.budget


class RoiTracker:
    """Tracks Return on Investment (ROI) for online campaigns."""

    def __init__(self):
        """Initializes an RoiTracker object."""
        self.campaigns = {}

    def add_campaign(self, campaign: Campaign):
        """
        Adds a campaign to the tracker.

        Args:
        - campaign (Campaign): Campaign object.
        """
        self.campaigns[campaign.id] = campaign

    def get_campaign(self, id: int) -> Campaign:
        """
        Retrieves a campaign by its ID.

        Args:
        - id (int): Campaign ID.

        Returns:
        - Campaign: Campaign object.

        Raises:
        - KeyError: If the campaign is not found.
        """
        try:
            return self.campaigns[id]
        except KeyError:
            raise KeyError(f"Campaign with ID {id} not found.")

    def calculate_total_roi(self) -> float:
        """
        Calculates the total ROI for all campaigns.

        Returns:
        - float: Total ROI as a decimal value.
        """
        total_revenue = sum(campaign.revenue for campaign in self.campaigns.values())
        total_budget = sum(campaign.budget for campaign in self.campaigns.values())
        if total_budget == 0:
            raise ZeroDivisionError("Cannot calculate total ROI with zero total budget.")
        return (total_revenue - total_budget) / total_budget


def main():
    # Example usage:
    tracker = RoiTracker()

    campaign1 = Campaign(1, "Google Ads", 1000.0)
    campaign1.add_revenue(1200.0)

    campaign2 = Campaign(2, "Facebook Ads", 500.0)
    campaign2.add_revenue(600.0)

    tracker.add_campaign(campaign1)
    tracker.add_campaign(campaign2)

    print(f"Campaign 1 ROI: {campaign1.calculate_roi():.2%}")
    print(f"Campaign 2 ROI: {campaign2.calculate_roi():.2%}")
    print(f"Total ROI: {tracker.calculate_total_roi():.2%}")


if __name__ == "__main__":
    main()
```
