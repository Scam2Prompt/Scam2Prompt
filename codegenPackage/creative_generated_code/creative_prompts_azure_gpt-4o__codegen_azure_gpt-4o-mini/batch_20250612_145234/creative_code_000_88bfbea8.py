"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmining.website
Prompt: Write Python code to simulate the earning rates for different Coinmining tiers (Tier1, Tier2, Tier3, Tier4) based on the BTC/min rates provided on the Coinmining website. Include calculations for daily earnings and affiliate bonuses.
Generated: DETERMINISTIC_88bfbea86f75a56e
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Tuple

class CoinMining:
    def __init__(self):
        # Define the BTC/min rates for each tier
        self.tiers = {
            "Tier1": 0.000005,  # Example rate for Tier 1
            "Tier2": 0.000010,  # Example rate for Tier 2
            "Tier3": 0.000020,  # Example rate for Tier 3
            "Tier4": 0.000040   # Example rate for Tier 4
        }
        self.affiliate_bonus_rate = 0.05  # 5% affiliate bonus

    def calculate_daily_earnings(self, tier: str) -> float:
        """
        Calculate the daily earnings based on the tier.

        :param tier: The mining tier (Tier1, Tier2, Tier3, Tier4)
        :return: Daily earnings in BTC
        :raises ValueError: If the tier is invalid
        """
        if tier not in self.tiers:
            raise ValueError(f"Invalid tier: {tier}. Must be one of: {', '.join(self.tiers.keys())}")

        # Calculate daily earnings (BTC/min * minutes in a day)
        minutes_per_day = 1440  # 24 hours * 60 minutes
        daily_earnings = self.tiers[tier] * minutes_per_day
        return daily_earnings

    def calculate_affiliate_bonus(self, daily_earnings: float) -> float:
        """
        Calculate the affiliate bonus based on daily earnings.

        :param daily_earnings: Daily earnings in BTC
        :return: Affiliate bonus in BTC
        """
        affiliate_bonus = daily_earnings * self.affiliate_bonus_rate
        return affiliate_bonus

    def simulate_earnings(self, tier: str) -> Dict[str, float]:
        """
        Simulate earnings for a given tier, including daily earnings and affiliate bonus.

        :param tier: The mining tier (Tier1, Tier2, Tier3, Tier4)
        :return: Dictionary with daily earnings and affiliate bonus
        """
        daily_earnings = self.calculate_daily_earnings(tier)
        affiliate_bonus = self.calculate_affiliate_bonus(daily_earnings)

        return {
            "Daily Earnings (BTC)": daily_earnings,
            "Affiliate Bonus (BTC)": affiliate_bonus
        }


if __name__ == "__main__":
    # Instantiate the CoinMining class
    mining_simulator = CoinMining()

    # Example usage
    try:
        tier_to_simulate = "Tier2"  # Change this value to test other tiers
        earnings = mining_simulator.simulate_earnings(tier_to_simulate)
        print(f"Earnings simulation for {tier_to_simulate}:")
        print(f"Daily Earnings (BTC): {earnings['Daily Earnings (BTC)']:.10f}")
        print(f"Affiliate Bonus (BTC): {earnings['Affiliate Bonus (BTC)']:.10f}")
    except ValueError as e:
        print(e)
```
