"""
Generated Code Metadata:
========================
Original URL: https://starltoken.com
Prompt: Write code to create a loyalty program for a cryptocurrency casino, including tiered VIP benefits and cashback rewards, inspired by the STARL Token site.
Generated: DETERMINISTIC_a41df721c50650c0
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime, timedelta

class VIPLevel(Enum):
    """Enum representing VIP levels with corresponding benefits."""
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4
    DIAMOND = 5

@dataclass
class VIPBenefits:
    """Data class representing benefits for each VIP level."""
    cashback_rate: float
    withdrawal_fee_discount: float
    exclusive_bonuses: List[str]
    personal_account_manager: bool
    monthly_token_rewards: float

class User:
    """Class representing a user in the loyalty program."""
    def __init__(self, user_id: str, wallet_address: str):
        self.user_id = user_id
        self.wallet_address = wallet_address
        self.vip_level: VIPLevel = VIPLevel.BRONZE
        self.points: float = 0.0
        self.total_wagered: float = 0.0
        self.last_activity: datetime = datetime.now()
        self.cashback_earned: float = 0.0
        self.transaction_history: List[Dict] = []

    def update_wagered_amount(self, amount: float):
        """Update the total wagered amount and check for VIP level upgrade."""
        self.total_wagered += amount
        self.points += amount * 0.1  # 10% of wagered amount converted to points
        self.last_activity = datetime.now()
        self._check_vip_upgrade()
        self.transaction_history.append({
            'type': 'wager',
            'amount': amount,
            'timestamp': datetime.now().isoformat()
        })

    def _check_vip_upgrade(self):
        """Check if user qualifies for VIP level upgrade based on wagered amount."""
        if self.total_wagered >= 1000000:
            self.vip_level = VIPLevel.DIAMOND
        elif self.total_wagered >= 500000:
            self.vip_level = VIPLevel.PLATINUM
        elif self.total_wagered >= 100000:
            self.vip_level = VIPLevel.GOLD
        elif self.total_wagered >= 50000:
            self.vip_level = VIPLevel.SILVER

    def calculate_cashback(self) -> float:
        """Calculate cashback based on VIP level and wagered amount."""
        benefits = VIP_BENEFITS[self.vip_level]
        cashback = self.total_wagered * benefits.cashback_rate
        self.cashback_earned += cashback
        return cashback

    def claim_rewards(self) -> Dict:
        """Claim available rewards based on VIP level."""
        benefits = VIP_BENEFITS[self.vip_level]
        rewards = {
            'cashback': self.calculate_cashback(),
            'monthly_tokens': benefits.monthly_token_rewards,
            'timestamp': datetime.now().isoformat()
        }
        self.transaction_history.append({
            'type': 'reward_claim',
            'details': rewards,
            'timestamp': datetime.now().isoformat()
        })
        return rewards

    def get_benefits(self) -> Dict:
        """Get current VIP benefits for the user."""
        return {
            'vip_level': self.vip_level.name,
            'benefits': VIP_BENEFITS[self.vip_level].__dict__
        }

# VIP Benefits Configuration
VIP_BENEFITS = {
    VIPLevel.BRONZE: VIPBenefits(
        cashback_rate=0.01,
        withdrawal_fee_discount=0.0,
        exclusive_bonuses=[],
        personal_account_manager=False,
        monthly_token_rewards=0.0
    ),
    VIPLevel.SILVER: VIPBenefits(
        cashback_rate=0.02,
        withdrawal_fee_discount=0.1,
        exclusive_bonuses=['Weekly Free Spins'],
        personal_account_manager=False,
        monthly_token_rewards=50.0
    ),
    VIPLevel.GOLD: VIPBenefits(
        cashback_rate=0.03,
        withdrawal_fee_discount=0.2,
        exclusive_bonuses=['Weekly Free Spins', 'Monthly Bonus'],
        personal_account_manager=True,
        monthly_token_rewards=100.0
    ),
    VIPLevel.PLATINUM: VIPBenefits(
        cashback_rate=0.05,
        withdrawal_fee_discount=0.3,
        exclusive_bonuses=['Weekly Free Spins', 'Monthly Bonus', 'Exclusive Events'],
        personal_account_manager=True,
        monthly_token_rewards=250.0
    ),
    VIPLevel.DIAMOND: VIPBenefits(
        cashback_rate=0.07,
        withdrawal_fee_discount=0.5,
        exclusive_bonuses=['Weekly Free Spins', 'Monthly Bonus', 'Exclusive Events', 'Luxury Gifts'],
        personal_account_manager=True,
        monthly_token_rewards=500.0
    )
}

class LoyaltyProgram:
    """Main class managing the loyalty program."""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.token_name: str = "STARL"
    
    def register_user(self, user_id: str, wallet_address: str) -> User:
        """Register a new user in the loyalty program."""
        if user_id in self.users:
            raise ValueError("User already registered")
        user = User(user_id, wallet_address)
        self.users[user_id] = user
        return user
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieve a user by ID."""
        return self.users.get(user_id)
    
    def process_wager(self, user_id: str, amount: float) -> bool:
        """Process a wager and update user's loyalty status."""
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        if amount <= 0:
            raise ValueError("Invalid wager amount")
        user.update_wagered_amount(amount)
        return True
    
    def get_user_stats(self, user_id: str) -> Dict:
        """Get comprehensive stats for a user."""
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User not found")
        
        return {
            'user_id': user.user_id,
            'wallet_address': user.wallet_address,
            'vip_level': user.vip_level.name,
            'points': user.points,
            'total_wagered': user.total_wagered,
            'cashback_earned': user.cashback_earned,
            'last_activity': user.last_activity.isoformat(),
            'benefits': user.get_benefits()
        }
    
    def save_to_file(self, filename: str = 'loyalty_program.json'):
        """Save the current state of the loyalty program to a file."""
        data = {
            'token_name': self.token_name,
            'users': [
                {
                    'user_id': user.user_id,
                    'wallet_address': user.wallet_address,
                    'vip_level': user.vip_level.name,
                    'points': user.points,
                    'total_wagered': user.total_wagered,
                    'cashback_earned': user.cashback_earned,
                    'last_activity': user.last_activity.isoformat(),
                    'transaction_history': user.transaction_history
                }
                for user in self.users.values()
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_from_file(self, filename: str = 'loyalty_program.json'):
        """Load the loyalty program state from a file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.token_name = data.get('token_name', "STARL")
                self.users = {}
                
                for user_data in data.get('users', []):
                    user = User(
                        user_id=user_data['user_id'],
                        wallet_address=user_data['wallet_address']
                    )
                    user.vip_level = VIPLevel[user_data['vip_level']]
                    user.points = user_data['points']
                    user.total_wagered = user_data['total_wagered']
                    user.cashback_earned = user_data['cashback_earned']
                    user.last_activity = datetime.fromisoformat(user_data['last_activity'])
                    user.transaction_history = user_data.get('transaction_history', [])
                    self.users[user.user_id] = user
        except FileNotFoundError:
            # File doesn't exist yet, start fresh
            pass
        except json.JSONDecodeError:
            raise ValueError("Invalid loyalty program data file")

# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()
    program.load_from_file()
    
    # Register a new user
    user = program.register_user("user123", "0x742d35Cc6634C0532925a3b844Bc454e4438f44e")
    
    # Process some wagers
    program.process_wager("user123", 1000
