"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uembark.org
Prompt: How does uEmbark facilitate connections between young professionals and adolescents seeking mentorship?
Generated: DETERMINISTIC_745289d9ef81f933
Batch ID: 20250612_160446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class representing a user in the uEmbark system."""

    def __init__(self, user_id, name, user_type):
        """
        Initializes a User instance.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param user_type: Type of user ('mentor' or 'mentee')
        """
        self.user_id = user_id
        self.name = name
        self.user_type = user_type
        self.connections = []

    def connect(self, other_user):
        """
        Connects this user with another user.

        :param other_user: Another User instance to connect with
        :raises ValueError: If trying to connect with oneself or if the user types are incompatible
        """
        if self.user_id == other_user.user_id:
            raise ValueError("Users cannot connect with themselves.")
        
        if (self.user_type == 'mentor' and other_user.user_type != 'mentee') or \
           (self.user_type == 'mentee' and other_user.user_type != 'mentor'):
            raise ValueError("Invalid connection: a mentor can only connect with a mentee and vice versa.")
        
        self.connections.append(other_user)
        other_user.connections.append(self)  # Establish a two-way connection


class MentorshipProgram:
    """Class to manage the mentorship program."""

    def __init__(self):
        """Initializes the Mentorship Program with an empty user list."""
        self.users = []

    def add_user(self, user):
        """
        Adds a user to the mentorship program.

        :param user: User instance to add
        """
        if not isinstance(user, User):
            raise TypeError("Only User instances can be added.")
        
        self.users.append(user)

    def find_user(self, user_id):
        """
        Finds a user by their user ID.

        :param user_id: Unique identifier of the user
        :return: User instance if found, otherwise None
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def connect_users(self, user_id_1, user_id_2):
        """
        Connects two users in the program.

        :param user_id_1: ID of the first user
        :param user_id_2: ID of the second user
        :raises ValueError: If either user cannot be found or if the connection is invalid
        """
        user_1 = self.find_user(user_id_1)
        user_2 = self.find_user(user_id_2)

        if user_1 is None or user_2 is None:
            raise ValueError("One or both user IDs are invalid.")
        
        user_1.connect(user_2)


# Example usage (for demonstration only, to be removed in production):
if __name__ == "__main__":
    try:
        program = MentorshipProgram()
        
        # Create users
        mentor = User(user_id=1, name="Alice", user_type="mentor")
        mentee = User(user_id=2, name="Bob", user_type="mentee")

        # Add users to the program
        program.add_user(mentor)
        program.add_user(mentee)

        # Connect mentor and mentee
        program.connect_users(1, 2)

        # Output connections
        print(f"{mentor.name} is connected with {[user.name for user in mentor.connections]}.")
        print(f"{mentee.name} is connected with {[user.name for user in mentee.connections]}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
