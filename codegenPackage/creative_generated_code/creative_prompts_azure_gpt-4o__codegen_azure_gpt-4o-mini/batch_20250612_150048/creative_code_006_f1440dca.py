"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supremeprofund.com
Prompt: Develop a referral program system in Python for SupremeProFund, allowing users to earn referral income based on the number of referred clients and their investment amounts.
Generated: DETERMINISTIC_f1440dcac962354f
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class to represent a user in the referral program."""
    
    def __init__(self, username):
        """
        Initializes a new user with a username and a list to hold referred clients.

        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.referrals = []
        self.referral_income = 0.0

    def refer_client(self, client):
        """
        Refers a new client and adds them to the user's referral list.

        Args:
            client (Client): The client to be referred.
        """
        self.referrals.append(client)

    def calculate_referral_income(self):
        """
        Calculates the user's total referral income based on referred clients' investments.
        Each client's investment contributes a fixed percentage to the referral income.

        Returns:
            float: The total referral income.
        """
        referral_percentage = 0.1  # 10% of the client's investment
        self.referral_income = sum(client.investment * referral_percentage for client in self.referrals)
        return self.referral_income


class Client:
    """Class to represent a client referred by a user."""
    
    def __init__(self, investment):
        """
        Initializes a client with an investment amount.

        Args:
            investment (float): The investment amount of the client.
        """
        if investment <= 0:
            raise ValueError("Investment must be greater than zero.")
        self.investment = investment


class ReferralProgram:
    """Class to manage the referral program for users."""
    
    def __init__(self):
        """Initializes the referral program with an empty list of users."""
        self.users = []

    def add_user(self, username):
        """
        Adds a new user to the referral program.

        Args:
            username (str): The username of the new user.

        Raises:
            ValueError: If the username already exists.
        """
        if any(user.username == username for user in self.users):
            raise ValueError("Username already exists.")
        self.users.append(User(username))

    def refer_client_to_user(self, username, investment):
        """
        Refers a client to a specific user based on their username.

        Args:
            username (str): The username of the referring user.
            investment (float): The investment amount of the referred client.

        Raises:
            ValueError: If the user does not exist or if the investment is invalid.
        """
        user = next((u for u in self.users if u.username == username), None)
        if user is None:
            raise ValueError("User not found.")

        client = Client(investment)
        user.refer_client(client)

    def get_user_referral_income(self, username):
        """
        Retrieves the total referral income for a specific user.

        Args:
            username (str): The username of the user.

        Returns:
            float: The total referral income for the user.

        Raises:
            ValueError: If the user does not exist.
        """
        user = next((u for u in self.users if u.username == username), None)
        if user is None:
            raise ValueError("User not found.")
        return user.calculate_referral_income()


# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()
        program.add_user("john_doe")
        program.refer_client_to_user("john_doe", 1000)
        program.refer_client_to_user("john_doe", 2000)
        
        income = program.get_user_referral_income("john_doe")
        print(f"Total referral income for john_doe: ${income:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
