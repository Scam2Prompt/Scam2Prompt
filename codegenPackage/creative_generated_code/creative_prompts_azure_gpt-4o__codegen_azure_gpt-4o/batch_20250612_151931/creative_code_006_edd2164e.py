"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cajicacompra.com
Prompt: Generate code to implement a notification system for judicial updates via email, similar to the "Correo para Notificaciones Judiciales" feature on Cajicá Compra.
Generated: DETERMINISTIC_edd2164e13c02aa1
Batch ID: 20250612_151931
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
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email notification system class
class JudicialNotificationSystem:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the notification system.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_email(self, recipient_email, subject, body):
        """
        Sends an email notification.
        
        :param recipient_email: Recipient's email address
        :param subject: Email subject
        :param body: Email body content
        """
        try:
            # Create email message
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient_email
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))
            
            # Connect to SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Enable secure connection (TLS)
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
                logging.info(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {str(e)}")

# Function to load environment variables for sensitive data
def load_env_variables():
    """
    Loads sensitive configuration data from environment variables.
    
    :return: Dictionary with SMTP configuration and sender credentials
    """
    return {
        'smtp_server': os.getenv('SMTP_SERVER', 'smtp.example.com'),
        'smtp_port': int(os.getenv('SMTP_PORT', 587)),
        'sender_email': os.getenv('SENDER_EMAIL', 'your_email@example.com'),
        'sender_password': os.getenv('SENDER_PASSWORD', 'your_password')
    }

# Example usage
if __name__ == '__main__':
    # Load configuration from environment variables
    config = load_env_variables()
    
    # Initialize the notification system
    notification_system = JudicialNotificationSystem(
        smtp_server=config['smtp_server'],
        smtp_port=config['smtp_port'],
        sender_email=config['sender_email'],
        sender_password=config['sender_password']
    )
    
    # Send a test judicial update notification
    recipient_email = 'recipient@example.com'
    subject = 'Judicial Update Notification'
    body = (
        "Dear User,\n\n"
        "This is a notification regarding judicial updates. Please review the following information:\n"
        "- Update Type: New case filing\n"
        "- Case ID: 12345\n\n"
        "Thank you,\nJudicial Notification System"
    )
    
    notification_system.send_email(recipient_email, subject, body)
```

Note: For production deployment, ensure sensitive data (e.g., SMTP credentials) is securely stored and retrieved using environment variables or a secure vault service.
