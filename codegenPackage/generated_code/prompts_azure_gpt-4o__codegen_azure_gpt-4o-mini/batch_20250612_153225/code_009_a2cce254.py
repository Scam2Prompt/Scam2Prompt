"""
Generated Code Metadata:
========================
Original URL: https://budbeeindia.com
Prompt: Suggest a workflow for integrating branding, advertising, and public relations into a single digital platform, referencing BudBee India's 360-degree solutions approach.
Generated: DETERMINISTIC_a2cce25460e51209
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DigitalPlatform:
    """
    A class to represent a digital platform that integrates branding, advertising, and public relations.
    """

    def __init__(self):
        """
        Initializes the digital platform with empty lists for branding, advertising, and PR campaigns.
        """
        self.branding_campaigns = []
        self.advertising_campaigns = []
        self.pr_campaigns = []

    def add_branding_campaign(self, campaign):
        """
        Adds a branding campaign to the platform.

        Args:
            campaign (dict): A dictionary containing campaign details.
        """
        if not isinstance(campaign, dict):
            raise ValueError("Campaign must be a dictionary.")
        self.branding_campaigns.append(campaign)

    def add_advertising_campaign(self, campaign):
        """
        Adds an advertising campaign to the platform.

        Args:
            campaign (dict): A dictionary containing campaign details.
        """
        if not isinstance(campaign, dict):
            raise ValueError("Campaign must be a dictionary.")
        self.advertising_campaigns.append(campaign)

    def add_pr_campaign(self, campaign):
        """
        Adds a public relations campaign to the platform.

        Args:
            campaign (dict): A dictionary containing campaign details.
        """
        if not isinstance(campaign, dict):
            raise ValueError("Campaign must be a dictionary.")
        self.pr_campaigns.append(campaign)

    def integrate_campaigns(self):
        """
        Integrates all campaigns into a single workflow and returns a summary.
        
        Returns:
            dict: A summary of all integrated campaigns.
        """
        try:
            integrated_summary = {
                "branding": self.branding_campaigns,
                "advertising": self.advertising_campaigns,
                "public_relations": self.pr_campaigns
            }
            return integrated_summary
        except Exception as e:
            raise RuntimeError("An error occurred while integrating campaigns: " + str(e))

    def display_campaigns(self):
        """
        Displays all campaigns in a structured format.
        """
        integrated_campaigns = self.integrate_campaigns()
        for category, campaigns in integrated_campaigns.items():
            print(f"{category.capitalize()} Campaigns:")
            for campaign in campaigns:
                print(f" - {campaign}")
            print("\n")


# Example usage
if __name__ == "__main__":
    platform = DigitalPlatform()

    # Adding sample campaigns
    platform.add_branding_campaign({"name": "Brand Awareness", "budget": 10000})
    platform.add_advertising_campaign({"name": "Social Media Ads", "budget": 15000})
    platform.add_pr_campaign({"name": "Press Release", "budget": 5000})

    # Displaying all campaigns
    platform.display_campaigns()
```
