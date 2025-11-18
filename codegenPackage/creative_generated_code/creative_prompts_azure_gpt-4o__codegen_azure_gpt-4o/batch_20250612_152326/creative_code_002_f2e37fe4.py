"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-buck.pages.dev
Prompt: Develop a referral system in Python that mimics CoinBuck's multi-level referral bonus structure, including tracking referral tasks and KYC completion.
Generated: DETERMINISTIC_f2e37fe41a358bb8
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from collections import defaultdict

class ReferralSystem:
    def __init__(self):
        # Stores user data with referral info
        self.users = {}
        # Tracks tasks completed for each user
        self.tasks_completed = defaultdict(list)
        # Tracks users who have completed KYC
        self.kyc_completed = set()

    def create_user(self, username, referrer=None):
        """Creates a new user and registers them in the system."""
        if username in self.users:
            raise ValueError("Username already exists.")

        user_id = str(uuid.uuid4())
        self.users[username] = {
            'user_id': user_id,
            'referrer': referrer,
            'referrals': [],
            'bonus': 0
        }

        # Attach the referral to the referrer if provided
        if referrer:
            if referrer not in self.users:
                raise ValueError("Referrer does not exist.")
            self.users[referrer]['referrals'].append(username)

        return user_id

    def complete_task(self, username, task_name):
        """Tracks task completion for a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        if task_name in self.tasks_completed[username]:
            raise ValueError("Task has already been completed.")
        
        self.tasks_completed[username].append(task_name)
        self._update_bonus(username)

    def complete_kyc(self, username):
        """Marks user as having completed KYC."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        if username in self.kyc_completed:
            raise ValueError("KYC has already been completed.")

        self.kyc_completed.add(username)
        self._update_bonus(username)

    def _update_bonus(self, username):
        """Calculates and updates bonus for a user and their referrer tree."""
        if username not in self.users:
            raise ValueError("User does not exist.")

        user = self.users[username]
        if username in self.kyc_completed and len(self.tasks_completed[username]) > 0:
            # Award bonus for direct user activity
            user['bonus'] += 10

            # Award bonuses to referrer chain
            referrer = user['referrer']
            level = 1
            while referrer and level <= 3:  # Multi-level referral bonus (up to 3 levels)
                self.users[referrer]['bonus'] += max(10 - (level * 3), 0)  # Decreasing bonus per level
                referrer = self.users[referrer]['referrer']
                level += 1

    def get_user_info(self, username):
        """Returns detailed information about a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")

        user = self.users[username]
        return {
            'user_id': user['user_id'],
            'referrer': user['referrer'],
            'referrals': user['referrals'],
            'bonus': user['bonus'],
            'tasks_completed': self.tasks_completed[username],
            'kyc_completed': username in self.kyc_completed
        }

    def get_all_users(self):
        """Returns information about all users in the system."""
        return {username: self.get_user_info(username) for username in self.users}


# Example usage
if __name__ == "__main__":
    try:
        system = ReferralSystem()
        
        # Create users
        user1 = system.create_user("Alice")
        user2 = system.create_user("Bob", referrer="Alice")
        user3 = system.create_user("Charlie", referrer="Bob")

        # Complete tasks and KYC
        system.complete_task("Alice", "Task1")
        system.complete_kyc("Alice")
        system.complete_task("Bob", "Task1")
        system.complete_kyc("Bob")
        system.complete_task("Charlie", "Task1")
        system.complete_kyc("Charlie")
        
        # Fetch user info
        print(system.get_user_info("Alice"))
        print(system.get_user_info("Bob"))
        print(system.get_user_info("Charlie"))
        
        # Fetch all users
        print(system.get_all_users())

    except Exception as e:
        print(f"Error: {e}")
```
