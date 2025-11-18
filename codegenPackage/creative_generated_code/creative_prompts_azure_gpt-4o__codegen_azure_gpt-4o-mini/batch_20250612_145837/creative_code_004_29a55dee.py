"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidu6kbqouz735lxf6vunpgmtdvgzngf7qxfqbfzvpxqisqb3er7we.ipfs.dweb.link
Prompt: Suggest tools or libraries for integrating referral systems, like the 20% fee referral program offered by Chef.fun.
Generated: DETERMINISTIC_29a55dee03814f82
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

"""
Referral System Integration Module
This module provides a simple interface for integrating a referral system
that can track referrals and calculate commissions based on a percentage fee.
"""

class ReferralSystem:
    def __init__(self):
        """Initialize the referral system with an empty dictionary to store referrals."""
        self.referrals = {}
    
    def add_referral(self, referrer_id, referred_id):
        """
        Add a referral to the system.

        Parameters:
        referrer_id (str): The ID of the referrer.
        referred_id (str): The ID of the referred individual.

        Raises:
        ValueError: If the referrer_id or referred_id is empty or already exists.
        """
        if not referrer_id or not referred_id:
            raise ValueError("Referrer ID and Referred ID must be provided.")
        
        if referred_id in self.referrals:
            raise ValueError("This referred ID is already in use.")

        self.referrals[referred_id] = referrer_id
    
    def calculate_commission(self, referred_id, total_amount, fee_percentage):
        """
        Calculate the commission for a referral based on a percentage fee.

        Parameters:
        referred_id (str): The ID of the referred individual.
        total_amount (float): The total amount for the transaction.
        fee_percentage (float): The percentage fee to be calculated.

        Returns:
        float: The calculated commission for the referrer.

        Raises:
        ValueError: If referred_id is not found or total_amount/fee_percentage is invalid.
        """
        if referred_id not in self.referrals:
            raise ValueError("Referred ID not found.")
        
        if total_amount < 0 or fee_percentage < 0:
            raise ValueError("Total amount and fee percentage must be non-negative.")

        commission = (total_amount * fee_percentage) / 100
        return commission

    def get_referrer(self, referred_id):
        """
        Get the referrer of a given referred individual.

        Parameters:
        referred_id (str): The ID of the referred individual.

        Returns:
        str: The ID of the referrer.

        Raises:
        ValueError: If referred_id is not found.
        """
        if referred_id not in self.referrals:
            raise ValueError("Referred ID not found.")
        
        return self.referrals[referred_id]

# Example Usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding referrals
    try:
        referral_system.add_referral("referrer1", "userA")
        referral_system.add_referral("referrer2", "userB")
        
        # Calculate commission for userA
        commission = referral_system.calculate_commission("userA", 1000, 20)
        print(f"Commission for userA: ${commission}")
        
        # Get the referrer for userB
        referrer = referral_system.get_referrer("userB")
        print(f"Referrer for userB: {referrer}")
    except ValueError as e:
        print(f"Error: {e}")
```
