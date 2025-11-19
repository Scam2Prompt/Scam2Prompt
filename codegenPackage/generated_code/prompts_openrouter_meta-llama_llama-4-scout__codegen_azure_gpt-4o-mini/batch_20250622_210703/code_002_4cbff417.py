"""
Generated Code Metadata:
========================
Original URL: https://masmedia.xyz
Prompt: "Generate a social marketing campaign plan for a small business, incorporating online marketing and email marketing tactics, and provide metrics for measuring success."
Generated: DETERMINISTIC_4cbff417debb0f38
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SocialMarketingCampaign:
    """
    A class to represent a social marketing campaign for a small business.
    """

    def __init__(self, business_name, target_audience):
        """
        Initializes the campaign with the business name and target audience.

        :param business_name: Name of the small business
        :param target_audience: Description of the target audience
        """
        self.business_name = business_name
        self.target_audience = target_audience
        self.online_marketing_tactics = []
        self.email_marketing_tactics = []
        self.metrics = {}

    def add_online_marketing_tactic(self, tactic):
        """
        Adds an online marketing tactic to the campaign.

        :param tactic: A string describing the online marketing tactic
        """
        self.online_marketing_tactics.append(tactic)

    def add_email_marketing_tactic(self, tactic):
        """
        Adds an email marketing tactic to the campaign.

        :param tactic: A string describing the email marketing tactic
        """
        self.email_marketing_tactics.append(tactic)

    def set_metrics(self, metric_name, target_value):
        """
        Sets a metric for measuring the success of the campaign.

        :param metric_name: Name of the metric
        :param target_value: Target value for the metric
        """
        self.metrics[metric_name] = target_value

    def generate_campaign_plan(self):
        """
        Generates a detailed campaign plan including tactics and metrics.

        :return: A dictionary containing the campaign plan
        """
        return {
            "Business Name": self.business_name,
            "Target Audience": self.target_audience,
            "Online Marketing Tactics": self.online_marketing_tactics,
            "Email Marketing Tactics": self.email_marketing_tactics,
            "Metrics": self.metrics
        }

    def display_campaign_plan(self):
        """
        Displays the campaign plan in a readable format.
        """
        plan = self.generate_campaign_plan()
        for key, value in plan.items():
            print(f"{key}: {value}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a new social marketing campaign
        campaign = SocialMarketingCampaign("Small Biz Co", "Local community members aged 25-40")

        # Add online marketing tactics
        campaign.add_online_marketing_tactic("Social Media Advertising on Facebook and Instagram")
        campaign.add_online_marketing_tactic("Content Marketing through Blog Posts")

        # Add email marketing tactics
        campaign.add_email_marketing_tactic("Monthly Newsletter with Promotions")
        campaign.add_email_marketing_tactic("Automated Welcome Email Series")

        # Set metrics for success
        campaign.set_metrics("Website Traffic Increase", "20%")
        campaign.set_metrics("Email Open Rate", "25%")
        campaign.set_metrics("Social Media Engagement", "15%")

        # Display the campaign plan
        campaign.display_campaign_plan()

    except Exception as e:
        print(f"An error occurred: {e}")
```
