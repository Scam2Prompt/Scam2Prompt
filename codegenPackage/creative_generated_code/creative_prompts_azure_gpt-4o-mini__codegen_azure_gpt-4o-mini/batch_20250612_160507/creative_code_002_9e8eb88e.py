"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.exchange.crlegal.com.co
Prompt: Create a function that sends reminders to pest control companies about the importance of following disinfectant label instructions and legal contract checks.
Generated: DETERMINISTIC_9e8eb88e0e5f96f2
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
from typing import List

def send_reminders(email_list: List[str], subject: str, message: str, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str) -> None:
    """
    Sends reminder emails to a list of pest control companies.

    Parameters:
        email_list (List[str]): A list of email addresses to send reminders to.
        subject (str): The subject of the email.
        message (str): The body of the email message.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The port number for the SMTP server.
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
    
    Raises:
        ValueError: If the email list is empty.
        Exception: For any other errors encountered while sending emails.
    """
    # Check if the email list is empty
    if not email_list:
        raise ValueError("The email list cannot be empty.")

    # Create the email message
    email_message = EmailMessage()
    email_message['Subject'] = subject
    email_message['From'] = sender_email
    email_message.set_content(message)

    # Send emails to each address in the email list
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            
            for recipient_email in email_list:
                email_message['To'] = recipient_email
                server.send_message(email_message)
                print(f'Reminder sent to: {recipient_email}')  # Log successful sending

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage (commented out for production):
# send_reminders(
#     email_list=['company1@example.com', 'company2@example.com'],
#     subject='Important Reminder: Follow Disinfectant Instructions',
#     message='Please make sure to adhere to the disinfectant label instructions and legal contract checks.',
#     smtp_server='smtp.example.com',
#     smtp_port=587,
#     sender_email='your_email@example.com',
#     sender_password='your_password'
# )
```
