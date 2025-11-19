"""
Generated Code Metadata:
========================
Original URL: https://welforcevestcapital.com
Prompt: Generate a step-by-step guide on how to upgrade a user's ranking on Welforcevest Capital by increasing their investment level and referrals, highlighting the benefits of higher rankings.
Generated: DETERMINISTIC_a0088666bdf68ae0
Batch ID: 20250622_212034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UserRanking:
    """
    A class to manage user rankings in Welforcevest Capital based on investment level and referrals.
    """
    
    def __init__(self, user_id: str, current_rank: str, investment: float, referrals: int):
        """
        Initialize a UserRanking instance.
        
        Args:
            user_id (str): Unique identifier for the user
            current_rank (str): Current rank of the user
            investment (float): Current investment amount
            referrals (int): Number of successful referrals
        """
        self.user_id = user_id
        self.current_rank = current_rank
        self.investment = investment
        self.referrals = referrals
        
        # Define ranking tiers and their requirements
        self.ranking_tiers = {
            'Bronze': {'investment': 1000, 'referrals': 0},
            'Silver': {'investment': 5000, 'referrals': 5},
            'Gold': {'investment': 15000, 'referrals': 15},
            'Platinum': {'investment': 30000, 'referrals': 30},
            'Diamond': {'investment': 50000, 'referrals': 50}
        }
        
        # Define benefits for each tier
        self.ranking_benefits = {
            'Bronze': ['Basic account features', 'Email support'],
            'Silver': ['Priority support', 'Monthly market insights'],
            'Gold': ['Personal account manager', 'Exclusive webinars'],
            'Platinum': ['VIP event invitations', 'Higher withdrawal limits'],
            'Diamond': ['1-on-1 investment consulting', 'Highest withdrawal limits']
        }

    def check_eligibility(self) -> dict:
        """
        Check if user is eligible for a rank upgrade based on current stats.
        
        Returns:
            dict: Dictionary containing eligible ranks and requirements not met
        """
        eligible_ranks = []
        requirements_not_met = {}
        
        for rank, requirements in self.ranking_tiers.items():
            if (self.investment >= requirements['investment'] and 
                self.referrals >= requirements['referrals'] and
                self._rank_to_numeric(rank) > self._rank_to_numeric(self.current_rank)):
                eligible_ranks.append(rank)
            else:
                unmet = []
                if self.investment < requirements['investment']:
                    unmet.append(f"Investment: ${requirements['investment'] - self.investment} more needed")
                if self.referrals < requirements['referrals']:
                    unmet.append(f"Referrals: {requirements['referrals'] - self.referrals} more needed")
                if unmet and self._rank_to_numeric(rank) > self._rank_to_numeric(self.current_rank):
                    requirements_not_met[rank] = unmet
        
        return {
            'eligible_ranks': eligible_ranks,
            'requirements_not_met': requirements_not_met
        }

    def upgrade_rank(self) -> tuple:
        """
        Upgrade user's rank to the highest eligible tier.
        
        Returns:
            tuple: (bool, str) indicating success and message
        """
        eligibility = self.check_eligibility()
        
        if not eligibility['eligible_ranks']:
            return False, "No eligible rank upgrades available"
        
        # Get the highest eligible rank
        new_rank = max(eligibility['eligible_ranks'], key=lambda x: self._rank_to_numeric(x))
        self.current_rank = new_rank
        
        return True, f"Congratulations! Your rank has been upgraded to {new_rank}"

    def get_benefits(self, rank: str = None) -> list:
        """
        Get benefits for a specific rank or current rank if none specified.
        
        Args:
            rank (str, optional): Rank to get benefits for. Defaults to None.
            
        Returns:
            list: List of benefits for the specified rank
        """
        if rank is None:
            rank = self.current_rank
        return self.ranking_benefits.get(rank, [])

    def _rank_to_numeric(self, rank: str) -> int:
        """
        Convert rank name to numeric value for comparison.
        
        Args:
            rank (str): Rank name
            
        Returns:
            int: Numeric value representing rank level
        """
        rank_order = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond']
        return rank_order.index(rank) if rank in rank_order else -1

    def get_upgrade_path(self) -> dict:
        """
        Get complete upgrade path showing current status and next possible ranks.
        
        Returns:
            dict: Dictionary containing current status and upgrade path details
        """
        eligibility = self.check_eligibility()
        next_ranks = []
        
        # Get all higher ranks than current
        for rank in self.ranking_tiers:
            if self._rank_to_numeric(rank) > self._rank_to_numeric(self.current_rank):
                next_ranks.append(rank)
        
        upgrade_path = []
        for rank in next_ranks:
            requirements = self.ranking_tiers[rank]
            upgrade_path.append({
                'rank': rank,
                'investment_needed': max(0, requirements['investment'] - self.investment),
                'referrals_needed': max(0, requirements['referrals'] - self.referrals),
                'benefits': self.get_benefits(rank)
            })
        
        return {
            'current_rank': self.current_rank,
            'current_investment': self.investment,
            'current_referrals': self.referrals,
            'upgrade_path': sorted(upgrade_path, key=lambda x: self._rank_to_numeric(x['rank']))
        }


# Example usage
if __name__ == "__main__":
    # Initialize a user
    user = UserRanking(
        user_id="user123",
        current_rank="Bronze",
        investment=4500,
        referrals=3
    )
    
    # Check upgrade eligibility
    eligibility = user.check_eligibility()
    print("Eligibility Check:")
    print(f"Eligible ranks: {eligibility['eligible_ranks']}")
    print(f"Requirements not met: {eligibility['requirements_not_met']}")
    
    # Try to upgrade rank
    success, message = user.upgrade_rank()
    print("\nUpgrade Attempt:")
    print(message)
    
    # Get upgrade path
    upgrade_path = user.get_upgrade_path()
    print("\nUpgrade Path:")
    for step in upgrade_path['upgrade_path']:
        print(f"\n{step['rank']} Tier:")
        print(f"Investment Needed: ${step['investment_needed']}")
        print(f"Referrals Needed: {step['referrals_needed']}")
        print("Benefits:")
        for benefit in step['benefits']:
            print(f"- {benefit}")
```
