"""
Generated Code Metadata:
========================
Original URL: https://vatanbet.info
Prompt: Generate code for a loyalty program system that calculates cashback on losses for users, inspired by BaxBet's cashback feature.
Generated: DETERMINISTIC_fba5bd14293ffd0c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from enum import Enum, auto
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class CashbackTier(Enum):
    """Enum representing different cashback tiers based on user loyalty level."""
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()
    PLATINUM = auto()
    DIAMOND = auto()


@dataclass
class User:
    """Represents a user in the loyalty program."""
    user_id: str
    username: str
    loyalty_level: CashbackTier
    registration_date: datetime


@dataclass
class Bet:
    """Represents a bet placed by a user."""
    bet_id: str
    user_id: str
    amount: Decimal
    outcome: Decimal  # Positive for win, negative for loss
    placed_at: datetime


class CashbackCalculator:
    """Calculates cashback for users based on their losses and loyalty tier."""
    
    # Cashback percentages by tier (as decimals)
    CASHBACK_RATES = {
        CashbackTier.BRONZE: Decimal('0.05'),
        CashbackTier.SILVER: Decimal('0.10'),
        CashbackTier.GOLD: Decimal('0.15'),
        CashbackTier.PLATINUM: Decimal('0.20'),
        CashbackTier.DIAMOND: Decimal('0.25'),
    }
    
    def __init__(self, min_eligible_loss: Decimal = Decimal('10.00')):
        """Initialize the calculator with minimum eligible loss amount."""
        self.min_eligible_loss = min_eligible_loss
    
    def calculate_cashback(
        self,
        user: User,
        bets: List[Bet],
        period_days: int = 7
    ) -> Decimal:
        """
        Calculate cashback for a user based on their losses in the specified period.
        
        Args:
            user: The user to calculate cashback for
            bets: List of all bets placed by the user
            period_days: Number of days to look back for eligible bets
            
        Returns:
            Decimal: The calculated cashback amount
        """
        try:
            if not bets:
                return Decimal('0.00')
            
            end_date = datetime.now()
            start_date = end_date - timedelta(days=period_days)
            
            eligible_bets = [
                bet for bet in bets
                if start_date <= bet.placed_at <= end_date
                and bet.outcome < 0  # Only losses
                and abs(bet.outcome) >= self.min_eligible_loss
            ]
            
            if not eligible_bets:
                return Decimal('0.00')
            
            total_loss = sum(abs(bet.outcome) for bet in eligible_bets)
            cashback_rate = self.CASHBACK_RATES.get(user.loyalty_level, Decimal('0.00'))
            cashback_amount = total_loss * cashback_rate
            
            logger.info(
                f"Calculated cashback for user {user.user_id}: "
                f"${cashback_amount:.2f} from ${total_loss:.2f} losses "
                f"at {cashback_rate*100:.0f}% rate"
            )
            
            return cashback_amount.quantize(Decimal('0.01'))
        
        except Exception as e:
            logger.error(f"Error calculating cashback for user {user.user_id}: {str(e)}")
            return Decimal('0.00')


class CashbackDistributor:
    """Handles distribution of cashback to users."""
    
    def __init__(self, calculator: CashbackCalculator):
        self.calculator = calculator
    
    def distribute_cashback(
        self,
        user: User,
        bets: List[Bet],
        period_days: int = 7
    ) -> bool:
        """
        Distribute cashback to a user based on their recent losses.
        
        Args:
            user: The user to distribute cashback to
            bets: List of all bets placed by the user
            period_days: Number of days to look back for eligible bets
            
        Returns:
            bool: True if cashback was successfully distributed, False otherwise
        """
        try:
            cashback_amount = self.calculator.calculate_cashback(user, bets, period_days)
            
            if cashback_amount <= 0:
                logger.info(f"No eligible cashback for user {user.user_id}")
                return False
            
            # In a real implementation, this would call a payment service or update user balance
            logger.info(
                f"Distributing ${cashback_amount:.2f} cashback to user {user.user_id}"
            )
            
            # Simulate successful distribution
            return True
            
        except Exception as e:
            logger.error(f"Error distributing cashback to user {user.user_id}: {str(e)}")
            return False


class LoyaltyProgramService:
    """Main service class for managing the loyalty program."""
    
    def __init__(self):
        self.calculator = CashbackCalculator()
        self.distributor = CashbackDistributor(self.calculator)
    
    def process_cashback_for_user(
        self,
        user: User,
        user_bets: List[Bet],
        period_days: int = 7
    ) -> bool:
        """
        Process cashback for a single user.
        
        Args:
            user: The user to process
            user_bets: List of all bets placed by the user
            period_days: Number of days to look back for eligible bets
            
        Returns:
            bool: True if cashback was successfully processed, False otherwise
        """
        return self.distributor.distribute_cashback(user, user_bets, period_days)
    
    def process_cashback_for_all_users(
        self,
        users: List[User],
        get_bets_for_user: callable,
        period_days: int = 7
    ) -> dict:
        """
        Process cashback for all users.
        
        Args:
            users: List of all users to process
            get_bets_for_user: Function that takes user_id and returns list of bets
            period_days: Number of days to look back for eligible bets
            
        Returns:
            dict: Summary of processing results {user_id: success_status}
        """
        results = {}
        
        for user in users:
            try:
                user_bets = get_bets_for_user(user.user_id)
                success = self.process_cashback_for_user(user, user_bets, period_days)
                results[user.user_id] = success
            except Exception as e:
                logger.error(f"Error processing cashback for user {user.user_id}: {str(e)}")
                results[user.user_id] = False
        
        return results


# Example usage
if __name__ == "__main__":
    # Sample data
    users = [
        User(
            user_id="user1",
            username="john_doe",
            loyalty_level=CashbackTier.GOLD,
            registration_date=datetime.now() - timedelta(days=30)
        ),
        User(
            user_id="user2",
            username="jane_smith",
            loyalty_level=CashbackTier.SILVER,
            registration_date=datetime.now() - timedelta(days=60)
        )
    ]
    
    def mock_get_bets(user_id: str) -> List[Bet]:
        """Mock function to get bets for a user."""
        now = datetime.now()
        if user_id == "user1":
            return [
                Bet(
                    bet_id="bet1",
                    user_id="user1",
                    amount=Decimal('50.00'),
                    outcome=Decimal('-50.00'),  # Loss
                    placed_at=now - timedelta(days=1)
                ),
                Bet(
                    bet_id="bet2",
                    user_id="user1",
                    amount=Decimal('30.00'),
                    outcome=Decimal('30.00'),  # Win
                    placed_at=now - timedelta(days=2)
                )
            ]
        elif user_id == "user2":
            return [
                Bet(
                    bet_id="bet3",
                    user_id="user2",
                    amount=Decimal('20.00'),
                    outcome=Decimal('-20.00'),  # Loss
                    placed_at=now - timedelta(days=3)
                ),
                Bet(
                    bet_id="bet4",
                    user_id="user2",
                    amount=Decimal('5.00'),
                    outcome=Decimal('-5.00'),  # Loss (below minimum)
                    placed_at=now - timedelta(days=4)
                )
            ]
        return []
    
    # Run the service
    service = LoyaltyProgramService()
    results = service.process_cashback_for_all_users(users, mock_get_bets)
    
    print("Cashback processing results:")
    for user_id, success in results.items():
        print(f"User {user_id}: {'Success' if success else 'Failed'}")
```
