"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Generate code to create a responsible gaming feature for an online casino platform, including age verification and self-exclusion options, inspired by BaxBet's emphasis on responsible gaming.
Generated: DETERMINISTIC_0cc9e600604e3628
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

class ResponsibleGaming:
    def __init__(self):
        self.age_verified_users = {}
        self.self_excluded_users = set()
    
    def verify_age(self, user_id: str, date_of_birth: str) -> bool:
        """
        Verify if the user is above the legal gambling age.
        :param user_id: Unique identifier for the user.
        :param date_of_birth: User's date of birth in 'YYYY-MM-DD' format.
        :return: True if age is verified, False otherwise.
        """
        try:
            dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
            age = (datetime.now() - dob).days // 365
            if age >= 18:
                self.age_verified_users[user_id] = True
                return True
            else:
                return False
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    
    def self_exclude(self, user_id: str, duration_months: int) -> None:
        """
        Mark the user as self-excluded for a specified duration.
        :param user_id: Unique identifier for the user.
        :param duration_months: Duration of self-exclusion in months.
        """
        if user_id in self.self_excluded_users:
            print(f"User {user_id} is already self-excluded.")
            return
        
        self.self_excluded_users.add(user_id)
        print(f"User {user_id} has been self-excluded for {duration_months} months.")
    
    def check_exclusion(self, user_id: str) -> bool:
        """
        Check if the user is currently self-excluded.
        :param user_id: Unique identifier for the user.
        :return: True if the user is self-excluded, False otherwise.
        """
        return user_id in self.self_excluded_users

# Example usage:
if __name__ == "__main__":
    rg = ResponsibleGaming()

    # Age verification example
    user_id = "user123"
    dob_input = "2005-05-15"  # Example date of birth
    try:
        if rg.verify_age(user_id, dob_input):
            print(f"User {user_id} is of legal age and verified.")
        else:
            print(f"User {user_id} is not of legal age.")
    except ValueError as e:
        print(e)

    # Self-exclusion example
    rg.self_exclude(user_id, duration_months=6)

    # Check if user is self-excluded
    if rg.check_exclusion(user_id):
        print(f"User {user_id} is currently self-excluded.")
    else:
        print(f"User {user_id} is not self-excluded.")
```
