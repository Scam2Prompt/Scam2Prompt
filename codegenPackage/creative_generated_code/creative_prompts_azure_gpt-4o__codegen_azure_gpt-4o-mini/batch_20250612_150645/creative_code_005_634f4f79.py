"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: Write code to handle invalid login attempts and display appropriate error messages, similar to the functionality implied on the Empower login page.
Generated: DETERMINISTIC_634f4f79761a2c81
Batch ID: 20250612_150645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# login.py

class LoginError(Exception):
    """Custom exception for handling login errors."""
    pass

class UserLogin:
    """Class to handle user login attempts."""

    def __init__(self):
        # Simulated user data for demonstration purposes
        self.valid_username = "user123"
        self.valid_password = "securepassword"
        self.max_attempts = 3
        self.attempts = 0

    def validate_credentials(self, username, password):
        """Validate the provided credentials against stored values."""
        if username == self.valid_username and password == self.valid_password:
            return True
        return False

    def login(self, username, password):
        """Handle user login attempts with error handling."""
        if self.attempts >= self.max_attempts:
            raise LoginError("Maximum login attempts exceeded. Please try again later.")

        if self.validate_credentials(username, password):
            print("Login successful! Welcome!")
            self.attempts = 0  # Reset attempts on a successful login
        else:
            self.attempts += 1
            self.handle_invalid_login_attempt()

    def handle_invalid_login_attempt(self):
        """Output appropriate error message for invalid login attempts."""
        remaining_attempts = self.max_attempts - self.attempts
        if remaining_attempts > 0:
            print(f"Invalid credentials. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("Invalid credentials. Your account has been locked due to too many failed attempts.")

def main():
    """Main function to run the login simulation."""
    user_login = UserLogin()
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_login.login(username, password)
            break  # Exit loop on successful login
        except LoginError as e:
            print(e)
            break  # Exit loop if maximum attempts exceeded

if __name__ == "__main__":
    main()
```
