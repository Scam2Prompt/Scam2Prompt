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

Your request involves creating a PPC advertising strategy, which is typically a marketing plan rather than code. However, I can provide Python code for simulating a PPC campaign, setting KPIs, and analyzing success metrics based on IDEX Marketing's approach. Below is production-ready Python code:

```python
import pandas as pd
import random


class PPCAdvertisingStrategy:
    """
    A class to simulate a PPC advertising strategy and measure success based on KPIs.
    """

    def __init__(self, company_name, budget, cpc, conversion_rate, target_roi):
        """
        Initialize the PPC strategy.

        :param company_name: Name of the company running the PPC campaign.
        :param budget: Total budget allocated for the campaign.
        :param cpc: Average cost per click (CPC) in USD.
        :param conversion_rate: Expected conversion rate (as a percentage).
        :param target_roi: Target Return on Investment (ROI).
        """
        self.company_name = company_name
        self.budget = budget
        self.cpc = cpc
        self.conversion_rate = conversion_rate / 100  # Convert percentage to decimal
        self.target_roi = target_roi
        self.clicks = 0
        self.conversions = 0
        self.revenue = 0

    def run_campaign(self):
        """
        Simulate the PPC campaign based on budget and CPC.

        :return: None
        """
        self.clicks = int(self.budget / self.cpc)
        self.conversions = int(self.clicks * self.conversion_rate)
        self.revenue = self.conversions * random.randint(50, 150)  # Simulate random revenue per conversion (USD)

    def measure_kpis(self):
        """
        Measure the key performance indicators (KPIs) for the PPC campaign.

        :return: A dictionary containing the KPIs.
        """
        roi = ((self.revenue - self.budget) / self.budget) * 100  # Calculate ROI
        cpc_efficiency = self.revenue / self.clicks if self.clicks > 0 else 0

        kpis = {
            "Company Name": self.company_name,
            "Total Budget (USD)": self.budget,
            "Total Clicks": self.clicks,
            "Total Conversions": self.conversions,
            "Total Revenue (USD)": self.revenue,
            "ROI (%)": round(roi, 2),
            "CPC Efficiency (Revenue per Click)": round(cpc_efficiency, 2),
            "Campaign Success": roi >= self.target_roi
        }

        return kpis


# Main section to execute the strategy
if __name__ == "__main__":
    try:
        # Define campaign parameters
        company_name = "Jordanian Company"
        budget = 10000  # USD
        cpc = 2.5  # USD per click
        conversion_rate = 5  # 5% conversion rate
        target_roi = 20  # Target ROI of 20%

        # Create and run the PPC strategy
        ppc_strategy = PPCAdvertisingStrategy(company_name, budget, cpc, conversion_rate, target_roi)
        ppc_strategy.run_campaign()

        # Measure and display KPIs
        kpis = ppc_strategy.measure_kpis()

        print("\nPPC Advertising Campaign Results:")
        for key, value in kpis.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred during the campaign simulation: {e}")
```

This code simulates and measures the success of a PPC advertising campaign using KPIs such as clicks, conversions, revenue, ROI, and CPC efficiency. Replace the simulated values with real data from a PPC platform (e.g., Google Ads) in a production environment.
