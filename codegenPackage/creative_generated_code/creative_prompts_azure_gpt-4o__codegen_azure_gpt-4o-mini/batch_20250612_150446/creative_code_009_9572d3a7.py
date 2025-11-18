"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smart-coins.pro
Prompt: Write code to automate email notifications for account registration, deposit confirmations, and withdrawal requests, as outlined in the smart-coins.pro workflow.
Generated: DETERMINISTIC_9572d3a7d2df924c
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Any

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the EmailNotifier with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send an email to the specified recipient with the given subject and body.
        
        Args:
            recipient (str): Email address of the recipient.
            subject (str): Subject of the email.
            body (str): Body of the email content.
        
        Returns:
            bool: True if email is sent successfully, False otherwise.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(self.username, self.password)  # Login to the SMTP server
                server.send_message(msg)  # Send the email

            return True
        except Exception as e:
            print(f"Error sending email to {recipient}: {e}")
            return False

def generate_registration_email(user_info: Dict[str, Any]) -> str:
    """Generate the email content for account registration notification.
    
    Args:
        user_info (Dict[str, Any]): Dictionary containing user information.
        
    Returns:
        str: The email body for account registration.
    """
    return f"Hello {user_info['name']},\n\nThank you for registering your account at Smart Coins!\n\nBest Regards,\nSmart Coins Team"

def generate_deposit_confirmation_email(user_info: Dict[str, Any], amount: float) -> str:
    """Generate the email content for deposit confirmation notification.
    
    Args:
        user_info (Dict[str, Any]): Dictionary containing user information.
        amount (float): The deposit amount.
        
    Returns:
        str: The email body for deposit confirmation.
    """
    return f"Hello {user_info['name']},\n\nYour deposit of ${amount:.2f} has been confirmed!\n\nBest Regards,\nSmart Coins Team"

def generate_withdrawal_request_email(user_info: Dict[str, Any>, amount: float) -> str:
    """Generate the email content for withdrawal request notification.
    
    Args:
        user_info (Dict[str, Any]): Dictionary containing user information.
        amount (float): The requested withdrawal amount.
        
    Returns:
        str: The email body for withdrawal request.
    """
    return f"Hello {user_info['name']},\n\nYour withdrawal request of ${amount:.2f} is being processed.\n\nBest Regards,\nSmart Coins Team"

if __name__ == "__main__":
    # Example usage
    email_notifier = EmailNotifier(smtp_server="smtp.your-email.com",
                                    smtp_port=587,
                                    username="your-email@example.com",
                                    password="your-password")
    
    user_info = {'name': 'John Doe', 'email': 'john.doe@example.com'}

    # Send registration email
    registration_email_body = generate_registration_email(user_info)
    email_notifier.send_email(user_info['email'], "Welcome to Smart Coins", registration_email_body)

    # Send deposit confirmation email
    deposit_amount = 100.0
    deposit_email_body = generate_deposit_confirmation_email(user_info, deposit_amount)
    email_notifier.send_email(user_info['email'], "Deposit Confirmation", deposit_email_body)

    # Send withdrawal request email
    withdrawal_amount = 50.0
    withdrawal_email_body = generate_withdrawal_request_email(user_info, withdrawal_amount)
    email_notifier.send_email(user_info['email'], "Withdrawal Request", withdrawal_email_body)
```
