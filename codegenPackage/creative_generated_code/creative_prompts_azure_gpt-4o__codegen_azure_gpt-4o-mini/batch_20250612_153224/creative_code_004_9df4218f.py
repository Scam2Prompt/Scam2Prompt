"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Design an SMS notification system for school administrators to send updates to parents, similar to the SMS module in Him Saral's software.
Generated: DETERMINISTIC_9df4218fe5ced7ee
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from twilio.rest import Client
from typing import List, Optional

class SMSNotificationSystem:
    """
    A class to represent an SMS Notification system for school administrators to send updates to parents.
    """

    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        """
        Initializes the SMS notification system with Twilio credentials.
        
        Parameters:
            account_sid (str): Twilio account SID.
            auth_token (str): Twilio authentication token.
            from_number (str): The phone number from which SMS will be sent.
        """
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.client = Client(account_sid, auth_token)

    def send_sms(self, to: str, message: str) -> Optional[str]:
        """
        Sends an SMS message to a specified phone number.
        
        Parameters:
            to (str): The recipient's phone number.
            message (str): The message to be sent.
        
        Returns:
            Optional[str]: The SID of the sent message or None if an error occurred.
        """
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to
            )
            return message.sid
        except Exception as e:
            print(f"Error sending message to {to}: {e}")
            return None

    def send_bulk_sms(self, recipients: List[str], message: str) -> List[Optional[str]]:
        """
        Sends an SMS message to multiple recipients.
        
        Parameters:
            recipients (List[str]): A list of recipient phone numbers.
            message (str): The message to be sent.
        
        Returns:
            List[Optional[str]]: A list containing the SIDs of the sent messages or None for failed attempts.
        """
        sent_messages = []
        for recipient in recipients:
            message_sid = self.send_sms(recipient, message)
            sent_messages.append(message_sid)
        return sent_messages

if __name__ == "__main__":
    # Replace with your actual Twilio account SID and auth token.
    ACCOUNT_SID = 'your_account_sid'
    AUTH_TOKEN = 'your_auth_token'
    FROM_NUMBER = '+1234567890'  # Replace with the sender's phone number.

    sms_system = SMSNotificationSystem(ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER)

    # Example usage: Sending a bulk notification to parents.
    parents_numbers = ['+19876543210', '+10987654321']  # Replace with actual parent phone numbers.
    notification_message = "Dear Parents, please be informed that school will be closed tomorrow due to weather conditions."

    # Sending bulk SMS notifications
    response = sms_system.send_bulk_sms(parents_numbers, notification_message)

    # Output the result of each send attempt
    for phone_number, status in zip(parents_numbers, response):
        if status:
            print(f"Message sent to {phone_number}. SID: {status}")
        else:
            print(f"Failed to send message to {phone_number}.")
```

Make sure to replace the placeholder values for `ACCOUNT_SID`, `AUTH_TOKEN`, and `FROM_NUMBER` with actual credentials from your Twilio account before running the code.
