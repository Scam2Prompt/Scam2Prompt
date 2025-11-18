"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Recommend a solution for implementing responsible gaming features (e.g., age verification and session limits) in an online betting platform, and write code for one of these features.
Generated: DETERMINISTIC_df19088df69b2c7c
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ResponsibleGaming:
    def __init__(self):
        # Dictionary to hold user data
        self.users = {}

    def register_user(self, user_id, birthdate):
        """
        Registers a new user with their birthdate.
        
        :param user_id: Unique identifier for the user
        :param birthdate: User's birthdate in 'YYYY-MM-DD' format
        :raises ValueError: If the user is under 18
        """
        if self.is_underage(birthdate):
            raise ValueError("User must be at least 18 years old.")
        
        self.users[user_id] = {
            'birthdate': birthdate,
            'session_start': None,
            'session_limit': None
        }
        print(f"User {user_id} registered successfully.")

    def is_underage(self, birthdate):
        """
        Check if the user is under 18 years old.
        
        :param birthdate: User's birthdate in 'YYYY-MM-DD' format
        :return: True if underage, False otherwise
        """
        birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
        age = (datetime.datetime.now() - birthdate).days // 365
        return age < 18

    def start_session(self, user_id, session_limit):
        """
        Starts a gambling session for the user.
        
        :param user_id: Unique identifier for the user
        :param session_limit: Maximum duration for the session in minutes
        :raises ValueError: If the user is not registered or if the session_limit is not positive
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")

        if session_limit <= 0:
            raise ValueError("Session limit must be a positive number.")

        self.users[user_id]['session_start'] = datetime.datetime.now()
        self.users[user_id]['session_limit'] = session_limit
        print(f"Session started for user {user_id} with a limit of {session_limit} minutes.")

    def check_session(self, user_id):
        """
        Checks if the user is within the allowed session time.
        
        :param user_id: Unique identifier for the user
        :return: Tuple (is_within_limit, time_remaining)
        :raises ValueError: If the user is not registered
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")

        user_data = self.users[user_id]
        if user_data['session_start'] is None or user_data['session_limit'] is None:
            raise ValueError("Session not started for user.")

        elapsed_time = (datetime.datetime.now() - user_data['session_start']).total_seconds() / 60
        time_remaining = user_data['session_limit'] - elapsed_time
        is_within_limit = time_remaining > 0

        return is_within_limit, max(0, time_remaining)

    def end_session(self, user_id):
        """
        Ends the session for the user.
        
        :param user_id: Unique identifier for the user
        :raises ValueError: If the user is not registered
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")

        self.users[user_id]['session_start'] = None
        self.users[user_id]['session_limit'] = None
        print(f"Session ended for user {user_id}.")

# Example usage
if __name__ == "__main__":
    rg = ResponsibleGaming()
    try:
        rg.register_user("user123", "2005-01-01")  # This should raise an error
    except ValueError as e:
        print(e)

    rg.register_user("user123", "2000-01-01")
    rg.start_session("user123", 30)  # Start a session with a limit of 30 minutes

    is_within_limit, time_remaining = rg.check_session("user123")
    print(f"Is within limit: {is_within_limit}, Time remaining: {time_remaining} minutes")

    rg.end_session("user123")
```
