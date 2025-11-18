"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wordpress.armelin.media
Prompt: Generate a Python script to manage subscriptions for the Études Newsletter, ensuring users receive exclusive design insights and case studies, as highlighted on the Armelin Media site.
Generated: DETERMINISTIC_3704a710af99a8e7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Études Newsletter Subscription Manager

This script allows users to manage subscriptions for the Études Newsletter, which provides exclusive 
design insights and case studies as featured on the Armelin Media site.

Features:
- Add new subscribers
- Remove existing subscribers
- List all subscribers
- Safely handle errors and persist data

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

import json
import os

# File to store subscriber data
DATA_FILE = "subscribers.json"

def load_subscribers():
    """
    Loads the subscriber list from the data file.
    Returns:
        list: A list of subscribers.
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_subscribers(subscribers):
    """
    Saves the subscriber list to the data file.
    Args:
        subscribers (list): The list of subscribers to save.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(subscribers, file, indent=4)
    except IOError as e:
        print(f"Error saving subscribers: {e}")

def add_subscriber(email):
    """
    Adds a new subscriber to the list.
    Args:
        email (str): The email address of the subscriber to add.
    """
    subscribers = load_subscribers()
    if email in subscribers:
        print("This email is already subscribed.")
        return
    subscribers.append(email)
    save_subscribers(subscribers)
    print(f"Successfully subscribed: {email}")

def remove_subscriber(email):
    """
    Removes an existing subscriber from the list.
    Args:
        email (str): The email address of the subscriber to remove.
    """
    subscribers = load_subscribers()
    if email not in subscribers:
        print("This email is not subscribed.")
        return
    subscribers.remove(email)
    save_subscribers(subscribers)
    print(f"Successfully unsubscribed: {email}")

def list_subscribers():
    """
    Lists all subscribers.
    """
    subscribers = load_subscribers()
    if not subscribers:
        print("No subscribers found.")
        return
    print("List of subscribers:")
    for idx, email in enumerate(subscribers, start=1):
        print(f"{idx}. {email}")

def main():
    """
    Main function to manage the Études Newsletter subscriptions.
    Provides a command-line interface for subscription management.
    """
    print("Welcome to the Études Newsletter Subscription Manager!")
    while True:
        print("\nChoose an option:")
        print("1. Add Subscriber")
        print("2. Remove Subscriber")
        print("3. List Subscribers")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            email = input("Enter the email to subscribe: ").strip()
            add_subscriber(email)
        elif choice == 2:
            email = input("Enter the email to unsubscribe: ").strip()
            remove_subscriber(email)
        elif choice == 3:
            list_subscribers()
        elif choice == 4:
            print("Exiting the Subscription Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
```
