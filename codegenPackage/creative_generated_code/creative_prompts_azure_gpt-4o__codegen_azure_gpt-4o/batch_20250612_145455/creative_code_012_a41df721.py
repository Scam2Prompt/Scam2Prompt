"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starltoken.com
Prompt: Write code to create a loyalty program for a cryptocurrency casino, including tiered VIP benefits and cashback rewards, inspired by the STARL Token site.
Generated: DETERMINISTIC_a41df721c50650c0
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
from typing import Dict, List

class User:
    """
    Represents a user in the loyalty program.
    """
    def __init__(self, user_id: int, total_wagered: Decimal = Decimal(0)):
        self.user_id = user_id
        self.total_wagered = total_wagered
        self.vip_tier = "Bronze"  # Default VIP tier
        self.cashback_balance = Decimal(0)  # Cashback balance

    def update_total_wagered(self, amount: Decimal):
        """Updates the total wagered amount by the user."""
        self.total_wagered += amount

    def update_vip_tier(self):
        """Updates the user's VIP tier based on total wagered."""
        if self.total_wagered >= Decimal(10000):
            self.vip_tier = "Platinum"
        elif self.total_wagered >= Decimal(5000):
            self.vip_tier = "Gold"
        elif self.total_wagered >= Decimal(1000):
            self.vip_tier = "Silver"
        else:
            self.vip_tier = "Bronze"

    def add_cashback(self, amount: Decimal):
        """Adds cashback rewards to the user's account."""
        self.cashback_balance += amount

    def claim_cashback(self) -> Decimal:
        """Allows the user to claim their accumulated cashback balance."""
        cashback_to_claim = self.cashback_balance
        self.cashback_balance = Decimal(0)
        return cashback_to_claim


class LoyaltyProgram:
    """
    Represents the loyalty program for the cryptocurrency casino.
    """
    VIP_TIERS: Dict[str, Decimal] = {
        "Bronze": Decimal(0.01),  # 1% cashback
        "Silver": Decimal(0.02),  # 2% cashback
        "Gold": Decimal(0.03),    # 3% cashback
        "Platinum": Decimal(0.05) # 5% cashback
    }

    def __init__(self):
        self.users: Dict[int, User] = {}  # Store all users by their user_id

    def register_user(self, user_id: int):
        """
        Registers a new user to the loyalty program.
        If the user already exists, raise an exception.
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        self.users[user_id] = User(user_id)

    def process_bet(self, user_id: int, bet_amount: Decimal):
        """
        Processes a bet made by a user, updates their wagered amount, VIP tier,
        and calculates cashback rewards.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} is not registered.")

        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive.")

        user = self.users[user_id]
        user.update_total_wagered(bet_amount)
        user.update_vip_tier()

        # Calculate and add cashback based on VIP tier
        cashback_rate = self.VIP_TIERS[user.vip_tier]
        cashback_reward = bet_amount * cashback_rate
        user.add_cashback(cashback_reward)

    def get_user_status(self, user_id: int) -> Dict:
        """
        Retrieves the current status of a user, including VIP tier, total wagered,
        and cashback balance.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} is not registered.")

        user = self.users[user_id]
        return {
            "user_id": user.user_id,
            "vip_tier": user.vip_tier,
            "total_wagered": user.total_wagered,
            "cashback_balance": user.cashback_balance
        }

    def claim_cashback(self, user_id: int) -> Decimal:
        """
        Allows a user to claim their cashback balance.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} is not registered.")

        user = self.users[user_id]
        return user.claim_cashback()


# Example usage
if __name__ == '__main__':
    casino_loyalty = LoyaltyProgram()

    # Register users
    casino_loyalty.register_user(1)
    casino_loyalty.register_user(2)

    # Process bets
    casino_loyalty.process_bet(1, Decimal('1500'))
    casino_loyalty.process_bet(2, Decimal('6000'))

    # Get user statuses
    print(casino_loyalty.get_user_status(1))
    print(casino_loyalty.get_user_status(2))

    # Claim cashback
    print(f"User 1 claimed cashback: {casino_loyalty.claim_cashback(1)}")
    print(casino_loyalty.get_user_status(1))
```
