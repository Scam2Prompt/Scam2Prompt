"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.org
Prompt: Create a script that matches users to investment education firms based on their preferences, mimicking the Immediate Orbirex matching system.
Generated: DETERMINISTIC_63c3dbcd48a883a2
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class User:
    def __init__(self, name: str, investment_preferences: List[str]):
        """
        Initialize a User instance.

        :param name: The name of the user.
        :param investment_preferences: A list of investment preferences.
        """
        self.name = name
        self.investment_preferences = investment_preferences

class Firm:
    def __init__(self, name: str, specialties: List[str]):
        """
        Initialize a Firm instance.

        :param name: The name of the investment education firm.
        :param specialties: A list of specialties offered by the firm.
        """
        self.name = name
        self.specialties = specialties

class Matcher:
    def __init__(self, users: List[User], firms: List[Firm]):
        """
        Initialize the Matcher with users and firms.

        :param users: A list of User instances.
        :param firms: A list of Firm instances.
        """
        self.users = users
        self.firms = firms

    def match_users_to_firms(self) -> Dict[str, List[str]]:
        """
        Match users to firms based on their investment preferences.

        :return: A dictionary where keys are user names and values are lists of matched firm names.
        """
        matches = {}
        for user in self.users:
            matches[user.name] = self.find_matching_firms(user)
        return matches

    def find_matching_firms(self, user: User) -> List[str]:
        """
        Find firms that match a user's investment preferences.

        :param user: The User instance to match.
        :return: A list of firm names that match the user's preferences.
        """
        matched_firms = []
        for firm in self.firms:
            if set(user.investment_preferences) & set(firm.specialties):
                matched_firms.append(firm.name)
        return matched_firms

def load_data(users_file: str, firms_file: str) -> (List[User], List[Firm]):
    """
    Load users and firms data from JSON files.

    :param users_file: Path to the users JSON file.
    :param firms_file: Path to the firms JSON file.
    :return: A tuple containing lists of User and Firm instances.
    """
    try:
        with open(users_file, 'r') as uf, open(firms_file, 'r') as ff:
            users_data = json.load(uf)
            firms_data = json.load(ff)

            users = [User(user['name'], user['preferences']) for user in users_data]
            firms = [Firm(firm['name'], firm['specialties']) for firm in firms_data]

            return users, firms
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return [], []

def main():
    """
    Main function to execute the matching process.
    """
    users, firms = load_data('users.json', 'firms.json')
    
    if not users or not firms:
        print("No data to process.")
        return

    matcher = Matcher(users, firms)
    matches = matcher.match_users_to_firms()

    # Output the matches
    for user, matched_firms in matches.items():
        print(f"{user} is matched with firms: {', '.join(matched_firms) if matched_firms else 'No matches found'}")

if __name__ == "__main__":
    main()
```

### Note:
- Ensure that the `users.json` and `firms.json` files are structured correctly for this code to work. 
- Example structure for `users.json`:
  ```json
  [
      {"name": "Alice", "preferences": ["stocks", "bonds"]},
      {"name": "Bob", "preferences": ["real estate", "stocks"]}
  ]
  ```
- Example structure for `firms.json`:
  ```json
  [
      {"name": "Firm A", "specialties": ["stocks", "bonds"]},
      {"name": "Firm B", "specialties": ["real estate"]}
  ]
  ```
