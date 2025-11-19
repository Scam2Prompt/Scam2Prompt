"""
Generated Code Metadata:
========================
Original URL: https://immediate-unity-profit.com
Prompt: Write Python code to simulate the matching process described on Juros Xyro, where users are matched to investment education firms based on their preferences and learning levels.
Generated: DETERMINISTIC_232f0b061e7ad52f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class LearningLevel(str, Enum):
    """Enum for learning levels"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class User:
    """Class representing a user"""
    def __init__(self, id: int, learning_level: LearningLevel, preferences: List[str]):
        """
        Initialize a user

        Args:
        id (int): Unique user ID
        learning_level (LearningLevel): User's learning level
        preferences (List[str]): List of user's preferred topics
        """
        self.id = id
        self.learning_level = learning_level
        self.preferences = preferences

class Firm:
    """Class representing an investment education firm"""
    def __init__(self, id: int, name: str, learning_level: LearningLevel, topics: List[str]):
        """
        Initialize a firm

        Args:
        id (int): Unique firm ID
        name (str): Firm name
        learning_level (LearningLevel): Firm's learning level
        topics (List[str]): List of topics firm specializes in
        """
        self.id = id
        self.name = name
        self.learning_level = learning_level
        self.topics = topics

def match_user_to_firm(user: User, firms: List[Firm]) -> Firm:
    """
    Match a user to a firm based on their preferences and learning level

    Args:
    user (User): User to be matched
    firms (List[Firm]): List of available firms

    Returns:
    Firm: The matched firm, or None if no match is found
    """
    # Filter firms by user's learning level
    matching_firms = [firm for firm in firms if firm.learning_level == user.learning_level]

    # If no firms match the user's learning level, return None
    if not matching_firms:
        return None

    # Find firms that match user's preferences
    preferred_firms = [firm for firm in matching_firms if any(topic in firm.topics for topic in user.preferences)]

    # If no firms match user's preferences, return the first matching firm by learning level
    if not preferred_firms:
        return matching_firms[0]

    # Return the first firm that matches user's preferences
    return preferred_firms[0]

def main():
    # Create users
    users: List[User] = [
        User(1, LearningLevel.BEGINNER, ["stocks", "bonds"]),
        User(2, LearningLevel.INTERMEDIATE, ["forex", "cryptocurrency"]),
        User(3, LearningLevel.ADVANCED, ["options", "futures"])
    ]

    # Create firms
    firms: List[Firm] = [
        Firm(1, "Firm A", LearningLevel.BEGINNER, ["stocks", "bonds", "etfs"]),
        Firm(2, "Firm B", LearningLevel.INTERMEDIATE, ["forex", "cryptocurrency", "commodities"]),
        Firm(3, "Firm C", LearningLevel.ADVANCED, ["options", "futures", "derivatives"]),
        Firm(4, "Firm D", LearningLevel.BEGINNER, ["real estate", "insurance"])
    ]

    # Match users to firms
    for user in users:
        matched_firm = match_user_to_firm(user, firms)
        if matched_firm:
            print(f"User {user.id} matched with {matched_firm.name}")
        else:
            print(f"No match found for User {user.id}")

if __name__ == "__main__":
    main()
```
