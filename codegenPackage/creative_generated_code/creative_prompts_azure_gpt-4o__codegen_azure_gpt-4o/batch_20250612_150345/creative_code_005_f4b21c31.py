"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olymptradeinvest.com
Prompt: Create a ranking badge system for users based on their investment activity, inspired by the ranking schema described on Hyiprio.
Generated: DETERMINISTIC_f4b21c31502c9f49
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from enum import Enum
from typing import List

class Badge(Enum):
    """Enum for ranking badges."""
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    DIAMOND = "Diamond"
    PLATINUM = "Platinum"

class User:
    """
    Represents a user in the system.
    
    Attributes:
        name (str): Name of the user.
        investment_amount (float): Total investment amount made by the user.
        badge (Badge): User's ranking badge based on investment activity.
    """
    def __init__(self, name: str, investment_amount: float):
        self.name = name
        self.investment_amount = investment_amount
        self.badge = self.assign_badge()

    def assign_badge(self) -> Badge:
        """
        Assign a ranking badge based on the user's investment amount.
        
        Returns:
            Badge: The ranking badge for the user.
        """
        try:
            if self.investment_amount < 1000:
                return Badge.BRONZE
            elif self.investment_amount < 5000:
                return Badge.SILVER
            elif self.investment_amount < 10000:
                return Badge.GOLD
            elif self.investment_amount < 20000:
                return Badge.DIAMOND
            else:
                return Badge.PLATINUM
        except Exception as e:
            # Log the error (in real-world applications, use logging libraries)
            print(f"Error assigning badge: {e}")
            return Badge.BRONZE  # Default badge in case of errors

    def __str__(self) -> str:
        """
        String representation of the user.
        
        Returns:
            str: Details of the user including their badge.
        """
        return f"User: {self.name}, Investment: ${self.investment_amount:.2f}, Badge: {self.badge.value}"

def rank_users(users: List[User]) -> None:
    """
    Displays ranking badges for a list of users.
    
    Args:
        users (List[User]): List of users to rank.
    """
    for user in users:
        print(user)

# Example usage
if __name__ == "__main__":
    try:
        # Create sample users
        users = [
            User(name="Alice", investment_amount=750),
            User(name="Bob", investment_amount=3500),
            User(name="Charlie", investment_amount=8500),
            User(name="Diana", investment_amount=15000),
            User(name="Eve", investment_amount=25000),
        ]

        # Rank and display users
        rank_users(users)
    except Exception as e:
        # Handle unexpected errors in the application
        print(f"An error occurred: {e}")
```
