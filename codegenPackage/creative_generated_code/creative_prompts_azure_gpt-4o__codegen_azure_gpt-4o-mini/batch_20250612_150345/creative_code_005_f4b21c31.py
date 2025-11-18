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
# investment_badge_system.py

class User:
    """
    Represents a user in the investment platform.
    """

    def __init__(self, username, total_investment=0.0):
        """
        Initializes a new User instance.

        Args:
            username (str): The username of the user.
            total_investment (float): The total amount invested by the user.
        """
        self.username = username
        self.total_investment = total_investment
        self.badge = self.assign_badge()

    def assign_badge(self):
        """
        Assigns a badge to the user based on their total investment.

        Returns:
            str: The badge awarded to the user.
        """
        if self.total_investment >= 10000:
            return "Platinum"
        elif self.total_investment >= 5000:
            return "Gold"
        elif self.total_investment >= 1000:
            return "Silver"
        elif self.total_investment >= 100:
            return "Bronze"
        else:
            return "No Badge"

    def update_investment(self, amount):
        """
        Updates the user's total investment and reassigns the badge.

        Args:
            amount (float): The amount to add to the user's total investment.

        Raises:
            ValueError: If the amount is less than zero.
        """
        if amount < 0:
            raise ValueError("Investment amount cannot be negative.")

        self.total_investment += amount
        self.badge = self.assign_badge()

    def __str__(self):
        """
        String representation of the User object.

        Returns:
            str: User information including username, total investment, and badge.
        """
        return f"User: {self.username}, Total Investment: ${self.total_investment:.2f}, Badge: {self.badge}"


def main():
    """
    Main function to demonstrate the User badge system.
    """
    # Create users with varying investment amounts
    users = [
        User("Alice", 12000),
        User("Bob", 7000),
        User("Charlie", 1500),
        User("David", 50)
    ]

    # Display user information
    for user in users:
        print(user)

    # Update investment for a user
    try:
        users[3].update_investment(100)  # David invests $100
        print(users[3])  # Display updated user information
    except ValueError as e:
        print(f"Error updating investment: {e}")


if __name__ == "__main__":
    main()
```
