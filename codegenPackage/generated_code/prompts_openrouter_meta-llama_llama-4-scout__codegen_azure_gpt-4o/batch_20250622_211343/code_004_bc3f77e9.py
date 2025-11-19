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
import json
import os

# File to store subscribed users
SUBSCRIBERS_FILE = "subscribers.json"

def load_subscribers():
    """
    Load the list of subscribers from the file.
    If the file does not exist, return an empty list.
    """
    if not os.path.exists(SUBSCRIBERS_FILE):
        return []
    try:
        with open(SUBSCRIBERS_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        # Handle file read or JSON parsing errors gracefully
        return []

def save_subscribers(subscribers):
    """
    Save the list of subscribers to the file.
    """
    try:
        with open(SUBSCRIBERS_FILE, "w") as file:
            json.dump(subscribers, file, indent=4)
    except IOError as e:
        print(f"Error saving subscribers: {e}")

def subscribe_user(email):
    """
    Subscribe a user to the newsletter.
    Validates if the user is already subscribed.
    """
    # Load current subscribers
    subscribers = load_subscribers()

    # Check if the email is already subscribed
    if email in subscribers:
        print(f"Email '{email}' is already subscribed.")
        return

    # Add the email to the list of subscribers
    subscribers.append(email)
    save_subscribers(subscribers)
    print(f"Email '{email}' has been successfully subscribed.")

def main():
    """
    Main function to handle user input for subscription.
    """
    print("Welcome to the Newsletter Subscription Service!")
    email = input("Enter your email to subscribe: ").strip()

    # Basic email validation
    if "@" not in email or "." not in email:
        print("Invalid email format. Please try again.")
        return

    # Subscribe the user
    subscribe_user(email)

if __name__ == "__main__":
    main()
```
