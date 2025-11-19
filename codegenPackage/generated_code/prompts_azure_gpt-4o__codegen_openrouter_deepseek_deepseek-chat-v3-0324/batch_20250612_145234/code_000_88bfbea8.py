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
import math
from typing import Dict, Tuple

class CoinMiningSimulator:
    """
    Simulates earning rates for different Coinmining tiers based on BTC/min rates.
    Includes calculations for daily earnings and affiliate bonuses.
    """

    def __init__(self):
        """
        Initialize the simulator with tier rates and other constants.
        """
        # BTC/min rates for each tier (example values - should be updated with actual rates)
        self.tier_rates = {
            'Tier1': 0.00000010,  # BTC/min
            'Tier2': 0.00000025,
            'Tier3': 0.00000050,
            'Tier4': 0.00000100
        }

        # Affiliate bonus percentages (percentage of referee's earnings)
        self.affiliate_bonus = {
            'direct': 0.05,    # 5% for direct referrals
            'indirect': 0.02   # 2% for indirect referrals (level 2)
        }

        self.minutes_per_day = 24 * 60

    def calculate_daily_earnings(self, tier: str) -> float:
        """
        Calculate daily earnings for a given tier.
        
        Args:
            tier: The mining tier (Tier1, Tier2, Tier3, Tier4)
            
        Returns:
            float: Daily earnings in BTC
            
        Raises:
            ValueError: If invalid tier is provided
        """
        if tier not in self.tier_rates:
            raise ValueError(f"Invalid tier: {tier}. Valid tiers are: {list(self.tier_rates.keys())}")
        
        return self.tier_rates[tier] * self.minutes_per_day

    def calculate_affiliate_earnings(
        self, 
        tier: str, 
        direct_referees: int = 0, 
        indirect_referees: int = 0
    ) -> Tuple[float, Dict[str, float]]:
        """
        Calculate affiliate earnings from direct and indirect referrals.
        
        Args:
            tier: The mining tier of the user
            direct_referees: Number of direct referrals
            indirect_referees: Number of indirect referrals (level 2)
            
        Returns:
            Tuple[float, Dict[str, float]]: 
                - Total affiliate earnings (BTC/day)
                - Breakdown of earnings by referral type
                
        Raises:
            ValueError: If invalid tier is provided
        """
        if tier not in self.tier_rates:
            raise ValueError(f"Invalid tier: {tier}. Valid tiers are: {list(self.tier_rates.keys())}")

        daily_earnings = self.calculate_daily_earnings(tier)
        
        # Calculate earnings from each referral type
        direct_earnings = daily_earnings * self.affiliate_bonus['direct'] * direct_referees
        indirect_earnings = daily_earnings * self.affiliate_bonus['indirect'] * indirect_referees
        
        breakdown = {
            'direct': direct_earnings,
            'indirect': indirect_earnings
        }
        
        total_affiliate_earnings = direct_earnings + indirect_earnings
        
        return (total_affiliate_earnings, breakdown)

    def calculate_total_earnings(
        self, 
        tier: str, 
        direct_referees: int = 0, 
        indirect_referees: int = 0
    ) -> Dict[str, float]:
        """
        Calculate total daily earnings including mining and affiliate bonuses.
        
        Args:
            tier: The mining tier of the user
            direct_referees: Number of direct referrals
            indirect_referees: Number of indirect referrals (level 2)
            
        Returns:
            Dict[str, float]: Dictionary containing:
                - mining_earnings: Base mining earnings
                - affiliate_earnings: Total from referrals
                - total_earnings: Sum of mining and affiliate
                - affiliate_breakdown: Detailed affiliate earnings
        """
        mining_earnings = self.calculate_daily_earnings(tier)
        affiliate_earnings, affiliate_breakdown = self.calculate_affiliate_earnings(
            tier, direct_referees, indirect_referees
        )
        
        return {
            'mining_earnings': mining_earnings,
            'affiliate_earnings': affiliate_earnings,
            'total_earnings': mining_earnings + affiliate_earnings,
            'affiliate_breakdown': affiliate_breakdown
        }

    def convert_to_fiat(self, btc_amount: float, btc_price: float) -> float:
        """
        Convert BTC amount to fiat currency.
        
        Args:
            btc_amount: Amount in BTC
            btc_price: Current BTC price in fiat
            
        Returns:
            float: Value in fiat currency
        """
        return btc_amount * btc_price


# Example usage
if __name__ == "__main__":
    simulator = CoinMiningSimulator()
    
    # Example 1: Basic mining earnings
    tier = 'Tier3'
    daily_btc = simulator.calculate_daily_earnings(tier)
    print(f"Daily BTC earnings for {tier}: {daily_btc:.8f} BTC")
    
    # Example 2: With affiliate bonuses
    results = simulator.calculate_total_earnings(
        tier='Tier2',
        direct_referees=5,
        indirect_referees=10
    )
    print("\nDetailed earnings with affiliate bonuses:")
    for key, value in results.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value:.8f} BTC")
        else:
            print(f"{key}: {value:.8f} BTC")
    
    # Example 3: Convert to USD (assuming BTC price is $50,000)
    btc_price = 50000
    usd_value = simulator.convert_to_fiat(results['total_earnings'], btc_price)
    print(f"\nTotal daily earnings in USD (BTC at ${btc_price:,.2f}): ${usd_value:.2f}")
```
