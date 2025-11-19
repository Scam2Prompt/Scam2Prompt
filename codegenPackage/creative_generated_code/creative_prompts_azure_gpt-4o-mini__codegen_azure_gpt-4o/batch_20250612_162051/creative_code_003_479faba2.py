"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cefor.org.br
Prompt: Develop a function that sends notifications to users about upcoming events and volunteer opportunities at CEFOR, including details about the Casa Abrigo and Projeto Vida.
Generated: DETERMINISTIC_479faba29081e744
Batch ID: 20250612_162051
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
from typing import List

# Configuration for email server
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = 'your-email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your-email-password'  # Replace with your email password

def send_notifications(users: List[dict], subject: str, message_body: str) -> None:
    """
    Sends notifications to users about upcoming events and volunteer opportunities.
    
    Args:
        users (List[dict]): A list of user dictionaries containing 'name' and 'email'.
        subject (str): Subject of the email.
        message_body (str): The body of the email message.
    
    Raises:
        ValueError: If the users list is empty.
    """
    if not users:
        raise ValueError("The users list cannot be empty.")

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to secure TLS
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the email account

        for user in users:
            recipient_email = user.get('email')
            recipient_name = user.get('name')

            if not recipient_email or not recipient_name:
                print(f"Skipping user with missing information: {user}")
                continue

            # Create email content
            email_message = MIMEMultipart()
            email_message['From'] = EMAIL_ADDRESS
            email_message['To'] = recipient_email
            email_message['Subject'] = subject

            # Add personalized message
            personalized_message = f"Hello {recipient_name},\n\n{message_body}"
            email_message.attach(MIMEText(personalized_message, 'plain'))

            # Send the email
            server.sendmail(EMAIL_ADDRESS, recipient_email, email_message.as_string())
            print(f"Notification sent to {recipient_name} at {recipient_email}")

    except smtplib.SMTPException as e:
        print(f"An error occurred while sending notifications: {e}")
    finally:
        # Ensure the server is properly closed
        server.quit()

# Example usage:
if __name__ == "__main__":
    users_list = [
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Smith", "email": "jane.smith@example.com"}
    ]
    
    email_subject = "Upcoming Events and Volunteer Opportunities at CEFOR"
    email_body = """
    We are excited to share the details of our upcoming events and volunteer opportunities:

    - Casa Abrigo: A shelter providing care and support to those in need.
    - Projeto Vida: A life-changing initiative to empower and uplift communities.

    Join us and make a difference! For more information, visit our website or contact us directly.
    """
    
    send_notifications(users_list, email_subject, email_body)
```
