"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holders.sellpass.io
Prompt: Generate a script to implement AI fraud prevention using historical tracking and blacklist rules as described by Sellpass.
Generated: DETERMINISTIC_077fa6fc4071966a
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json


class FraudPreventionSystem:
    """
    A class to implement AI fraud prevention using historical tracking
    and blacklist rules as described by Sellpass.
    """

    def __init__(self):
        """
        Initialize the Fraud Prevention System.
        """
        self.transaction_history = {}  # Stores transaction history of users
        self.blacklist = set()  # Stores blacklisted user IDs or IPs

    def load_blacklist(self, filepath):
        """
        Load the blacklist from a JSON file.

        :param filepath: Path to the JSON file containing blacklist data.
        """
        try:
            with open(filepath, 'r') as file:
                self.blacklist = set(json.load(file))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading blacklist: {e}")
            self.blacklist = set()

    def save_blacklist(self, filepath):
        """
        Save the blacklist to a JSON file.

        :param filepath: Path to save the blacklist data.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(list(self.blacklist), file)
        except IOError as e:
            print(f"Error saving blacklist: {e}")

    def add_to_blacklist(self, user_id_or_ip):
        """
        Add a user ID or IP address to the blacklist.

        :param user_id_or_ip: The user ID or IP address to blacklist.
        """
        self.blacklist.add(user_id_or_ip)

    def record_transaction(self, user_id, transaction_amount, ip_address):
        """
        Record a new transaction for a user.

        :param user_id: Unique identifier of the user.
        :param transaction_amount: Amount of the transaction.
        :param ip_address: IP address of the user.
        """
        if user_id not in self.transaction_history:
            self.transaction_history[user_id] = []
        self.transaction_history[user_id].append({
            "amount": transaction_amount,
            "timestamp": datetime.datetime.now(),
            "ip_address": ip_address
        })

    def check_fraud(self, user_id, transaction_amount, ip_address):
        """
        Check if a transaction is fraudulent based on historical data and blacklist.

        :param user_id: Unique identifier of the user.
        :param transaction_amount: Amount of the transaction.
        :param ip_address: IP address of the user.
        :return: True if fraud detected, False otherwise.
        """
        # Check if user ID or IP address is blacklisted
        if user_id in self.blacklist or ip_address in self.blacklist:
            return True

        # Check transaction patterns
        if user_id in self.transaction_history:
            history = self.transaction_history[user_id]
            recent_transactions = [
                t for t in history if (datetime.datetime.now() - t["timestamp"]).days <= 30
            ]

            # Example rule: Flag users with unusually frequent transactions in the last 30 days
            if len(recent_transactions) > 10:
                return True

            # Example rule: Flag users with a transaction amount exceeding a threshold
            if transaction_amount > 5000:  # Threshold can be customized
                return True

        return False

    def handle_transaction(self, user_id, transaction_amount, ip_address):
        """
        Process a transaction and determine if it should be allowed or flagged as fraud.

        :param user_id: Unique identifier of the user.
        :param transaction_amount: Amount of the transaction.
        :param ip_address: IP address of the user.
        :return: None
        """
        if self.check_fraud(user_id, transaction_amount, ip_address):
            print(f"Transaction flagged as potential fraud for user {user_id} with IP {ip_address}")
        else:
            print(f"Transaction approved for user {user_id} with IP {ip_address}")
            self.record_transaction(user_id, transaction_amount, ip_address)


# Example usage
if __name__ == "__main__":
    # Initialize the fraud prevention system
    fps = FraudPreventionSystem()

    # Load blacklist data
    fps.load_blacklist("blacklist.json")

    # Handle transactions
    fps.handle_transaction("user123", 100, "192.168.1.1")
    fps.handle_transaction("user123", 6000, "192.168.1.1")  # High amount transaction
    fps.handle_transaction("blacklisted_user", 50, "192.168.1.2")  # Blacklisted user

    # Save updated blacklist
    fps.add_to_blacklist("user456")
    fps.save_blacklist("blacklist.json")
```
