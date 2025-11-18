"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexium-ai-system.com
Prompt: Create a script to automate sending personalized email notifications to users after registration, following the Apexium AI onboarding process.
Generated: DETERMINISTIC_59c50f76bbf6dc07
Batch ID: 20250612_150048
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
from email.utils import formataddr
import logging
from typing import List, Dict

# Logger setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to send personalized email notifications
def send_email_notifications(users: List[Dict[str, str]], smtp_config: Dict[str, str]) -> None:
    """
    Sends personalized email notifications to users post-registration.

    Args:
        users (List[Dict[str, str]]): A list of user dictionaries with keys 'name' and 'email'.
        smtp_config (Dict[str, str]): SMTP configuration with keys:
            'smtp_server', 'smtp_port', 'email', 'password'.

    Raises:
        Exception: If an email fails to send.
    """
    logging.info("Starting email notification process...")
    
    for user in users:
        try:
            # Validate required fields
            if 'name' not in user or 'email' not in user:
                logging.error(f"Invalid user data: {user}")
                continue

            # Email details
            sender_email = smtp_config['email']
            receiver_email = user['email']
            subject = "Welcome to Apexium AI Platform!"

            # Email content
            message_body = f"""
            Dear {user['name']},
            
            Welcome to Apexium AI! We're thrilled to have you on board.
            
            The onboarding process is designed to help you get started quickly and seamlessly.
            Please visit your dashboard to access the next steps, tutorials, and resources.
            
            If you have any questions, feel free to reach out to our support team.
            
            Best regards,
            The Apexium AI Team
            """

            # Create MIME message
            msg = MIMEMultipart()
            msg['From'] = formataddr(('Apexium AI Support', sender_email))
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message_body, 'plain'))

            # Connect to SMTP server and send email
            logging.info(f"Sending email to {user['name']} ({user['email']})...")
            with smtplib.SMTP(smtp_config['smtp_server'], smtp_config['smtp_port']) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, smtp_config['password'])
                server.sendmail(sender_email, receiver_email, msg.as_string())
            logging.info(f"Email sent successfully to {user['email']}!")
        
        except Exception as e:
            logging.error(f"Failed to send email to {user['email']}: {e}")


# Example usage
if __name__ == "__main__":
    # List of new users
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]

    # SMTP configuration
    smtp_config = {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "email": "your_email@gmail.com",
        "password": "your_email_password"
    }

    # Send emails
    send_email_notifications(users, smtp_config)
```
