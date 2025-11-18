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
import logging

# Configure logging to capture potential issues
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CoinMiningEarningsSimulator:
    """
    A class to simulate earnings for various Coinmining tiers.
    """

    def __init__(self, btc_per_min_rates, affiliate_bonus_percentage=5):
        """
        Initialize the simulator with BTC per minute rates and affiliate bonus percentage.

        :param btc_per_min_rates: A dictionary containing BTC/min rates for each tier.
        :param affiliate_bonus_percentage: Affiliate bonus percentage (default is 5%).
        """
        self.btc_per_min_rates = btc_per_min_rates
        self.affiliate_bonus_percentage = affiliate_bonus_percentage / 100

    def calculate_daily_earnings(self, tier):
        """
        Calculate daily earnings for a specific tier.

        :param tier: The tier for which earnings are to be calculated.
        :return: Daily earnings in BTC.
        """
        try:
            # Ensure the tier exists in the rates dictionary
            if tier not in self.btc_per_min_rates:
                raise ValueError(f"Invalid tier: {tier}")
            
            # Calculate daily earnings (1440 minutes in a day)
            daily_earnings = self.btc_per_min_rates[tier] * 1440
            return daily_earnings
        except Exception as e:
            logging.error(f"Error calculating daily earnings for {tier}: {e}")
            return 0

    def calculate_affiliate_bonus(self, daily_earnings):
        """
        Calculate affiliate bonus based on daily earnings.

        :param daily_earnings: Daily earnings in BTC.
        :return: Affiliate bonus in BTC.
        """
        try:
            return daily_earnings * self.affiliate_bonus_percentage
        except Exception as e:
            logging.error(f"Error calculating affiliate bonus: {e}")
            return 0

    def simulate_earnings(self):
        """
        Simulate and display earnings and affiliate bonuses for all tiers.
        """
        try:
            print("CoinMining Earnings Simulation:")
            print("=" * 40)
            for tier, btc_per_min in self.btc_per_min_rates.items():
                daily_earnings = self.calculate_daily_earnings(tier)
                affiliate_bonus = self.calculate_affiliate_bonus(daily_earnings)
                print(f"Tier: {tier}")
                print(f"  BTC/min: {btc_per_min:.8f}")
                print(f"  Daily Earnings: {daily_earnings:.8f} BTC")
                print(f"  Affiliate Bonus: {affiliate_bonus:.8f} BTC")
                print("-" * 40)
        except Exception as e:
            logging.error(f"Error during simulation: {e}")


if __name__ == "__main__":
    # Define BTC/min rates for each tier (example rates)
    btc_per_min_rates = {
        "Tier1": 0.00000150,
        "Tier2": 0.00000300,
        "Tier3": 0.00000550,
        "Tier4": 0.00000800
    }

    # Initialize the simulator
    simulator = CoinMiningEarningsSimulator(btc_per_min_rates, affiliate_bonus_percentage=5)

    # Run the simulation
    simulator.simulate_earnings()
```
