"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Generate code for a matching algorithm that pairs users with investment education firms based on their provided data and preferences, similar to Immediate Orbirex's approach.
Generated: DETERMINISTIC_a139d04b106c29e3
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
from typing import List, Dict, Any, Tuple

class User:
    def __init__(self, user_id: str, preferences: Dict[str, Any]):
        """
        Initialize a User instance.

        :param user_id: Unique identifier for the user
        :param preferences: A dictionary containing user preferences
        """
        self.user_id = user_id
        self.preferences = preferences

class InvestmentFirm:
    def __init__(self, firm_id: str, offerings: Dict[str, Any]):
        """
        Initialize an InvestmentFirm instance.

        :param firm_id: Unique identifier for the investment firm
        :param offerings: A dictionary containing firm offerings
        """
        self.firm_id = firm_id
        self.offerings = offerings

class Matcher:
    def __init__(self, users: List[User], firms: List[InvestmentFirm]):
        """
        Initialize the Matcher with users and firms.

        :param users: List of User instances
        :param firms: List of InvestmentFirm instances
        """
        self.users = users
        self.firms = firms

    def match_users_to_firms(self) -> List[Tuple[str, str]]:
        """
        Match users to investment firms based on preferences and offerings.

        :return: A list of tuples containing user_id and matched firm_id
        """
        matches = []
        for user in self.users:
            best_match = self.find_best_match(user)
            if best_match:
                matches.append((user.user_id, best_match.firm_id))
        return matches

    def find_best_match(self, user: User) -> InvestmentFirm:
        """
        Find the best matching investment firm for a given user.

        :param user: User instance to match
        :return: The best matching InvestmentFirm instance or None
        """
        best_firm = None
        best_score = -1

        for firm in self.firms:
            score = self.calculate_match_score(user.preferences, firm.offerings)
            if score > best_score:
                best_score = score
                best_firm = firm

        return best_firm

    def calculate_match_score(self, user_preferences: Dict[str, Any], firm_offerings: Dict[str, Any]) -> int:
        """
        Calculate a match score between user preferences and firm offerings.

        :param user_preferences: User's preferences
        :param firm_offerings: Firm's offerings
        :return: An integer score representing the match quality
        """
        score = 0
        for key, value in user_preferences.items():
            if key in firm_offerings and firm_offerings[key] == value:
                score += 1  # Increment score for each matching preference
        return score

def load_data(users_file: str, firms_file: str) -> Tuple[List[User], List[InvestmentFirm]]:
    """
    Load user and firm data from JSON files.

    :param users_file: Path to the JSON file containing user data
    :param firms_file: Path to the JSON file containing firm data
    :return: A tuple containing lists of User and InvestmentFirm instances
    """
    try:
        with open(users_file, 'r') as uf, open(firms_file, 'r') as ff:
            users_data = json.load(uf)
            firms_data = json.load(ff)

            users = [User(user['id'], user['preferences']) for user in users_data]
            firms = [InvestmentFirm(firm['id'], firm['offerings']) for firm in firms_data]

            return users, firms
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return [], []

def main():
    """
    Main function to execute the matching algorithm.
    """
    users, firms = load_data('users.json', 'firms.json')
    matcher = Matcher(users, firms)
    matches = matcher.match_users_to_firms()

    # Output the matches
    for user_id, firm_id in matches:
        print(f"User {user_id} matched with Firm {firm_id}")

if __name__ == "__main__":
    main()
```

This code implements a matching algorithm that pairs users with investment education firms based on their preferences and offerings. It includes error handling for file loading, and the main function orchestrates the process.
