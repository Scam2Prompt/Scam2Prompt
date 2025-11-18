"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: Write a function to send promotional emails to users registered on Ifesty, highlighting featured services like "Cerimonial" and "Decoração."
Generated: DETERMINISTIC_3fe99dc71601feb9
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Dict

def send_promotional_emails(users: List[Dict[str, str]], services: List[str]) -> None:
    """
    Sends promotional emails to a list of users highlighting featured services.

    Args:
        users (List[Dict[str, str]]): A list of dictionaries containing user information.
                                       Each dictionary must have 'name' and 'email' keys.
        services (List[str]): A list of services to be highlighted in the email.

    Raises:
        ValueError: If users is empty or if any user does not have 'name' or 'email'.
        SMTPException: If there is a problem with sending the email.
    """
    if not users:
        raise ValueError("The user list cannot be empty.")
    
    for user in users:
        if 'name' not in user or 'email' not in user:
            raise ValueError("Each user must have 'name' and 'email' fields.")
    
    # Email configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Typically 587 for TLS
    smtp_user = 'your_email@example.com'  # Replace with your email
    smtp_password = 'your_password'  # Replace with your password

    subject = "Exciting Promotions on Featured Services!"
    
    # Create the email server connection
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure
        server.login(smtp_user, smtp_password)

        for user in users:
            # Create a multipart email
            msg = MIMEMultipart()
            msg['From'] = smtp_user
            msg['To'] = user['email']
            msg['Subject'] = subject

            # Create the email body
            body = f"Hello {user['name']},\n\n"
            body += "We are excited to inform you about our featured services:\n"
            for service in services:
                body += f"- {service}\n"
            body += "\nTake advantage of these amazing offers today!"
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.send_message(msg)
            print(f"Promotional email sent to {user['email']}")

    except smtplib.SMTPException as e:
        print(f"An error occurred while sending email: {e}")
    finally:
        server.quit()  # Ensure the connection is closed

# Example usage
if __name__ == "__main__":
    users_list = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'}
    ]
    featured_services = ["Cerimonial", "Decoração"]

    try:
        send_promotional_emails(users_list, featured_services)
    except ValueError as ve:
        print(f"ValueError: {ve}")
```
