"""
Generated Code Metadata:
========================
Original URL: https://coinmining.website
Prompt: Write Python code to simulate the earning rates for different Coinmining tiers (Tier1, Tier2, Tier3, Tier4) based on the BTC/min rates provided on the Coinmining website. Include calculations for daily earnings and affiliate bonuses.
Generated: DETERMINISTIC_88bfbea86f75a56e
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CoinMining:
    def __init__(self, tier_rates):
        """
        Initialize the CoinMining class with tier rates.

        :param tier_rates: A dictionary containing the BTC/min rates for each tier.
        """
        self.tier_rates = tier_rates

    def calculate_daily_earnings(self, tier, minutes_per_day=1440):
        """
        Calculate the daily earnings for a given tier.

        :param tier: The tier for which to calculate earnings (e.g., 'Tier1').
        :param minutes_per_day: The number of minutes in a day (default is 1440).
        :return: Daily earnings in BTC.
        """
        try:
            rate = self.tier_rates[tier]
            daily_earnings = rate * minutes_per_day
            logging.info(f"Daily earnings for {tier}: {daily_earnings} BTC")
            return daily_earnings
        except KeyError:
            logging.error(f"Tier '{tier}' not found in tier rates.")
            raise ValueError(f"Invalid tier: {tier}")

    def calculate_affiliate_bonus(self, earnings, bonus_percentage):
        """
        Calculate the affiliate bonus based on earnings.

        :param earnings: The earnings to calculate the bonus from.
        :param bonus_percentage: The percentage of the earnings to be given as a bonus.
        :return: Affiliate bonus in BTC.
        """
        if not (0 <= bonus_percentage <= 100):
            logging.error("Bonus percentage must be between 0 and 100.")
            raise ValueError("Bonus percentage must be between 0 and 100.")
        
        bonus = (bonus_percentage / 100) * earnings
        logging.info(f"Affiliate bonus calculated: {bonus} BTC")
        return bonus

def main():
    # Define the BTC/min rates for each tier
    tier_rates = {
        'Tier1': 0.0001,
        'Tier2': 0.0002,
        'Tier3': 0.0003,
        'Tier4': 0.0004
    }

    # Create a CoinMining instance
    coin_mining = CoinMining(tier_rates)

    # Calculate daily earnings for each tier
    for tier in tier_rates.keys():
        try:
            daily_earnings = coin_mining.calculate_daily_earnings(tier)
            affiliate_bonus = coin_mining.calculate_affiliate_bonus(daily_earnings, bonus_percentage=10)
            logging.info(f"Total earnings for {tier} including affiliate bonus: {daily_earnings + affiliate_bonus} BTC")
        except ValueError as e:
            logging.error(e)

if __name__ == "__main__":
    main()
```
