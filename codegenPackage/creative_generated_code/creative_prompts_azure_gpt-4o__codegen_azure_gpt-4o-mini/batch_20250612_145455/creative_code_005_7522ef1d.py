"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://echotradeoptions.com
Prompt: Implement a referral program in Python that tracks referrals and calculates bonuses, following Echo Trade's signup bonus system.
Generated: DETERMINISTIC_7522ef1d308c4337
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class that represents a user in the referral program."""
    
    def __init__(self, username):
        """
        Initialize a new user with a username and no referrals.
        
        :param username: The username of the user.
        """
        self.username = username
        self.referrals = []  # List to store usernames of referred users
        self.bonus = 0.0     # The current bonus of the user

    def refer(self, new_user):
        """
        Refer a new user and add them to the list of referrals.
        
        :param new_user: An instance of User that is being referred.
        """
        if isinstance(new_user, User):
            self.referrals.append(new_user.username)
            self.calculate_bonus()  # Calculate the bonus after a successful referral
        else:
            raise ValueError("new_user must be an instance of User.")

    def calculate_bonus(self):
        """Calculate the bonus based on the number of referrals."""
        num_referrals = len(self.referrals)
        self.bonus = num_referrals * 50.0  # Assume each referral gives a $50 bonus

    def __str__(self):
        """Return a string representation of the user."""
        return f"User: {self.username}, Referrals: {self.referrals}, Bonus: ${self.bonus:.2f}"


class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        """Initialize the referral program with an empty user list."""
        self.users = {}  # A dictionary to store users by username

    def add_user(self, username):
        """
        Add a new user to the program.
        
        :param username: The username of the new user.
        :raises ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError(f"Username '{username}' already exists.")
        self.users[username] = User(username)

    def refer_user(self, referrer_username, new_user_username):
        """
        Process a referral where one user refers another.
        
        :param referrer_username: The username of the referrer.
        :param new_user_username: The username of the new user being referred.
        :raises ValueError: If either user does not exist.
        """
        if referrer_username not in self.users:
            raise ValueError(f"Referrer '{referrer_username}' does not exist.")
        if new_user_username not in self.users:
            raise ValueError(f"New user '{new_user_username}' does not exist.")

        referrer = self.users[referrer_username]
        new_user = self.users[new_user_username]

        referrer.refer(new_user)

    def get_user_info(self, username):
        """
        Retrieve user information including referrals and bonus.
        
        :param username: The username of the user to retrieve.
        :raises ValueError: If the user does not exist.
        :return: A string with user information.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' does not exist.")
        return str(self.users[username])


# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Adding users
    referral_program.add_user("alice")
    referral_program.add_user("bob")
    
    # Referring users
    try:
        referral_program.refer_user("alice", "bob")
    except ValueError as e:
        print(e)

    # Display user information
    try:
        print(referral_program.get_user_info("alice"))
        print(referral_program.get_user_info("bob"))
    except ValueError as e:
        print(e)
```
