"""
Generated Code Metadata:
========================
Original URL: https://crypto4rex360.com
Prompt: Generate a Python script to simulate the referral program earnings described on Crypto 4Rex 360, based on user referrals and their respective investment amounts.
Generated: DETERMINISTIC_43f60e16bfd1907d
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class ReferralProgram:
    """
    Simulates a referral program earnings calculator for Crypto 4Rex 360.
    Calculates earnings based on user referrals and their investment amounts.
    """
    
    def __init__(self, commission_rate: float = 0.05, levels: int = 3):
        """
        Initialize the referral program with commission rate and referral levels.
        
        Args:
            commission_rate (float): Commission rate per referral level (default: 0.05 or 5%)
            levels (int): Number of referral levels to calculate (default: 3)
        """
        if commission_rate <= 0 or commission_rate > 1:
            raise ValueError("Commission rate must be between 0 and 1")
        if levels <= 0:
            raise ValueError("Number of levels must be positive")
            
        self.commission_rate = commission_rate
        self.levels = levels
        self.users = {}  # type: Dict[str, Dict]
        
    def add_user(self, user_id: str, referrer_id: Optional[str] = None, investment: float = 0.0) -> None:
        """
        Add a user to the referral program.
        
        Args:
            user_id (str): Unique identifier for the user
            referrer_id (str, optional): ID of the referring user. Defaults to None.
            investment (float): Investment amount by the user. Defaults to 0.0.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists")
            
        if referrer_id is not None and referrer_id not in self.users:
            raise ValueError(f"Referrer {referrer_id} does not exist")
            
        if investment < 0:
            raise ValueError("Investment amount cannot be negative")
            
        self.users[user_id] = {
            'referrer': referrer_id,
            'investment': investment,
            'referrals': []
        }
        
        if referrer_id is not None:
            self.users[referrer_id]['referrals'].append(user_id)
    
    def calculate_earnings(self, user_id: str) -> Dict[int, float]:
        """
        Calculate earnings for a user based on their referral network.
        
        Args:
            user_id (str): User ID to calculate earnings for
            
        Returns:
            Dict[int, float]: Dictionary mapping level to earnings amount
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist")
            
        earnings = {level: 0.0 for level in range(1, self.levels + 1)}
        current_level_users = [user_id]
        
        for level in range(1, self.levels + 1):
            next_level_users = []
            
            for current_user in current_level_users:
                for referral in self.users[current_user]['referrals']:
                    investment = self.users[referral]['investment']
                    earnings[level] += investment * self.commission_rate
                    next_level_users.append(referral)
                    
            current_level_users = next_level_users
            
        return earnings
    
    def get_total_earnings(self, user_id: str) -> float:
        """
        Get total earnings across all levels for a user.
        
        Args:
            user_id (str): User ID to calculate total earnings for
            
        Returns:
            float: Total earnings across all levels
        """
        earnings = self.calculate_earnings(user_id)
        return sum(earnings.values())
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the current state of the referral program to a JSON file.
        
        Args:
            filename (str): Path to the output file
        """
        with open(filename, 'w') as f:
            json.dump({
                'commission_rate': self.commission_rate,
                'levels': self.levels,
                'users': self.users
            }, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'ReferralProgram':
        """
        Load a referral program from a JSON file.
        
        Args:
            filename (str): Path to the input file
            
        Returns:
            ReferralProgram: Loaded referral program instance
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            
        program = cls(data['commission_rate'], data['levels'])
        program.users = data['users']
        return program

# Example usage
if __name__ == "__main__":
    try:
        # Initialize referral program
        program = ReferralProgram(commission_rate=0.05, levels=3)
        
        # Add users with their referrers and investments
        program.add_user("user1", investment=1000.0)
        program.add_user("user2", "user1", 500.0)
        program.add_user("user3", "user2", 300.0)
        program.add_user("user4", "user3", 200.0)
        
        # Calculate and display earnings
        user_id = "user1"
        earnings = program.calculate_earnings(user_id)
        total = program.get_total_earnings(user_id)
        
        print(f"Earnings for {user_id}:")
        for level, amount in earnings.items():
            print(f"Level {level}: ${amount:.2f}")
        print(f"Total earnings: ${total:.2f}")
        
        # Save to file
        program.save_to_file("referral_program.json")
        
    except Exception as e:
        print(f"Error: {e}")
```
