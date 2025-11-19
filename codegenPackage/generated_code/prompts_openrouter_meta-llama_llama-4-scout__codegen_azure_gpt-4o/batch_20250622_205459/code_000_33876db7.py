"""
Generated Code Metadata:
========================
Original URL: https://myrmp.org
Prompt: Write a Python script to manage membership subscriptions for a professional organization like RMP.
Generated: DETERMINISTIC_33876db7f776b609
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class MembershipManager:
    """
    A class to manage membership subscriptions for a professional organization.
    """

    def __init__(self, data_file="members.json"):
        """
        Initialize the MembershipManager with a data file to store member information.
        :param data_file: Path to the JSON file where member data is stored.
        """
        self.data_file = data_file
        self.members = self._load_members()

    def _load_members(self):
        """
        Load member data from the JSON file.
        :return: A dictionary of members.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading member data. Starting with an empty database.")
                return {}
        return {}

    def _save_members(self):
        """
        Save member data to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.members, file, indent=4)
        except IOError as e:
            print(f"Error saving member data: {e}")

    def add_member(self, name, email, subscription_type):
        """
        Add a new member to the organization.
        :param name: Name of the member.
        :param email: Email address of the member.
        :param subscription_type: Type of subscription (e.g., "monthly", "annual").
        """
        if email in self.members:
            print("Error: A member with this email already exists.")
            return

        self.members[email] = {
            "name": name,
            "email": email,
            "subscription_type": subscription_type,
            "start_date": datetime.date.today().isoformat(),
            "end_date": self._calculate_end_date(subscription_type)
        }
        self._save_members()
        print(f"Member {name} added successfully.")

    def _calculate_end_date(self, subscription_type):
        """
        Calculate the end date of a subscription based on its type.
        :param subscription_type: Type of subscription (e.g., "monthly", "annual").
        :return: End date as a string in ISO format.
        """
        if subscription_type == "monthly":
            return (datetime.date.today() + datetime.timedelta(days=30)).isoformat()
        elif subscription_type == "annual":
            return (datetime.date.today() + datetime.timedelta(days=365)).isoformat()
        else:
            print("Error: Invalid subscription type. Defaulting to monthly.")
            return (datetime.date.today() + datetime.timedelta(days=30)).isoformat()

    def remove_member(self, email):
        """
        Remove a member from the organization.
        :param email: Email address of the member to remove.
        """
        if email in self.members:
            del self.members[email]
            self._save_members()
            print(f"Member with email {email} removed successfully.")
        else:
            print("Error: No member found with this email.")

    def list_members(self):
        """
        List all members in the organization.
        """
        if not self.members:
            print("No members found.")
            return

        print("Current Members:")
        for email, info in self.members.items():
            print(f"Name: {info['name']}, Email: {email}, Subscription: {info['subscription_type']}, "
                  f"Start Date: {info['start_date']}, End Date: {info['end_date']}")

    def renew_subscription(self, email, subscription_type):
        """
        Renew a member's subscription.
        :param email: Email address of the member.
        :param subscription_type: New subscription type (e.g., "monthly", "annual").
        """
        if email in self.members:
            self.members[email]["subscription_type"] = subscription_type
            self.members[email]["start_date"] = datetime.date.today().isoformat()
            self.members[email]["end_date"] = self._calculate_end_date(subscription_type)
            self._save_members()
            print(f"Subscription for {email} renewed successfully.")
        else:
            print("Error: No member found with this email.")

# Example usage
if __name__ == "__main__":
    manager = MembershipManager()

    # Add members
    manager.add_member("Alice Johnson", "alice@example.com", "monthly")
    manager.add_member("Bob Smith", "bob@example.com", "annual")

    # List members
    manager.list_members()

    # Renew subscription
    manager.renew_subscription("alice@example.com", "annual")

    # Remove a member
    manager.remove_member("bob@example.com")

    # List members again
    manager.list_members()
```
