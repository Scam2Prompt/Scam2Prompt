"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherroll.cash
Prompt: Suggest tools or libraries for implementing a referral and affiliate program system for an online casino, inspired by the affiliate program described on "etherroll.cash."
Generated: DETERMINISTIC_a86a397177c007b0
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_affiliate_program.py

class AffiliateProgram:
    def __init__(self):
        """Initialize the affiliate program with an empty list of affiliates."""
        self.affiliates = {}
    
    def add_affiliate(self, affiliate_id, commission_rate):
        """
        Add a new affiliate to the program.
        
        Parameters:
            affiliate_id (str): Unique identifier for the affiliate.
            commission_rate (float): Commission rate for the affiliate.

        Raises:
            ValueError: If the affiliate_id already exists or commission_rate is invalid.
        """
        if affiliate_id in self.affiliates:
            raise ValueError(f"Affiliate ID {affiliate_id} already exists.")
        if not (0 <= commission_rate <= 1):
            raise ValueError("Commission rate must be between 0 and 1.")
        
        self.affiliates[affiliate_id] = {
            'commission_rate': commission_rate,
            'referrals': [],
            'earnings': 0.0
        }
    
    def record_referral(self, affiliate_id, referral_id, amount_won):
        """
        Record a referral made by an affiliate.
        
        Parameters:
            affiliate_id (str): The ID of the affiliate making the referral.
            referral_id (str): The ID of the referred player.
            amount_won (float): The total amount won by the referred player.
        
        Raises:
            ValueError: If the affiliate_id does not exist.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError(f"Affiliate ID {affiliate_id} does not exist.")
        
        # Record the referral
        self.affiliates[affiliate_id]['referrals'].append(referral_id)
        
        # Calculate earnings for the affiliate
        commission = amount_won * self.affiliates[affiliate_id]['commission_rate']
        self.affiliates[affiliate_id]['earnings'] += commission
    
    def get_affiliate_info(self, affiliate_id):
        """
        Get information about a specific affiliate.
        
        Parameters:
            affiliate_id (str): The ID of the affiliate.
        
        Returns:
            dict: Information about the affiliate including commission rate, referrals, and earnings.
        
        Raises:
            ValueError: If the affiliate_id does not exist.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError(f"Affiliate ID {affiliate_id} does not exist.")
        
        return self.affiliates[affiliate_id]
    
    def payout(self, affiliate_id):
        """
        Process a payout for an affiliate based on their earnings.
        
        Parameters:
            affiliate_id (str): The ID of the affiliate to payout.
        
        Returns:
            float: The amount paid out to the affiliate.
        
        Raises:
            ValueError: If the affiliate_id does not exist or has no earnings.
        """
        if affiliate_id not in self.affiliates:
            raise ValueError(f"Affiliate ID {affiliate_id} does not exist.")
        
        earnings = self.affiliates[affiliate_id]['earnings']
        if earnings <= 0:
            raise ValueError("No earnings available for payout.")
        
        # Reset earnings after payout
        self.affiliates[affiliate_id]['earnings'] = 0.0
        return earnings

# Example usage
if __name__ == "__main__":
    program = AffiliateProgram()
    
    try:
        program.add_affiliate("aff1", 0.1)
        program.record_referral("aff1", "player1", 1000)
        info = program.get_affiliate_info("aff1")
        print(f"Affiliate Info: {info}")
        
        payout_amount = program.payout("aff1")
        print(f"Payout Amount: ${payout_amount:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
