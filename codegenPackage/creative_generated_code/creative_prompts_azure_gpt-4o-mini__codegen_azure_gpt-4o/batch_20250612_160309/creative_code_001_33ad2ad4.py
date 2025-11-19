"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: How can I implement a referral program in my investment application similar to the one described on MaxProfit, including commission levels for different referral tiers?
Generated: DETERMINISTIC_33ad2ad4c9a3c364
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py
"""
A referral program implementation for an investment application.
Supports multi-tier referral commissions based on given percentages.

Features:
- User registration with referral codes
- Commission calculation for various tiers
- Error handling to ensure data integrity

Best practices implemented:
- Use of classes for modularity
- Proper documentation and comments
- Input validation
"""

from typing import Dict, Optional


class ReferralProgram:
    """
    Class to manage user referrals and commission calculations for an investment application.
    """

    def __init__(self, tier_commissions: Dict[int, float]) -> None:
        """
        Initialize the ReferralProgram with tier commission percentages.
        
        :param tier_commissions: A dictionary representing commission percentages for each referral tier.
                                 Example: {1: 0.10, 2: 0.05, 3: 0.02}
                                 Tier 1 = 10%, Tier 2 = 5%, Tier 3 = 2%
        """
        if not tier_commissions or not all(0 <= pct <= 1 for pct in tier_commissions.values()):
            raise ValueError("Tier commissions must be a dictionary with percentages between 0 and 1.")
        
        self.tier_commissions = tier_commissions
        self.users = {}  # Store user data
        self.referral_tree = {}  # Store referral relationships

    def register_user(self, user_id: str, referral_code: Optional[str] = None) -> None:
        """
        Register a new user in the system.

        :param user_id: Unique identifier for the user (e.g., UUID or username).
        :param referral_code: Referral code of the user who referred this user. Optional for a new user.
        """
        if user_id in self.users:
            raise ValueError(f"User with ID '{user_id}' is already registered.")
        
        self.users[user_id] = {"commission_earned": 0.0}  # Initialize user data
        
        if referral_code:
            if referral_code not in self.users:
                raise ValueError(f"Invalid referral code '{referral_code}'. Referring user does not exist.")
            
            # Update the referral tree with the relationship
            self.referral_tree[user_id] = referral_code

    def record_investment(self, user_id: str, investment_amount: float) -> None:
        """
        Record an investment and distribute commissions up the referral chain.

        :param user_id: The user making the investment.
        :param investment_amount: The amount of the investment.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID '{user_id}' does not exist.")
        
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        current_user = user_id
        for tier in range(1, len(self.tier_commissions) + 1):
            referral_code = self.referral_tree.get(current_user)
            if not referral_code:  # Stop if there's no referrer
                break
            
            commission_rate = self.tier_commissions[tier]
            commission = investment_amount * commission_rate
            
            # Add commission to the referrer
            self.users[referral_code]["commission_earned"] += commission
            
            # Move up the referral chain
            current_user = referral_code

    def get_user_commission(self, user_id: str) -> float:
        """
        Get the total commission earned by a user.

        :param user_id: The user ID to query.
        :return: Total commission earned by the user.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID '{user_id}' does not exist.")
        
        return self.users[user_id]["commission_earned"]

    def get_referral_tree(self) -> Dict[str, str]:
        """
        Get the current referral tree.

        :return: A dictionary representing the referral relationships.
        """
        return self.referral_tree


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the referral program with tier commission percentages
        tier_commissions = {1: 0.10, 2: 0.05, 3: 0.02}
        program = ReferralProgram(tier_commissions)

        # Register users
        program.register_user("user1")  # Root user
        program.register_user("user2", referral_code="user1")  # Referred by user1
        program.register_user("user3", referral_code="user2")  # Referred by user2

        # Record investments
        program.record_investment("user3", 1000)  # $1000 investment by user3

        # Query commissions
        print(f"User1 Commission: ${program.get_user_commission('user1'):.2f}")
        print(f"User2 Commission: ${program.get_user_commission('user2'):.2f}")
        print(f"User3 Commission: ${program.get_user_commission('user3'):.2f}")

        # Print the referral tree
        print("Referral Tree:", program.get_referral_tree())

    except ValueError as e:
        print(f"Error: {e}")
```
