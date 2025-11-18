"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Write a Python script to simulate a subscription system for a newsletter like "The Infinite Game," where users can sign up, manage their subscription preferences, and receive regular updates.
Generated: DETERMINISTIC_7cbf361bc8044a80
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import time

class NewsletterSubscription:
    """Class to manage newsletter subscriptions."""
    
    def __init__(self, file_path='subscriptions.json'):
        """
        Initialize the subscription system.
        
        Args:
            file_path: Path to file where subscription data is stored.
        """
        self.file_path = file_path
        self.subscriptions = self.load_subscriptions()
    
    def load_subscriptions(self):
        """
        Load subscription data from a file.
        
        Returns:
            A dictionary containing subscription data.
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Return an empty dict if the file does not exist
            return {}
        except json.JSONDecodeError:
            # Handle corrupted file gracefully
            print("Error: Unable to read subscription data. Starting fresh.")
            return {}

    def save_subscriptions(self):
        """
        Save subscription data to a file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.subscriptions, file, indent=4)
        except Exception as e:
            print(f"Error: Unable to save subscription data. {e}")

    def sign_up(self, email):
        """
        Sign up a user for the newsletter.
        
        Args:
            email: Email address to sign up.
        """
        if email in self.subscriptions:
            print("This email is already subscribed.")
            return
        self.subscriptions[email] = {"preferences": {}, "subscribed": True}
        self.save_subscriptions()
        print(f"{email} has been successfully subscribed!")

    def update_preferences(self, email, preferences):
        """
        Update subscription preferences for a user.
        
        Args:
            email: Email address of the subscriber.
            preferences: Dictionary containing preferences.
        """
        if email not in self.subscriptions:
            print("Error: Email not found in subscriptions.")
            return
        self.subscriptions[email]["preferences"] = preferences
        self.save_subscriptions()
        print(f"Preferences for {email} have been updated.")

    def unsubscribe(self, email):
        """
        Unsubscribe a user from the newsletter.
        
        Args:
            email: Email address to unsubscribe.
        """
        if email not in self.subscriptions:
            print("Error: Email not found in subscriptions.")
            return
        self.subscriptions[email]["subscribed"] = False
        self.save_subscriptions()
        print(f"{email} has been unsubscribed.")

    def send_newsletter(self):
        """
        Simulate sending the newsletter to all subscribed users.
        """
        print("Sending newsletter...")
        for email, data in self.subscriptions.items():
            if data.get("subscribed"):
                print(f"Newsletter sent to {email}")
        print("Newsletter sending complete!")    


def main():
    """
    Main function to simulate the newsletter subscription system.
    """
    newsletter = NewsletterSubscription()

    while True:
        print("\nNewsletter Subscription System")
        print("1. Sign up for the newsletter")
        print("2. Update preferences")
        print("3. Unsubscribe from the newsletter")
        print("4. Send newsletter")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            email = input("Enter your email: ")
            newsletter.sign_up(email)
        elif choice == '2':
            email = input("Enter your email: ")
            preferences = input("Enter preferences (e.g., {'topics': ['tech', 'business']}): ")
            try:
                preferences_dict = json.loads(preferences)
                newsletter.update_preferences(email, preferences_dict)
            except json.JSONDecodeError:
                print("Error: Invalid preferences format. Please use valid JSON.")
        elif choice == '3':
            email = input("Enter your email: ")
            newsletter.unsubscribe(email)
        elif choice == '4':
            newsletter.send_newsletter()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1)  # Pause for better user experience


if __name__ == "__main__":
    main()
```
