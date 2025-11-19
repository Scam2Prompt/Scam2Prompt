"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Develop a PPC advertising strategy for a Jordanian company, including key performance indicators to measure success based on IDEX Marketing's approach.
Generated: DETERMINISTIC_9761495e92fac51c
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PPCAdvertisingStrategy:
    """
    A class to represent a PPC advertising strategy for a Jordanian company.
    """

    def __init__(self, company_name, budget, target_audience):
        """
        Initializes the PPCAdvertisingStrategy with company details.

        :param company_name: Name of the company
        :param budget: Monthly budget for PPC advertising
        :param target_audience: Target audience demographics
        """
        self.company_name = company_name
        self.budget = budget
        self.target_audience = target_audience
        self.campaigns = []

    def add_campaign(self, campaign_name, keywords, ad_copy):
        """
        Adds a PPC campaign to the strategy.

        :param campaign_name: Name of the campaign
        :param keywords: List of keywords for the campaign
        :param ad_copy: Ad copy for the campaign
        """
        campaign = {
            'name': campaign_name,
            'keywords': keywords,
            'ad_copy': ad_copy,
            'performance': {}
        }
        self.campaigns.append(campaign)

    def set_kpis(self, campaign_name, kpis):
        """
        Sets key performance indicators for a specific campaign.

        :param campaign_name: Name of the campaign
        :param kpis: Dictionary of KPIs to measure success
        """
        for campaign in self.campaigns:
            if campaign['name'] == campaign_name:
                campaign['performance'] = kpis
                return
        raise ValueError(f"Campaign '{campaign_name}' not found.")

    def calculate_roi(self, campaign_name, revenue):
        """
        Calculates the return on investment (ROI) for a specific campaign.

        :param campaign_name: Name of the campaign
        :param revenue: Revenue generated from the campaign
        :return: ROI as a percentage
        """
        for campaign in self.campaigns:
            if campaign['name'] == campaign_name:
                cost = self.budget / len(self.campaigns)  # Assuming equal budget distribution
                roi = ((revenue - cost) / cost) * 100
                return roi
        raise ValueError(f"Campaign '{campaign_name}' not found.")

    def generate_report(self):
        """
        Generates a report of all campaigns and their performance.
        
        :return: A summary report of campaigns
        """
        report = {}
        for campaign in self.campaigns:
            report[campaign['name']] = {
                'keywords': campaign['keywords'],
                'ad_copy': campaign['ad_copy'],
                'performance': campaign['performance']
            }
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the PPC advertising strategy
        ppc_strategy = PPCAdvertisingStrategy("Jordanian Company", 5000, "Young Adults")

        # Add campaigns
        ppc_strategy.add_campaign("Summer Sale", ["discount", "summer", "sale"], "Get 20% off this summer!")
        ppc_strategy.add_campaign("New Arrivals", ["new", "fashion", "trends"], "Check out our new arrivals!")

        # Set KPIs for campaigns
        ppc_strategy.set_kpis("Summer Sale", {"CTR": 0.05, "CPC": 0.50, "Conversions": 100})
        ppc_strategy.set_kpis("New Arrivals", {"CTR": 0.04, "CPC": 0.60, "Conversions": 80})

        # Calculate ROI for a campaign
        roi = ppc_strategy.calculate_roi("Summer Sale", 3000)
        print(f"ROI for 'Summer Sale': {roi:.2f}%")

        # Generate and print report
        report = ppc_strategy.generate_report()
        print("Campaign Report:", report)

    except Exception as e:
        print(f"An error occurred: {e}")
```
