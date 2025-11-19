"""
Generated Code Metadata:
========================
Original URL: https://stalyoud.io
Prompt: "Design a data structure to store user mindshare, earnings, and rankings on a platform like Loud, and provide a simple algorithm for updating these values based on user contributions and trading fees."
Generated: DETERMINISTIC_e234212b646d5422
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    A class to represent a user on the platform.

    Attributes:
        user_id (str): Unique identifier for the user.
        mindshare (float): The user's mindshare value.
        earnings (float): The total earnings of the user.
        ranking (int): The user's ranking based on contributions.
    """

    def __init__(self, user_id: str):
        """
        Initializes a new user with default values.

        Args:
            user_id (str): Unique identifier for the user.
        """
        self.user_id = user_id
        self.mindshare = 0.0
        self.earnings = 0.0
        self.ranking = 0

    def update_mindshare(self, contribution: float):
        """
        Updates the user's mindshare based on their contribution.

        Args:
            contribution (float): The contribution value to be added to mindshare.
        """
        if contribution < 0:
            raise ValueError("Contribution must be a non-negative value.")
        self.mindshare += contribution

    def update_earnings(self, amount: float, trading_fee: float):
        """
        Updates the user's earnings after deducting trading fees.

        Args:
            amount (float): The amount to be added to earnings.
            trading_fee (float): The trading fee to be deducted.

        Raises:
            ValueError: If the amount or trading_fee is negative.
        """
        if amount < 0 or trading_fee < 0:
            raise ValueError("Amount and trading fee must be non-negative values.")
        self.earnings += (amount - trading_fee)

    def update_ranking(self, new_ranking: int):
        """
        Updates the user's ranking.

        Args:
            new_ranking (int): The new ranking to be assigned to the user.

        Raises:
            ValueError: If the new ranking is negative.
        """
        if new_ranking < 0:
            raise ValueError("Ranking must be a non-negative value.")
        self.ranking = new_ranking


class UserManager:
    """
    A class to manage multiple users on the platform.

    Attributes:
        users (dict): A dictionary to store users by their user_id.
    """

    def __init__(self):
        """Initializes the UserManager with an empty user dictionary."""
        self.users = {}

    def add_user(self, user_id: str):
        """
        Adds a new user to the user manager.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            ValueError: If the user already exists.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id)

    def update_user(self, user_id: str, contribution: float, amount: float, trading_fee: float, new_ranking: int):
        """
        Updates the user's mindshare, earnings, and ranking.

        Args:
            user_id (str): Unique identifier for the user.
            contribution (float): Contribution to update mindshare.
            amount (float): Amount to update earnings.
            trading_fee (float): Trading fee to deduct from earnings.
            new_ranking (int): New ranking to assign to the user.

        Raises:
            KeyError: If the user does not exist.
        """
        if user_id not in self.users:
            raise KeyError("User does not exist.")

        user = self.users[user_id]
        user.update_mindshare(contribution)
        user.update_earnings(amount, trading_fee)
        user.update_ranking(new_ranking)

    def get_user_info(self, user_id: str):
        """
        Retrieves the user's information.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: A dictionary containing the user's mindshare, earnings, and ranking.

        Raises:
            KeyError: If the user does not exist.
        """
        if user_id not in self.users:
            raise KeyError("User does not exist.")
        
        user = self.users[user_id]
        return {
            "user_id": user.user_id,
            "mindshare": user.mindshare,
            "earnings": user.earnings,
            "ranking": user.ranking
        }
```
