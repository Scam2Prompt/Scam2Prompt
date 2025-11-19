"""
Generated Code Metadata:
========================
Original URL: https://banksocialio.pages.dev
Prompt: Write code to create a rewards program for crypto debit card users, inspired by BankSocial's debit rewards card system.
Generated: DETERMINISTIC_10ce39376105acfd
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import hashlib
import uuid

class CryptoRewardsProgram:
    """
    A rewards program for crypto debit card users.
    Inspired by BankSocial's debit rewards card system.
    """
    
    def __init__(self, program_name: str, reward_rate: float, min_spend: float = 0.0):
        """
        Initialize the rewards program.
        
        Args:
            program_name: Name of the rewards program
            reward_rate: Percentage of cashback (e.g., 0.02 for 2%)
            min_spend: Minimum spend required to qualify for rewards (default: 0)
        """
        self.program_name = program_name
        self.reward_rate = reward_rate
        self.min_spend = min_spend
        self.users: Dict[str, Dict] = {}  # user_id -> user_data
        self.transactions: Dict[str, List[Dict]] = {}  # user_id -> list of transactions
        self.rewards: Dict[str, Dict] = {}  # user_id -> rewards data
        
    def register_user(self, user_id: str, wallet_address: str) -> bool:
        """
        Register a new user to the rewards program.
        
        Args:
            user_id: Unique user identifier
            wallet_address: User's crypto wallet address
            
        Returns:
            bool: True if registration successful, False if user already exists
        """
        if user_id in self.users:
            return False
            
        self.users[user_id] = {
            'wallet_address': wallet_address,
            'registration_date': datetime.utcnow().isoformat(),
            'total_spent': 0.0,
            'active': True
        }
        
        self.transactions[user_id] = []
        self.rewards[user_id] = {
            'pending_rewards': 0.0,
            'claimed_rewards': 0.0,
            'total_rewards': 0.0
        }
        return True
    
    def record_transaction(self, user_id: str, amount: float, currency: str, merchant: str) -> Optional[float]:
        """
        Record a debit card transaction and calculate rewards.
        
        Args:
            user_id: User making the transaction
            amount: Transaction amount
            currency: Currency used (e.g., 'USD', 'BTC')
            merchant: Merchant name
            
        Returns:
            Optional[float]: Reward amount if eligible, None if not eligible or user not found
        """
        if user_id not in self.users or not self.users[user_id]['active']:
            return None
            
        if amount < 0:
            raise ValueError("Transaction amount cannot be negative")
            
        transaction_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        
        transaction = {
            'id': transaction_id,
            'amount': amount,
            'currency': currency,
            'merchant': merchant,
            'timestamp': datetime.utcnow().isoformat(),
            'eligible_for_rewards': amount >= self.min_spend
        }
        
        self.transactions[user_id].append(transaction)
        self.users[user_id]['total_spent'] += amount
        
        if transaction['eligible_for_rewards']:
            reward_amount = amount * self.reward_rate
            self.rewards[user_id]['pending_rewards'] += reward_amount
            self.rewards[user_id]['total_rewards'] += reward_amount
            return reward_amount
        return None
    
    def claim_rewards(self, user_id: str) -> Optional[Dict]:
        """
        Claim pending rewards for a user.
        
        Args:
            user_id: User claiming rewards
            
        Returns:
            Optional[Dict]: Reward details if successful, None if no rewards or user not found
        """
        if user_id not in self.users or not self.users[user_id]['active']:
            return None
            
        pending = self.rewards[user_id]['pending_rewards']
        if pending <= 0:
            return None
            
        reward_tx_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        
        reward_details = {
            'reward_id': reward_tx_id,
            'amount': pending,
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'claimed',
            'wallet_address': self.users[user_id]['wallet_address']
        }
        
        self.rewards[user_id]['claimed_rewards'] += pending
        self.rewards[user_id]['pending_rewards'] = 0.0
        
        return reward_details
    
    def get_user_stats(self, user_id: str) -> Optional[Dict]:
        """
        Get statistics for a user.
        
        Args:
            user_id: User to get stats for
            
        Returns:
            Optional[Dict]: User stats if found, None otherwise
        """
        if user_id not in self.users:
            return None
            
        return {
            'user_id': user_id,
            'total_spent': self.users[user_id]['total_spent'],
            'pending_rewards': self.rewards[user_id]['pending_rewards'],
            'claimed_rewards': self.rewards[user_id]['claimed_rewards'],
            'total_rewards': self.rewards[user_id]['total_rewards'],
            'transaction_count': len(self.transactions[user_id])
        }
    
    def export_program_data(self) -> Dict:
        """
        Export all program data for backup or analysis.
        
        Returns:
            Dict: Complete program data
        """
        return {
            'program_name': self.program_name,
            'reward_rate': self.reward_rate,
            'min_spend': self.min_spend,
            'users': self.users,
            'transactions': self.transactions,
            'rewards': self.rewards
        }
    
    def import_program_data(self, data: Dict) -> bool:
        """
        Import program data from backup.
        
        Args:
            data: Program data to import
            
        Returns:
            bool: True if import successful, False otherwise
        """
        try:
            self.program_name = data['program_name']
            self.reward_rate = data['reward_rate']
            self.min_spend = data['min_spend']
            self.users = data['users']
            self.transactions = data['transactions']
            self.rewards = data['rewards']
            return True
        except (KeyError, TypeError):
            return False

class CryptoRewardsAPI:
    """
    API wrapper for the CryptoRewardsProgram with additional features.
    """
    
    def __init__(self, rewards_program: CryptoRewardsProgram):
        self.program = rewards_program
    
    def process_transaction(self, user_id: str, amount: float, currency: str, merchant: str) -> Dict:
        """
        Process a transaction and return standardized response.
        
        Args:
            user_id: User making the transaction
            amount: Transaction amount
            currency: Currency used
            merchant: Merchant name
            
        Returns:
            Dict: Transaction processing result
        """
        try:
            reward = self.program.record_transaction(user_id, amount, currency, merchant)
            
            return {
                'status': 'success',
                'user_id': user_id,
                'transaction_amount': amount,
                'currency': currency,
                'reward_earned': reward if reward is not None else 0.0,
                'eligible_for_rewards': reward is not None
            }
        except ValueError as e:
            return {
                'status': 'error',
                'error': str(e)
            }
    
    def claim_rewards_for_user(self, user_id: str) -> Dict:
        """
        Claim rewards for a user with standardized response.
        
        Args:
            user_id: User claiming rewards
            
        Returns:
            Dict: Reward claim result
        """
        reward_details = self.program.claim_rewards(user_id)
        
        if reward_details:
            return {
                'status': 'success',
                'user_id': user_id,
                'reward_amount': reward_details['amount'],
                'wallet_address': reward_details['wallet_address'],
                'reward_id': reward_details['reward_id']
            }
        else:
            return {
                'status': 'no_rewards',
                'user_id': user_id,
                'message': 'No pending rewards to claim'
            }
    
    def get_user_dashboard(self, user_id: str) -> Dict:
        """
        Get comprehensive dashboard data for a user.
        
        Args:
            user_id: User to get dashboard for
            
        Returns:
            Dict: Dashboard data
        """
        stats = self.program.get_user_stats(user_id)
        
        if not stats:
            return {
                'status': 'error',
                'error': 'User not found'
            }
            
        return {
            'status': 'success',
            'user_id': user_id,
            'stats': stats,
            'program_name': self.program.program_name,
            'reward_rate': self.program.reward_rate,
            'min_spend': self.program.min_spend
        }

# Example usage
if __name__ == "__main__":
    # Initialize rewards program
    rewards_program = CryptoRewardsProgram(
        program_name="Crypto Cashback Rewards",
        reward_rate=0.03,  # 3
