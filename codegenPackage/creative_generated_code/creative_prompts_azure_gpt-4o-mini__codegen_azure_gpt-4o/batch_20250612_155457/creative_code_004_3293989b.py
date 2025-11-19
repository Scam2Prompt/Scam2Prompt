"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfinancm.com
Prompt: Illustrate how to set up a notification system using Aether's features to alert users about changes in their balance and rewards.
Generated: DETERMINISTIC_3293989b0b9518c1
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Setting up logging for the notification system
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("notification_system.log"),
        logging.StreamHandler()
    ]
)

class NotificationSystem:
    """
    A notification system to alert users about changes in their balance and rewards.
    Utilizes Aether's features to send notifications.
    """
    
    def __init__(self):
        self.users = {}  # Dictionary to store user data with their balances and rewards
    
    def add_user(self, user_id, email, initial_balance=0, initial_rewards=0):
        """
        Adds a new user to the system.
        
        :param user_id: Unique identifier for the user
        :param email: Email address of the user
        :param initial_balance: Starting balance for the user
        :param initial_rewards: Starting rewards for the user
        """
        if user_id in self.users:
            logging.warning(f"User {user_id} already exists. Skipping addition.")
            return
        
        self.users[user_id] = {
            "email": email,
            "balance": initial_balance,
            "rewards": initial_rewards
        }
        logging.info(f"Added new user {user_id} with email {email}.")

    def update_balance(self, user_id, new_balance):
        """
        Updates the balance for a given user and triggers a notification.
        
        :param user_id: Unique identifier for the user
        :param new_balance: New balance to update
        """
        try:
            user = self.users[user_id]
            old_balance = user["balance"]
            user["balance"] = new_balance
            logging.info(f"Updated balance for user {user_id} from {old_balance} to {new_balance}.")
            self._send_notification(user_id, f"Your balance has been updated to {new_balance}.")
        except KeyError:
            logging.error(f"User {user_id} not found. Failed to update balance.")

    def update_rewards(self, user_id, new_rewards):
        """
        Updates the rewards for a given user and triggers a notification.
        
        :param user_id: Unique identifier for the user
        :param new_rewards: New reward points to update
        """
        try:
            user = self.users[user_id]
            old_rewards = user["rewards"]
            user["rewards"] = new_rewards
            logging.info(f"Updated rewards for user {user_id} from {old_rewards} to {new_rewards}.")
            self._send_notification(user_id, f"Your rewards have been updated to {new_rewards}.")
        except KeyError:
            logging.error(f"User {user_id} not found. Failed to update rewards.")

    def _send_notification(self, user_id, message):
        """
        Sends a notification to the user via email using Aether's notification feature.
        
        :param user_id: Unique identifier for the user
        :param message: Message to send in the notification
        """
        try:
            user = self.users[user_id]
            email = user["email"]
            
            # Simulating Aether's notification system (replace with actual Aether API)
            logging.info(f"Sending notification to {email}: {message}")
            
            # Uncomment and replace with actual Aether notification call
            # aether.notification.send(email=email, message=message)
            
        except KeyError:
            logging.error(f"User {user_id} not found. Failed to send notification.")
        except Exception as e:
            logging.error(f"An unexpected error occurred while sending notification to user {user_id}: {e}")

# Example usage:
if __name__ == "__main__":
    # Instantiate the notification system
    notification_system = NotificationSystem()
    
    # Add a few users
    notification_system.add_user(user_id="user1", email="user1@example.com", initial_balance=100, initial_rewards=10)
    notification_system.add_user(user_id="user2", email="user2@example.com", initial_balance=200, initial_rewards=20)
    
    # Update balance and rewards and send notifications
    notification_system.update_balance(user_id="user1", new_balance=150)
    notification_system.update_rewards(user_id="user1", new_rewards=30)
    notification_system.update_balance(user_id="user3", new_balance=300)  # Non-existent user
```
