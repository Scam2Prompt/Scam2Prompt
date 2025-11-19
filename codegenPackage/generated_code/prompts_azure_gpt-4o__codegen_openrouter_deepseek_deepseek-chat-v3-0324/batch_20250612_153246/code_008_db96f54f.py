"""
Generated Code Metadata:
========================
Original URL: https://mywanderloop.com
Prompt: Write code to implement a no-deposit bonus system for an online casino platform, based on the examples provided by myWanderLoop.
Generated: DETERMINISTIC_db96f54f0500dd83
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
from datetime import datetime, timedelta
from typing import Optional, List, Dict

class NoDepositBonus:
    """
    Represents a no-deposit bonus for a casino platform.
    """
    def __init__(
        self,
        bonus_id: str,
        amount: float,
        currency: str,
        wagering_requirement: float,
        expiry_days: int,
        max_withdrawal: Optional[float] = None,
        min_games: Optional[int] = None,
        allowed_games: Optional[List[str]] = None
    ):
        """
        Initialize a no-deposit bonus.

        Args:
            bonus_id: Unique identifier for the bonus
            amount: Bonus amount
            currency: Currency of the bonus
            wagering_requirement: Wagering requirement multiplier
            expiry_days: Number of days until bonus expires
            max_withdrawal: Maximum withdrawal amount from bonus (optional)
            min_games: Minimum games to play before withdrawal (optional)
            allowed_games: List of game IDs allowed with this bonus (optional)
        """
        self.bonus_id = bonus_id
        self.amount = amount
        self.currency = currency
        self.wagering_requirement = wagering_requirement
        self.expiry_date = datetime.now() + timedelta(days=expiry_days)
        self.max_withdrawal = max_withdrawal
        self.min_games = min_games
        self.allowed_games = allowed_games or []
        self.is_active = True
        self.created_at = datetime.now()

    def is_expired(self) -> bool:
        """Check if the bonus has expired."""
        return datetime.now() > self.expiry_date

    def is_eligible_for_withdrawal(self, total_wagered: float, games_played: int) -> bool:
        """
        Check if bonus funds can be withdrawn.

        Args:
            total_wagered: Total amount wagered by player
            games_played: Number of games played by player

        Returns:
            bool: True if eligible for withdrawal
        """
        if not self.is_active or self.is_expired():
            return False
        
        wagering_met = total_wagered >= (self.amount * self.wagering_requirement)
        games_met = self.min_games is None or games_played >= self.min_games
        
        return wagering_met and games_met

    def calculate_withdrawal_amount(self, current_balance: float) -> float:
        """
        Calculate the maximum withdrawal amount from bonus funds.

        Args:
            current_balance: Player's current bonus balance

        Returns:
            float: Withdrawable amount
        """
        if self.max_withdrawal is None:
            return current_balance
        return min(current_balance, self.max_withdrawal)

class NoDepositBonusSystem:
    """
    Manages no-deposit bonuses for a casino platform.
    """
    def __init__(self):
        self.active_bonuses: Dict[str, NoDepositBonus] = {}
        self.claimed_bonuses: Dict[str, Dict[str, NoDepositBonus]] = {}  # user_id -> {bonus_id: bonus}

    def generate_bonus_id(self) -> str:
        """Generate a unique bonus ID."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def create_bonus(
        self,
        amount: float,
        currency: str,
        wagering_requirement: float,
        expiry_days: int,
        max_withdrawal: Optional[float] = None,
        min_games: Optional[int] = None,
        allowed_games: Optional[List[str]] = None
    ) -> NoDepositBonus:
        """
        Create a new no-deposit bonus.

        Args:
            amount: Bonus amount
            currency: Currency of the bonus
            wagering_requirement: Wagering requirement multiplier
            expiry_days: Number of days until bonus expires
            max_withdrawal: Maximum withdrawal amount from bonus (optional)
            min_games: Minimum games to play before withdrawal (optional)
            allowed_games: List of game IDs allowed with this bonus (optional)

        Returns:
            NoDepositBonus: The created bonus object
        """
        bonus_id = self.generate_bonus_id()
        bonus = NoDepositBonus(
            bonus_id=bonus_id,
            amount=amount,
            currency=currency,
            wagering_requirement=wagering_requirement,
            expiry_days=expiry_days,
            max_withdrawal=max_withdrawal,
            min_games=min_games,
            allowed_games=allowed_games
        )
        self.active_bonuses[bonus_id] = bonus
        return bonus

    def claim_bonus(self, user_id: str, bonus_id: str) -> Optional[NoDepositBonus]:
        """
        Claim a no-deposit bonus for a user.

        Args:
            user_id: ID of the user claiming the bonus
            bonus_id: ID of the bonus to claim

        Returns:
            Optional[NoDepositBonus]: The claimed bonus if successful, None otherwise
        """
        if bonus_id not in self.active_bonuses:
            return None
        
        bonus = self.active_bonuses[bonus_id]
        
        if bonus.is_expired() or not bonus.is_active:
            return None
        
        if user_id not in self.claimed_bonuses:
            self.claimed_bonuses[user_id] = {}
        
        if bonus_id in self.claimed_bonuses[user_id]:
            return None  # User already claimed this bonus
        
        self.claimed_bonuses[user_id][bonus_id] = bonus
        return bonus

    def get_user_bonuses(self, user_id: str) -> List[NoDepositBonus]:
        """
        Get all bonuses claimed by a user.

        Args:
            user_id: ID of the user

        Returns:
            List[NoDepositBonus]: List of claimed bonuses
        """
        return list(self.claimed_bonuses.get(user_id, {}).values())

    def check_withdrawal_eligibility(
        self,
        user_id: str,
        bonus_id: str,
        total_wagered: float,
        games_played: int
    ) -> bool:
        """
        Check if a user can withdraw funds from a bonus.

        Args:
            user_id: ID of the user
            bonus_id: ID of the bonus
            total_wagered: Total amount wagered by player
            games_played: Number of games played by player

        Returns:
            bool: True if eligible for withdrawal
        """
        if user_id not in self.claimed_bonuses or bonus_id not in self.claimed_bonuses[user_id]:
            return False
        
        bonus = self.claimed_bonuses[user_id][bonus_id]
        return bonus.is_eligible_for_withdrawal(total_wagered, games_played)

    def calculate_withdrawal_amount(
        self,
        user_id: str,
        bonus_id: str,
        current_balance: float
    ) -> float:
        """
        Calculate the maximum withdrawal amount from bonus funds.

        Args:
            user_id: ID of the user
            bonus_id: ID of the bonus
            current_balance: Player's current bonus balance

        Returns:
            float: Withdrawable amount
        """
        if user_id not in self.claimed_bonuses or bonus_id not in self.claimed_bonuses[user_id]:
            return 0.0
        
        bonus = self.claimed_bonuses[user_id][bonus_id]
        return bonus.calculate_withdrawal_amount(current_balance)

    def expire_bonus(self, bonus_id: str) -> bool:
        """
        Mark a bonus as expired.

        Args:
            bonus_id: ID of the bonus to expire

        Returns:
            bool: True if bonus was successfully expired
        """
        if bonus_id not in self.active_bonuses:
            return False
        
        self.active_bonuses[bonus_id].is_active = False
        return True

    def get_active_bonuses(self) -> List[NoDepositBonus]:
        """
        Get all active bonuses.

        Returns:
            List[NoDepositBonus]: List of active bonuses
        """
        return [b for b in self.active_bonuses.values() if b.is_active and not b.is_expired()]
```
