"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Create a program that links stored user interaction data to automatic notifications for product recalls, based on the analytics features described by Interactive Warning Systems.
Generated: DETERMINISTIC_48e0312f316140a1
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Any

class UserInteractionData:
    """Class to handle user interaction data."""

    def __init__(self, filepath: str):
        """
        Initializes the UserInteractionData with a filepath to the JSON data.

        :param filepath: Path to the JSON file containing user interaction data.
        """
        self.filepath = filepath
        self.user_data = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """Loads user interaction data from a JSON file."""
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            return []

    def get_users_to_notify(self, product_id: str) -> List[str]:
        """
        Retrieves a list of users who interacted with a specific product.

        :param product_id: The ID of the product to check notifications for.
        :return: A list of user emails to notify.
        """
        return [user['email'] for user in self.user_data if product_id in user.get('interactions', [])]

class NotificationSystem:
    """Class to handle sending notifications."""

    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initializes the NotificationSystem with server details.

        :param smtp_server: SMTP server address.
        :param smtp_port: SMTP server port.
        :param sender_email: Sender's email address.
        :param sender_password: Sender's email password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email: str, subject: str, message: str) -> None:
        """
        Sends an email notification.

        :param recipient_email: Recipient's email address.
        :param subject: Subject of the email.
        :param message: Body of the email.
        """
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                print(f"Notification sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send notification to {recipient_email}: {e}")

def notify_users_of_recall(product_id: str, user_data_filepath: str, notification_system: NotificationSystem) -> None:
    """
    Notifies users of a product recall based on user interaction data.

    :param product_id: The ID of the recalled product.
    :param user_data_filepath: Path to the user interaction data JSON file.
    :param notification_system: Instance of NotificationSystem to send emails.
    """
    user_data = UserInteractionData(user_data_filepath)
    users_to_notify = user_data.get_users_to_notify(product_id)

    if not users_to_notify:
        print(f"No users found for product ID: {product_id}.")
        return

    subject = f"Important Recall Notice for Product ID: {product_id}"
    message = f"The product with ID {product_id} has been recalled. Please check the details on our website."

    for email in users_to_notify:
        notification_system.send_notification(email, subject, message)

# Example usage
if __name__ == "__main__":
    # Configure the notification system
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    sender_password = "your_secure_password"

    # Create an instance of NotificationSystem
    notification_system = NotificationSystem(smtp_server, smtp_port, sender_email, sender_password)

    # Trigger notifications for a product recall
    product_id_to_recall = "12345"
    user_data_filepath = "user_interactions.json"
    
    notify_users_of_recall(product_id_to_recall, user_data_filepath, notification_system)
```
