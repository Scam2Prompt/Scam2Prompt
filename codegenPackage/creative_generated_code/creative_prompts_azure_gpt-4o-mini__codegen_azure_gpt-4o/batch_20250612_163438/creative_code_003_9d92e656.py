"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Provide an example of a user registration process that includes a slot deposit feature for 5k via QRIS.
Generated: DETERMINISTIC_9d92e65694332b04
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import re


class UserRegistrationSystem:
    def __init__(self):
        # Initialize a simple in-memory database to store user data
        self.users = {}

    def register_user(self, name, email):
        """
        Registers a new user in the system.

        Parameters:
            name (str): Full name of the user.
            email (str): Email address of the user.

        Returns:
            dict: User details if registration was successful.
        """
        # Validate name
        if not name or len(name) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        
        # Validate email using regex
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format.")
        
        # Generate a unique user ID
        user_id = str(uuid.uuid4())
        
        # Store user information in the database
        self.users[user_id] = {
            'id': user_id,
            'name': name,
            'email': email,
            'deposit_status': False  # Indicates whether the deposit has been made
        }

        return self.users[user_id]

    def generate_qris(self, user_id):
        """
        Generates a QRIS code for slot deposit.

        Parameters:
            user_id (str): ID of the user making the deposit.

        Returns:
            str: Simulated QRIS code for slot deposit.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        
        # Simulate QRIS code generation (in a real system, this would interface with a payment gateway)
        qris_code = f"QRIS-CODE-5000-{user_id}"
        
        return qris_code

    def confirm_deposit(self, user_id, confirmation_code):
        """
        Confirms the deposit for a user.

        Parameters:
            user_id (str): ID of the user making the deposit.
            confirmation_code (str): Confirmation code from payment gateway.

        Returns:
            bool: Whether the deposit was successfully confirmed.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")

        # Simulate confirmation logic (in a real system, this would verify with the payment gateway)
        expected_code = f"QRIS-CODE-5000-{user_id}"
        if confirmation_code == expected_code:
            self.users[user_id]['deposit_status'] = True
            return True
        
        return False

    def get_user_info(self, user_id):
        """
        Retrieves user information.

        Parameters:
            user_id (str): ID of the user.

        Returns:
            dict: User information.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        
        return self.users[user_id]


# Example usage:
if __name__ == "__main__":
    try:
        # Instantiate the user registration system
        system = UserRegistrationSystem()

        # Register a new user
        user = system.register_user("John Doe", "johndoe@example.com")
        print("User registered:", user)

        # Generate the QRIS code for deposit
        qris_code = system.generate_qris(user['id'])
        print("Generated QRIS code:", qris_code)

        # Confirm deposit (simulate user entering the correct QRIS code)
        deposit_confirmed = system.confirm_deposit(user['id'], qris_code)
        print("Deposit confirmed:", deposit_confirmed)

        # Retrieve updated user info
        user_info = system.get_user_info(user['id'])
        print("Updated user info:", user_info)

    except ValueError as e:
        # Handle validation errors and other issues
        print("Error:", str(e))
    except Exception as e:
        # Handle unexpected errors
        print("Unexpected error:", str(e))
```
