"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Develop a PPC advertising strategy for a Jordanian company, including key performance indicators to measure success based on IDEX Marketing's approach.
Generated: DETERMINISTIC_9761495e92fac51c
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# PPC Advertising Strategy for a Jordanian Company

class PPCAdvertisingStrategy:
    def __init__(self, company_name):
        """
        Initialize the PPC Advertising Strategy for a company.

        Args:
            company_name (str): The name of the company for which the strategy is being developed.
        """
        self.company_name = company_name
        self.budgets = {}
        self.keywords = []
        self.ad_copy = ""
        self.kpis = {
            'impressions': 0,
            'clicks': 0,
            'conversion_rate': 0.0,
            'cost_per_click': 0.0,
            'return_on_investment': 0.0
        }

    def set_budget(self, platform, amount):
        """
        Set the advertising budget for a specific platform.

        Args:
            platform (str): The ad platform (e.g., Google, Facebook).
            amount (float): The budget amount to be allocated.

        Raises:
            ValueError: If the budget amount is negative.
        """
        if amount < 0:
            raise ValueError("Budget amount cannot be negative.")
        self.budgets[platform] = amount

    def add_keywords(self, keywords):
        """
        Add keywords for the PPC campaign.

        Args:
            keywords (list): A list of keywords relevant to the business.
        """
        self.keywords.extend(keywords)

    def set_ad_copy(self, ad_copy):
        """
        Set the advertisement copy.

        Args:
            ad_copy (str): The text that will appear in the ad.
        """
        self.ad_copy = ad_copy

    def update_kpis(self, impressions, clicks, conversions, total_spend):
        """
        Update Key Performance Indicators based on campaign performance.

        Args:
            impressions (int): The number of times the ad was shown.
            clicks (int): The number of times the ad was clicked.
            conversions (int): The number of successful conversions.
            total_spend (float): The total amount spent on the campaign.
        """
        self.kpis['impressions'] += impressions
        self.kpis['clicks'] += clicks
        
        if impressions > 0:
            self.kpis['conversion_rate'] = conversions / impressions
        
        if clicks > 0:
            self.kpis['cost_per_click'] = total_spend / clicks
        
        if total_spend > 0:
            self.kpis['return_on_investment'] = (conversions * 100) / total_spend

    def generate_report(self):
        """
        Generate a report of the PPC campaign performance.

        Returns:
            dict: A dictionary containing the KPI results.
        """
        return {
            'Company': self.company_name,
            'Budget Allocation': self.budgets,
            'Keywords': self.keywords,
            'Ad Copy': self.ad_copy,
            'Key Performance Indicators': self.kpis
        }


# Example Usage
if __name__ == "__main__":
    try:
        # Create a PPC strategy for a Jordanian company
        strategy = PPCAdvertisingStrategy("Jordanian Company X")

        # Set budgets for different platforms
        strategy.set_budget("Google Ads", 500.00)
        strategy.set_budget("Facebook Ads", 300.00)

        # Add relevant keywords
        strategy.add_keywords(["Jordan tourism", "buy in Amman", "best restaurants in Jordan"])

        # Set advertisement copy
        strategy.set_ad_copy("Discover the best experiences in Jordan!")

        # Update KPIs based on campaign performance
        strategy.update_kpis(impressions=10000, clicks=500, conversions=50, total_spend=800.00)

        # Generate and print report
        report = strategy.generate_report()
        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")
```
