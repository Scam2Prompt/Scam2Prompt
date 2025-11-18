"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitfxt.com
Prompt: Generate a code snippet for verifying account ownership on Profitfxt Limited by sending an email request to block an account. Include steps for email validation.
Generated: DETERMINISTIC_b567e71f23514ec7
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import smtplib
from email.mime.text import MIMEText

def validate_email(email):
    """
    Validates the email address format using a regular expression.
    
    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    # Regular expression for a standard email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def send_account_block_request(user_email, account_id):
    """
    Sends an email request to block an account.

    Args:
        user_email (str): The user's email address.
        account_id (str): The account ID to be blocked.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    # Validate the email format
    if not validate_email(user_email):
        print("Invalid email format. Please provide a valid email address.")
        return False

    # Email server configuration
    smtp_server = "smtp.gmail.com"  # Update as per your email provider
    smtp_port = 587
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your app password

    # Email content
    subject = "Account Block Request"
    body = f"Dear Profitfxt Limited,\n\nPlease block the following account.\n\nAccount ID: {account_id}\nRequester Email: {user_email}\n\nThank you."

    try:
        # Set up the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = "support@profitfxt.com"  # Replace with the company's support email

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the email server
            server.sendmail(sender_email, "support@profitfxt.com", msg.as_string())  # Send email
            print("Account block request email sent successfully.")
            return True

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        return False


# Example usage:
if __name__ == "__main__":
    user_email = "user@example.com"  # Replace with the user's email
    account_id = "12345678"          # Replace with the account ID to block
    send_account_block_request(user_email, account_id)
```
