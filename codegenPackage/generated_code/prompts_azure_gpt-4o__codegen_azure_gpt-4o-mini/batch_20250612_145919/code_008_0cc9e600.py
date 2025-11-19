"""
Generated Code Metadata:
========================
Original URL: https://vatanplatform.bet
Prompt: Generate code to create a responsible gaming feature for an online casino platform, including age verification and self-exclusion options, inspired by BaxBet's emphasis on responsible gaming.
Generated: DETERMINISTIC_0cc9e600604e3628
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime, timedelta

class ResponsibleGaming:
    def __init__(self):
        # Initialize user data
        self.users = {}
    
    def register_user(self, username, birthdate):
        """
        Register a new user with a username and birthdate.
        
        :param username: str - The username of the user
        :param birthdate: str - The birthdate of the user in 'YYYY-MM-DD' format
        :raises ValueError: If the user is underage (under 18 years)
        """
        if not self.is_valid_username(username):
            raise ValueError("Invalid username. It must be alphanumeric and between 3-20 characters.")
        
        if not self.is_valid_birthdate(birthdate):
            raise ValueError("Invalid birthdate format. Use 'YYYY-MM-DD'.")
        
        age = self.calculate_age(birthdate)
        if age < 18:
            raise ValueError("User must be at least 18 years old to register.")
        
        self.users[username] = {
            'birthdate': birthdate,
            'self_excluded': False,
            'exclusion_end_date': None
        }
        print(f"User {username} registered successfully.")

    def is_valid_username(self, username):
        """Check if the username is valid."""
        return re.match(r'^[a-zA-Z0-9]{3,20}$', username) is not None

    def is_valid_birthdate(self, birthdate):
        """Check if the birthdate is in the correct format."""
        try:
            datetime.strptime(birthdate, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def calculate_age(self, birthdate):
        """Calculate the age of the user based on their birthdate."""
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def self_exclude(self, username, duration_days):
        """
        Enable self-exclusion for a user for a specified duration.
        
        :param username: str - The username of the user
        :param duration_days: int - The number of days for self-exclusion
        :raises ValueError: If the user is not registered or already self-excluded
        """
        if username not in self.users:
            raise ValueError("User not found.")
        
        if self.users[username]['self_excluded']:
            raise ValueError("User is already self-excluded.")
        
        self.users[username]['self_excluded'] = True
        self.users[username]['exclusion_end_date'] = datetime.today() + timedelta(days=duration_days)
        print(f"User {username} has been self-excluded for {duration_days} days.")

    def check_exclusion_status(self, username):
        """
        Check if a user is currently self-excluded.
        
        :param username: str - The username of the user
        :return: bool - True if the user is self-excluded, False otherwise
        """
        if username not in self.users:
            raise ValueError("User not found.")
        
        user_data = self.users[username]
        if user_data['self_excluded']:
            if datetime.today() > user_data['exclusion_end_date']:
                user_data['self_excluded'] = False
                user_data['exclusion_end_date'] = None
                print(f"User {username}'s self-exclusion period has ended.")
                return False
            return True
        return False

# Example usage
if __name__ == "__main__":
    rg = ResponsibleGaming()
    try:
        rg.register_user("john_doe", "2000-01-01")
        rg.self_exclude("john_doe", 30)
        print(rg.check_exclusion_status("john_doe"))
    except ValueError as e:
        print(f"Error: {e}")
```
