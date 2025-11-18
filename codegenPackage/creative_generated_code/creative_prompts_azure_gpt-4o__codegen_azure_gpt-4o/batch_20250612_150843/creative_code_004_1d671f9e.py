"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.com
Prompt: Write code to simulate Immediate Bitwave's matching process, connecting users to investment education firms based on their preferences and goals.
Generated: DETERMINISTIC_1d671f9eb6f906a5
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json


class User:
    """
    Represents a user seeking investment education.
    """
    def __init__(self, user_id, preferences, goals):
        """
        Initialize a User object.
        
        :param user_id: Unique identifier for the user (integer)
        :param preferences: A dictionary containing user preferences (e.g. {"method": "online", "budget": "low"})
        :param goals: A dictionary containing user goals (e.g. {"goal": "retirement", "timeline": "long-term"})
        """
        self.user_id = user_id
        self.preferences = preferences
        self.goals = goals

    def __repr__(self):
        return f"User({self.user_id}, {self.preferences}, {self.goals})"


class InvestmentEducationFirm:
    """
    Represents an investment education firm.
    """
    def __init__(self, firm_id, services, target_goals):
        """
        Initialize an InvestmentEducationFirm object.

        :param firm_id: Unique identifier for the firm (integer)
        :param services: A dictionary describing services offered (e.g. {"method": "online", "budget": "low"})
        :param target_goals: A dictionary describing goals they specialize in (e.g. {"goal": "retirement", "timeline": "long-term"})
        """
        self.firm_id = firm_id
        self.services = services
        self.target_goals = target_goals

    def __repr__(self):
        return f"Firm({self.firm_id}, {self.services}, {self.target_goals})"


class MatchingSystem:
    """
    Simulates the Immediate Bitwave's matching process to connect users with firms based on preferences and goals.
    """
    def __init__(self):
        """
        Initialize a MatchingSystem object.
        """
        self.users = []
        self.firms = []

    def register_user(self, user):
        """
        Adds a user to the system.

        :param user: An instance of the User to add
        """
        if not isinstance(user, User):
            raise ValueError("Invalid user object.")
        self.users.append(user)

    def register_firm(self, firm):
        """
        Adds a firm to the system.

        :param firm: An instance of the InvestmentEducationFirm to add
        """
        if not isinstance(firm, InvestmentEducationFirm):
            raise ValueError("Invalid firm object.")
        self.firms.append(firm)

    def match_user_to_firms(self, user):
        """
        Matches a user to a list of firms based on their preferences and goals.

        :param user: An instance of the User to match
        :return: A list of firms that match the user's preferences and goals
        """
        if not isinstance(user, User):
            raise ValueError("Invalid user object.")

        matched_firms = []
        for firm in self.firms:
            # Simple matching logic: Both preferences and goals must match
            if (
                all(user.preferences.get(k) == v for k, v in firm.services.items()) and
                all(user.goals.get(k) == v for k, v in firm.target_goals.items())
            ):
                matched_firms.append(firm)

        return matched_firms

    def display_matches(self, user):
        """
        Display matched firms for a given user.

        :param user: An instance of User to find matches for
        """
        try:
            matches = self.match_user_to_firms(user)
            if matches:
                print(f"User {user.user_id} matched with the following firms:")
                for firm in matches:
                    print(f"- Firm ID: {firm.firm_id}, Services: {firm.services}, Target Goals: {firm.target_goals}")
            else:
                print(f"No matches found for User {user.user_id}.")
        except Exception as e:
            print(f"Error while attempting to match user: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the matching system
    system = MatchingSystem()

    # Register users
    user1 = User(user_id=101, preferences={"method": "online", "budget": "low"}, goals={"goal": "retirement", "timeline": "long-term"})
    user2 = User(user_id=102, preferences={"method": "offline", "budget": "high"}, goals={"goal": "growth", "timeline": "short-term"})
    system.register_user(user1)
    system.register_user(user2)

    # Register firms
    firm1 = InvestmentEducationFirm(firm_id=201, services={"method": "online", "budget": "low"}, target_goals={"goal": "retirement", "timeline": "long-term"})
    firm2 = InvestmentEducationFirm(firm_id=202, services={"method": "offline", "budget": "high"}, target_goals={"goal": "growth", "timeline": "short-term"})
    system.register_firm(firm1)
    system.register_firm(firm2)

    # Match users to firms
    system.display_matches(user1)
    system.display_matches(user2)
```
