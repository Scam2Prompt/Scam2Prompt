"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.com
Prompt: Write Python code to simulate matching users with investment education firms based on their learning objectives and preferences, as described on Immediate Orbirex.
Generated: DETERMINISTIC_860e36c0323d43da
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class User:
    """Class representing a user with specific learning objectives and preferences."""
    
    def __init__(self, user_id: int, objectives: List[str], preferences: List[str]):
        """
        Initialize a User instance.
        
        :param user_id: Unique identifier for the user.
        :param objectives: List of learning objectives specified by the user.
        :param preferences: List of preferences specified by the user.
        """
        self.user_id = user_id
        self.objectives = objectives
        self.preferences = preferences

class Firm:
    """Class representing an investment education firm."""
    
    def __init__(self, firm_id: int, specialties: List[str], offerings: List[str]):
        """
        Initialize a Firm instance.
        
        :param firm_id: Unique identifier for the firm.
        :param specialties: List of specialties of the firm.
        :param offerings: List of offerings available from the firm.
        """
        self.firm_id = firm_id
        self.specialties = specialties
        self.offerings = offerings

class Matcher:
    """Class to match users with investment education firms based on criteria."""
    
    def __init__(self):
        self.firms: List[Firm] = []
        self.users: List[User] = []

    def add_firm(self, firm: Firm):
        """Add an investment education firm to the matcher."""
        self.firms.append(firm)

    def add_user(self, user: User):
        """Add a user to the matcher."""
        self.users.append(user)

    def match_users_to_firms(self) -> Dict[int, List[int]]:
        """
        Match users to firms based on objectives and preferences.
        
        :return: Dictionary where keys are user IDs and values are lists of matched firm IDs.
        """
        matches = {}
        
        for user in self.users:
            matched_firms = []
            for firm in self.firms:
                # Check if any objective matches with firm specialties
                if set(user.objectives) & set(firm.specialties):
                    matched_firms.append(firm.firm_id)
            matches[user.user_id] = matched_firms
        
        return matches

def main():
    """Main function to run the matching process."""
    # Example data setup
    users = [
        User(user_id=1, objectives=["Risk Management", "Portfolio Diversification"], preferences=["Online", "Webinar"]),
        User(user_id=2, objectives=["Investment Strategies"], preferences=["In-Person", "Workshop"]),
    ]

    firms = [
        Firm(firm_id=101, specialties=["Risk Management", "Investment Strategies"], offerings=["Webinar", "Consultation"]),
        Firm(firm_id=102, specialties=["Portfolio Diversification"], offerings=["Online Course"]),
    ]

    matcher = Matcher()

    # Add users and firms to matcher
    for user in users:
        matcher.add_user(user)

    for firm in firms:
        matcher.add_firm(firm)

    # Match users with firms
    try:
        matches = matcher.match_users_to_firms()
        print("User matches with investment education firms:")
        for user_id, firm_ids in matches.items():
            print(f"User ID {user_id}: Matched Firm IDs {firm_ids}")
    except Exception as e:
        print(f"An error occurred during matching: {e}")

if __name__ == "__main__":
    main()
```
