"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Generate Python code to implement a newsletter subscription system with email validation, referencing the "Subscribe Our Newsletter" section from "Meet A Great American."
Generated: DETERMINISTIC_209646286a40cce5
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List


class NewsletterSubscription:
    """
    Class to manage newsletter subscriptions.
    Includes email validation and subscription management.
    """

    def __init__(self):
        # List to store subscribed email addresses
        self.subscribers: List[str] = []

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validate email address using regular expression.

        :param email: Email address as a string
        :return: True if the email is valid, False otherwise
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def subscribe(self, email: str) -> str:
        """
        Subscribe a user to the newsletter.

        :param email: Email address to subscribe
        :return: Success or error message
        """
        if not self.is_valid_email(email):
            return "Error: Invalid email address. Please provide a valid email."

        if email in self.subscribers:
            return "Error: This email is already subscribed to the newsletter."

        self.subscribers.append(email)
        return "Success: You have successfully subscribed to the newsletter!"

    def unsubscribe(self, email: str) -> str:
        """
        Unsubscribe a user from the newsletter.

        :param email: Email address to unsubscribe
        :return: Success or error message
        """
        if email not in self.subscribers:
            return "Error: This email is not subscribed to the newsletter."

        self.subscribers.remove(email)
        return "Success: You have successfully unsubscribed from the newsletter."

    def list_subscribers(self) -> List[str]:
        """
        Get a list of all subscribed email addresses.

        :return: List of subscribed emails
        """
        return self.subscribers


# Example usage
if __name__ == "__main__":
    newsletter = NewsletterSubscription()

    # Subscribe users
    print(newsletter.subscribe("john.doe@example.com"))  # Valid email
    print(newsletter.subscribe("invalid-email"))         # Invalid email
    print(newsletter.subscribe("john.doe@example.com"))  # Duplicate email

    # Unsubscribe users
    print(newsletter.unsubscribe("john.doe@example.com"))  # Valid unsubscribe
    print(newsletter.unsubscribe("jane.doe@example.com"))  # Email not subscribed

    # List current subscribers
    print("Current subscribers:", newsletter.list_subscribers())
```
