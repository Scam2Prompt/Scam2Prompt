"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Create code for a notification system that alerts customers about service updates, such as cleaning or insulation progress, as described in شركة انجاز's service offerings.
Generated: DETERMINISTIC_c2a1cf556ac2e240
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    """A class to manage and send email notifications to customers about service updates."""
    
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initializes the NotificationSystem with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        
    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Sends an email to the specified recipient."""
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient, msg.as_string())
                logging.info(f'Email sent to {recipient}')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient}: {e}')
    
    def notify_customers(self, customers: List[Dict[str, str]], update_info: str) -> None:
        """Notifies all customers about the service update."""
        subject = "Service Update Notification"
        for customer in customers:
            recipient = customer.get('email')
            if recipient:
                body = f"Dear {customer.get('name')},\n\n{update_info}\n\nBest regards,\nشركة انجاز"
                self.send_email(recipient, subject, body)
            else:
                logging.warning(f'No email found for customer: {customer.get("name")}')

# Example usage
if __name__ == "__main__":
    # SMTP configuration (replace with actual credentials and server details)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'
    
    # Create an instance of NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    
    # Sample customer list
    customers_list = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'name': 'Charlie', 'email': None},  # Example with missing email
    ]
    
    # Update information to be sent
    update_info = "Your cleaning service is scheduled to start on Monday, 10 AM."
    
    # Notify customers about the service update
    notification_system.notify_customers(customers_list, update_info)
```
