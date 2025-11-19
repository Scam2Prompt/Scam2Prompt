"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: Design a promotional campaign for สล็อตเว็บตรง, focusing on attracting new players with free sign-up bonuses and no turnover requirements.
Generated: DETERMINISTIC_5f92b84c65f15796
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random
import string

class PromotionalCampaign:
    """
    A class to manage promotional campaigns for a direct web slot (สล็อตเว็บตรง) platform.
    Features include free sign-up bonuses and no turnover requirements.
    """
    
    def __init__(self, campaign_name: str, start_date: datetime, end_date: datetime):
        """
        Initialize the promotional campaign.
        
        Args:
            campaign_name (str): Name of the campaign
            start_date (datetime): Campaign start date
            end_date (datetime): Campaign end date
        """
        self.campaign_name = campaign_name
        self.start_date = start_date
        self.end_date = end_date
        self.participants: List[Dict] = []
        self.bonus_amount = 100  # Default bonus amount in credits
        
    def generate_promo_code(self, length: int = 8) -> str:
        """
        Generate a random promotional code for new players.
        
        Args:
            length (int): Length of the promo code (default: 8)
            
        Returns:
            str: Generated promo code
        """
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    
    def register_player(self, player_id: str, player_name: str, registration_date: datetime) -> Optional[Dict]:
        """
        Register a new player to the campaign and issue a bonus.
        
        Args:
            player_id (str): Unique player ID
            player_name (str): Player's name
            registration_date (datetime): Date of registration
            
        Returns:
            Optional[Dict]: Player details with bonus info if successful, None if campaign is not active
        """
        if not self.is_campaign_active(registration_date):
            return None
            
        promo_code = self.generate_promo_code()
        player_data = {
            'player_id': player_id,
            'player_name': player_name,
            'registration_date': registration_date,
            'promo_code': promo_code,
            'bonus_amount': self.bonus_amount,
            'bonus_claimed': False,
            'turnover_requirement': 0  # No turnover requirement
        }
        
        self.participants.append(player_data)
        return player_data
    
    def is_campaign_active(self, current_date: datetime) -> bool:
        """
        Check if the campaign is currently active.
        
        Args:
            current_date (datetime): Date to check against campaign period
            
        Returns:
            bool: True if campaign is active, False otherwise
        """
        return self.start_date <= current_date <= self.end_date
    
    def get_campaign_summary(self) -> Dict:
        """
        Generate a summary of the campaign performance.
        
        Returns:
            Dict: Campaign summary including participant count and bonus distribution
        """
        total_participants = len(self.participants)
        total_bonus = sum(p['bonus_amount'] for p in self.participants if p['bonus_claimed'])
        
        return {
            'campaign_name': self.campaign_name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'total_participants': total_participants,
            'total_bonus_distributed': total_bonus,
            'active': self.is_campaign_active(datetime.now())
        }
    
    def claim_bonus(self, player_id: str) -> bool:
        """
        Mark a player's bonus as claimed.
        
        Args:
            player_id (str): Player ID to claim bonus for
            
        Returns:
            bool: True if bonus was successfully claimed, False otherwise
        """
        for player in self.participants:
            if player['player_id'] == player_id:
                if not player['bonus_claimed']:
                    player['bonus_claimed'] = True
                    return True
        return False


# Example usage
if __name__ == "__main__":
    # Initialize a campaign running for 30 days
    campaign = PromotionalCampaign(
        campaign_name="Summer Slot Bonanza",
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=30)
    )
    
    # Register a new player
    player = campaign.register_player(
        player_id="player123",
        player_name="John Doe",
        registration_date=datetime.now()
    )
    
    if player:
        print(f"Player registered with bonus: {player['bonus_amount']} credits")
        print(f"Promo code: {player['promo_code']}")
        
        # Claim the bonus
        if campaign.claim_bonus("player123"):
            print("Bonus successfully claimed!")
    
    # Get campaign summary
    summary = campaign.get_campaign_summary()
    print(f"\nCampaign Summary: {summary}")
```
