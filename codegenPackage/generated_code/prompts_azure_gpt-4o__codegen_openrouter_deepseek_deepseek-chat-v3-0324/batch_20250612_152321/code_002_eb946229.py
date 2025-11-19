"""
Generated Code Metadata:
========================
Original URL: https://claim-bits.com
Prompt: Generate a Python script to calculate referral earnings based on the Claim-Bits model of up to 200% of referral gains.
Generated: DETERMINISTIC_eb94622984e28272
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Tuple

class ReferralCalculator:
    """
    A class to calculate referral earnings based on the Claim-Bits model.
    Supports up to 200% of referral gains.
    """
    
    def __init__(self, base_earnings: float, referral_rate: float = 1.0, max_referral_rate: float = 2.0):
        """
        Initialize the ReferralCalculator with base parameters.
        
        Args:
            base_earnings: The base earnings amount before referrals.
            referral_rate: The referral rate (default 1.0 for 100%).
            max_referral_rate: The maximum allowed referral rate (default 2.0 for 200%).
        """
        if base_earnings < 0:
            raise ValueError("Base earnings must be non-negative.")
        if referral_rate < 0 or referral_rate > max_referral_rate:
            raise ValueError(f"Referral rate must be between 0 and {max_referral_rate}.")
        
        self.base_earnings = base_earnings
        self.referral_rate = referral_rate
        self.max_referral_rate = max_referral_rate
    
    def calculate_earnings(self, referrals: List[Tuple[str, float]]) -> Dict[str, float]:
        """
        Calculate total earnings including referral bonuses.
        
        Args:
            referrals: List of tuples containing (referral_id, referral_amount).
            
        Returns:
            Dictionary with 'total_earnings' and individual referral earnings.
        """
        if not referrals:
            return {
                'total_earnings': self.base_earnings,
                'referral_earnings': {}
            }
        
        referral_earnings = {}
        total_referral_bonus = 0.0
        
        for referral_id, amount in referrals:
            if amount < 0:
                raise ValueError(f"Referral amount for {referral_id} must be non-negative.")
            
            bonus = amount * self.referral_rate
            referral_earnings[referral_id] = bonus
            total_referral_bonus += bonus
        
        # Cap total referral bonus at max_referral_rate * base_earnings
        max_allowed_bonus = self.base_earnings * self.max_referral_rate
        if total_referral_bonus > max_allowed_bonus:
            scaling_factor = max_allowed_bonus / total_referral_bonus
            for ref_id in referral_earnings:
                referral_earnings[ref_id] *= scaling_factor
            total_referral_bonus = max_allowed_bonus
        
        return {
            'total_earnings': self.base_earnings + total_referral_bonus,
            'referral_earnings': referral_earnings
        }

def main():
    try:
        # Example usage
        calculator = ReferralCalculator(base_earnings=1000.0)
        
        referrals = [
            ("user1", 200.0),
            ("user2", 300.0),
            ("user3", 500.0)
        ]
        
        result = calculator.calculate_earnings(referrals)
        
        print("Base Earnings:", calculator.base_earnings)
        print("Referral Earnings:", result['referral_earnings'])
        print("Total Earnings:", result['total_earnings'])
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
