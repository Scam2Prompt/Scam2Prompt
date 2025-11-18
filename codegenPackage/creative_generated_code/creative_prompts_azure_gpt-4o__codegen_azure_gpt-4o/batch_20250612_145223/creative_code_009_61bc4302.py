"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Write a function to verify user email input and send a password reset code, similar to the functionality described on the Vertiv portal.
Generated: DETERMINISTIC_61bc4302dfe9f248
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import random
import smtplib
from email.message import EmailMessage

def send_password_reset_email(user_email):
    """
    Verifies the user's email input and sends a password reset code to the provided email.
    
    Args:
        user_email (str): The email address to send the password reset code to.

    Returns:
        str: A success message if the email is sent successfully.
    
    Raises:
        ValueError: If the email address is invalid.
        Exception: If there's an error while sending the email.
    """
    # Validate email address using regex
    def is_valid_email(email):
        """Checks if the provided email is in a valid format."""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    if not is_valid_email(user_email):
        raise ValueError("Invalid email address. Please provide a valid email.")

    # Generate a random 6-digit password reset code
    reset_code = f"{random.randint(100000, 999999)}"

    # Configure email parameters
    sender_email = "no-reply@example.com"  # Replace with your sender's email
    sender_password = "yourpassword"      # Replace with your sender's email password
    subject = "Password Reset Code"
    body = f"Hello,\n\nYour password reset code is: {reset_code}\n\nIf you did not request this, please ignore this email.\n\nThank you."

    # Set up the email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.example.com', 465) as server:  # Replace with your SMTP server and port
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except smtplib.SMTPException as e:
        raise Exception(f"Failed to send the email: {str(e)}")

    return f"Password reset code sent successfully to {user_email}."
```
