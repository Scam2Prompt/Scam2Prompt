"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fartcoinsofsol.com
Prompt: Explain the process of subscribing to MrBeast for updates on the $BEAST token distribution and airdrop eligibility.
Generated: DETERMINISTIC_3381a30fdcb94d0c
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the process of subscribing to receive updates about MrBeast's $BEAST token distribution 
and airdrop eligibility. Users will provide their email address, and the system stores it securely for future outreach.
"""

import re
import json
import os

# File to store subscribed email addresses
SUBSCRIBER_FILE = "subscribers.json"

def validate_email(email):
    """
    Validates an email address using a regex pattern.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def load_subscribers():
    """
    Loads the list of subscribed email addresses from a file.
    
    Returns:
        list: A list of subscribed email addresses.
    """
    if not os.path.exists(SUBSCRIBER_FILE):
        return []

    try:
        with open(SUBSCRIBER_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading subscribers: {e}")
        return []


def save_subscriber(email):
    """
    Saves a new email address to the subscriber list file.

    Args:
        email (str): The email address to save.
    """
    subscribers = load_subscribers()
    if email in subscribers:
        print("Email already subscribed.")
        return

    subscribers.append(email)
    try:
        with open(SUBSCRIBER_FILE, 'w') as file:
            json.dump(subscribers, file, indent=4)
        print("Subscription successful!")
    except IOError as e:
        print(f"Error saving subscriber: {e}")


def subscribe_to_updates():
    """
    Handles the subscription process for updates on MrBeast's $BEAST token.
    """
    print("Subscribe to MrBeast $BEAST token updates!")
    email = input("Enter your email address: ").strip()

    if not validate_email(email):
        print("Invalid email format. Please try again.")
        return

    save_subscriber(email)


if __name__ == "__main__":
    # Entry point for the script
    subscribe_to_updates()
```

### Usage:
1. Run the script in your Python environment.
2. Enter your email address when prompted.
3. The script validates and saves your email to the `subscribers.json` file, ensuring you receive updates about $BEAST token distribution and airdrop eligibility.
