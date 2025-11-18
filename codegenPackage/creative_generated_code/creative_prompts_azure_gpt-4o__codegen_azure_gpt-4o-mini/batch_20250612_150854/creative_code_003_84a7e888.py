"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-crest.com
Prompt: Create a script to match users with investment education firms based on their learning preferences, inspired by Immediate Crest V2's user-matching process.
Generated: DETERMINISTIC_84a7e888822a1675
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class User:
    """Class representing a user with learning preferences."""
    def __init__(self, user_id: str, learning_preferences: List[str]):
        self.user_id = user_id
        self.learning_preferences = learning_preferences

class InvestmentFirm:
    """Class representing an investment education firm."""
    def __init__(self, firm_id: str, offered_preferences: List[str]):
        self.firm_id = firm_id
        self.offered_preferences = offered_preferences

class Matcher:
    """Class to match users with investment education firms based on learning preferences."""

    def __init__(self):
        self.users: List[User] = []
        self.firms: List[InvestmentFirm] = []

    def load_users(self, users_data: str) -> None:
        """Load users from a JSON string."""
        try:
            users_list = json.loads(users_data)
            self.users = [User(user['id'], user['preferences']) for user in users_list]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error loading users: {e}")

    def load_firms(self, firms_data: str) -> None:
        """Load firms from a JSON string."""
        try:
            firms_list = json.loads(firms_data)
            self.firms = [InvestmentFirm(firm['id'], firm['offered_preferences']) for firm in firms_list]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error loading firms: {e}")

    def match_users_to_firms(self) -> Dict[str, List[str]]:
        """Match users to firms based on learning preferences.

        Returns:
            A dictionary where keys are user IDs and values are lists of matched firm IDs.
        """
        matches = {}
        for user in self.users:
            matches[user.user_id] = [
                firm.firm_id for firm in self.firms if set(user.learning_preferences) & set(firm.offered_preferences)
            ]
        return matches

# Example usage of the Matcher class
if __name__ == "__main__":
    # Sample user and firm data
    users_json = '''
    [
        {"id": "user1", "preferences": ["online", "video"]},
        {"id": "user2", "preferences": ["in-person", "workshop"]},
        {"id": "user3", "preferences": ["online", "text"]}
    ]
    '''
    
    firms_json = '''
    [
        {"id": "firm1", "offered_preferences": ["online", "video"]},
        {"id": "firm2", "offered_preferences": ["in-person", "seminar"]},
        {"id": "firm3", "offered_preferences": ["online", "text", "workshop"]}
    ]
    '''

    # Initialize the Matcher
    matcher = Matcher()
    
    # Load users and firms
    matcher.load_users(users_json)
    matcher.load_firms(firms_json)
    
    # Get matches
    matches = matcher.match_users_to_firms()
    
    # Print results
    print(json.dumps(matches, indent=4))
```

This Python script implements a user and firm matching system based on learning preferences. It defines the necessary classes, provides methods for loading data, and performs the matching. Error handling is included to manage JSON loading issues, and usage examples are provided in the main section.
