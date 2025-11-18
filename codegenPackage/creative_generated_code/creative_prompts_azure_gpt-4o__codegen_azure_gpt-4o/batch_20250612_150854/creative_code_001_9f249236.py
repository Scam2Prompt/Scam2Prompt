"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-elevate.com
Prompt: Create a script that connects users to investment education firms after registration on Immediate Elevate, simulating the "Instant Connection" feature described on the website.
Generated: DETERMINISTIC_9f24923693f22146
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging


# Setup logging for error handling and tracing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ImmediateElevate:
    """
    ImmediateElevate class simulates a platform that registers users and connects them to investment education firms.

    Attributes:
        users (list): A list to store registered users.
        education_firms (list): A list of simulated investment education firms.
    """

    def __init__(self):
        self.users = []  # Store registered users
        self.education_firms = ["InvestSmart Academy", "Finance 101 Group", "WealthUp Learning"]  # Mock education firms

    def register_user(self, user_info):
        """
        Registers a new user to the ImmediateElevate platform.

        Args:
            user_info (dict): Dictionary containing user details like name, email, and experience level.

        Returns:
            dict: Confirmation of user registration.
        """
        try:
            # Basic validation
            if not user_info.get("name") or not user_info.get("email"):
                raise ValueError("User name and email are required fields.")

            self.users.append(user_info)  # Add user to the list
            logging.info(f"User {user_info['name']} registered successfully.")
            return {"status": "success", "message": "User registered successfully."}
        except Exception as e:
            logging.error(f"Error registering user: {e}")
            return {"status": "error", "message": str(e)}

    def connect_to_firm(self, user_email):
        """
        Simulates an "Instant Connection" feature by connecting a user to an investment education firm.

        Args:
            user_email (str): Email of the registered user.

        Returns:
            dict: Information about the connected firm or error if the user is not registered.
        """
        try:
            # Find user by email
            user = next((u for u in self.users if u["email"] == user_email), None)
            if not user:
                raise ValueError("User not found. Please register first.")

            # Simulate firm assignment (round-robin for simplicity)
            assigned_firm = self.education_firms[self.users.index(user) % len(self.education_firms)]
            logging.info(f"User {user['name']} connected to {assigned_firm}.")
            return {
                "status": "success",
                "user": user,
                "connected_firm": assigned_firm
            }
        except Exception as e:
            logging.error(f"Error connecting user to a firm: {e}")
            return {"status": "error", "message": str(e)}


# Example usage
if __name__ == "__main__":
    # Create an instance of ImmediateElevate
    platform = ImmediateElevate()

    # Registering users
    user1 = {"name": "Alice Johnson", "email": "alice@example.com", "experience_level": "beginner"}
    user2 = {"name": "Bob Smith", "email": "bob@example.com", "experience_level": "intermediate"}

    print(json.dumps(platform.register_user(user1), indent=4))  # Register Alice
    print(json.dumps(platform.register_user(user2), indent=4))  # Register Bob

    # Connecting users to investment education firms
    print(json.dumps(platform.connect_to_firm("alice@example.com"), indent=4))  # Connect Alice
    print(json.dumps(platform.connect_to_firm("bob@example.com"), indent=4))    # Connect Bob

    # Error handling example: Connect a non-registered user
    print(json.dumps(platform.connect_to_firm("charlie@example.com"), indent=4))  # User not registered
```
