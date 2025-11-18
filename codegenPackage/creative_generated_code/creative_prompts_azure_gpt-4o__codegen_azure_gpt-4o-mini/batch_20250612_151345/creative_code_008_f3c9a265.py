"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegaincapital.com
Prompt: Create a ranking badge system for users based on their investment activity, as described in The Gain Capital's ranking system.
Generated: DETERMINISTIC_f3c9a26575b5e8c5
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    Class representing a user in the ranking badge system.

    Attributes:
        username (str): The username of the user.
        investment_amount (float): The total investment amount by the user.
        badges (list): List of badges earned by the user.
    """

    def __init__(self, username: str):
        """Initialize a new user with a username and no initial investments or badges."""
        self.username = username
        self.investment_amount = 0.0
        self.badges = []

    def invest(self, amount: float) -> None:
        """
        Add an investment amount to the user's total.

        Args:
            amount (float): The amount to invest.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Investment amount cannot be negative.")
        self.investment_amount += amount
        self.update_badges()

    def update_badges(self) -> None:
        """Update the user's badges based on the current investment amount."""
        self.badges = []  # Reset badges before reassessment
        if self.investment_amount >= 1000:
            self.badges.append("Bronze Investor")
        if self.investment_amount >= 5000:
            self.badges.append("Silver Investor")
        if self.investment_amount >= 10000:
            self.badges.append("Gold Investor")
        if self.investment_amount >= 25000:
            self.badges.append("Platinum Investor")

    def __str__(self) -> str:
        """Return a string representation of the user and their badges."""
        return f"User: {self.username}, Investment Amount: ${self.investment_amount:.2f}, Badges: {', '.join(self.badges) if self.badges else 'None'}"


# Example usage:
if __name__ == "__main__":
    try:
        user1 = User("JohnDoe")
        user1.invest(1200)
        print(user1)

        user1.invest(5000)
        print(user1)

        user1.invest(-100)  # This will raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")
```
