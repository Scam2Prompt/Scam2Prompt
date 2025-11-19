"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Design a loyalty program, similar to BaxBet's, that rewards users with cashback and bonuses, using a Python-based data analysis tool to track user activity and reward eligibility.
Generated: DETERMINISTIC_c07a7c4cd08c886e
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LoyaltyProgram:
    """
    A loyalty program that rewards users with cashback and bonuses based on their activity.
    """

    def __init__(self, base_cashback_rate: float = 0.01, bonus_threshold: float = 1000.0):
        """
        Initialize the loyalty program with base cashback rate and bonus threshold.

        Args:
            base_cashback_rate: Base cashback rate (default: 1%)
            bonus_threshold: Minimum spend to qualify for bonus (default: $1000)
        """
        self.base_cashback_rate = base_cashback_rate
        self.bonus_threshold = bonus_threshold
        self.user_activity = pd.DataFrame(columns=['user_id', 'transaction_amount', 'transaction_date'])
        self.user_rewards = pd.DataFrame(columns=['user_id', 'cashback', 'bonus', 'last_updated'])

    def add_transaction(self, user_id: int, amount: float, transaction_date: Optional[datetime] = None) -> None:
        """
        Record a user transaction.

        Args:
            user_id: Unique identifier for the user
            amount: Transaction amount
            transaction_date: Date of transaction (default: current date)
        """
        try:
            if transaction_date is None:
                transaction_date = datetime.now()

            new_transaction = pd.DataFrame({
                'user_id': [user_id],
                'transaction_amount': [amount],
                'transaction_date': [transaction_date]
            })

            self.user_activity = pd.concat([self.user_activity, new_transaction], ignore_index=True)
            logger.info(f"Added transaction for user {user_id}: ${amount:.2f} on {transaction_date}")
        except Exception as e:
            logger.error(f"Error adding transaction: {e}")
            raise

    def calculate_rewards(self, user_id: int) -> Tuple[float, float]:
        """
        Calculate cashback and bonus for a user based on their activity.

        Args:
            user_id: User ID to calculate rewards for

        Returns:
            Tuple of (cashback, bonus) amounts
        """
        try:
            user_transactions = self.user_activity[self.user_activity['user_id'] == user_id]
            
            if user_transactions.empty:
                logger.warning(f"No transactions found for user {user_id}")
                return 0.0, 0.0

            total_spend = user_transactions['transaction_amount'].sum()
            cashback = total_spend * self.base_cashback_rate
            bonus = 50.0 if total_spend >= self.bonus_threshold else 0.0

            logger.info(f"Calculated rewards for user {user_id}: Cashback ${cashback:.2f}, Bonus ${bonus:.2f}")
            return cashback, bonus
        except Exception as e:
            logger.error(f"Error calculating rewards: {e}")
            raise

    def update_user_rewards(self, user_id: int) -> None:
        """
        Update the rewards for a user based on their current activity.

        Args:
            user_id: User ID to update rewards for
        """
        try:
            cashback, bonus = self.calculate_rewards(user_id)
            now = datetime.now()

            if user_id in self.user_rewards['user_id'].values:
                # Update existing record
                idx = self.user_rewards[self.user_rewards['user_id'] == user_id].index[0]
                self.user_rewards.at[idx, 'cashback'] = cashback
                self.user_rewards.at[idx, 'bonus'] = bonus
                self.user_rewards.at[idx, 'last_updated'] = now
            else:
                # Create new record
                new_reward = pd.DataFrame({
                    'user_id': [user_id],
                    'cashback': [cashback],
                    'bonus': [bonus],
                    'last_updated': [now]
                })
                self.user_rewards = pd.concat([self.user_rewards, new_reward], ignore_index=True)

            logger.info(f"Updated rewards for user {user_id}")
        except Exception as e:
            logger.error(f"Error updating rewards: {e}")
            raise

    def get_user_rewards(self, user_id: int) -> Dict[str, float]:
        """
        Get the current rewards for a user.

        Args:
            user_id: User ID to retrieve rewards for

        Returns:
            Dictionary with cashback and bonus amounts
        """
        try:
            user_reward = self.user_rewards[self.user_rewards['user_id'] == user_id]
            
            if user_reward.empty:
                logger.warning(f"No rewards found for user {user_id}")
                return {'cashback': 0.0, 'bonus': 0.0}

            return {
                'cashback': user_reward['cashback'].values[0],
                'bonus': user_reward['bonus'].values[0]
            }
        except Exception as e:
            logger.error(f"Error retrieving rewards: {e}")
            raise

    def analyze_user_activity(self, user_id: int) -> Dict[str, float]:
        """
        Analyze user activity and return key metrics.

        Args:
            user_id: User ID to analyze

        Returns:
            Dictionary with activity metrics
        """
        try:
            user_transactions = self.user_activity[self.user_activity['user_id'] == user_id]
            
            if user_transactions.empty:
                logger.warning(f"No transactions found for user {user_id}")
                return {
                    'total_spend': 0.0,
                    'transaction_count': 0,
                    'avg_transaction': 0.0
                }

            total_spend = user_transactions['transaction_amount'].sum()
            transaction_count = len(user_transactions)
            avg_transaction = total_spend / transaction_count

            return {
                'total_spend': total_spend,
                'transaction_count': transaction_count,
                'avg_transaction': avg_transaction
            }
        except Exception as e:
            logger.error(f"Error analyzing user activity: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize loyalty program
    program = LoyaltyProgram(base_cashback_rate=0.02, bonus_threshold=500.0)
    
    # Add some transactions
    program.add_transaction(1, 100.0, datetime.now() - timedelta(days=3))
    program.add_transaction(1, 200.0, datetime.now() - timedelta(days=2))
    program.add_transaction(1, 300.0, datetime.now() - timedelta(days=1))
    program.add_transaction(2, 50.0, datetime.now())
    
    # Update and get rewards
    program.update_user_rewards(1)
    program.update_user_rewards(2)
    
    # Print rewards
    print("User 1 rewards:", program.get_user_rewards(1))
    print("User 2 rewards:", program.get_user_rewards(2))
    
    # Analyze activity
    print("User 1 activity:", program.analyze_user_activity(1))
```
