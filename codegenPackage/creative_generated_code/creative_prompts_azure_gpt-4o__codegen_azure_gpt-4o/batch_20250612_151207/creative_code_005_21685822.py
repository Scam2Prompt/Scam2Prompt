"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://client-website1.pages.dev
Prompt: Provide code examples for implementing a subscription system for publications, similar to the "Subscribe to our publications" feature on the Innodapter ApS website.
Generated: DETERMINISTIC_21685822281fa783
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_system.py

from datetime import datetime
import json
import re

# Define custom exception for invalid email format
class InvalidEmailException(Exception):
    pass

# Define a data store class to simulate a database
class DataStore:
    def __init__(self):
        # Dictionary to store subscriptions
        self.subscriptions = {}

    def add_subscription(self, email, publication_name):
        """
        Adds a subscription to the data store.
        :param email: Subscriber's email address
        :param publication_name: Publication name to subscribe to
        """
        if email not in self.subscriptions:
            self.subscriptions[email] = []

        self.subscriptions[email].append({
            "publication_name": publication_name,
            "subscribed_at": datetime.now().isoformat()
        })

    def get_subscriptions(self, email):
        """
        Retrieves all subscriptions for a given email.
        :param email: Subscriber's email address
        :return: List of subscriptions
        """
        return self.subscriptions.get(email, [])

    def save_to_file(self, file_path):
        """
        Save subscriptions to a JSON file.
        :param file_path: Path to file
        """
        with open(file_path, 'w') as file:
            json.dump(self.subscriptions, file, indent=4)

    def load_from_file(self, file_path):
        """
        Load subscriptions from a JSON file.
        :param file_path: Path to file
        """
        try:
            with open(file_path, 'r') as file:
                self.subscriptions = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.subscriptions = {}

# Utility function to validate email
def validate_email(email):
    """
    Validates an email address format.
    :param email: Email address to validate
    :return: True if valid, otherwise raises InvalidEmailException
    """
    email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_regex.match(email):
        raise InvalidEmailException("Invalid email format.")
    return True

# Main subscription system class
class SubscriptionSystem:
    def __init__(self):
        self.data_store = DataStore()

    def subscribe(self, email, publication_name):
        """
        Allows a user to subscribe to a publication.
        :param email: Subscriber's email address
        :param publication_name: Publication name to subscribe to
        """
        try:
            validate_email(email)
            self.data_store.add_subscription(email, publication_name)
            print(f"Successfully subscribed {email} to '{publication_name}'.")
        except InvalidEmailException as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def view_subscriptions(self, email):
        """
        Allows a user to view their subscriptions.
        :param email: Subscriber's email address
        """
        try:
            validate_email(email)
            subscriptions = self.data_store.get_subscriptions(email)
            if subscriptions:
                print(f"Subscriptions for {email}:")
                for subscription in subscriptions:
                    print(f"- {subscription['publication_name']} (Subscribed at: {subscription['subscribed_at']})")
            else:
                print(f"No subscriptions found for {email}.")
        except InvalidEmailException as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def save_data(self, file_path):
        """
        Save subscription data to a file.
        :param file_path: Path to file
        """
        try:
            self.data_store.save_to_file(file_path)
            print(f"Data successfully saved to {file_path}.")
        except Exception as e:
            print(f"An unexpected error occurred while saving data: {str(e)}")

    def load_data(self, file_path):
        """
        Load subscription data from a file.
        :param file_path: Path to file
        """
        try:
            self.data_store.load_from_file(file_path)
            print(f"Data successfully loaded from {file_path}.")
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {str(e)}")

# Example usage (uncomment below to test locally)
if __name__ == "__main__":
    subscription_system = SubscriptionSystem()

    # Subscribe users to publications
    subscription_system.subscribe("john.doe@example.com", "Tech News")
    subscription_system.subscribe("jane.doe@example.com", "Health Weekly")
    subscription_system.subscribe("invalid-email", "Tech News")  # Should trigger error

    # View subscriptions
    subscription_system.view_subscriptions("john.doe@example.com")
    subscription_system.view_subscriptions("jane.doe@example.com")
    subscription_system.view_subscriptions("non.existent@example.com")  # No subscriptions

    # Save and load data
    subscription_system.save_data("subscriptions.json")
    subscription_system.load_data("subscriptions.json")
```
