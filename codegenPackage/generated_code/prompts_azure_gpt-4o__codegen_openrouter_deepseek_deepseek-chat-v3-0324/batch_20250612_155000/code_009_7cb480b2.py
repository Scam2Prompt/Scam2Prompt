"""
Generated Code Metadata:
========================
Original URL: https://ethminer.world
Prompt: Write a Python script to estimate the total ETH earnings for a user who advertises their referral link on platforms like A-ads.com, based on hypothetical referral conversion rates.
Generated: DETERMINISTIC_7cb480b254c85cba
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
from typing import Optional, Union

class ETHReferralEarningsEstimator:
    """
    Estimates total ETH earnings from referral links based on conversion rates.
    """
    
    def __init__(self, eth_per_referral: float, base_conversion_rate: float = 0.01):
        """
        Initialize the estimator with ETH per referral and base conversion rate.
        
        Args:
            eth_per_referral: ETH earned per successful referral
            base_conversion_rate: Default conversion rate (1% as default)
        """
        self.eth_per_referral = eth_per_referral
        self.base_conversion_rate = base_conversion_rate
        
    def calculate_earnings(
        self,
        impressions: int,
        custom_conversion_rate: Optional[float] = None
    ) -> Union[float, str]:
        """
        Calculate estimated ETH earnings based on impressions and conversion rate.
        
        Args:
            impressions: Number of ad impressions
            custom_conversion_rate: Optional custom conversion rate (overrides base)
            
        Returns:
            Estimated ETH earnings or error message
        """
        try:
            if impressions <= 0:
                return "Impressions must be a positive integer"
            
            conversion_rate = custom_conversion_rate if custom_conversion_rate else self.base_conversion_rate
            
            if not 0 <= conversion_rate <= 1:
                return "Conversion rate must be between 0 and 1"
            
            referrals = impressions * conversion_rate
            earnings = referrals * self.eth_per_referral
            return round(earnings, 8)  # Round to 8 decimal places (standard for ETH)
            
        except Exception as e:
            return f"Error in calculation: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="ETH Referral Earnings Estimator")
    parser.add_argument(
        "--eth-per-referral",
        type=float,
        required=True,
        help="ETH earned per successful referral"
    )
    parser.add_argument(
        "--impressions",
        type=int,
        required=True,
        help="Number of ad impressions"
    )
    parser.add_argument(
        "--conversion-rate",
        type=float,
        help="Custom conversion rate (0-1). Default is 0.01 (1%%)"
    )
    
    args = parser.parse_args()
    
    estimator = ETHReferralEarningsEstimator(args.eth_per_referral)
    result = estimator.calculate_earnings(args.impressions, args.conversion_rate)
    
    if isinstance(result, str):
        print(f"Error: {result}")
    else:
        print(f"Estimated ETH earnings: {result} ETH")

if __name__ == "__main__":
    main()
```
