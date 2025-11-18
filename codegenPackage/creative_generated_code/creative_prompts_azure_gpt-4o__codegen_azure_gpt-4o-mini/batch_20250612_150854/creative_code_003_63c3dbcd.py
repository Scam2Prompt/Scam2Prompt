"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.org
Prompt: Create a script that matches users to investment education firms based on their preferences, mimicking the Immediate Orbirex matching system.
Generated: DETERMINISTIC_63c3dbcd48a883a2
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
    """Represents a user with preferences for matching to an investment education firm."""
    def __init__(self, user_id: int, preferences: Dict[str, Any]):
        self.user_id = user_id
        self.preferences = preferences

class Firm:
    """Represents an investment education firm with specific attributes."""
    def __init__(self, firm_id: int, attributes: Dict[str, Any]):
        self.firm_id = firm_id
        self.attributes = attributes

class Matcher:
    """Handles the matching of users to investment education firms based on preferences."""
    
    def __init__(self, users: List[User], firms: List[Firm]):
        self.users = users
        self.firms = firms
        
    def match_users_to_firms(self) -> Dict[int, List[int]]:
        """Matches users to firms based on their preferences.
        
        Returns:
            A dictionary where keys are user IDs and values are lists of matched firm IDs.
        """
        matches = {}
        for user in self.users:
            matches[user.user_id] = self.find_matching_firms(user)
        return matches

    def find_matching_firms(self, user: User) -> List[int]:
        """Finds firms that match a given user's preferences.
        
        Args:
            user (User): The user for whom we are finding matches.

        Returns:
            A list of firm IDs that match the user's preferences.
        """
        matched_firms = []
        for firm in self.firms:
            if self.is_match(user.preferences, firm.attributes):
                matched_firms.append(firm.firm_id)
        return matched_firms

    def is_match(self, user_prefs: Dict[str, Any], firm_attrs: Dict[str, Any]) -> bool:
        """Determines if a user's preferences match a firm's attributes.
        
        Args:
            user_prefs (Dict[str, Any]): The preferences of the user.
            firm_attrs (Dict[str, Any]): The attributes of the firm.

        Returns:
            bool: True if there is a match, False otherwise.
        """
        # Example matching logic based on preferences
        return all(user_prefs.get(key) == firm_attrs.get(key) for key in user_prefs if key in firm_attrs)

def load_data(users_file: str, firms_file: str) -> (List[User], List[Firm]):
    """Loads users and firms from JSON files.
    
    Args:
        users_file (str): The path to the users JSON file.
        firms_file (str): The path to the firms JSON file.
        
    Returns:
        A tuple consisting of a list of User and a list of Firm instances.
    """
    try:
        with open(users_file, 'r') as uf, open(firms_file, 'r') as ff:
            users_data = json.load(uf)
            firms_data = json.load(ff)

            users = [User(user['id'], user['preferences']) for user in users_data]
            firms = [Firm(firm['id'], firm['attributes']) for firm in firms_data]
            return users, firms
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def main():
    """Main entry point for the matching script."""
    users_file = 'users.json'
    firms_file = 'firms.json'

    users, firms = load_data(users_file, firms_file)

    matcher = Matcher(users, firms)
    matches = matcher.match_users_to_firms()
    
    # Output the matches, this could be logged or sent to another system
    print(json.dumps(matches, indent=4))

if __name__ == "__main__":
    main()
```
