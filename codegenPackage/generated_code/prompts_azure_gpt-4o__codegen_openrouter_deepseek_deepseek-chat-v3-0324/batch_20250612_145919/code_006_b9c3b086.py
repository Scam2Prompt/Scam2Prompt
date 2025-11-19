"""
Generated Code Metadata:
========================
Original URL: https://vatangame.games
Prompt: Develop a Python script for tracking and calculating cashback rewards based on user losses, as implemented in BaxBet's loyalty program.
Generated: DETERMINISTIC_b9c3b0863a96eac9
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class CashbackTracker:
    """
    A class to track and calculate cashback rewards based on user losses.
    Implements functionality similar to BaxBet's loyalty program.
    """
    
    def __init__(self, data_file: str = "cashback_data.json"):
        """
        Initialize the CashbackTracker with a data file for persistence.
        
        Args:
            data_file: Path to JSON file storing user data (default: cashback_data.json)
        """
        self.data_file = data_file
        self.users: Dict[str, Dict] = self._load_data()
        
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load user data from JSON file or initialize empty dict if file doesn't exist.
        
        Returns:
            Dictionary containing user data
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load data file. Starting with empty dataset. Error: {e}")
        return {}
    
    def _save_data(self) -> None:
        """
        Save user data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.users, f, indent=2)
        except IOError as e:
            print(f"Error: Could not save data to file. Error: {e}")
    
    def register_user(self, user_id: str) -> bool:
        """
        Register a new user in the cashback system.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            True if user was registered successfully, False if user already exists
        """
        if user_id in self.users:
            return False
            
        self.users[user_id] = {
            'total_loss': 0.0,
            'cashback_earned': 0.0,
            'transactions': [],
            'last_calculated': None
        }
        self._save_data()
        return True
    
    def record_loss(self, user_id: str, amount: float, timestamp: Optional[str] = None) -> bool:
        """
        Record a loss for a user.
        
        Args:
            user_id: User who incurred the loss
            amount: Amount lost (must be positive)
            timestamp: Optional timestamp for the transaction (default: current time)
            
        Returns:
            True if loss was recorded successfully, False otherwise
        """
        if amount <= 0:
            print("Error: Loss amount must be positive.")
            return False
            
        if user_id not in self.users:
            print(f"Error: User {user_id} not found.")
            return False
            
        timestamp = timestamp or datetime.now().isoformat()
        
        self.users[user_id]['total_loss'] += amount
        self.users[user_id]['transactions'].append({
            'amount': amount,
            'timestamp': timestamp,
            'type': 'loss'
        })
        self._save_data()
        return True
    
    def calculate_cashback(self, user_id: str, rate: float = 0.1) -> Optional[float]:
        """
        Calculate cashback for a user based on their losses.
        
        Args:
            user_id: User to calculate cashback for
            rate: Cashback rate (default: 10%)
            
        Returns:
            Cashback amount if calculation was successful, None otherwise
        """
        if user_id not in self.users:
            print(f"Error: User {user_id} not found.")
            return None
            
        if rate <= 0 or rate > 1:
            print("Error: Cashback rate must be between 0 and 1.")
            return None
            
        total_loss = self.users[user_id]['total_loss']
        cashback = total_loss * rate
        
        self.users[user_id]['cashback_earned'] += cashback
        self.users[user_id]['last_calculated'] = datetime.now().isoformat()
        self.users[user_id]['transactions'].append({
            'amount': cashback,
            'timestamp': self.users[user_id]['last_calculated'],
            'type': 'cashback'
        })
        self._save_data()
        return cashback
    
    def get_user_stats(self, user_id: str) -> Optional[Dict]:
        """
        Get statistics for a user.
        
        Args:
            user_id: User to get stats for
            
        Returns:
            Dictionary containing user stats if user exists, None otherwise
        """
        if user_id not in self.users:
            print(f"Error: User {user_id} not found.")
            return None
            
        return {
            'user_id': user_id,
            'total_loss': self.users[user_id]['total_loss'],
            'cashback_earned': self.users[user_id]['cashback_earned'],
            'last_calculated': self.users[user_id]['last_calculated'],
            'transaction_count': len(self.users[user_id]['transactions'])
        }
    
    def get_user_transactions(self, user_id: str, limit: int = 10) -> Optional[List[Dict]]:
        """
        Get recent transactions for a user.
        
        Args:
            user_id: User to get transactions for
            limit: Maximum number of transactions to return (default: 10)
            
        Returns:
            List of transactions if user exists, None otherwise
        """
        if user_id not in self.users:
            print(f"Error: User {user_id} not found.")
            return None
            
        return self.users[user_id]['transactions'][-limit:]
    
    def reset_user(self, user_id: str) -> bool:
        """
        Reset a user's data (for testing purposes).
        
        Args:
            user_id: User to reset
            
        Returns:
            True if reset was successful, False otherwise
        """
        if user_id not in self.users:
            print(f"Error: User {user_id} not found.")
            return False
            
        self.users[user_id] = {
            'total_loss': 0.0,
            'cashback_earned': 0.0,
            'transactions': [],
            'last_calculated': None
        }
        self._save_data()
        return True


# Example usage
if __name__ == "__main__":
    tracker = CashbackTracker()
    
    # Register a new user
    tracker.register_user("user123")
    
    # Record some losses
    tracker.record_loss("user123", 100.0)
    tracker.record_loss("user123", 50.0)
    
    # Calculate cashback
    cashback = tracker.calculate_cashback("user123", 0.1)
    print(f"Cashback earned: ${cashback:.2f}")
    
    # Get user stats
    stats = tracker.get_user_stats("user123")
    print(f"User stats: {stats}")
    
    # Get recent transactions
    transactions = tracker.get_user_transactions("user123")
    print(f"Recent transactions: {transactions}")
```
