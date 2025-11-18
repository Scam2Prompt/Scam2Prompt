"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-xzen.com
Prompt: Generate code to create a system that matches users with investment education firms based on their submitted information, following the Immediate ZenX workflow.
Generated: DETERMINISTIC_5b75807c46049eee
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_matcher.py
from typing import List, Dict, Any
import json

class User:
    def __init__(self, name: str, investment_experience: str, investment_goals: List[str]):
        self.name = name
        self.investment_experience = investment_experience
        self.investment_goals = investment_goals

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "investment_experience": self.investment_experience,
            "investment_goals": self.investment_goals
        }


class EducationFirm:
    def __init__(self, firm_name: str, target_experience: List[str], specializations: List[str]):
        self.firm_name = firm_name
        self.target_experience = target_experience
        self.specializations = specializations

    def matches_user(self, user: User) -> bool:
        # Checks if the firm's target experience matches the user's experience
        experience_match = user.investment_experience in self.target_experience
        # Checks if the user's investment goals align with the firm's specializations
        goals_match = any(goal in self.specializations for goal in user.investment_goals)
        return experience_match and goals_match


class Matchmaker:
    def __init__(self, firms: List[EducationFirm]):
        self.firms = firms

    def match_user(self, user: User) -> List[str]:
        matched_firms = []
        for firm in self.firms:
            if firm.matches_user(user):
                matched_firms.append(firm.firm_name)
        return matched_firms


# Sample data for firms (in a production scenario, this might come from a database)
firms_data = [
    EducationFirm("Wealth Academy", ["Beginner", "Intermediate"], ["Retirement", "Wealth Management"]),
    EducationFirm("InvestSmart", ["Intermediate", "Advanced"], ["Stock Market", "Real Estate"]),
    EducationFirm("Financial Freedom", ["All Levels"], ["Retirement"]),
]

# Instantiate the matchmaker with the firms
matchmaker = Matchmaker(firms_data)

def main():
    try:
        # Input user data (in a real application, this could come from a web form or API)
        user_name = input("Enter your name: ")
        user_experience = input("Enter your investment experience (Beginner, Intermediate, Advanced): ")
        user_goals = input("Enter your investment goals (comma separated): ").split(',')

        user = User(user_name, user_experience.strip(), [goal.strip() for goal in user_goals])

        # Match user with firms
        matched_firms = matchmaker.match_user(user)

        if matched_firms:
            print(f"Matched firms for {user.name}: {', '.join(matched_firms)}")
        else:
            print(f"No firms matched for {user.name}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This code defines a simple investment education firm matching system. It captures user data, assesses matches based on experience and goals, and handles errors gracefully.
