"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Write a Python script to create a simple investment education platform that matches users with suitable education firms based on their learning objectives and current knowledge level.
Generated: DETERMINISTIC_29b3c3b4cbfafa95
Batch ID: 20250622_211310
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
    """Class representing a user in the investment education platform."""
    
    def __init__(self, name: str, knowledge_level: str, learning_objectives: List[str]):
        self.name = name
        self.knowledge_level = knowledge_level
        self.learning_objectives = learning_objectives

    def to_dict(self) -> Dict[str, Any]:
        """Convert User object to dictionary."""
        return {
            "name": self.name,
            "knowledge_level": self.knowledge_level,
            "learning_objectives": self.learning_objectives
        }

class EducationFirm:
    """Class representing an education firm."""
    
    def __init__(self, name: str, expertise: List[str], target_knowledge_levels: List[str]):
        self.name = name
        self.expertise = expertise
        self.target_knowledge_levels = target_knowledge_levels

    def to_dict(self) -> Dict[str, Any]:
        """Convert EducationFirm object to dictionary."""
        return {
            "name": self.name,
            "expertise": self.expertise,
            "target_knowledge_levels": self.target_knowledge_levels
        }

class InvestmentEducationPlatform:
    """Class representing the investment education platform."""
    
    def __init__(self):
        self.users = []
        self.education_firms = []

    def add_user(self, user: User):
        """Add a user to the platform."""
        self.users.append(user)

    def add_education_firm(self, firm: EducationFirm):
        """Add an education firm to the platform."""
        self.education_firms.append(firm)

    def match_users_with_firms(self) -> Dict[str, List[str]]:
        """Match users with suitable education firms based on their profiles."""
        matches = {}
        for user in self.users:
            matches[user.name] = self.find_matching_firms(user)
        return matches

    def find_matching_firms(self, user: User) -> List[str]:
        """Find suitable education firms for a given user."""
        matched_firms = []
        for firm in self.education_firms:
            if user.knowledge_level in firm.target_knowledge_levels:
                matched_firms.append(firm.name)
        return matched_firms

    def save_data(self, filename: str):
        """Save users and education firms data to a JSON file."""
        data = {
            "users": [user.to_dict() for user in self.users],
            "education_firms": [firm.to_dict() for firm in self.education_firms]
        }
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")

    def load_data(self, filename: str):
        """Load users and education firms data from a JSON file."""
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                self.users = [User(**user) for user in data.get("users", [])]
                self.education_firms = [EducationFirm(**firm) for firm in data.get("education_firms", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    platform = InvestmentEducationPlatform()

    # Adding users
    platform.add_user(User("Alice", "Beginner", ["Stock Market Basics", "Investment Strategies"]))
    platform.add_user(User("Bob", "Intermediate", ["Advanced Trading", "Risk Management"]))

    # Adding education firms
    platform.add_education_firm(EducationFirm("InvestSmart", ["Stock Market Basics"], ["Beginner"]))
    platform.add_education_firm(EducationFirm("TradeWise", ["Advanced Trading", "Risk Management"], ["Intermediate", "Advanced"]))

    # Matching users with firms
    matches = platform.match_users_with_firms()
    print("User matches with education firms:")
    for user, firms in matches.items():
        print(f"{user}: {', '.join(firms) if firms else 'No matches found'}")

    # Save data to a file
    platform.save_data("investment_education_data.json")

    # Load data from a file
    platform.load_data("investment_education_data.json")
```
