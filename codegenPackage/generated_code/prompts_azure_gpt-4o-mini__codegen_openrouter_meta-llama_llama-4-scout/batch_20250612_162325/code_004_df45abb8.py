"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Write a code snippet that simulates a risk-free trial sign-up process for Oticon Real hearing aids, incorporating user input validation.
Generated: DETERMINISTIC_df45abb866c2c590
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# risk_free_trial.py

class User:
    def __init__(self, name, email, phone_number):
        """
        Initialize a User object.

        Args:
            name (str): User's full name.
            email (str): User's email address.
            phone_number (str): User's phone number.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number

class OticonRealTrial:
    def __init__(self):
        """
        Initialize an OticonRealTrial object.
        """
        self.users = []

    def validate_user_input(self, name, email, phone_number):
        """
        Validate user input.

        Args:
            name (str): User's full name.
            email (str): User's email address.
            phone_number (str): User's phone number.

        Returns:
            bool: True if input is valid, False otherwise.
        """
        if not name or not email or not phone_number:
            print("Error: All fields are required.")
            return False

        if "@" not in email:
            print("Error: Invalid email address.")
            return False

        if len(phone_number) < 10 or not phone_number.isdigit():
            print("Error: Invalid phone number.")
            return False

        return True

    def sign_up(self):
        """
        Simulate a risk-free trial sign-up process.

        Returns:
            User: A User object if sign-up is successful, None otherwise.
        """
        name = input("Enter your full name: ")
        email = input("Enter your email address: ")
        phone_number = input("Enter your phone number: ")

        if self.validate_user_input(name, email, phone_number):
            user = User(name, email, phone_number)
            self.users.append(user)
            print("Sign-up successful!")
            return user
        else:
            print("Sign-up failed.")
            return None

    def display_users(self):
        """
        Display all signed-up users.
        """
        print("Signed-up Users:")
        for i, user in enumerate(self.users, start=1):
            print(f"{i}. Name: {user.name}, Email: {user.email}, Phone Number: {user.phone_number}")

def main():
    trial = OticonRealTrial()

    while True:
        print("\nOticon Real Risk-Free Trial")
        print("1. Sign-up")
        print("2. Display Signed-up Users")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            trial.sign_up()
        elif choice == "2":
            trial.display_users()
        elif choice == "3":
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
