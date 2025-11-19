"""
Generated Code Metadata:
========================
Original URL: https://omninetwork.org
Prompt: Create a Python script that handles user subscription to a newsletter, including validation for already subscribed users, inspired by the subscription functionality on Omni Network.
Generated: DETERMINISTIC_bc3f77e962d5b9b3
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# newsletter_subscriber.py

import re
import hashlib
from typing import Dict

class NewsletterSubscriber:
    def __init__(self, subscribers: Dict[str, str] = {}):
        """
        Initialize the NewsletterSubscriber class.

        Args:
        subscribers (Dict[str, str]): A dictionary of subscribers where the key is the email and the value is the subscription date.
        """
        self.subscribers = subscribers

    def validate_email(self, email: str) -> bool:
        """
        Validate an email address.

        Args:
        email (str): The email address to validate.

        Returns:
        bool: True if the email is valid, False otherwise.
        """
        # Regular expression for validating an email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return bool(re.match(regex, email))

    def is_subscribed(self, email: str) -> bool:
        """
        Check if a user is already subscribed.

        Args:
        email (str): The email address to check.

        Returns:
        bool: True if the user is subscribed, False otherwise.
        """
        return email in self.subscribers

    def subscribe(self, email: str) -> str:
        """
        Subscribe a user to the newsletter.

        Args:
        email (str): The email address to subscribe.

        Returns:
        str: A success message or an error message if the user is already subscribed.

        Raises:
        ValueError: If the email is not valid.
        """
        if not self.validate_email(email):
            raise ValueError("Invalid email address")

        if self.is_subscribed(email):
            return f"{email} is already subscribed."

        # Generate a hash of the email to store (for simplicity and to avoid storing personal data)
        email_hash = hashlib.sha256(email.encode()).hexdigest()
        self.subscribers[email] = email_hash
        return f"{email} subscribed successfully."

    def unsubscribe(self, email: str) -> str:
        """
        Unsubscribe a user from the newsletter.

        Args:
        email (str): The email address to unsubscribe.

        Returns:
        str: A success message or an error message if the user is not subscribed.

        Raises:
        ValueError: If the email is not valid.
        """
        if not self.validate_email(email):
            raise ValueError("Invalid email address")

        if not self.is_subscribed(email):
            return f"{email} is not subscribed."

        del self.subscribers[email]
        return f"{email} unsubscribed successfully."


def main():
    subscriber = NewsletterSubscriber()

    while True:
        print("\n1. Subscribe\n2. Unsubscribe\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            email = input("Enter your email: ")
            try:
                print(subscriber.subscribe(email))
            except ValueError as e:
                print(e)
        elif choice == "2":
            email = input("Enter your email: ")
            try:
                print(subscriber.unsubscribe(email))
            except ValueError as e:
                print(e)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
