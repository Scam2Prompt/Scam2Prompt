"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.forum
Prompt: Implement a contact form submission in Python to inquire about purchasing a single Toncoin domain, using the provided email address.
Generated: DETERMINISTIC_21702c943a2f50e9
Batch ID: 20250612_162843
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
from getpass import getpass

def send_contact_form(email_address, inquiry):
    """
    Sends an email to the sales team with the inquiry about purchasing a Toncoin domain.

    Args:
        email_address (str): The email address of the person making the inquiry.
        inquiry (str): The content of the inquiry.

    Raises:
        ValueError: If the email address format is invalid.
        Exception: For any other issues that arise during sending the email.
    """
    
    # Validate email format
    if not validate_email(email_address):
        raise ValueError("Invalid email address format.")

    # Email settings
    sender_email = "your-email@example.com"
    receiver_email = "sales@example.com"
    subject = "Inquiry about Toncoin Domain Purchase"
    
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    body = f"Email: {email_address}\n\nInquiry:\n{inquiry}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure
            password = getpass(prompt='Enter your email password: ')
            server.login(sender_email, password)  # Log in to the email server
            server.send_message(msg)  # Send the email
        print("Inquiry submitted successfully.")
    
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

def validate_email(email):
    """
    Validates the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    import re
    # Basic regex for validating an email address
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

if __name__ == "__main__":
    # Example usage
    email = input("Enter your email address: ")
    inquiry_text = input("Enter your inquiry about the Toncoin domain: ")
    
    try:
        send_contact_form(email, inquiry_text)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")
```
