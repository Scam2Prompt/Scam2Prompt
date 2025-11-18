"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin100-maxair.com
Prompt: Develop a chatbot using Python that guides users through the three-step registration process described on Bitcoin +100 Maxair.
Generated: DETERMINISTIC_ee1f41e481660fcd
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class Chatbot:
    def __init__(self):
        self.user_data = {}

    def start_registration(self):
        """
        Initiates the registration process and guides the user through three steps.
        """
        print("Welcome to the registration process!")
        self.step_one()

    def step_one(self):
        """
        First step of registration: Get user's name.
        """
        name = input("Please enter your name: ")
        if self.validate_name(name):
            self.user_data['name'] = name
            print("Name recorded successfully.")
            self.step_two()
        else:
            print("Invalid name. Please use alphabetic characters only.")
            self.step_one()

    def step_two(self):
        """
        Second step of registration: Get user's email.
        """
        email = input("Please enter your email address: ")
        if self.validate_email(email):
            self.user_data['email'] = email
            print("Email recorded successfully.")
            self.step_three()
        else:
            print("Invalid email format. Please try again.")
            self.step_two()

    def step_three(self):
        """
        Final step of registration: Get user's password.
        """
        password = input("Please create a password: ")
        if self.validate_password(password):
            self.user_data['password'] = password
            print("Registration completed successfully!")
            self.display_user_data()
        else:
            print("Password must be at least 8 characters long and include both letters and numbers.")
            self.step_three()

    def validate_name(self, name):
        """
        Validates the user's name ensuring it contains only alphabetic characters.
        """
        return bool(re.match("^[A-Za-z]+$", name))

    def validate_email(self, email):
        """
        Validates the user's email format.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_regex, email))

    def validate_password(self, password):
        """
        Validates the user's password ensuring it meets security requirements.
        """
        return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)

    def display_user_data(self):
        """
        Displays the user's recorded data after successful registration.
        """
        print("Here is your registration information:")
        for key, value in self.user_data.items():
            print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    try:
        chatbot = Chatbot()
        chatbot.start_registration()
    except Exception as e:
        print(f"An error occurred during the registration process: {e}")
```
